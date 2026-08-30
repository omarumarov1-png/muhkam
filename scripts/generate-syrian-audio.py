#!/usr/bin/env python3
"""Overnight TTS sweep for Syrian Arabic: finds every Arabic sentence used
across data/syrian-src/*.json (regular-lesson items + reading-lesson
paragraphs) that isn't already in data/audio-syrian/manifest.json, generates
it via the local Voicebox server (designed-ar-syrian-female / qwen), and
appends it to the manifest as it goes. Re-run any time -- it always rescans
from the source files, so it naturally picks up newly authored lessons
(e.g. from the still-running lesson-expansion loop) without any bookkeeping.
"""
import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data/syrian-src"
AUDIO_DIR = ROOT / "data/audio-syrian"
MANIFEST_PATH = AUDIO_DIR / "manifest.json"
LEVELS = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]

VOICEBOX = "http://localhost:17493"
PROFILE_ID = "4d5b4032-ac3e-4069-9f3b-d4102797def2"  # designed-ar-syrian-female
VOICE_NAME = "designed-ar-syrian-female"

POLL_INTERVAL = 1.5
POLL_TIMEOUT = 60
MAX_RETRIES = 3


def collect_needed_texts():
    texts = []
    seen = set()
    for level in LEVELS:
        f = SRC_DIR / f"{level}.json"
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for lesson in d.get("lessons", []):
            for it in lesson.get("items", []):
                t = it.get("ar", "").strip()
                if t and t not in seen:
                    seen.add(t)
                    texts.append(t)
            for p in lesson.get("paragraphs", []):
                t = p.get("ar", "").strip()
                if t and t not in seen:
                    seen.add(t)
                    texts.append(t)
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
        out_mp3 = AUDIO_DIR / f"apc_{h}.mp3"
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
