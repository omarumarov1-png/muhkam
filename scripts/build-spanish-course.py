#!/usr/bin/env python3
"""Compile lean Spanish lesson authoring data into Muhkam's baked exercise schema.

Input:  data/spanish-src/*.json — each file: { "level": "<levelId>", "lessons": [...] }
        A lesson is either:
          regular:  { number, title, titleNative?, topicId?, items: [{es, en, translit?}] }
          reading:  { number, title, titleNative?, context?, paragraphs: [{es, en}],
                      questions: [{question, options, answerIndex}] }
        Optionally a file may also carry { "grammarTopics": { id: {title,pattern,explanation,fact,dialogue} } }.
Output: data/courses-spanish.json — full course document, same shape as data/courses.json.

Spanish uses the Latin alphabet, so unlike Hebrew/Arabic there is no
alphabet-drill phase and no separate translit field is needed for most
content -- the native script IS already Latin (translit is only used for
occasional pronunciation notes, e.g. stress marks on tricky words).

This course targets neutral Latin American Spanish (ustedes, not
vosotros; pan-American vocabulary like "computadora"/"carro" rather than
Peninsular "ordenador"/"coche"), confirmed with the user before writing
any content. Vocabulary is cross-checked against the Spanish Wiktionary
dump on kaikki.org before use, same discipline as this project's other
courses. Audio is genuine, dedicated Spanish TTS (Kokoro engine via the
local Voicebox app, voices ef_dora/em_alex/em_santa) -- real neural
Spanish speech, not a cross-language TTS compromise like several of this
project's underserved-language courses had to accept -- so, unlike
Uzbek/Avar, listening/listening-tap exercises ARE generated here.
"""
import json
import random
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "spanish-src"
OUT_PATH = ROOT / "data" / "courses-spanish.json"

random.seed(20260828)  # deterministic distractor shuffling across runs

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]
LEVEL_META = {
    "a1": dict(cefr="A1", label="Foundations", labelNative="Fundamentos"),
    "a2": dict(cefr="A2", label="Building Blocks", labelNative="Bloques básicos"),
    "b1": dict(cefr="B1", label="Everyday Fluency", labelNative="Fluidez cotidiana"),
    "b1plus": dict(cefr="B1+", label="Expanding Range", labelNative="Ampliando el alcance"),
    "b2": dict(cefr="B2", label="Complex Structures", labelNative="Estructuras complejas"),
    "b2plus": dict(cefr="B2+", label="Precision & Nuance", labelNative="Precisión y matiz"),
    "c1": dict(cefr="C1", label="Advanced", labelNative="Avanzado"),
    "c2": dict(cefr="C2", label="Mastery", labelNative="Maestría"),
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
    """en-sentence pool per level (for distractors) and a global content-word pool (for fill-blank)."""
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
    pool = list(dict.fromkeys(pool))  # dedupe, preserve order
    if len(pool) <= n:
        return pool
    return random.sample(pool, n)


def compile_regular_lesson(level, lesson, en_pool_by_level, word_pool):
    items = lesson["items"]
    exercises = []
    for i, item in enumerate(items):
        es, en = item["es"], item["en"]
        translit = item.get("translit")

        distractors = sample_distractors(en, level, en_pool_by_level)
        options = [en] + distractors
        random.shuffle(options)
        mc = {
            "type": "multiple-choice",
            "direction": "es-en",
            "prompt": es,
            "options": options,
            "answerIndex": options.index(en),
        }
        if translit:
            mc["translit"] = translit
        exercises.append(mc)

        tokens = es.split()
        bank = tokens[:]
        random.shuffle(bank)
        exercises.append({
            "type": "word-bank",
            "direction": "en-es",
            "prompt": en,
            "bank": bank,
            "answer": tokens,
        })

        if i % 3 == 0:
            d2 = sample_distractors(en, level, en_pool_by_level)
            opts2 = [en] + d2
            random.shuffle(opts2)
            exercises.append({
                "type": "listening",
                "native": es,
                "options": opts2,
                "answerIndex": opts2.index(en),
            })
        elif i % 3 == 1:
            exercises.append({"type": "listening-tap", "native": es, "answer": tokens})

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
                        "native": es,
                        "blankedEn": blanked_en,
                        "answer": blank_word,
                        "options": opts,
                    })

    for start in range(0, len(items) - 3, 4):
        chunk = items[start:start + 4]
        exercises.append({
            "type": "matching",
            "pairs": [{"native": c["es"], "en": c["en"]} for c in chunk],
        })

    out = {
        "id": f"es-{level}-{lesson['number']}",
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
        "id": f"es-{level}-{lesson['number']}-reading",
        "number": lesson["number"],
        "title": lesson["title"],
        "titleNative": lesson.get("titleNative", ""),
        "description": lesson.get("context", lesson["title"]),
        "readingPassage": {
            "context": lesson.get("context", lesson["title"]),
            "paragraphs": [{"native": p["es"], "en": p["en"]} for p in lesson["paragraphs"]],
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
        "id": "spanish",
        "title": "Spanish, Start to Fluent",
        "subtitle": "Latin American Spanish from real-world basics through fluent, everyday command — real sentences, real grammar, real conversation",
        "dir": "ltr",
        "lang": "es",
        "languageName": "Spanish",
        "fontNative": "'Inter', 'Noto Sans', sans-serif",
        "flag": "Español",
        "heroEyebrow": "Latin American Spanish · A2 →",
        "heroNative": "De lo esencial a la fluidez",
        "heroLedeSuffix": "Real sentences from lesson one, with genuine native-quality audio for every single line.",
        "uiStrings": {"wordHoard": "Vocabulario", "review": "Repaso", "revision": "Práctica"},
        "grammarTopics": grammar_topics,
        "levels": out_levels,
    }

    OUT_PATH.write_text(json.dumps({"course": course}, ensure_ascii=False, indent=2), encoding="utf-8")
    # round-trip validate
    json.loads(OUT_PATH.read_text(encoding="utf-8"))

    print(f"Levels: {len(out_levels)}  Lessons: {total_lessons}  Exercises: {total_exercises}  Sentences: {total_sentences}")
    for lv in out_levels:
        print(f"  {lv['id']:8s} {len(lv['lessons']):4d} lessons")


if __name__ == "__main__":
    main()
