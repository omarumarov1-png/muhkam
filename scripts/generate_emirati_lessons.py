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

# Both topics were fully swept across every level in the previous batch
# (already shipped/committed) -- mark every level covered so a re-run of
# this script never re-appends the same sweep content a second time.
ALREADY_COVERED = {(topic, lvl) for topic in ("clothing", "food") for lvl in FRAMES}


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


# ---------------------------------------------------------------------------
# Second research round: weather, household, animals, numbers 13-100, and
# five new verbs (eat/cook/work/love/sleep) confirmed via researched_vocab.json
# ("verbs" section). Only confirmed persons are used -- see that file for the
# exact sourcing per form. Ambiguous forms (identical script across two
# different persons, e.g. طبخت for both 2sm and 3sf) are always given an
# explicit subject pronoun to disambiguate.
# ---------------------------------------------------------------------------

def block_weather_a1():
    items = [
        {"ar": check("الجو حار اليوم"), "en": "The weather is hot today"},
        {"ar": check("الجو بارد"), "en": "The weather is cold"},
        {"ar": check("الجو مشمس بكرا"), "en": "It's sunny tomorrow"},
        {"ar": check("فيه ريح الحين"), "en": "There's wind now"},
    ]
    return [("Weather", "الجو", items)]


def block_weather_lazim():
    items = [
        {"ar": check("فيه ريح، ما أبغى أروح الحين"), "en": "There's wind, I don't want to go now"},
        {"ar": check("فيه مطر، لازم أروح البيت"), "en": "There's rain, I have to go home"},
        {"ar": check("الجو بارد، لازم أروح البيت"), "en": "It's cold, I have to go home"},
        {"ar": check("الجو حار كثير، ما أبغى أروح الشغل"), "en": "It's very hot, I don't want to go to work"},
    ]
    return [("Weather and Must", "الجو ولازم", items)]


def block_household_a1():
    items = [
        {"ar": check("في البيت فيه باب زين"), "en": "In the house there's a good door"},
        {"ar": check("في البيت فيه دريشة زين"), "en": "In the house there's a good window"},
        {"ar": check("في البيت فيه مطبخ زين"), "en": "In the house there's a good kitchen"},
    ]
    return [("Around the House", "البيت", items)]


def block_household_a2():
    items = [
        {"ar": check("عندي طاولة زين في المطبخ"), "en": "I have a good table in the kitchen"},
        {"ar": check("عندي كرسي زين في المطبخ"), "en": "I have a good chair in the kitchen"},
        {"ar": check("عندي صحن زين في المطبخ"), "en": "I have a good plate in the kitchen"},
    ]
    return [("Furniture", "الأثاث", items)]


def block_animals_a1():
    items = [
        {"ar": check("عندي قطوة زين في البيت"), "en": "I have a good cat at home"},
        {"ar": check("شفت جلب كبير أمس"), "en": "I saw a big dog yesterday"},
        {"ar": check("شفت جمل كبير"), "en": "I saw a big camel"},
        {"ar": check("شفت طير صغير الحين"), "en": "I just saw a small bird"},
    ]
    return [("Animals", "الحيوانات", items)]


def block_numbers_13_20():
    items = [
        {"ar": check("أبغى ثلاث طعش وأربع طعش"), "en": "I want thirteen and fourteen"},
        {"ar": check("هذا خمس طعش، وهذا عشرين"), "en": "This is fifteen, and this is twenty"},
        {"ar": check("كم هذا؟ هذا ثلاث طعش"), "en": "How much is this? This is thirteen"},
        {"ar": check("أبغى أربع طعش وخمس طعش وعشرين"), "en": "I want fourteen and fifteen and twenty"},
    ]
    return [("Numbers 13-20", "الأرقام ١٣-٢٠", items)]


def block_numbers_30_60():
    items = [
        {"ar": check("أبغى ثلاثين وأربعين"), "en": "I want thirty and forty"},
        {"ar": check("هذا خمسين، وهذا ستين"), "en": "This is fifty, and this is sixty"},
        {"ar": check("كم هذا؟ هذا ثلاثين"), "en": "How much is this? This is thirty"},
        {"ar": check("أبغى أربعين وخمسين وستين"), "en": "I want forty and fifty and sixty"},
    ]
    return [("Numbers 30-60", "الأرقام ٣٠-٦٠", items)]


