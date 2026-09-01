#!/usr/bin/env python3
"""Overnight TTS sweep for Modern Standard Arabic (Fusha): finds every unique
fully-diacritized Arabic sentence used across data/courses.json (readingPassage
paragraphs, multiple-choice prompts, word-bank answers, listening/listening-tap
native text) that isn't already in data/audio-arabic/manifest.json, generates
it via the local Voicebox server (designed-ar-msa-female / qwen), and appends
it to the manifest as it goes. Re-run any time -- it always rescans
data/courses.json fresh, so it naturally picks up any future content changes
without any bookkeeping.
"""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE_PATH = ROOT / "data/courses.json"
AUDIO_DIR = ROOT / "data/audio-arabic"
MANIFEST_PATH = AUDIO_DIR / "manifest.json"

# Profile IDs are local to each Voicebox install's database, so they don't
# transfer across machines even when the profile is recreated with the exact
# same design_prompt. Override per-machine via env vars rather than editing
# this file (which is shared/committed across machines).
VOICEBOX = os.environ.get("VOICEBOX_URL", "http://localhost:17493")
PROFILE_ID = os.environ.get(
    "VOICEBOX_PROFILE_ID", "e975228b-59d9-4599-a32b-3e801f172c22"
)  # designed-ar-msa-female
VOICE_NAME = "designed-ar-msa-female"

POLL_INTERVAL = 1.5
POLL_TIMEOUT = 60
MAX_RETRIES = 3


def collect_needed_texts():
    d = json.loads(COURSE_PATH.read_text(encoding="utf-8"))
    texts = []
    seen = set()

    def add(t):
        t = t.strip()
        if t and t not in seen:
            seen.add(t)
            texts.append(t)

    for lvl in d["course"]["levels"]:
        for lesson in lvl["lessons"]:
            rp = lesson.get("readingPassage")
            if rp:
                for p in rp.get("paragraphs", []):
                    add(p.get("native", ""))
            for ex in lesson.get("exercises", []):
                t = ex.get("type")
                if t == "multiple-choice":
                    add(ex.get("prompt", ""))
                elif t == "word-bank":
                    add(" ".join(ex.get("answer", [])))
                elif t in ("listening", "listening-tap"):
                    add(ex.get("native", ""))
                elif t == "fill-blank":
                    add(ex.get("native", ""))
                elif t == "matching":
                    for p in ex.get("pairs", []):
                        add(p.get("native", ""))
    return texts


def load_manifest():
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest):
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8"
    )


def api_post(path, payload):
    req = urllib.request.Request(
        f"{VOICEBOX}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def api_get(path):
    with urllib.request.urlopen(f"{VOICEBOX}{path}", timeout=15) as r:
        return json.loads(r.read())


def generate_one(text):
    resp = api_post(
        "/generate",
        {
            "profile_id": PROFILE_ID,
            "text": text,
            "language": "ar",
            "engine": "qwen",
        },
    )
    gid = resp["id"]
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        status = api_get(f"/history/{gid}")
        st = status.get("status")
        if st == "completed":
            return gid
        if st == "failed" or status.get("error"):
            raise RuntimeError(f"generation failed: {status.get('error')}")
    raise TimeoutError(f"generation timed out after {POLL_TIMEOUT}s")


def fetch_and_convert(gid, out_mp3):
    wav_path = out_mp3.with_suffix(".wav")
    req = urllib.request.Request(f"{VOICEBOX}/audio/{gid}")
    with urllib.request.urlopen(req, timeout=30) as r:
        wav_path.write_bytes(r.read())
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav_path),
         "-codec:a", "libmp3lame", "-qscale:a", "2", str(out_mp3)],
        check=True,
    )
    wav_path.unlink()


def main():
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    try:
        health = api_get("/health")
    except Exception as e:
        sys.exit(f"Voicebox not reachable at {VOICEBOX}: {e}")
    if health.get("status") != "healthy":
        sys.exit(f"Voicebox reports unhealthy: {health}")

    needed = collect_needed_texts()
    manifest = load_manifest()
    missing = [t for t in needed if t not in manifest]
    print(f"[{time.strftime('%H:%M:%S')}] {len(needed)} sentences total, "
          f"{len(needed) - len(missing)} already have audio, "
          f"{len(missing)} to generate", flush=True)

    done, failed = 0, 0
    for i, text in enumerate(missing, 1):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]
        out_mp3 = AUDIO_DIR / f"ar_{h}.mp3"
        ok = False
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                gid = generate_one(text)
                fetch_and_convert(gid, out_mp3)
                ok = True
                break
            except Exception as e:
                print(f"  [{i}/{len(missing)}] attempt {attempt} failed for "
                      f"{text!r}: {e}", flush=True)
                time.sleep(3)
        if ok:
            manifest[text] = {"file": out_mp3.name, "voice": VOICE_NAME}
            done += 1
        else:
            failed += 1
        if i % 10 == 0 or i == len(missing):
            save_manifest(manifest)
            print(f"[{time.strftime('%H:%M:%S')}] progress {i}/{len(missing)} "
                  f"(done={done} failed={failed})", flush=True)

    save_manifest(manifest)
    print(f"[{time.strftime('%H:%M:%S')}] FINISHED: {done} generated, "
          f"{failed} failed, manifest now has {len(manifest)} entries",
          flush=True)


if __name__ == "__main__":
    main()
