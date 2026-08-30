#!/usr/bin/env python3
"""Compute per-course download size (course JSON + bundled audio dir) for the offline-download UI. Output: data/course-sizes.json"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def load_courses_array():
    app_js = open(os.path.join(ROOT, "app.js"), encoding="utf-8").read()
    start = app_js.index("const COURSES = [")
    start = app_js.index("[", start)
    depth = 0
    for i, ch in enumerate(app_js[start:], start):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    body = app_js[start:end]
    courses = []
    for line in body.splitlines():
        line = line.strip()
        id_match = re.search(r'\bid:\s*"([^"]+)"', line)
        file_match = re.search(r'\bfile:\s*"([^"]+)"', line)
        if id_match and file_match:
            has_audio = bool(re.search(r'\baudioManifest:\s*"', line))
            courses.append((id_match.group(1), file_match.group(1), has_audio))
    return courses


def dir_size(path):
    total = 0
    if not os.path.isdir(path):
        return 0
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.endswith((".mp3", ".m4a")):
            total += entry.stat().st_size
    return total


def main():
    courses = load_courses_array()
    sizes = {}
    for course_id, file_rel, has_audio in courses:
        json_path = os.path.join(ROOT, file_rel)
        json_bytes = os.path.getsize(json_path) if os.path.exists(json_path) else 0
        audio_bytes = dir_size(os.path.join(DATA, f"audio-{course_id}")) if has_audio else 0
        sizes[course_id] = {"jsonBytes": json_bytes, "audioBytes": audio_bytes}
    out_path = os.path.join(DATA, "course-sizes.json")
    json.dump(sizes, open(out_path, "w"), indent=1)
    print(f"Wrote {out_path} ({len(sizes)} courses)")
    for cid, s in sizes.items():
        total_mb = (s["jsonBytes"] + s["audioBytes"]) / 1024 / 1024
        print(f"  {cid}: {total_mb:.1f} MB")


if __name__ == "__main__":
    main()