def block_numbers_70_100():
    items = [
        {"ar": check("أبغى سبعين وثمانين"), "en": "I want seventy and eighty"},
        {"ar": check("هذا تسعين، وهذا مية"), "en": "This is ninety, and this is a hundred"},
        {"ar": check("كم هذا؟ هذا سبعين"), "en": "How much is this? This is seventy"},
        {"ar": check("أبغى ثمانين وتسعين ومية"), "en": "I want eighty and ninety and a hundred"},
    ]
    return [("Numbers 70-100", "الأرقام ٧٠-١٠٠", items)]


def block_eat():
    items = [
        {"ar": check("آكل لحم زين"), "en": "I eat good meat"},
        {"ar": check("تاكل بيض زين"), "en": "You eat good eggs"},
        {"ar": check("تاكلين سلطة زين"), "en": "You (f.) eat good salad"},
        {"ar": check("ياكل لحم زين في المطعم"), "en": "He eats good meat at the restaurant"},
        {"ar": check("راح المطعم واكل لحم زين"), "en": "He went to the restaurant and ate good meat"},
        {"ar": check("خالي راح المطعم واكل بيض زين"), "en": "My uncle went to the restaurant and ate good eggs"},
    ]
    return [("Eating", "الأكل", items)]


def block_cook_present_1():
    items = [
        {"ar": check("أطبخ لحم زين"), "en": "I cook good meat"},
        {"ar": check("تطبخ بيض زين"), "en": "You cook good eggs"},
        {"ar": check("تطبخين سلطة زين"), "en": "You (f.) cook good salad"},
        {"ar": check("يطبخ لحم زين"), "en": "He cooks good meat"},
    ]
    return [("I Cook, You Cook", "أطبخ، تطبخ", items)]


def block_cook_present_2():
    items = [
        {"ar": check("هي تطبخ سلطة زين"), "en": "She cooks good salad"},
        {"ar": check("نطبخ لحم زين"), "en": "We cook good meat"},
        {"ar": check("انتوا تطبخون بيض زين"), "en": "You all cook good eggs"},
        {"ar": check("هم يطبخون سلطة زين"), "en": "They cook good salad"},
    ]
    return [("She Cooks, We Cook", "تطبخ، نطبخ", items)]


def block_cook_past():
    items = [
        {"ar": check("انت طبخت لحم زين"), "en": "You cooked good meat"},
        {"ar": check("هو طبخ بيض زين أمس"), "en": "He cooked good eggs yesterday"},
        {"ar": check("هي طبخت سلطة زين"), "en": "She cooked good salad"},
        {"ar": check("احنا طبخنا لحم زين أمس"), "en": "We cooked good meat yesterday"},
    ]
    return [("I Cooked, You Cooked", "طبخت، طبخ", items)]


def block_work():
    items = [
        {"ar": check("أشتغل في المستشفى"), "en": "I work at the hospital"},
        {"ar": check("انت تشتغل في المطعم"), "en": "You work at the restaurant"},
        {"ar": check("يشتغل في المستشفى"), "en": "He works at the hospital"},
        {"ar": check("هي تشتغل في المطعم"), "en": "She works at the restaurant"},
        {"ar": check("انتوا تشتغلون في المستشفى"), "en": "You all work at the hospital"},
        {"ar": check("هم يشتغلون في المطعم"), "en": "They work at the restaurant"},
    ]
    return [("Working", "الشغل", items)]


def block_love():
    items = [
        {"ar": check("أحب القهوة"), "en": "I love coffee"},
        {"ar": check("انت تحب الشاي"), "en": "You love tea"},
        {"ar": check("يحب القهوة"), "en": "He loves coffee"},
        {"ar": check("هي تحب الشاي"), "en": "She loves tea"},
        {"ar": check("خالي حب الشاي زين"), "en": "My uncle loved good tea"},
    ]
    return [("Loving Things", "أحب", items)]


def block_sleep():
    items = [
        {"ar": check("ينام كثير"), "en": "He sleeps a lot"},
        {"ar": check("أنا نمت كثير أمس"), "en": "I slept a lot yesterday"},
        {"ar": check("هو نام زين أمس"), "en": "He slept well yesterday"},
        {"ar": check("احنا نمنا زين أمس"), "en": "We slept well yesterday"},
    ]
    return [("Sleeping", "النوم", items)]


