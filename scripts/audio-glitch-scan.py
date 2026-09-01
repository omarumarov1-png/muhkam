#!/usr/bin/env python3
"""Technical (not semantic) glitch scan for generated course audio.

Catches objective defects ffmpeg/numpy can measure reliably: corrupted/
unreadable files, near-zero duration, total silence, severe clipping,
duration wildly out of proportion to the sentence's word count, and
repeated-segment loops (a qwen/Voicebox TTS failure mode confirmed in
practice -- e.g. a stuck syllable looping for ~1 minute, or a trailing word
repeated once at the end of an otherwise normal-length clip). It CANNOT
tell you whether the pronunciation is actually correct -- past Whisper-
based semantic checks for this project were noisy and unreliable (see
feedback_ielts_tts_verification memory), so this only flags files worth a
human listen, not confirmed defects.

Usage: python3 scripts/audio-glitch-scan.py data/audio-syrian
       python3 scripts/audio-glitch-scan.py data/audio-arabic
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent

# seconds of audio per Arabic word, outside this range is suspicious
MIN_SEC_PER_WORD = 0.18
MAX_SEC_PER_WORD = 1.6

# repeated-segment (loop) detection tuning
REPEAT_SAMPLE_RATE = 16000
REPEAT_WIN_SEC = 0.3
REPEAT_HOP_SEC = 0.15
REPEAT_MIN_FRAME_GAP = 4  # skip trivially-overlapping neighbors
REPEAT_SIMILARITY_THRESHOLD = 0.97


def ffprobe_duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def volume_stats(path):
    r = subprocess.run(
        ["ffmpeg", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    mean_v = max_v = None
    for line in r.stderr.splitlines():
        if "mean_volume:" in line:
            mean_v = float(line.split("mean_volume:")[1].split("dB")[0].strip())
        if "max_volume:" in line:
            max_v = float(line.split("max_volume:")[1].split("dB")[0].strip())
    return mean_v, max_v


def longest_silence_gap(path):
    """Longest internal silence, excluding leading/trailing silence -- a long
    mid-clip gap is a decent proxy for the model stalling or repeating itself
    mid-generation, which a duration-only check can miss on an otherwise
    normal-length file."""
    r = subprocess.run(
        ["ffmpeg", "-i", str(path), "-af", "silencedetect=noise=-35dB:d=0.4",
         "-f", "null", "-"],
        capture_output=True, text=True,
    )
    starts, ends = [], []
    for line in r.stderr.splitlines():
        if "silence_start:" in line:
            starts.append(float(line.split("silence_start:")[1].strip()))
        elif "silence_end:" in line:
            ends.append(float(line.split("silence_end:")[1].split("|")[0].strip()))
    gaps = [e - s for s, e in zip(starts, ends) if e > s]
    return max(gaps) if gaps else 0.0


def detect_repeated_segment(path):
    """Flags a clip where some segment closely repeats another, non-adjacent
    segment later on -- catches stuck-syllable loops (long) and a trailing
    repeated word/phrase (short, otherwise-normal duration) alike, neither of
    which duration/volume/silence checks can see. Returns (similarity, gap_s)
    for the most similar non-adjacent frame pair, or None if undecodable/too
    short to analyze."""
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1",
         "-ar", str(REPEAT_SAMPLE_RATE), "-f", "f32le", "-"],
        capture_output=True,
    )
    if r.returncode != 0 or not r.stdout:
        return None
    audio = np.frombuffer(r.stdout, dtype=np.float32)
    sr = REPEAT_SAMPLE_RATE
    win = int(REPEAT_WIN_SEC * sr)
    hop = int(REPEAT_HOP_SEC * sr)
    n_frames = 1 + (len(audio) - win) // hop
    if n_frames < REPEAT_MIN_FRAME_GAP + 2:
        return None

    frames = np.stack([audio[i * hop:i * hop + win] for i in range(n_frames)])
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    active = rms > (rms.max() * 0.15) if rms.max() > 0 else np.zeros(n_frames, dtype=bool)

    window = np.hanning(win)
    spec = np.abs(np.fft.rfft(frames * window, axis=1))
    norms = np.linalg.norm(spec, axis=1, keepdims=True)
    norms[norms == 0] = 1
    spec_n = spec / norms

    best_sim = 0.0
    best_gap = 0.0
    for i in range(n_frames):
        if not active[i]:
            continue
        for j in range(i + REPEAT_MIN_FRAME_GAP, n_frames):
            if not active[j]:
                continue
            sim = float(np.dot(spec_n[i], spec_n[j]))
            if sim > best_sim:
                best_sim = sim
                best_gap = (j - i) * REPEAT_HOP_SEC
    return best_sim, best_gap


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: audio-glitch-scan.py <audio-dir>")
    audio_dir = ROOT / sys.argv[1]
    manifest_path = audio_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    flagged = []
    checked = 0
    for text, meta in manifest.items():
        f = audio_dir / meta["file"]
        checked += 1
        if not f.exists():
            flagged.append((f.name, "missing file", text))
            continue

        dur = ffprobe_duration(f)
        if dur is None:
            flagged.append((f.name, "unreadable/corrupted", text))
            continue
        if dur < 0.3:
            flagged.append((f.name, f"near-zero duration ({dur:.2f}s)", text))
            continue

        word_count = max(len(text.split()), 1)
        sec_per_word = dur / word_count
        if sec_per_word < MIN_SEC_PER_WORD or sec_per_word > MAX_SEC_PER_WORD:
            flagged.append((f.name, f"duration/word-count mismatch ({dur:.2f}s, {word_count}w, {sec_per_word:.2f}s/w)", text))
            continue

        mean_v, max_v = volume_stats(f)
        if mean_v is None:
            flagged.append((f.name, "volumedetect failed", text))
            continue
        if mean_v < -50:
            flagged.append((f.name, f"near-silent (mean {mean_v:.1f}dB)", text))
            continue
        if max_v is not None and max_v >= -0.1:
            flagged.append((f.name, f"possible clipping (max {max_v:.1f}dB)", text))
            continue

        gap = longest_silence_gap(f)
        if gap > 1.2:
            flagged.append((f.name, f"long mid-clip silence gap ({gap:.2f}s) -- possible stutter/stall", text))
            continue

        rep = detect_repeated_segment(f)
        if rep is not None:
            sim, seg_gap = rep
            if sim >= REPEAT_SIMILARITY_THRESHOLD:
                flagged.append((f.name, f"repeated segment detected (similarity {sim:.2f}, {seg_gap:.2f}s apart) -- possible stuck loop/repeated word", text))
                continue

        if checked % 200 == 0:
            print(f"  checked {checked}/{len(manifest)}...", flush=True)

    print()
    print(f"Checked {checked} files, flagged {len(flagged)} for review")
    print("(technical defects only -- mispronunciation/garbling needs a human listen)")
    print()
    out_path = audio_dir / "glitch-scan-report.json"
    out_path.write_text(
        json.dumps(
            [{"file": f, "reason": r, "text": t} for f, r, t in flagged],
            ensure_ascii=False, indent=1,
        ),
        encoding="utf-8",
    )
    print(f"Report written to {out_path}")
    for f, r, t in flagged[:30]:
        print(f"  {f}: {r} -- {t[:60]}")
    if len(flagged) > 30:
        print(f"  ... and {len(flagged) - 30} more, see report file")


if __name__ == "__main__":
    main()
