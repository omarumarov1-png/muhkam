#!/usr/bin/env python3
"""Compile lean Dalail al-Khayrat authoring data into Muhkam's baked exercise schema.

Input:  data/dalail-src/*.json -- each file: { "level": "<levelId>", "lessons": [...] }
        A lesson is { number, title, titleNative?, items: [{ar, en, translit?}] }.
Output: data/courses-dalail.json -- full course document, same shape as data/courses.json.

Dalail al-Khayrat (دلائل الخيرات), compiled by Imam Muhammad al-Jazuli, is a
classical Arabic collection of salawat (blessings upon the Prophet Muhammad)
divided into 8 hizbs read across the days of the week (Monday is split into
two parts, "Monday" and "Monday Again", to fit 8 hizbs into 7 days -- this
matches the structure used by the Muhammadan Way app / nurmuhammad.com).

Sourcing discipline (stricter than any other Muhkam course, since this is a
religious text): every item's Arabic text is reconstructed from a verified
Romanised-Arabic + English transliteration/translation document published by
Naqshbandi Center Michigan (the same organization behind nurmuhammad.com and
the Muhammadan Way app), cross-checked directly against real in-app
screenshots the user provided (matching pixel-for-pixel on every checked
item). No content here is recalled from model memory or invented -- every
item traces to that transliteration source, converted to Arabic script using
standard Classical Arabic orthography for these well-established salawat
formulas. Never extend this course with a salawat/dua the transliteration
source doesn't contain.

TTS: Voicebox qwen engine, "designed-ar-dalail-reciter" voice profile --
prompted for a reverent, deep adult-male, tarteel-style recitation cadence
(deliberately different from the casual conversational voices used for the
dialect courses), user-confirmed before content began.

Levels here are hizb-days, not CEFR levels: monday1, tuesday, wednesday,
thursday, friday, saturday, sunday, monday2 (the second Monday hizb).
"""
import json
import random
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "dalail-src"
OUT_PATH = ROOT / "data" / "courses-dalail.json"

random.seed(20260913)