def block_eat_negation():
    items = [
        {"ar": check("ما آكل لحم لأن ما عندي فلوس"), "en": "I don't eat meat because I don't have money"},
        {"ar": check("ما تاكل بيض لأن ما تبغى بيض"), "en": "You don't eat eggs because you don't want eggs"},
        {"ar": check("ما ياكل لحم لأن مريض"), "en": "He doesn't eat meat because he's sick"},
    ]
    return [("Not Eating", "ما آكل", items)]


def block_cook_lazim():
    items = [
        {"ar": check("لازم أطبخ لحم بكرا"), "en": "I have to cook meat tomorrow"},
        {"ar": check("لازم تطبخ بيض"), "en": "You have to cook eggs"},
        {"ar": check("هي لازم تطبخ سلطة الحين"), "en": "She has to cook salad now"},
        {"ar": check("لازم نطبخ لحم زين"), "en": "We have to cook good meat"},
    ]
    return [("I Must Cook", "لازم أطبخ", items)]


def block_work_negation():
    items = [
        {"ar": check("ما أشتغل في المطعم لأن مشغولين كثير"), "en": "I don't work at the restaurant because it's very busy"},
        {"ar": check("انت ما تشتغل في المستشفى"), "en": "You don't work at the hospital"},
        {"ar": check("هي ما تشتغل الحين لأن تعبانة"), "en": "She isn't working now because she's tired"},
    ]
    return [("Not Working", "ما أشتغل", items)]


def block_love_chain():
    items = [
        {"ar": check("أحب القهوة لأن زينة كثير"), "en": "I love coffee because it's very good"},
        {"ar": check("انت تحب الشاي لأن رخيص"), "en": "You love tea because it's cheap"},
        {"ar": check("يحب القهوة، بس ما عنده فلوس"), "en": "He loves coffee, but he doesn't have money"},
    ]
    return [("Why I Love It", "أحب لأن", items)]


def block_numbers_because():
    items = [
        {"ar": check("أبغى عشرين لأن رخيص"), "en": "I want twenty because it's cheap"},
        {"ar": check("أبغى ثلاثين لأن السعر زين"), "en": "I want thirty because the price is good"},
        {"ar": check("ما أبغى مية لأن غالي كثير"), "en": "I don't want a hundred because it's very expensive"},
    ]
    return [("Numbers, Because", "الأرقام، لأن", items)]


def block_weather_chain():
    items = [
        {"ar": check("الجو حار كثير، ولازم أروح البيت، بس أبغى أروح الشغل"),
         "en": "It's very hot, and I have to go home, but I want to go to work"},
        {"ar": check("فيه مطر الحين، ما أبغى أروح، بس لازم أروح المستشفى"),
         "en": "There's rain now, I don't want to go, but I have to go to the hospital"},
    ]
    return [("Weather, Chained", "الجو، جمل مركبة", items)]


def block_adjectives_1():
    items = [
        {"ar": check("البيت جميل"), "en": "The house is beautiful"},
        {"ar": check("الشغل صعب"), "en": "The work is difficult"},
        {"ar": check("هذا سهل"), "en": "This is easy"},
        {"ar": check("القميص نظيف"), "en": "The shirt is clean"},
    ]
    return [("New Adjectives", "صفات جديدة", items)]


def block_adjectives_2():
    items = [
        {"ar": check("القطار سريع"), "en": "The train is fast"},
        {"ar": check("الدريول بطيء"), "en": "The driver is slow"},
        {"ar": check("اللحم لذيذ"), "en": "The meat is delicious"},
        {"ar": check("الكرسي ضعيف"), "en": "The chair is weak"},
    ]
    return [("More Adjectives", "صفات أكثر", items)]


def block_adjectives_3():
    items = [
        {"ar": check("الباب قبيح"), "en": "The door is ugly"},
        {"ar": check("البيت وسخ الحين"), "en": "The house is dirty now"},
        {"ar": check("المطبخ نظيف زين"), "en": "The kitchen is very clean"},
    ]
    return [("Ugly and Clean", "قبيح ونظيف", items)]


def block_objects_1():
    items = [
        {"ar": check("أبغى كتاب جديد"), "en": "I want a new book"},
        {"ar": check("أبغى قلم جديد"), "en": "I want a new pen"},
        {"ar": check("أبغى مفتاح جديد"), "en": "I want a new key"},
    ]
    return [("Things I Want", "أشياء أبغاها", items)]


