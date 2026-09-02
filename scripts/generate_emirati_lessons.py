#!/usr/bin/env python3
"""Generate new Emirati Arabic (Khaleeji) lesson content to expand the
course from 240 toward ~800 lessons.

Design: purposeful topic blocks (professions, family, clothing, food,
health, transport, phone/tech -- the newly-researched vocabulary domains),
each composed with real topical coherence per lesson, not one uniform
randomized template. Every VERB form is copied verbatim from what's
already empirically confirmed in the shipped course; every new NOUN/
ADJECTIVE comes from data/emirati-research/researched_vocab.json (itself
cross-referenced against >=2 independent sources). Every generated
sentence is checked against verify_emirati_vocab.py before being written;
a failure here is a bug in this script, not something to silently drop.

Known real grammar gaps, respected throughout:
- بغى "want" has NO plural forms confirmed (1s/2sm/3sm/3sf only).
- شاف "see" has ONLY past-tense forms confirmed (no present).
- عند "have" has a full person paradigm confirmed.

Usage: python3 scripts/generate_emirati_lessons.py [--write]
Without --write, does a dry run (prints counts + samples, writes nothing).
With --write, appends new lessons to data/emirati-src/*.json (numbered
after the existing lessons in each file; never touches/renumbers what's
already there).
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "emirati-src"

sys.path.insert(0, str(ROOT / "scripts"))
import verify_emirati_vocab as V  # noqa: E402

random.seed(11)

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]

# ---------------------------------------------------------------------------
# Confirmed verb paradigms, copied verbatim from the shipped course.
# ---------------------------------------------------------------------------
GO_PRESENT = {"1s": "أروح", "2sm": "تروح", "2sf": "تروحين", "3sm": "يروح",
              "3sf": "تروح", "1p": "نروح", "2p": "تروحون", "3p": "يروحون"}
GO_PAST = {"1s": "رحت", "2sm": "رحت", "2sf": "رحتي", "3sm": "راح",
           "3sf": "راحت", "1p": "رحنا", "2p": "رحتو", "3p": "راحو"}
DRINK_PRESENT = {"1s": "أشرب", "2sm": "تشرب", "2sf": "تشربين", "3sm": "يشرب",
                 "3sf": "تشرب", "1p": "نشرب", "2p": "تشربون", "3p": "يشربون"}
WANT_PRESENT = {"1s": "أبغى", "2sm": "تبغى", "3sm": "يبغى", "3sf": "تبغى"}
KNOW_PRESENT = {"1s": "أدري", "2sm": "تدري", "2sf": "تدرين", "3sm": "يدري",
                "3sf": "تدري", "1p": "ندري", "2p": "تدرون", "3p": "يدرون"}
SEE_PAST = {"1s": "شفت", "3sm": "شاف", "3sf": "شافت", "3p": "شافو"}
HAVE = {"1s": "عندي", "2sm": "عندك", "3sm": "عنده", "3sf": "عندها",
        "1p": "عندنا", "2p": "عندكم", "3p": "عندهم"}

BECAUSE = "لأن"
AND = "و"
REASONS = ["تعبان كثير", "عطشان كثير", "مريض كثير", "مشغولين كثير", "مستعجل كثير"]

# ---------------------------------------------------------------------------
# New topic vocabulary (from data/emirati-research/researched_vocab.json)
# ---------------------------------------------------------------------------
PROFESSIONS = [("مدرس", "a teacher"), ("مهندس", "an engineer"), ("مترجم", "a translator"),
               ("تاجر", "a merchant"), ("كاتب", "a clerk"), ("دريول", "a driver"),
               ("ميكانيكي", "a mechanic"), ("سكرتير", "a secretary")]
FAMILY_EXT_G = [("خالي", "my maternal uncle", False), ("خالتي", "my maternal aunt", True),
                ("عمي", "my paternal uncle", False), ("عمتي", "my paternal aunt", True),
                ("جدي", "my grandfather", False), ("جدتي", "my grandmother", True)]
CLOTHING = [("قميص", "a shirt"), ("بنطلون", "pants"), ("عباية", "an abaya"), ("غترة", "a headdress")]
FOOD_NEW = [("لحم", "meat"), ("بيض", "eggs"), ("سلطة", "salad")]
HEALTH = [("مستشفى", "hospital"), ("طبيب", "a doctor"), ("طبيبة", "a doctor (f)")]
TRANSPORT_NEW = [("قطار", "a train")]
PHONE = [("جوال", "a mobile phone"), ("خط", "a phone line")]
FEELINGS_NEW = [("متوتر", "stressed"), ("متضايق", "upset")]

# Objects already confirmed in the shipped course (safe everywhere).
BASE_OBJECTS = ["البيت", "المطعم", "الشغل", "قهوة", "مويه", "شاي"]


def check(ar):
    ok, bad = V.check_sentence(ar)
    if not ok:
        raise ValueError(f"Unconfirmed words {bad} in: {ar!r}")
    return ar


# ---------------------------------------------------------------------------
# Topic-block builders -- each returns a list of (title, titleNative, [(ar,en),...])
# lessons for ONE level, with real topical coherence per lesson.
# ---------------------------------------------------------------------------

def block_professions_a1():
    lessons = []
    items = []
    for word, gloss in PROFESSIONS:
        ar = check(f"هذا {word} زين، وعنده شغل زين اليوم")
        en = f"This is a good {gloss.replace('a ', '').replace('an ', '')}, and he has good work today"
        items.append({"ar": ar, "en": en})
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Professions", "المهن", chunk))
    return lessons


def block_family_ext(level_tag):
    lessons = []
    items = []
    for word, gloss, fem in FAMILY_EXT_G:
        have = "عندها" if fem else "عنده"
        his_her_house = "بيتها" if fem else "بيته"
        ar = check(f"{word} {have} بيت كبير زين، وأبغى أروح {his_her_house} بكرا")
        en = f"{gloss.capitalize()} has a big nice house, and I want to go to {'her' if fem else 'his'} house tomorrow"
        items.append({"ar": ar, "en": en})
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Extended Family", "العائلة الكبيرة", chunk))
    return lessons


def block_clothing_shopping():
    lessons = []
    items = []
    for word, gloss in CLOTHING:
        ar = check(f"أبغى {word} جديد اليوم، بس السعر غالي كثير هناك")
        en = f"I want a new {gloss} today, but the price is very expensive there"
        items.append({"ar": ar, "en": en})
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Clothes Shopping", "شراء الملابس", chunk))
    return lessons


def block_food_new():
    lessons = []
    items = []
    for word, gloss in FOOD_NEW:
        ar = check(f"أبغى {word} زين اليوم، وعندي فلوس زين المطعم")
        en = f"I want good {gloss} today, and I have good money for the restaurant"
        items.append({"ar": ar, "en": en})
    for i in range(0, len(items), 3):
        chunk = items[i:i + 3]
        if len(chunk) < 3:
            continue
        lessons.append(("Food at the Restaurant", "الأكل في المطعم", chunk))
    return lessons


def block_health():
    lessons = []
    items = [
        {"ar": check("لازم أروح المستشفى الحين، مريض كثير اليوم"),
         "en": "I have to go to the hospital now, I'm very sick today"},
        {"ar": check("لازم تروح الطبيب بكرا لأن مريض كثير"),
         "en": "You have to go to the doctor tomorrow because you're very sick"},
        {"ar": check("الطبيبة زين كثير، وعندها شغل زين في المستشفى"),
         "en": "The doctor (f) is very good, and she has good work at the hospital"},
        {"ar": check("لازم ما تروح الشغل اليوم لأن مريض كثير، لازم تروح الطبيب"),
         "en": "You shouldn't go to work today because you're very sick, you have to go to the doctor"},
    ]
    lessons.append(("At the Hospital", "في المستشفى", items))
    return lessons


def block_transport():
    items = [
        {"ar": check("رحت الشغل في القطار أمس لأن السيارة ما زينة"),
         "en": "I went to work on the train yesterday because the car isn't good"},
        {"ar": check("تروح البيت في القطار بكرا لأن مستعجل كثير"),
         "en": "You're going home on the train tomorrow because you're in a hurry"},
        {"ar": check("لازم أروح المطعم في القطار الحين لأن أخوي عنده السيارة"),
         "en": "I have to go to the restaurant on the train now because my brother has the car"},
        {"ar": check("ما أبغى أروح في القطار اليوم لأن مشغولين كثير هناك"),
         "en": "I don't want to go on the train today because it's very busy there"},
    ]
    return [("Getting Around by Train", "بالقطار", items)]


def block_phone():
    items = [
        {"ar": check("أبغى جوال جديد اليوم لأن هذا قديم كثير"),
         "en": "I want a new mobile today because this one is very old"},
        {"ar": check("عندي جوال زين اليوم، بس ما عندي خط زين هناك"),
         "en": "I have a good mobile today, but I don't have a good line there"},
        {"ar": check("لازم أدري وين جوالي الحين، ما أدري وين هو"),
         "en": "I have to know where my mobile is now, I don't know where it is"},
        {"ar": check("ما أبغى جوال غالي اليوم لأن ما عندي فلوس زين"),
         "en": "I don't want an expensive mobile today because I don't have good money"},
    ]
    return [("On the Phone", "على الجوال", items)]


def block_feelings_new():
    items = [
        {"ar": check("متوتر كثير اليوم لأن عندي شغل كثير في المطعم"),
         "en": "I'm very stressed today because I have a lot of work at the restaurant"},
        {"ar": check("متضايق كثير الحين لأن ما رحت بيت خالي أمس"),
         "en": "I'm very upset now because I didn't go to my uncle's house yesterday"},
        {"ar": check("لازم ما تروح الشغل متوتر كثير، لازم تروح بيتك الحين"),
         "en": "You shouldn't go to work very stressed, you have to go home now"},
        {"ar": check("ما أبغى أروح بيتي متضايق، أبغى أروح بيت جدي"),
         "en": "I don't want to get upset, I want to go to my grandfather's house"},
    ]
    return [("Stress and Feelings", "التوتر والمشاعر", items)]


def block_professions_past():
    items = []
    for word, gloss in PROFESSIONS:
        ar = check(f"شفت {word} زين أمس، وعنده شغل زين هناك")
        en = f"I saw a good {gloss.replace('a ', '')} yesterday, and he had good work there"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Professions Yesterday", "المهن أمس", chunk))
    return lessons


def block_family_because():
    items = []
    for word, gloss, fem in FAMILY_EXT_G:
        have = "عندها" if fem else "عنده"
        ar = check(f"أبغى أروح بيت {word} اليوم {BECAUSE} {have} فلوس زين")
        en = f"I want to go to {gloss}'s house today because {'she' if fem else 'he'} has good money"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Family and Because", "العائلة ولأن", chunk))
    return lessons


def block_clothing_lazim():
    items = []
    for word, gloss in CLOTHING:
        ar = check(f"لازم أبغى {word} جديد الحين {BECAUSE} هذا قديم كثير")
        en = f"I have to want a new {gloss.replace('a ', '').replace('an ', '')} now because this one is very old"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Clothes and Must", "الملابس ولازم", chunk))
    return lessons


def block_food_negation():
    items = []
    for word, gloss in FOOD_NEW:
        ar = check(f"ما أبغى {word} اليوم {BECAUSE} ما عندي فلوس زين")
        en = f"I don't want {gloss} today because I don't have good money"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 3):
        chunk = items[i:i + 3]
        if len(chunk) < 3:
            continue
        lessons.append(("Not Wanting Food", "ما أبغى أكل", chunk))
    return lessons


def block_health_c1():
    items = [
        {"ar": check("لازم أروح المستشفى الحين لأن مريض كثير، وأبغى الطبيب زين"),
         "en": "I have to go to the hospital now because I'm very sick, and I want a good doctor"},
        {"ar": check("لازم تروح الطبيبة بكرا لأن مريض كثير، وعندها شغل زين"),
         "en": "You have to go to the doctor (f) tomorrow because you're very sick, and she has good work"},
        {"ar": check("ما أبغى أروح المستشفى اليوم لأن مشغولين كثير، بس لازم أروح"),
         "en": "I don't want to go to the hospital today because it's very busy, but I have to go"},
        {"ar": check("خالي عنده شغل زين في المستشفى، وأبغى شغل زين هناك بعدين"),
         "en": "My uncle has good work at the hospital, and I want good work there later"},
    ]
    return [("At the Hospital, Chained", "في المستشفى، جمل مركبة", items)]


def block_transport_chain():
    items = [
        {"ar": check(f"رحت الشغل في القطار أمس {BECAUSE} السيارة ما زينة، {AND}شفت أخوي هناك"),
         "en": "I went to work on the train yesterday because the car isn't good, and I saw my brother there"},
        {"ar": check(f"تروح البيت في القطار بكرا {BECAUSE} مستعجل كثير، {AND}تشرب قهوة هناك"),
         "en": "You're going home on the train tomorrow because you're in a hurry, and you'll drink coffee there"},
        {"ar": check(f"ما أبغى أروح في القطار اليوم {BECAUSE} مشغولين كثير هناك، {AND}عندي شغل"),
         "en": "I don't want to go on the train today because it's very busy there, and I have work"},
        {"ar": check(f"لازم أروح المطعم في القطار الحين {BECAUSE} أخوي عنده السيارة، {AND}تعبان كثير"),
         "en": "I have to go to the restaurant on the train now because my brother has the car, and I'm very tired"},
    ]
    return [("Train Rides, Chained", "القطار، جمل مركبة", items)]


def block_feelings_dense():
    items = [
        {"ar": check(f"متوتر كثير اليوم {BECAUSE} عندي شغل كثير في المطعم، {AND}تعبان كثير، بس لازم أروح الشغل"),
         "en": "I'm very stressed today because I have a lot of work at the restaurant, and I'm very tired, but I have to go to work"},
        {"ar": check(f"متضايق كثير الحين {BECAUSE} ما رحت بيت خالي أمس، {AND}عنده فلوس زين هناك، بس مشغولين كثير"),
         "en": "I'm very upset now because I didn't go to my uncle's house yesterday, and he has good money there, but they're very busy"},
        {"ar": check(f"خالي متوتر كثير اليوم {BECAUSE} عنده شغل كثير في المستشفى، {AND}تعبان كثير، بس لازم يروح"),
         "en": "My uncle is very stressed today because he has a lot of work at the hospital, and he's very tired, but he has to go"},
        {"ar": check(f"جدي متضايق كثير الحين {BECAUSE} ما شاف أهله أمس، {AND}عنده بيت كبير هناك، بس بعيد كثير"),
         "en": "My grandfather is very upset now because he didn't see his family yesterday, and he has a big house there, but it's very far"},
    ]
    return [("Feelings, Dense Chain", "المشاعر، جمل كثيفة", items)]


ALL_BLOCKS = {
    "professions": block_professions_a1,
    "professions_past": block_professions_past,
    "family_ext": lambda: block_family_ext(""),
    "family_because": block_family_because,
    "clothing": block_clothing_shopping,
    "clothing_lazim": block_clothing_lazim,
    "food_new": block_food_new,
    "food_negation": block_food_negation,
    "health": block_health,
    "health_c1": block_health_c1,
    "transport": block_transport,
    "transport_chain": block_transport_chain,
    "feelings_dense": block_feelings_dense,
    "phone": block_phone,
    "feelings_new": block_feelings_new,
}


def append_to_level(level_id, new_lessons):
    """new_lessons: list of (title, titleNative, items). Appends after the
    existing lessons, numbered to continue the sequence."""
    f = SRC / f"{level_id}.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    next_num = max((l["number"] for l in d["lessons"]), default=0) + 1
    for title, native, items in new_lessons:
        d["lessons"].append({
            "number": next_num,
            "title": title,
            "titleNative": native,
            "items": items,
        })
        next_num += 1
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(new_lessons)


# Map each block to the level it's grammatically appropriate for (a1 = simple
# present/nominal sentences, matching how these topic blocks are written).
BLOCK_LEVEL = {
    "professions": "a1",
    "professions_past": "a2",
    "family_ext": "a1",
    "family_because": "b1",
    "clothing": "a1",
    "clothing_lazim": "b1plus",
    "food_new": "a1",
    "food_negation": "b2",
    "health": "b1plus",
    "health_c1": "c1",
    "transport": "a2",
    "transport_chain": "c1",
    "feelings_dense": "c2",
    "phone": "b1",
    "feelings_new": "b2plus",
}


def main():
    write = "--write" in sys.argv
    total = 0
    by_level = {}
    for name, fn in ALL_BLOCKS.items():
        lessons = fn()
        print(f"=== {name} -> {BLOCK_LEVEL[name]}: {len(lessons)} lesson(s) ===")
        for title, native, items in lessons:
            print(f"  {title} ({native}) -- {len(items)} items")
        by_level.setdefault(BLOCK_LEVEL[name], []).extend(lessons)
        total += len(lessons)

    print(f"\n{total} lessons ready across {len(by_level)} levels.")
    if not write:
        print("Dry run only -- pass --write to append these to data/emirati-src/*.json")
        return

    for level_id, lessons in by_level.items():
        n = append_to_level(level_id, lessons)
        print(f"Appended {n} lessons to {level_id}.json")


if __name__ == "__main__":
    main()
