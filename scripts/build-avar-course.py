#!/usr/bin/env python3
"""Compile lean Avar lesson authoring data into Muhkam's baked exercise
schema.

Input:  data/avar-src/*.json -- each file: { "level": "<levelId>", "lessons": [...] }
        A lesson is either:
          regular:  { number, title, titleNative?, topicId?, items: [{av, en}] }
          reading:  { number, title, titleNative?, context?, paragraphs: [{av, en}],
                      questions: [{question, options, answerIndex}] }
        Optionally a file may also carry { "grammarTopics": { id: {title,pattern,explanation,fact,dialogue} } }.
Output: data/courses-avar.json -- full course document, same shape as data/courses.json.

Avar uses Cyrillic script plus the palochka letter (Ӏ/ӏ, U+04C0/U+04CF),
same as Chechen -- content is authored directly in this real orthography,
matching what facebook/mms-tts-ava's tokenizer expects (confirmed: its
vocab includes ӏ but not the ASCII "I"/"1" substitutes), so no
transliteration step is needed.
"""
import json
import random
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "avar-src"
OUT_PATH = ROOT / "data" / "courses-avar.json"

random.seed(20260729)  # deterministic distractor shuffling across runs

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]
## labelNative deliberately uses ONLY the confirmed cardinal numbers
## (Omniglot, cross-checked) rather than invented compound Avar phrases
## for abstract concepts like "Foundations"/"Mastery" -- no case-marking
## or derivational morphology has been confirmed for those yet, so this
## avoids guessing at grammar the same way the vocab lessons do.
LEVEL_META = {
    "a1": dict(cefr="A1", label="Foundations", labelNative="Цо"),
    "a2": dict(cefr="A2", label="Building Blocks", labelNative="КӀиго"),
    "b1": dict(cefr="B1", label="Everyday Fluency", labelNative="Лъабго"),
    "b1plus": dict(cefr="B1+", label="Expanding Range", labelNative="Ункъго"),
    "b2": dict(cefr="B2", label="Complex Structures", labelNative="Щуго"),
    "b2plus": dict(cefr="B2+", label="Precision & Nuance", labelNative="Анлъго"),
    "c1": dict(cefr="C1", label="Advanced", labelNative="Анкьго"),
    "c2": dict(cefr="C2", label="Mastery", labelNative="Микьго"),
}

STOPWORDS = set("""
a an the is are was were be been being to of in on at for with and or but not no
i you he she it we they my your his her its our their this that these those
do does did have has had will would can could should shall may might must
so as if then than too very just also here there up down out off over under
me him them us who what when where why how which
""".split())


def content_word(tok):
    w = re.sub(r"[^A-Za-z']", "", tok)
    return w


def pick_blank(en_text):
    words = en_text.split()
    candidates = [w for w in words if len(content_word(w)) >= 4 and content_word(w).lower() not in STOPWORDS]
    if not candidates:
        return None, None
    target = random.choice(candidates)
    clean = content_word(target)
    blanked = en_text.replace(target, "___", 1)
    return clean, blanked


def load_source():
    levels = defaultdict(list)
    grammar_topics = {}
    files = sorted(SRC_DIR.glob("*.json"))
    if not files:
        sys.exit(f"No source files found in {SRC_DIR}")
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        level = data["level"]
        levels[level].extend(data["lessons"])
        grammar_topics.update(data.get("grammarTopics", {}))
    return levels, grammar_topics


def build_pools(levels):
    en_pool_by_level = defaultdict(list)
    word_pool = set()
    for level, lessons in levels.items():
        for lesson in lessons:
            for item in lesson.get("items", []):
                en_pool_by_level[level].append(item["en"])
                for w in item["en"].split():
                    cw = content_word(w)
                    if len(cw) >= 4 and cw.lower() not in STOPWORDS:
                        word_pool.add(cw)
            for p in lesson.get("paragraphs", []):
                en_pool_by_level[level].append(p["en"])
    return en_pool_by_level, list(word_pool)


def sample_distractors(correct, level, en_pool_by_level, n=3):
    pool = [t for t in en_pool_by_level.get(level, []) if t != correct]
    if len(pool) < n:
        wide = [t for lvl in en_pool_by_level.values() for t in lvl if t != correct]
        pool = wide if len(wide) >= n else pool
    pool = list(dict.fromkeys(pool))
    if len(pool) <= n:
        return pool
    return random.sample(pool, n)