def block_objects_2():
    items = [
        {"ar": check("عندي شنطة زينة"), "en": "I have a good bag"},
        {"ar": check("عندي محفظة زينة"), "en": "I have a good wallet"},
        {"ar": check("عندي مظلة زينة"), "en": "I have a good umbrella"},
        {"ar": check("عندي نظارة زينة"), "en": "I have good glasses"},
    ]
    return [("Things I Have", "أشياء عندي", items)]


def block_body_parts():
    items = [
        {"ar": check("عيني تعبانة، لازم أروح الطبيب"), "en": "My eye is tired, I have to go to the doctor"},
        {"ar": check("يدي تعبانة الحين"), "en": "My hand is tired now"},
        {"ar": check("رجلي تعبانة كثير"), "en": "My leg is very tired"},
        {"ar": check("أذني تعبانة"), "en": "My ear is tired"},
    ]
    return [("Body Parts", "أعضاء الجسم", items)]


def block_see_present_past():
    items = [
        {"ar": check("أشوف بيت زين الحين"), "en": "I see a good house now"},
        {"ar": check("شفت بيت زين أمس"), "en": "I saw a good house yesterday"},
        {"ar": check("يشوف بيت زين"), "en": "He sees a good house"},
        {"ar": check("شاف بيت زين أمس"), "en": "He saw a good house yesterday"},
    ]
    return [("I See, I Saw", "أشوف، شفت", items)]


def block_clean_present():
    items = [
        {"ar": check("أنظف البيت"), "en": "I clean the house"},
        {"ar": check("انت تنظف المطبخ"), "en": "You clean the kitchen"},
        {"ar": check("ينظف البيت"), "en": "He cleans the house"},
        {"ar": check("هي تنظف المطبخ"), "en": "She cleans the kitchen"},
        {"ar": check("ننظف البيت"), "en": "We clean the house"},
    ]
    return [("I Clean, You Clean", "أنظف، تنظف", items)]


def block_clean_past():
    items = [
        {"ar": check("أنا نظفت البيت أمس"), "en": "I cleaned the house yesterday"},
        {"ar": check("نظفتي المطبخ أمس"), "en": "You (f.) cleaned the kitchen yesterday"},
        {"ar": check("نظف البيت أمس"), "en": "He cleaned the house yesterday"},
        {"ar": check("هي نظفت المطبخ"), "en": "She cleaned the kitchen"},
        {"ar": check("نظفنا البيت أمس"), "en": "We cleaned the house yesterday"},
    ]
    return [("I Cleaned, You Cleaned", "نظفت، نظف", items)]


def block_more_verbs():
    items = [
        {"ar": check("احنا ناطرين القطار"), "en": "We are waiting for the train"},
        {"ar": check("يغسل السيارة"), "en": "He washes the car"},
        {"ar": check("يلعب في البيت"), "en": "He plays at home"},
    ]
    return [("More Verbs", "أفعال أكثر", items)]


def block_objects_negation():
    items = [
        {"ar": check("ما أبغى الكتاب الصعب، أبغى الكتاب السهل"), "en": "I don't want the difficult book, I want the easy book"},
        {"ar": check("ما تبغى القلم القبيح، تبغى القلم الجميل"), "en": "You don't want the ugly pen, you want the beautiful pen"},
        {"ar": check("ما يبغى الشغل الصعب، يبغى الشغل السهل"), "en": "He doesn't want difficult work, he wants easy work"},
        {"ar": check("ما أبغى المفتاح القديم، أبغى المفتاح الجديد"), "en": "I don't want the old key, I want the new key"},
    ]
    return [("Not This, But That", "ما أبغى هذا", items)]


def block_objects_lazim():
    items = [
        {"ar": check("لازم أبغى كتاب سهل الحين"), "en": "I have to want an easy book now"},
        {"ar": check("لازم تبغى قلم جديد"), "en": "You have to want a new pen"},
        {"ar": check("لازم يبغى شنطة زينة"), "en": "He has to want a good bag"},
    ]
    return [("Lazim with Objects", "لازم مع الأشياء", items)]


