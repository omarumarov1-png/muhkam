#!/usr/bin/env python3
"""Compile lean Emirati Arabic lesson authoring data into Muhkam's baked exercise schema.

Input:  data/emirati-src/*.json -- each file: { "level": "<levelId>", "lessons": [...] }
        A lesson is either:
          regular:  { number, title, titleNative?, topicId?, items: [{ar, en, translit?}] }
          reading:  { number, title, titleNative?, context?, paragraphs: [{ar, en}],
                      questions: [{question, options, answerIndex}] }
        Optionally a file may also carry { "grammarTopics": { id: {title,pattern,explanation,fact,dialogue} } }.
Output: data/courses-emirati.json -- full course document, same shape as data/courses.json.

Emirati Arabic (Khaleeji/Gulf Arabic dialect, ISO 639-3 "afb" Gulf Arabic
umbrella code) is a SPOKEN dialect with no official standard orthography
and no dedicated Wiktionary lang-code dump -- unlike Standard Arabic,
German, French, Spanish, etc. Content was sourced by cross-referencing
multiple academic/pedagogical Gulf Arabic references (Wikipedia's
"Emirati Arabic" and "Gulf Arabic" articles, gulfarabic.com's structured
lessons, Amin Academy's Gulf Arabic course) rather than a single
dictionary, and every grammatical pattern used was corroborated across at
least two independent sources before being treated as safe to build on.
This is a stricter, more conservative sourcing discipline than the other
"world" language courses (Spanish/French/German), closer in spirit to
Muhkam's underserved-language builds (Pashto/Turkmen's sparse-dictionary
workarounds).

Confirmed grammatical skeleton (see scratchpad's grammar-notes.md for
full citations):
- Independent pronouns: انا (ana) I, انت (inta) you-m, انتي (inti) you-f,
  هو (huwa) he, هي (hiya) she, احنا (i7na) we, انتوا (intu) you-pl,
  هم (humma) they.
- No copula "to be" in the present tense (nominal sentences).
- Present tense: prefix conjugation, أ-/تِ-/تِ-...ين/يِ-/تِ-/نِ-/تِ-...ون/يِ-...ون
  (a-/ti-/ti-...iin/yi-/ti-/ni-/ti-...uun/yi-...uun).
- Past tense: suffix conjugation (e.g. شفت shift "I saw", شاف shaaf "he saw",
  شافت shaafat "she saw", شفنا shifna "we saw", شافوا shaafaw "they saw").
- Negation: ما (ma) prefixed to verbs; مب (mub) for nominal/equational
  sentences (Northern Emirates variant, most widely recognized).
- Question words: شنو (shinu) what, وين (wein) where, ليش (leish) why,
  شلون/شحال (shlon/sh7al) how, متى (mita) when, مِنو (minu) who.

TTS: Voicebox qwen engine, "designed" (text-prompted) voice profile
prompted for a Gulf/Khaleeji accent -- no Kokoro Arabic preset voice
exists, and a generic MSA-trained voice would likely default to
Modern-Standard phonology for dialectal spellings. User-confirmed
acceptable quality on a test sample before content began.

Encoding note: standard Arabic-script codepoints throughout (no
Persian-specific ی/ک substitution issue like Dari/Urdu face) -- but scan
for accidental Persian-script lookalikes if any content is ever copied
from a Farsi/Urdu/Pashto source by mistake.
"""
import json
import random
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "emirati-src"
OUT_PATH = ROOT / "data" / "courses-emirati.json"

random.seed(20260829)  # deterministic distractor shuffling across runs

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]
LEVEL_META = {
    "a1": dict(cefr="A1", label="Foundations", labelNative="الأساسيات"),
    "a2": dict(cefr="A2", label="Building Blocks", labelNative="لبنات البناء"),
    "b1": dict(cefr="B1", label="Everyday Fluency", labelNative="الطلاقة اليومية"),
    "b1plus": dict(cefr="B1+", label="Expanding Range", labelNative="توسيع المدى"),
    "b2": dict(cefr="B2", label="Complex Structures", labelNative="تراكيب معقدة"),
    "b2plus": dict(cefr="B2+", label="Precision & Nuance", labelNative="الدقة والفروق"),
    "c1": dict(cefr="C1", label="Advanced", labelNative="متقدم"),
    "c2": dict(cefr="C2", label="Mastery", labelNative="إتقان"),
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
        ar, en = item["ar"], item["en"]
        translit = item.get("translit")

        distractors = sample_distractors(en, level, en_pool_by_level)
        options = [en] + distractors
        random.shuffle(options)
        mc = {
            "type": "multiple-choice",
            # Must match course.lang ("afb", Gulf Arabic's ISO 639-3 code,
            # set below in main()) exactly -- app.js's exercise-rendering
            # and audio-lookup logic gates on `ex.direction === course.lang
            # + "-en"` in three separate places.
            "direction": "afb-en",
            "prompt": ar,
            "options": options,
            "answerIndex": options.index(en),
        }
        if translit:
            mc["translit"] = translit
        exercises.append(mc)

        tokens = ar.split()
        bank = tokens[:]
        random.shuffle(bank)
        exercises.append({
            "type": "word-bank",
            "direction": "en-afb",
            "prompt": en,
            "bank": bank,
            "answer": tokens,
        })

        listen_options = [en] + sample_distractors(en, level, en_pool_by_level)
        random.shuffle(listen_options)
        exercises.append({
            "type": "listening",
            "native": ar,
            "options": listen_options,
            "answerIndex": listen_options.index(en),
        })

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
                        "native": ar,
                        "blankedEn": blanked_en,
                        "answer": blank_word,
                        "options": opts,
                    })

    for start in range(0, len(items) - 3, 4):
        chunk = items[start:start + 4]
        exercises.append({
            "type": "matching",
            "pairs": [{"native": c["ar"], "en": c["en"]} for c in chunk],
        })

    out = {
        "id": f"afb-{level}-{lesson['number']}",
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
        "id": f"afb-{level}-{lesson['number']}-reading",
        "number": lesson["number"],
        "title": lesson["title"],
        "titleNative": lesson.get("titleNative", ""),
        "description": lesson.get("context", lesson["title"]),
        "readingPassage": {
            "context": lesson.get("context", lesson["title"]),
            "paragraphs": [{"native": p["ar"], "en": p["en"]} for p in lesson["paragraphs"]],
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
        "id": "emirati",
        "title": "Emirati Arabic, Start to Fluent",
        "subtitle": "Khaleeji Gulf Arabic as spoken in the UAE, from absolute beginner through fluent, everyday command",
        "dir": "rtl",
        "lang": "afb",
        "languageName": "Emirati Arabic",
        "fontNative": "'Noto Naskh Arabic', 'Noto Sans Arabic', serif",
        "flag": "الإماراتية",
        "heroEyebrow": "خليجي · A1 → C2",
        "heroNative": "من الألف للياء",
        "heroLedeSuffix": "Real spoken Emirati sentences from lesson one, with transliteration and native-style audio for every line.",
        "uiStrings": {"grammarNote": "قاعدة", "didYouKnow": "تعرف؟"},
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
