#!/usr/bin/env python3
"""Compile lean Georgian lesson authoring data into Muhkam's baked exercise schema.

Input:  data/georgian-src/*.json -- each file: { "level": "<levelId>", "lessons": [...] }
        A lesson is either:
          regular:  { number, title, titleNative?, topicId?, items: [{ka, en, translit}] }
          reading:  { number, title, titleNative?, context?, paragraphs: [{ka, en}],
                      questions: [{question, options, answerIndex}] }
        Optionally a file may also carry { "grammarTopics": { id: {title,pattern,explanation,fact,dialogue} } }.
Output: data/courses-georgian.json -- full course document, same shape as data/courses.json.

Georgian (ISO 639-1 "ka", Kartvelian family) is written in the Mkhedruli
alphabet: 33 letters, one sound per letter, no upper/lower case. Every
item carries a `translit` in Georgia's official national romanization
(2002), with ejectives marked by an apostrophe (k' p' t' ts' ch' q'),
generated mechanically from the Georgian text at authoring time.

Content is checked word by word against the kaikki.org Georgian
Wiktionary dump (~26,000 lemmas, ~486,000 inflected surface forms
including full verb conjugation tables). Words missing from the dump are
used only when they are regular forms whose paradigm siblings are
attested, each one documented with its reason (e.g. 1sg მქვია beside
attested 2sg გქვია / 3sg ჰქვია), per the project's never-invent-forms
rule. The short copula -ა ("is", e.g. ექიმია) is accepted only on a
dictionary-confirmed host word.

Audio: Microsoft's Georgian neural voices (ka-GE-EkaNeural, female, and
ka-GE-GiorgiNeural, male, alternated per sentence) via the unofficial
`edge-tts` package, the same route as the Pashto course. No Apple or
on-device Georgian voice exists, so bundled audio is required. Voice
quality is high, so listening / listening-tap exercises are generated,
as in the Spanish course.
"""
import json
import random
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "georgian-src"
OUT_PATH = ROOT / "data" / "courses-georgian.json"

random.seed(20261118)  # deterministic distractor shuffling across runs

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]
LEVEL_META = {
    "a1": dict(cefr="A1", label="Foundations", labelNative="A1"),
    "a2": dict(cefr="A2", label="Building Blocks", labelNative="A2"),
    "b1": dict(cefr="B1", label="Everyday Fluency", labelNative="B1"),
    "b1plus": dict(cefr="B1+", label="Expanding Range", labelNative="B1+"),
    "b2": dict(cefr="B2", label="Complex Structures", labelNative="B2"),
    "b2plus": dict(cefr="B2+", label="Precision & Nuance", labelNative="B2+"),
    "c1": dict(cefr="C1", label="Advanced", labelNative="C1"),
    "c2": dict(cefr="C2", label="Mastery", labelNative="C2"),
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
        ka, en = item["ka"], item["en"]
        translit = item.get("translit")

        distractors = sample_distractors(en, level, en_pool_by_level)
        options = [en] + distractors
        random.shuffle(options)
        mc = {
            "type": "multiple-choice",
            # Must match course.lang ("ka") exactly -- app.js gates
            # transliteration display and audio lookup on
            # `ex.direction === course.lang + "-en"`.
            "direction": "ka-en",
            "prompt": ka,
            "options": options,
            "answerIndex": options.index(en),
        }
        if translit:
            mc["translit"] = translit
        exercises.append(mc)

        tokens = ka.split()
        bank = tokens[:]
        random.shuffle(bank)
        exercises.append({
            "type": "word-bank",
            "direction": "en-ka",
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
                "native": ka,
                "options": opts2,
                "answerIndex": opts2.index(en),
            })
        elif i % 3 == 1:
            exercises.append({"type": "listening-tap", "native": ka, "answer": tokens})

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
                        "native": ka,
                        "blankedEn": blanked_en,
                        "answer": blank_word,
                        "options": opts,
                    })

    for start in range(0, len(items) - 3, 4):
        chunk = items[start:start + 4]
        exercises.append({
            "type": "matching",
            "pairs": [{"native": c["ka"], "en": c["en"]} for c in chunk],
        })

    out = {
        "id": f"ka-{level}-{lesson['number']}",
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
        "id": f"ka-{level}-{lesson['number']}-reading",
        "number": lesson["number"],
        "title": lesson["title"],
        "titleNative": lesson.get("titleNative", ""),
        "description": lesson.get("context", lesson["title"]),
        "readingPassage": {
            "context": lesson.get("context", lesson["title"]),
            "paragraphs": [{"native": p["ka"], "en": p["en"]} for p in lesson["paragraphs"]],
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


# Single dictionary-confirmed Georgian words only (checked against the kaikki dump), no composed phrases.
UI_STRINGS = {"grammarNote": "გრამატიკა", "didYouKnow": "საინტერესოა", "wordHoard": "ლექსიკონი", "review": "გამეორება", "revision": "ვარჯიში"}


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
        "id": "georgian",
        "title": "Georgian, Start to Fluent",
        "subtitle": "Georgian from the alphabet to fluent command -- real sentences with transliteration and native-quality audio",
        "dir": "ltr",
        "lang": "ka",
        "languageName": "Georgian",
        "fontNative": "'Noto Sans Georgian', 'Noto Sans', sans-serif",
        "flag": "ქართული",
        "heroEyebrow": "ქართული · A1 → C2",
        "heroNative": "ქართული",
        "heroLedeSuffix": "Starts with the 33-letter alphabet, then real sentences from the first lesson.",
        "uiStrings": UI_STRINGS,
        "grammarTopics": grammar_topics,
        "levels": out_levels,
    }

    OUT_PATH.write_text(json.dumps({"course": course}, ensure_ascii=False, indent=2), encoding="utf-8")
    json.loads(OUT_PATH.read_text(encoding="utf-8"))  # round-trip validate

    print(f"Levels: {len(out_levels)}  Lessons: {total_lessons}  Exercises: {total_exercises}  Sentences: {total_sentences}")
    for lv in out_levels:
        print(f"  {lv['id']:8s} {len(lv['lessons']):4d} lessons")


if __name__ == "__main__":
    main()