def block_body_parts_chain():
    items = [
        {"ar": check("عيني تعبانة لأن عندي شغل كثير، ولازم أروح الطبيب"),
         "en": "My eye is tired because I have a lot of work, and I have to go to the doctor"},
        {"ar": check("يدي تعبانة لأن نظفت البيت اليوم"), "en": "My hand is tired because I cleaned the house today"},
        {"ar": check("رجلي تعبانة لأن رحت الشغل في القطار"), "en": "My leg is tired because I went to work on the train"},
    ]
    return [("Body Parts, Because", "أعضاء الجسم، لأن", items)]


def block_time_of_day():
    items = [
        {"ar": check("أروح الشغل الصبح"), "en": "I go to work in the morning"},
        {"ar": check("أشرب قهوة عصر"), "en": "I drink coffee in the afternoon"},
        {"ar": check("لازم أروح البيت المساء"), "en": "I have to go home in the evening"},
        {"ar": check("ما أشتغل الليل"), "en": "I don't work at night"},
    ]
    return [("Time of Day", "أوقات اليوم", items)]


def block_telling_time():
    items = [
        {"ar": check("عندي ساعة زينة"), "en": "I have a good watch"},
        {"ar": check("أبغى دقيقة"), "en": "I want a minute"},
        {"ar": check("الظهر أروح المطعم"), "en": "At noon I go to the restaurant"},
    ]
    return [("Telling Time", "الساعة", items)]


def block_time_because():
    items = [
        {"ar": check("أروح الشغل الصبح لأن عندي شغل كثير"), "en": "I go to work in the morning because I have a lot of work"},
        {"ar": check("لازم أروح البيت الليل لأن تعبان"), "en": "I have to go home at night because I'm tired"},
        {"ar": check("ما أشتغل عصر لأن أطبخ في البيت"), "en": "I don't work in the afternoon because I cook at home"},
    ]
    return [("Time and Because", "الوقت ولأن", items)]


def block_polite_phrases():
    items = [
        {"ar": check("من فضلك، أبغى قهوة"), "en": "Please, I want coffee"},
        {"ar": check("لو سمحت، وين المطعم؟"), "en": "Excuse me, where is the restaurant?"},
        {"ar": check("طبعا، أبغى أروح"), "en": "Of course, I want to go"},
        {"ar": check("انشاالله بكرا"), "en": "God willing, tomorrow"},
    ]
    return [("Polite Phrases", "عبارات مؤدبة", items)]


def block_places_bus_market():
    items = [
        {"ar": check("أروح السوق الصبح"), "en": "I go to the market in the morning"},
        {"ar": check("أبغى أروح في الباص"), "en": "I want to go by bus"},
        {"ar": check("شفت طيارة كبيرة"), "en": "I saw a big airplane"},
        {"ar": check("شفت جاري في السوق"), "en": "I saw my neighbor at the market"},
    ]
    return [("Bus, Market, and Sky", "الباص والسوق", items)]


def block_always():
    items = [
        {"ar": check("دايما أشرب قهوة الصبح"), "en": "I always drink coffee in the morning"},
        {"ar": check("دايما يروح الشغل في الباص"), "en": "He always goes to work by bus"},
        {"ar": check("هي دايما تشتغل في المطعم"), "en": "She always works at the restaurant"},
    ]
    return [("Always", "دايماً", items)]


def block_polite_because():
    items = [
        {"ar": check("من فضلك أبغى قهوة لأن تعبان"), "en": "Please, I want coffee because I'm tired"},
        {"ar": check("لو سمحت، لازم أروح السوق الحين"), "en": "Excuse me, I have to go to the market now"},
        {"ar": check("طبعا أبغى أروح في الباص لأن رخيص"), "en": "Of course I want to go by bus because it's cheap"},
    ]
    return [("Polite Requests, Because", "عبارات مؤدبة، لأن", items)]


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
    "weather_a1": block_weather_a1,
    "weather_lazim": block_weather_lazim,
    "household_a1": block_household_a1,
    "household_a2": block_household_a2,
    "animals_a1": block_animals_a1,
    "numbers_13_20": block_numbers_13_20,
    "numbers_30_60": block_numbers_30_60,
    "numbers_70_100": block_numbers_70_100,
    "eat": block_eat,
    "cook_present_1": block_cook_present_1,
    "cook_present_2": block_cook_present_2,
    "cook_past": block_cook_past,
    "work": block_work,
    "love": block_love,
    "sleep": block_sleep,
    "eat_negation": block_eat_negation,
    "cook_lazim": block_cook_lazim,
    "work_negation": block_work_negation,
    "love_chain": block_love_chain,
    "numbers_because": block_numbers_because,
    "weather_chain": block_weather_chain,
    "adjectives_1": block_adjectives_1,
    "adjectives_2": block_adjectives_2,
    "adjectives_3": block_adjectives_3,
    "objects_1": block_objects_1,
    "objects_2": block_objects_2,
    "body_parts": block_body_parts,
    "see_present_past": block_see_present_past,
    "clean_present": block_clean_present,
    "clean_past": block_clean_past,
    "more_verbs": block_more_verbs,
    "objects_negation": block_objects_negation,
    "objects_lazim": block_objects_lazim,
    "body_parts_chain": block_body_parts_chain,
    "time_of_day": block_time_of_day,
    "telling_time": block_telling_time,
    "time_because": block_time_because,
    "polite_phrases": block_polite_phrases,
    "places_bus_market": block_places_bus_market,
    "always": block_always,
    "polite_because": block_polite_because,
}

