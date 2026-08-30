#!/usr/bin/env python3
"""Confirmed-vocabulary guard for authoring new Syrian Arabic (Shami) content.

The original vocab-verification tool from when this course was first built
was a scratchpad script tied to a since-ended session and no longer exists.
This rebuilds it from the safest possible ground truth: every word already
shipped in data/syrian-src/*.json has, by definition, already been vetted --
so the confirmed set is derived directly from that, not re-fetched from the
dictionary. Extending the course must only ever recombine these forms (plus
the documented fallback rules below), never invent new ones.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_RE = re.compile(r"[ء-يٰ-ۓ]+")


LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]


def load_level_vocab(level_id):
    f = os.path.join(ROOT, f"data/syrian-src/{level_id}.json")
    d = json.load(open(f, encoding="utf-8"))
    vocab = set()
    for lesson in d.get("lessons", []):
        for item in lesson.get("items", []):
            vocab.update(TOKEN_RE.findall(item.get("ar", "")))
    return vocab


def load_confirmed_vocab():
    vocab = set()
    for lvl in LEVEL_ORDER:
        vocab |= load_level_vocab(lvl)
    researched, _ = load_researched_vocab()
    vocab |= researched
    verb_forms, _ = load_researched_verb_forms()
    vocab |= verb_forms
    return vocab


def load_researched_vocab():
    """Words never shipped in any lesson but confirmed by >=2 independent
    sources outside the course itself (see researched_vocab.json for
    provenance). Distinct from load_level_vocab, which only trusts what's
    already shipped -- this is the one deliberate exception, and only
    words that survived real cross-referencing land here."""
    f = os.path.join(ROOT, "data/syrian-research/researched_vocab.json")
    if not os.path.exists(f):
        return set(), None
    d = json.load(open(f, encoding="utf-8"))
    return set(d.get("words", {}).keys()), d.get("available_from_level")


def load_researched_verb_forms():
    """Full 8-person conjugated forms for verbs confirmed via a real
    paradigm source (see researched_verb_paradigms.json) -- distinct from
    plain vocabulary since a verb needs every person confirmed, not just
    a citation form, to be safely usable in a sentence."""
    f = os.path.join(ROOT, "data/syrian-research/researched_verb_paradigms.json")
    if not os.path.exists(f):
        return set(), None
    d = json.load(open(f, encoding="utf-8"))
    forms = set()
    for verb, data in d.get("verbs", {}).items():
        for tense in ("perfect", "bi_imperfect"):
            forms.update(data.get(tense, {}).values())
    return forms, d.get("available_from_level")


RESEARCHED_VOCAB, RESEARCHED_AVAILABLE_FROM = load_researched_vocab()
RESEARCHED_VERB_FORMS, RESEARCHED_VERBS_AVAILABLE_FROM = load_researched_verb_forms()


def load_cumulative_vocab(up_to_level):
    """Vocabulary confirmed at or before up_to_level -- use this (not the
    full-course set) when authoring new lessons for a given level, so a
    later level's grammar (e.g. B1+'s لازم) can't leak into an earlier
    one just because it's confirmed SOMEWHERE in the shipped course."""
    vocab = set()
    reached_researched_level = RESEARCHED_AVAILABLE_FROM is None
    reached_verbs_level = RESEARCHED_VERBS_AVAILABLE_FROM is None
    for lvl in LEVEL_ORDER:
        vocab |= load_level_vocab(lvl)
        if lvl == RESEARCHED_AVAILABLE_FROM:
            reached_researched_level = True
        if lvl == RESEARCHED_VERBS_AVAILABLE_FROM:
            reached_verbs_level = True
        if lvl == up_to_level:
            break
    if reached_researched_level:
        vocab |= RESEARCHED_VOCAB
    if reached_verbs_level:
        vocab |= RESEARCHED_VERB_FORMS
    return vocab


CONFIRMED_VOCAB = load_confirmed_vocab()

POSSESSIVE_SUFFIXES = ["ها", "هم", "كم", "نا", "ي", "ك", "ه"]


def check_definite_article(word, vocab):
    return word.startswith("ال") and word[2:] in vocab


def check_wa_prefix(word, vocab):
    return word.startswith("و") and check_word(word[1:], vocab)


def check_possessive_suffix(word, vocab):
    for suf in POSSESSIVE_SUFFIXES:
        if not (word.endswith(suf) and len(word) > len(suf)):
            continue
        base = word[: -len(suf)]
        if base in vocab:
            return True
        # A feminine noun's ة becomes ت before a possessive suffix
        # (e.g. عيلة "family" -> عيلتي "my family") -- the stripped base
        # ends in ت but the confirmed form ends in ة.
        if base.endswith("ت") and (base[:-1] + "ة") in vocab:
            return True
    return False


def check_sound_plural_yn(word, vocab):
    return word.endswith("ين") and word[:-2] in vocab


def check_word(word, vocab=None):
    vocab = vocab or CONFIRMED_VOCAB
    if word in vocab:
        return True
    if check_definite_article(word, vocab):
        return True
    if check_wa_prefix(word, vocab):
        return True
    if check_possessive_suffix(word, vocab):
        return True
    if check_sound_plural_yn(word, vocab):
        return True
    return False


def check_sentence(text, vocab=None):
    """Returns (ok, [unconfirmed words])."""
    words = TOKEN_RE.findall(text)
    bad = [w for w in words if not check_word(w, vocab)]
    return (len(bad) == 0, bad)


if __name__ == "__main__":
    import sys
    level = sys.argv[1] if len(sys.argv) > 1 else None
    vocab = load_cumulative_vocab(level) if level else CONFIRMED_VOCAB
    print(f"Vocabulary in scope ({level or 'full course'}): {len(vocab)} forms")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        ok, bad = check_sentence(line, vocab)
        status = "OK" if ok else f"UNCONFIRMED: {bad}"
        print(f"{status}  {line}")
