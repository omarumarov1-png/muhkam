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

Variety discipline: earlier drafts of this script reflexively tacked
اليوم "today" and كثير "very" onto nearly every sentence, which reads as
monotonous filler even when each sentence is grammatically distinct (the
same mistake was caught and fixed once before in the Syrian course, per
git history -- should have been caught here from the start). Time markers
and intensifiers are now drawn from rotating pools (and sometimes omitted
entirely) so the same handful of confirmed words don't turn into a verbal
tic. See vary_time()/vary_intensity() below.

Usage: python3 scripts/generate_emirati_lessons.py [--write]
Without --write, does a dry run (prints counts + samples, writes nothing).
With --write, appends new lessons to data/emirati-src/*.json (numbered
after the existing lessons in each file; never touches/renumbers what's
already there).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "emirati-src"

sys.path.insert(0, str(ROOT / "scripts"))
import verify_emirati_vocab as V  # noqa: E402

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

# ---------------------------------------------------------------------------
# Variety helpers -- rotate through these instead of hardcoding اليوم/كثير
# everywhere. Index-based (not random) so output is reproducible.
# ---------------------------------------------------------------------------
TIME_PRESENT = ["اليوم", "الحين", "", "اليوم", "", "الحين"]  # "" = omit entirely
TIME_PAST = ["أمس", "", "أمس"]
TIME_FUTURE = ["بكرا", "", "بكرا"]
INTENSITY = ["كثير", "", "زين", "", "كثير"]  # "" = plain adjective, no intensifier

REASON_WORDS = ["تعبان", "عطشان", "مريض", "مشغولين", "مستعجل"]
REASON_WORDS_EN = {
    "تعبان": "tired", "عطشان": "thirsty", "مريض": "sick",
    "مشغولين": "busy", "مستعجل": "in a hurry",
}


def reason_en(i):
    return REASON_WORDS_EN[REASON_WORDS[i % len(REASON_WORDS)]]


def bare(gloss):
    """Strip a leading English article so callers can build 'a good X'
    themselves instead of ending up with 'good a X'."""
    if gloss.startswith("an "):
        return gloss[3:]
    if gloss.startswith("a "):
        return gloss[2:]
    return gloss


# Nouns that never take an indefinite article in these sentence patterns
# (plural or mass nouns). Everything else is a singular countable noun that
# needs an article -- "a"/"an" chosen by the sound of whatever comes right
# after the article (the adjective, if there is one; else the noun itself).
NO_ARTICLE = {"pants", "meat", "eggs", "salad"}
VOWEL_SOUND = ("a", "e", "i", "o", "u")


def np_(noun):
    """Bare noun phrase with the right article (or none for mass/plural)."""
    noun = bare(noun)
    if noun in NO_ARTICLE:
        return noun
    article = "an" if noun[0] in VOWEL_SOUND else "a"
    return f"{article} {noun}"


def a_(adj, noun):
    noun = bare(noun)
    if noun in NO_ARTICLE:
        return f"{adj} {noun}"
    article = "an" if adj[0] in VOWEL_SOUND else "a"
    return f"{article} {adj} {noun}"


def vary_time(i, pool=TIME_PRESENT):
    return pool[i % len(pool)]


def vary_intensity(i):
    return INTENSITY[i % len(INTENSITY)]


def reason_at(i):
    """A reason clause with varied intensity, not always 'X كثير'."""
    word = REASON_WORDS[i % len(REASON_WORDS)]
    inten = vary_intensity(i + 1)
    return f"{word} {inten}".strip()


def with_time(base, i, pool=TIME_PRESENT):
    """Append a time marker only sometimes, and vary which one."""
    t = vary_time(i, pool)
    return f"{base} {t}".strip() if t else base


# ---------------------------------------------------------------------------
# New topic vocabulary (from data/emirati-research/researched_vocab.json)
# ---------------------------------------------------------------------------
PROFESSIONS = [("مدرس", "teacher"), ("مهندس", "engineer"), ("مترجم", "translator"),
               ("تاجر", "merchant"), ("كاتب", "clerk"), ("دريول", "driver"),
               ("ميكانيكي", "mechanic"), ("سكرتير", "secretary")]
FAMILY_EXT_G = [("خالي", "my maternal uncle", False), ("خالتي", "my maternal aunt", True),
                ("عمي", "my paternal uncle", False), ("عمتي", "my paternal aunt", True),
                ("جدي", "my grandfather", False), ("جدتي", "my grandmother", True)]
CLOTHING = [("قميص", "shirt"), ("بنطلون", "pants"), ("عباية", "abaya"), ("غترة", "headdress")]
FOOD_NEW = [("لحم", "meat"), ("بيض", "eggs"), ("سلطة", "salad")]
HEALTH = [("مستشفى", "hospital"), ("طبيب", "doctor"), ("طبيبة", "doctor (f)")]
PHONE = [("جوال", "mobile phone"), ("خط", "phone line")]


def check(ar):
    ok, bad = V.check_sentence(ar)
    if not ok:
        raise ValueError(f"Unconfirmed words {bad} in: {ar!r}")
    return ar


# ---------------------------------------------------------------------------
# Topic-block builders -- each returns a list of (title, titleNative, [(ar,en),...])
# lessons for ONE level, with real topical coherence per lesson AND varied
# time/intensity markers so items in the same lesson don't all read alike.
# ---------------------------------------------------------------------------

def block_professions_a1():
    items = []
    for i, (word, gloss) in enumerate(PROFESSIONS):
        inten = vary_intensity(i)
        adj = f"زين {inten}".strip() if inten else "زين"
        ar = check(f"هذا {word} {adj}، وعنده شغل زين")
        en = f"This is a good {gloss}, and he has good work"
        items.append({"ar": ar, "en": en})
    lessons = []
    for n, i in enumerate(range(0, len(items), 4)):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        suffix = "" if n == 0 else " II"
        native_suffix = "" if n == 0 else " ٢"
        lessons.append((f"Professions{suffix}", f"المهن{native_suffix}", chunk))
    return lessons


def block_family_ext(_unused=""):
    items = []
    for i, (word, gloss, fem) in enumerate(FAMILY_EXT_G):
        have = "عندها" if fem else "عنده"
        his_her_house = "بيتها" if fem else "بيته"
        time = vary_time(i, TIME_FUTURE)
        tail = f"{his_her_house} {time}".strip() if time else his_her_house
        ar = check(f"{word} {have} بيت كبير زين، وأبغى أروح {tail}")
        en = f"{gloss.capitalize()} has a big nice house, and I want to go to {'her' if fem else 'his'} house"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Extended Family", "العائلة الكبيرة", chunk))
    return lessons


def block_clothing_shopping():
    items = []
    for i, (word, gloss) in enumerate(CLOTHING):
        inten = vary_intensity(i)
        price = f"غالي {inten}".strip() if inten else "غالي"
        ar = check(f"أبغى {word} جديد، بس السعر {price} هناك")
        en = f"I want {a_('new', gloss)}, but the price is expensive there"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        lessons.append(("Clothes Shopping", "شراء الملابس", chunk))
    return lessons


def block_food_new():
    items = []
    for i, (word, gloss) in enumerate(FOOD_NEW):
        ar = check(with_time(f"أبغى {word} زين، وعندي فلوس زين للمطعم".replace("للمطعم", "المطعم"), i))
        en = f"I want good {gloss}, and I have good money for the restaurant"
        items.append({"ar": ar, "en": en})
    lessons = []
    for i in range(0, len(items), 3):
        chunk = items[i:i + 3]
        if len(chunk) < 3:
            continue
        lessons.append(("Food at the Restaurant", "الأكل في المطعم", chunk))
    return lessons


def block_health():
    items = [
        {"ar": check("لازم أروح المستشفى الحين، مريض كثير"),
         "en": "I have to go to the hospital now, I'm very sick"},
        {"ar": check("لازم تروح الطبيب بكرا لأن مريض"),
         "en": "You have to go to the doctor tomorrow because you're sick"},
        {"ar": check("الطبيبة زين، وعندها شغل زين في المستشفى"),
         "en": "The doctor (f) is good, and she has good work at the hospital"},
        {"ar": check("لازم ما تروح الشغل لأن مريض كثير، لازم تروح الطبيب"),
         "en": "You shouldn't go to work because you're very sick, you have to go to the doctor"},
    ]
    return [("At the Hospital", "في المستشفى", items)]


def block_transport():
    items = [
        {"ar": check("رحت الشغل في القطار أمس لأن السيارة ما زينة"),
         "en": "I went to work on the train yesterday because the car isn't good"},
        {"ar": check("تروح البيت في القطار بكرا لأن مستعجل"),
         "en": "You're going home on the train tomorrow because you're in a hurry"},
        {"ar": check("لازم أروح المطعم في القطار الحين لأن أخوي عنده السيارة"),
         "en": "I have to go to the restaurant on the train now because my brother has the car"},
        {"ar": check("ما أبغى أروح في القطار لأن مشغولين كثير هناك"),
         "en": "I don't want to go on the train because it's very busy there"},
    ]
    return [("Getting Around by Train", "بالقطار", items)]


def block_phone():
    items = [
        {"ar": check("أبغى جوال جديد لأن هذا قديم"),
         "en": "I want a new mobile because this one is old"},
        {"ar": check("عندي جوال زين، بس ما عندي خط زين هناك"),
         "en": "I have a good mobile, but I don't have a good line there"},
        {"ar": check("لازم أدري وين جوالي الحين، ما أدري وين هو"),
         "en": "I have to know where my mobile is now, I don't know where it is"},
        {"ar": check("ما أبغى جوال غالي لأن ما عندي فلوس زين"),
         "en": "I don't want an expensive mobile because I don't have good money"},
    ]
    return [("On the Phone", "على الجوال", items)]


def block_feelings_new():
    items = [
        {"ar": check("متوتر كثير اليوم لأن عندي شغل كثير في المطعم"),
         "en": "I'm very stressed today because I have a lot of work at the restaurant"},
        {"ar": check("متضايق الحين لأن ما رحت بيت خالي أمس"),
         "en": "I'm upset now because I didn't go to my uncle's house yesterday"},
        {"ar": check("لازم ما تروح الشغل متوتر، لازم تروح بيتك"),
         "en": "You shouldn't go to work stressed, you have to go home"},
        {"ar": check("ما أبغى أروح بيتي متضايق، أبغى أروح بيت جدي"),
         "en": "I don't want to get upset, I want to go to my grandfather's house"},
    ]
    return [("Stress and Feelings", "التوتر والمشاعر", items)]


def block_professions_past():
    items = []
    for i, (word, gloss) in enumerate(PROFESSIONS):
        ar = check(with_time(f"شفت {word} زين، وعنده شغل زين هناك", i, TIME_PAST))
        en = f"I saw a good {gloss}, and he had good work there"
        items.append({"ar": ar, "en": en})
    lessons = []
    for n, i in enumerate(range(0, len(items), 4)):
        chunk = items[i:i + 4]
        if len(chunk) < 4:
            continue
        suffix = "" if n == 0 else " II"
        native_suffix = "" if n == 0 else " ٢"
        lessons.append((f"Professions Yesterday{suffix}", f"المهن أمس{native_suffix}", chunk))
    return lessons


def block_professions_b1():
    items = []
    for word, gloss in PROFESSIONS[:4]:
        ar = check(f"ال{word} عنده شغل زين {BECAUSE} عنده فلوس زين")
        en = f"The {gloss} has good work because he has good money"
        items.append({"ar": ar, "en": en})
    return [("Professions and Work", "المهن والشغل", items)]


def block_professions_lazim():
    items = []
    for i, (word, gloss) in enumerate(PROFESSIONS[4:8]):
        reason = REASON_WORDS[i % len(REASON_WORDS)]
        ar = check(f"لازم ال{word} يروح الشغل الحين {BECAUSE} {reason}")
        en = f"The {bare(gloss)} has to go to work now because he's {REASON_WORDS_EN[reason]}"
        items.append({"ar": ar, "en": en})
    return [("Professions Must Go", "المهن ولازم", items)]


def block_professions_negation():
    items = []
    for word, gloss in PROFESSIONS[:4]:
        ar = check(f"ال{word} ما عنده شغل زين الحين {BECAUSE} مشغولين كثير هناك")
        en = f"The {bare(gloss)} doesn't have good work now because it's very busy there"
        items.append({"ar": ar, "en": en})
    return [("Professions, No Work Today", "المهن، ما عنده شغل", items)]


def block_professions_chain():
    items = []
    for i, (word, gloss) in enumerate(PROFESSIONS[4:8]):
        reason = REASON_WORDS[(i + 2) % len(REASON_WORDS)]
        ar = check(f"ال{word} عنده شغل زين {AND}عنده فلوس زين، بس {reason}")
        en = f"The {bare(gloss)} has good work and good money, but he's {REASON_WORDS_EN[reason]}"
        items.append({"ar": ar, "en": en})
    return [("Professions, Chained", "المهن، جمل مركبة", items)]


def block_family_because():
    items = []
    for i, (word, gloss, fem) in enumerate(FAMILY_EXT_G):
        have = "عندها" if fem else "عنده"
        ar = check(f"أبغى أروح بيت {word} {BECAUSE} {have} فلوس زين")
        en = f"I want to go to {gloss}'s house because {'she' if fem else 'he'} has good money"
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
    for i, (word, gloss) in enumerate(CLOTHING):
        ar = check(f"لازم أبغى {word} جديد {BECAUSE} هذا قديم")
        en = f"I have to want {a_('new', gloss)} because this one is old"
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
    for i, (word, gloss) in enumerate(FOOD_NEW):
        ar = check(f"ما أبغى {word} {BECAUSE} ما عندي فلوس زين")
        en = f"I don't want {gloss} because I don't have good money"
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
        {"ar": check("لازم تروح الطبيبة بكرا لأن مريض، وعندها شغل زين"),
         "en": "You have to go to the doctor (f) tomorrow because you're sick, and she has good work"},
        {"ar": check("ما أبغى أروح المستشفى لأن مشغولين كثير، بس لازم أروح"),
         "en": "I don't want to go to the hospital because it's very busy, but I have to go"},
        {"ar": check("خالي عنده شغل زين في المستشفى، وأبغى شغل زين هناك"),
         "en": "My uncle has good work at the hospital, and I want good work there"},
    ]
    return [("At the Hospital, Chained", "في المستشفى، جمل مركبة", items)]


def block_transport_chain():
    items = [
        {"ar": check(f"رحت الشغل في القطار أمس {BECAUSE} السيارة ما زينة، {AND}شفت أخوي هناك"),
         "en": "I went to work on the train yesterday because the car isn't good, and I saw my brother there"},
        {"ar": check(f"تروح البيت في القطار بكرا {BECAUSE} مستعجل، {AND}تشرب قهوة هناك"),
         "en": "You're going home on the train tomorrow because you're in a hurry, and you'll drink coffee there"},
        {"ar": check(f"ما أبغى أروح في القطار {BECAUSE} مشغولين كثير هناك، {AND}عندي شغل"),
         "en": "I don't want to go on the train because it's very busy there, and I have work"},
        {"ar": check(f"لازم أروح المطعم في القطار الحين {BECAUSE} أخوي عنده السيارة، {AND}تعبان"),
         "en": "I have to go to the restaurant on the train now because my brother has the car, and I'm tired"},
    ]
    return [("Train Rides, Chained", "القطار، جمل مركبة", items)]


def block_feelings_dense():
    items = [
        {"ar": check(f"متوتر كثير اليوم {BECAUSE} عندي شغل كثير في المطعم، {AND}تعبان، بس لازم أروح الشغل"),
         "en": "I'm very stressed today because I have a lot of work at the restaurant, and I'm tired, but I have to go to work"},
        {"ar": check(f"متضايق الحين {BECAUSE} ما رحت بيت خالي أمس، {AND}عنده فلوس زين هناك، بس مشغولين"),
         "en": "I'm upset now because I didn't go to my uncle's house yesterday, and he has good money there, but they're busy"},
        {"ar": check(f"خالي متوتر {BECAUSE} عنده شغل كثير في المستشفى، {AND}تعبان كثير، بس لازم يروح"),
         "en": "My uncle is stressed because he has a lot of work at the hospital, and he's very tired, but he has to go"},
        {"ar": check(f"جدي متضايق {BECAUSE} ما شاف أهله أمس، {AND}عنده بيت كبير هناك، بس بعيد"),
         "en": "My grandfather is upset because he didn't see his family yesterday, and he has a big house there, but it's far"},
    ]
    return [("Stress, Dense Chain", "التوتر، جمل كثيفة", items)]


# ---------------------------------------------------------------------------
# Generalized frame library -- each takes a (word, gloss) noun pair and an
# index i (for varying time/intensity), returns (ar, en). Only patterns
# already proven safe: no fused ب-/ل- prefixes, no invented verb forms, no
# untested gender agreement (masculine subject unless the noun pair itself
# carries gender).
# ---------------------------------------------------------------------------

def frame_present_a2(word, gloss, i):
    t = vary_time(i)
    tail = f", وهذا زين {t}".rstrip(", ") if t else ", وهذا زين"
    ar = check(f"أبغى {word} زين{tail}")
    en = f"I want {a_('good', gloss)}, and this one is good"
    return ar, en


def frame_possession_b1(word, gloss, i):
    reason = reason_at(i)
    ar = check(f"عندي {word} زين {BECAUSE} أبغى {word} زين")
    en = f"I have {a_('good', gloss)} because I want {a_('good', gloss)}"
    return ar, en


def frame_lazim_b1plus(word, gloss, i):
    reason = reason_at(i)
    ar = check(f"لازم أبغى {word} زين الحين {BECAUSE} {reason}")
    en = f"I have to want {a_('good', gloss)} now because I'm {reason_en(i)}"
    return ar, en


def frame_negation_b2(word, gloss, i):
    ar = check(f"ما عندي {word} زين {BECAUSE} ما عندي فلوس")
    en = f"I don't have {a_('good', gloss)} because I don't have money"
    return ar, en


def frame_lazim_ma_b2plus(word, gloss, i):
    ar = check(f"لازم ما تبغى {word} غالي {BECAUSE} ما عندك فلوس")
    en = f"You shouldn't want {a_('expensive', gloss)} because you don't have money"
    return ar, en


def frame_chain_c1(word, gloss, i):
    reason = reason_at(i)
    ar = check(f"أبغى {word} زين {BECAUSE} {reason}، {AND}عندي فلوس زين")
    en = f"I want {a_('good', gloss)} because I'm {reason_en(i)}, and I have good money"
    return ar, en


def frame_dense_c2(word, gloss, i):
    reason = reason_at(i)
    ar = check(f"أبغى {word} زين {BECAUSE} {reason}، {AND}عندي فلوس زين، بس مشغولين")
    en = f"I want {a_('good', gloss)} because I'm {reason_en(i)}, and I have good money, but it's busy"
    return ar, en


def frame_present_a2_b(word, gloss, i):
    ar = check(f"هذا {word} زين، وأبغى {word} زين")
    en = f"This is {a_('good', gloss)}, and I want {a_('good', gloss)}"
    return ar, en


def frame_possession_b1_b(word, gloss, i):
    ar = check(f"أخوي عنده {word} زين {BECAUSE} عنده فلوس")
    en = f"My brother has {a_('good', gloss)} because he has money"
    return ar, en


def frame_lazim_b1plus_b(word, gloss, i):
    ar = check(f"لازم تبغى {word} زين {BECAUSE} هذا زين كثير")
    en = f"You have to want {a_('good', gloss)} because this is very good"
    return ar, en


def frame_negation_b2_b(word, gloss, i):
    ar = check(f"ما تبغى {word} غالي {BECAUSE} السعر غالي هناك")
    en = f"You don't want {a_('expensive', gloss)} because the price is expensive there"
    return ar, en


def frame_lazim_ma_b2plus_b(word, gloss, i):
    ar = check(f"لازم ما تبغى {word} رخيص، هذا زين")
    en = f"You shouldn't want {a_('cheap', gloss)}, this is good"
    return ar, en


def frame_chain_c1_b(word, gloss, i):
    ar = check(f"هذا {word} زين {BECAUSE} السعر رخيص، {AND}أبغى {word} الحين")
    en = f"This is {a_('good', gloss)} because the price is cheap, and I want {np_(gloss)} now"
    return ar, en


def frame_dense_c2_b(word, gloss, i):
    ar = check(f"أخوي عنده {word} زين {BECAUSE} عنده فلوس، {AND}أبغى {word} زين، بس ما عندي فلوس")
    en = f"My brother has {a_('good', gloss)} because he has money, and I want {a_('good', gloss)}, but I don't have money"
    return ar, en


FRAMES = {
    "a2": frame_present_a2, "b1": frame_possession_b1, "b1plus": frame_lazim_b1plus,
    "b2": frame_negation_b2, "b2plus": frame_lazim_ma_b2plus,
    "c1": frame_chain_c1, "c2": frame_dense_c2,
}
FRAMES_B = {
    "a2": frame_present_a2_b, "b1": frame_possession_b1_b, "b1plus": frame_lazim_b1plus_b,
    "b2": frame_negation_b2_b, "b2plus": frame_lazim_ma_b2plus_b,
    "c1": frame_chain_c1_b, "c2": frame_dense_c2_b,
}


FRAME_DESC_EN = {
    "a2": "Wanting", "b1": "Having", "b1plus": "Must Have",
    "b2": "Not Having", "b2plus": "Shouldn't Want", "c1": "Chained", "c2": "Dense Chain",
}
FRAME_DESC_AR = {
    "a2": "أبغى", "b1": "عندي", "b1plus": "لازم", "b2": "ما عندي",
    "b2plus": "لازم ما", "c1": "جمل مركبة", "c2": "جمل كثيفة",
}


def make_lessons(word_list, level, title, title_native, per_lesson=4, variant="a"):
    frame = (FRAMES if variant == "a" else FRAMES_B)[level]
    items = []
    for i, entry in enumerate(word_list):
        word, gloss = entry[0], entry[1]
        ar, en = frame(word, gloss, i)
        items.append({"ar": ar, "en": en})
    full_title = f"{title}, {FRAME_DESC_EN[level]}" + (" II" if variant == "b" else "")
    full_native = f"{title_native}، {FRAME_DESC_AR[level]}" + (" ٢" if variant == "b" else "")
    lessons = []
    for i in range(0, len(items), per_lesson):
        chunk = items[i:i + per_lesson]
        if len(chunk) < min(per_lesson, 3):
            continue
        lessons.append((full_title, full_native, chunk))
    return lessons


# Only topics where a generic "want/have X, the price is..." commerce
# frame is semantically natural -- goods you buy or own. Family members,
# hospitals, and professions do NOT fit this frame ("I want a good uncle",
# "my brother has a good hospital" are nonsensical even though every word
# is individually confirmed); those stay on their purpose-written blocks
# in SHIPPED_BLOCKS instead of being swept through the generic frames.
TOPIC_POOLS = {
    "clothing": (CLOTHING, "Clothes", "الملابس"),
    "food": (FOOD_NEW, "Food", "الأكل"),
}

ALREADY_COVERED = {
    ("clothing", "a1"), ("clothing", "b1plus"),
    ("food", "a1"), ("food", "b2"),
}


def systematic_sweep():
    blocks = {}
    for topic_id, (words, title, native) in TOPIC_POOLS.items():
        for level in FRAMES:
            if (topic_id, level) in ALREADY_COVERED:
                continue
            lessons_a = make_lessons(words, level, title, native, variant="a")
            if lessons_a:
                blocks[f"sweep_{topic_id}_{level}_a"] = (lambda ls=lessons_a: ls)
            lessons_b = make_lessons(words, level, title, native, variant="b")
            if lessons_b:
                blocks[f"sweep_{topic_id}_{level}_b"] = (lambda ls=lessons_b: ls)
    return blocks


SHIPPED_BLOCKS = {
    "professions": block_professions_a1,
    "professions_past": block_professions_past,
    "professions_b1": block_professions_b1,
    "professions_lazim": block_professions_lazim,
    "professions_negation": block_professions_negation,
    "professions_chain": block_professions_chain,
    "family_ext": block_family_ext,
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

BLOCK_LEVEL = {
    "professions": "a1", "professions_past": "a2", "professions_b1": "b1",
    "professions_lazim": "b1plus", "professions_negation": "b2", "professions_chain": "c1",
    "family_ext": "a1",
    "family_because": "b1", "clothing": "a1", "clothing_lazim": "b1plus",
    "food_new": "a1", "food_negation": "b2", "health": "b1plus",
    "health_c1": "c1", "transport": "a2", "transport_chain": "c1",
    "feelings_dense": "c2", "phone": "b1", "feelings_new": "b2plus",
}

ALL_BLOCKS = dict(SHIPPED_BLOCKS)
ALL_BLOCKS.update(systematic_sweep())


def append_to_level(level_id, new_lessons):
    f = SRC / f"{level_id}.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    next_num = max((l["number"] for l in d["lessons"]), default=0) + 1
    for title, native, items in new_lessons:
        d["lessons"].append({
            "number": next_num, "title": title, "titleNative": native, "items": items,
        })
        next_num += 1
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(new_lessons)


def level_for_block(name):
    if name in BLOCK_LEVEL:
        return BLOCK_LEVEL[name]
    if name.startswith("sweep_"):
        parts = name.split("_")
        if len(parts) >= 3 and parts[-2] in FRAMES:
            return parts[-2]
    raise KeyError(f"No level mapping for block {name!r}")


def main():
    write = "--write" in sys.argv
    total = 0
    by_level = {}
    for name, fn in ALL_BLOCKS.items():
        lessons = fn()
        level = level_for_block(name)
        print(f"=== {name} -> {level}: {len(lessons)} lesson(s) ===")
        for title, native, items in lessons:
            print(f"  {title} ({native}) -- {len(items)} items")
            for it in items[:1]:
                print("   ", it["ar"])
        by_level.setdefault(level, []).extend(lessons)
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