def compile_regular_lesson(level, lesson, en_pool_by_level, word_pool):
    items = lesson["items"]
    exercises = []
    for i, item in enumerate(items):
        av, en = item["av"], item["en"]

        distractors = sample_distractors(en, level, en_pool_by_level)
        options = [en] + distractors
        random.shuffle(options)
        exercises.append({
            "type": "multiple-choice",
            "direction": "av-en",
            "prompt": av,
            "options": options,
            "answerIndex": options.index(en),
        })

        tokens = av.split()
        bank = tokens[:]
        random.shuffle(bank)
        exercises.append({
            "type": "word-bank",
            "direction": "en-av",
            "prompt": en,
            "bank": bank,
            "answer": tokens,
        })

        # Bundled audio (data/audio-avar/manifest.json, facebook/mms-tts-ava)
        # makes listening/listening-tap viable from the start.
        if i % 3 == 0:
            d2 = sample_distractors(en, level, en_pool_by_level)
            opts2 = [en] + d2
            random.shuffle(opts2)
            exercises.append({
                "type": "listening",
                "native": av,
                "options": opts2,
                "answerIndex": opts2.index(en),
            })
        elif i % 3 == 1:
            exercises.append({"type": "listening-tap", "native": av, "answer": tokens})

        if i % 4 == 3:
            blank_word, blanked_en = pick_blank(en)
            if blank_word:
                wrongs = [w for w in random.sample(word_pool, min(12, len(word_pool)))
                          if w.lower() != blank_word.lower()][:3]
                if len(wrongs) == 3:
                    opts = [blank_word] + wrongs
                    random.shuffle(opts)
                    exercises.append({
                        "type": "fill-blank",
                        "native": av,
                        "blankedEn": blanked_en,
                        "answer": blank_word,
                        "options": opts,
                    })

    for start in range(0, len(items) - 3, 4):
        chunk = items[start:start + 4]
        exercises.append({
            "type": "matching",
            "pairs": [{"native": c["av"], "en": c["en"]} for c in chunk],
        })

    out = {
        "id": f"av-{level}-{lesson['number']}",
        "number": lesson["number"],
        "title": lesson["title"],
        "description": lesson.get("description", lesson["title"]),
        "exercises": exercises,
    }
    if lesson.get("titleNative"):
        out["titleNative"] = lesson["titleNative"]
    if lesson.get("topicId"):
        out["topicId"] = lesson["topicId"]
    return out


def compile_reading_lesson(level, lesson):
    return {
        "id": f"av-{level}-{lesson['number']}-reading",
        "number": lesson["number"],
        "title": lesson["title"],
        "titleNative": lesson.get("titleNative", ""),
        "description": lesson.get("context", lesson["title"]),
        "readingPassage": {
            "context": lesson.get("context", lesson["title"]),
            "paragraphs": [{"native": p["av"], "en": p["en"]} for p in lesson["paragraphs"]],
        },
        "exercises": [
            {
                "type": "comprehension",
                "question": q["question"],
                "options": q["options"],
                "answerIndex": q["answerIndex"],
            }
            for q in lesson["questions"]
        ],
    }


def main():
    levels, grammar_topics = load_source()
    en_pool_by_level, word_pool = build_pools(levels)
    if len(word_pool) < 15:
        sys.exit("Not enough English content words collected to build fill-blank distractors")

    out_levels = []
    total_lessons = 0
    total_exercises = 0
    total_sentences = 0
    for level_id in LEVEL_ORDER:
        lessons = sorted(levels.get(level_id, []), key=lambda l: l["number"])
        compiled = []
        for lesson in lessons:
            if "paragraphs" in lesson:
                cl = compile_reading_lesson(level_id, lesson)
                total_sentences += len(lesson["paragraphs"])
            else:
                cl = compile_regular_lesson(level_id, lesson, en_pool_by_level, word_pool)
                total_sentences += len(lesson["items"])
            total_exercises += len(cl["exercises"])
            compiled.append(cl)
        total_lessons += len(compiled)
        if not compiled:
            continue
        meta = LEVEL_META[level_id]
        out_levels.append({
            "id": level_id,
            "cefr": meta["cefr"],
            "label": meta["label"],
            "labelNative": meta["labelNative"],
            "lessons": compiled,
        })

    course = {
        "id": "avar",
        "title": "Avar, Start to Fluent",
        "subtitle": "Modern Avar from absolute beginner through fluent, everyday command -- real sentences, grammar, and conversational practice",
        "dir": "ltr",
        "lang": "av",
        "languageName": "Avar",
        "fontNative": "'Noto Sans', 'Inter', sans-serif",
        "flag": "МагӀарул мацӏ",
        "heroEyebrow": "МагӀарул мацӏ · A1 → C2",
        "heroNative": "МагӀарул мацӏ",
        "heroLedeSuffix": "Real sentences from lesson one, built the same way as this app's other courses.",
        "uiStrings": {},
        "grammarTopics": grammar_topics,
        "levels": out_levels,
    }

    OUT_PATH.write_text(json.dumps({"course": course}, ensure_ascii=False, indent=2), encoding="utf-8")
    json.loads(OUT_PATH.read_text(encoding="utf-8"))

    print(f"Levels: {len(out_levels)}  Lessons: {total_lessons}  Exercises: {total_exercises}  Sentences: {total_sentences}")
    for lv in out_levels:
        print(f"  {lv['id']:8s} {len(lv['lessons']):4d} lessons")


if __name__ == "__main__":
    main()