BLOCK_LEVEL = {
    "professions": "a1", "professions_past": "a2", "professions_b1": "b1",
    "professions_lazim": "b1plus", "professions_negation": "b2", "professions_chain": "c1",
    "family_ext": "a1",
    "family_because": "b1", "clothing": "a1", "clothing_lazim": "b1plus",
    "food_new": "a1", "food_negation": "b2", "health": "b1plus",
    "health_c1": "c1", "transport": "a2", "transport_chain": "c1",
    "feelings_dense": "c2", "phone": "b1", "feelings_new": "b2plus",
    "weather_a1": "a1", "weather_lazim": "b1plus",
    "household_a1": "a1", "household_a2": "a2",
    "animals_a1": "a1",
    "numbers_13_20": "a1", "numbers_30_60": "a2", "numbers_70_100": "a2",
    "eat": "a1", "cook_present_1": "a1", "cook_present_2": "a2", "cook_past": "a2",
    "work": "b1", "love": "a2", "sleep": "b1plus",
    "eat_negation": "b2", "cook_lazim": "b1plus", "work_negation": "b2",
    "love_chain": "c1", "numbers_because": "b1", "weather_chain": "c1",
    "adjectives_1": "a1", "adjectives_2": "a2", "adjectives_3": "b1",
    "objects_1": "a1", "objects_2": "a2", "body_parts": "b1plus",
    "see_present_past": "a2", "clean_present": "a1", "clean_past": "a2",
    "more_verbs": "b1",
    "objects_negation": "b2", "objects_lazim": "b1plus", "body_parts_chain": "c1",
    "time_of_day": "a1", "telling_time": "a2", "time_because": "b1",
    "polite_phrases": "a1", "places_bus_market": "a2", "always": "b1",
    "polite_because": "b1plus",
}

# Blocks introduced in this (second) research round -- the ones NOT already
# present in the previous commit. Re-running --write must only ever append
# these, never the already-shipped blocks above, or content gets duplicated.
# Blocks introduced in this (third) round only -- everything above this set
# is already shipped in a previous commit. Re-running --write must only
# ever append these, never re-append already-shipped blocks.
ROUND_3_BLOCKS = {
    "eat_negation", "cook_lazim", "work_negation", "love_chain",
    "numbers_because", "weather_chain",
}

# Blocks introduced in this (fourth) round only.
ROUND_4_BLOCKS = {
    "adjectives_1", "adjectives_2", "adjectives_3", "objects_1", "objects_2",
    "body_parts", "see_present_past", "clean_present", "clean_past", "more_verbs",
}

# Fifth round: negation/lazim/chain drilling on round 4's new vocab, no new research.
ROUND_5_BLOCKS = {"objects_negation", "objects_lazim", "body_parts_chain"}

# Sixth round: time-of-day vocabulary confirmed in round 1's research but
# never used until now.
ROUND_6_BLOCKS = {"time_of_day", "telling_time", "time_because"}

# Seventh round: politeness phrases, bus/market/airplane/neighbor, "always".
ROUND_7_BLOCKS = {"polite_phrases", "places_bus_market", "always", "polite_because"}

ALL_BLOCKS = {name: fn for name, fn in SHIPPED_BLOCKS.items() if name in ROUND_7_BLOCKS}
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