LEVEL_ORDER = ["monday1", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday2"]
LEVEL_META = {
    "monday1": dict(label="Monday, Part 1", labelNative="الحزب الأول - الاثنين"),
    "tuesday": dict(label="Tuesday", labelNative="الحزب الثاني - الثلاثاء"),
    "wednesday": dict(label="Wednesday", labelNative="الحزب الثالث - الأربعاء"),
    "thursday": dict(label="Thursday", labelNative="الحزب الرابع - الخميس"),
    "friday": dict(label="Friday", labelNative="الحزب الخامس - الجمعة"),
    "saturday": dict(label="Saturday", labelNative="الحزب السادس - السبت"),
    "sunday": dict(label="Sunday", labelNative="الحزب السابع - الأحد"),
    "monday2": dict(label="Monday, Part 2", labelNative="الحزب الثامن - الاثنين"),
}

STOPWORDS = set("""
a an the is are was were be been being to of in on at for with and or but not no
i you he she it we they my your his her its our their this that these those
do does did have has had will would can could should shall may might must
so as if then than too very just also here there up down out off over under
me him them us who what when where why how which
""".split())


def content_word(tok):
    return re.sub(r"[^A-Za-z']", "", tok)


def load_source():
    levels = defaultdict(list)
    files = sorted(SRC_DIR.glob("*.json"))
    if not files:
        sys.exit(f"No source files found in {SRC_DIR}")
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        level = data["level"]
        levels[level].extend(data["lessons"])
    return levels


def build_pools(levels):
    en_pool_by_level = defaultdict(list)
    for level, lessons in levels.items():
        for lesson in lessons:
            for item in lesson.get("items", []):
                en_pool_by_level[level].append(item["en"])
    return en_pool_by_level


def sample_distractors(correct, level, en_pool_by_level, n=3):
    pool = [t for t in en_pool_by_level.get(level, []) if t != correct]
    if len(pool) < n:
        wide = [t for lvl in en_pool_by_level.values() for t in lvl if t != correct]
        pool = wide if len(wide) >= n else pool
    pool = list(dict.fromkeys(pool))
    if len(pool) <= n:
        return pool
    return random.sample(pool, n)


def compile_lesson(level, lesson, en_pool_by_level):
    items = lesson["items"]
    exercises = []
    for item in items:
        ar, en = item["ar"], item["en"]
        translit = item.get("translit")

        distractors = sample_distractors(en, level, en_pool_by_level)
        options = [en] + distractors
        random.shuffle(options)
        mc = {
            "type": "multiple-choice",
            "direction": "ar-en",
            "prompt": ar,
            "options": options,
            "answerIndex": options.index(en),
        }
        if translit:
            mc["translit"] = translit
        exercises.append(mc)

        listen_options = [en] + sample_distractors(en, level, en_pool_by_level)
        random.shuffle(listen_options)
        exercises.append({
            "type": "listening",
            "native": ar,
            "options": listen_options,
            "answerIndex": listen_options.index(en),
        })

    for start in range(0, len(items) - 2, 3):
        chunk = items[start:start + 3]
        if len(chunk) >= 2:
            exercises.append({
                "type": "matching",
                "pairs": [{"native": c["ar"], "en": c["en"]} for c in chunk],
            })

    return {
        "id": f"dal-{level}-{lesson['number']}",
        "number": lesson["number"],
        "title": lesson["title"],
        "titleNative": lesson.get("titleNative", ""),
        "description": lesson.get("description", lesson["title"]),
        "exercises": exercises,
    }


def main():
    levels = load_source()
    en_pool_by_level = build_pools(levels)

    out_levels = []
    total_lessons = 0
    total_exercises = 0
    total_sentences = 0
    for level_id in LEVEL_ORDER:
        lessons = sorted(levels.get(level_id, []), key=lambda l: l["number"])
        compiled = []
        for lesson in lessons:
            cl = compile_lesson(level_id, lesson, en_pool_by_level)
            total_sentences += len(lesson["items"])
            total_exercises += len(cl["exercises"])
            compiled.append(cl)
        total_lessons += len(compiled)
        if not compiled:
            continue
        meta = LEVEL_META[level_id]
        out_levels.append({
            "id": level_id,
            "label": meta["label"],
            "labelNative": meta["labelNative"],
            "lessons": compiled,
        })

    course = {
        "id": "dalail",
        "title": "Dalail al-Khayrat",
        "subtitle": "The classical salawat collection of Imam al-Jazuli, one hizb per day of the week, with transliteration and reverent recitation-style audio for every line",
        "dir": "rtl",
        "lang": "ar",
        "languageName": "Dalail al-Khayrat",
        "fontNative": "'Noto Naskh Arabic', 'Noto Sans Arabic', serif",
        "flag": "دلائل الخيرات",
        "heroEyebrow": "دلائل الخيرات · الاثنين → الاثنين",
        "heroNative": "دلائل الخيرات",
        "heroLedeSuffix": "Learn Dalail al-Khayrat sentence by sentence, day by day, with transliteration and reverent tarteel-style audio for every line.",
        "uiStrings": {"grammarNote": "ملاحظة", "didYouKnow": "تعرف؟"},
        "grammarTopics": {},
        "levels": out_levels,
    }

    OUT_PATH.write_text(json.dumps({"course": course}, ensure_ascii=False, indent=2), encoding="utf-8")
    json.loads(OUT_PATH.read_text(encoding="utf-8"))  # round-trip validate

    print(f"Levels: {len(out_levels)}  Lessons: {total_lessons}  Exercises: {total_exercises}  Sentences: {total_sentences}")
    for lv in out_levels:
        print(f"  {lv['id']:10s} {len(lv['lessons']):4d} lessons")


if __name__ == "__main__":
    main()
