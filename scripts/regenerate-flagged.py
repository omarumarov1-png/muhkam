#!/usr/bin/env python3
"""Regenerate every audio file flagged by audio-glitch-scan.py's report.

Backs up each original file before overwriting (so genuinely-bad real
samples survive for future detector calibration instead of being destroyed),
regenerates via the local Voicebox server with the same retry logic as
generate-arabic-audio.py, and updates the manifest's voice field only if it
changes (it won't -- filenames are content-hashed from the sentence text).

Usage: python3 scripts/regenerate-flagged.py data/audio-arabic
"""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VOICEBOX = os.environ.get("VOICEBOX_URL", "http://localhost:17493")
PROFILE_ID = os.environ.get(
    "VOICEBOX_PROFILE_ID", "e975228b-59d9-4599-a32b-3e801f172c22"
)
POLL_INTERVAL = 1.5
POLL_TIMEOUT = 60
MAX_RETRIES = 3


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
    resp = api_post("/generate", {"profile_id": PROFILE_ID, "text": text, "language": "ar", "engine": "qwen"})
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
    raise TimeoutError("timed out")


def fetch_and_convert(gid, out_mp3):
    wav_path = out_mp3.with_suffix(".wav")
    with urllib.request.urlopen(f"{VOICEBOX}/audio/{gid}", timeout=30) as r:
        wav_path.write_bytes(r.read())
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav_path),
         "-codec:a", "libmp3lame", "-qscale:a", "2", str(out_mp3)],
        check=True,
    )
    wav_path.unlink()


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: regenerate-flagged.py <audio-dir>")
    audio_dir = ROOT / sys.argv[1]
    report_path = audio_dir / "glitch-scan-report.json"
    manifest_path = audio_dir / "manifest.json"
    backup_dir = audio_dir / "_flagged_originals"
    backup_dir.mkdir(exist_ok=True)

    try:
        health = api_get("/health")
    except Exception as e:
        sys.exit(f"Voicebox not reachable at {VOICEBOX}: {e}")
    if health.get("status") != "healthy":
        sys.exit(f"Voicebox reports unhealthy: {health}")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    print(f"[{time.strftime('%H:%M:%S')}] {len(report)} flagged files to regenerate", flush=True)

    done, failed = 0, 0
    for i, item in enumerate(report, 1):
        fname = item["file"]
        text = item["text"]
        f = audio_dir / fname

        if f.exists():
            backup_path = backup_dir / fname
            if not backup_path.exists():
                backup_path.write_bytes(f.read_bytes())

        ok = False
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                gid = generate_one(text)
                fetch_and_convert(gid, f)
                ok = True
                break
            except Exception as e:
                print(f"  [{i}/{len(report)}] attempt {attempt} failed for {fname}: {e}", flush=True)
                time.sleep(3)
        if ok:
            done += 1
        else:
            failed += 1

        if i % 10 == 0 or i == len(report):
            print(f"[{time.strftime('%H:%M:%S')}] progress {i}/{len(report)} (done={done} failed={failed})", flush=True)

    print(f"[{time.strftime('%H:%M:%S')}] FINISHED: {done} regenerated, {failed} still failed", flush=True)


if __name__ == "__main__":
    main()
