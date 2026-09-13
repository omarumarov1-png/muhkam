#!/usr/bin/env python3
"""Confirmed-vocabulary guard for authoring new Emirati Arabic (Khaleeji)
content.

Same technique as verify_syrian_vocab.py: the confirmed set is derived
directly from every word already shipped in data/emirati-src/*.json (by
definition already vetted when the course was built), plus any words
cross-referenced against >=2 independent external sources afterward
(data/emirati-research/researched_vocab.json, mirroring Syrian's
mechanism). Extending the course must only ever recombine these forms
(plus the documented fallback rules below), never invent new ones.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_RE = re.compile(r"[ء-يٰ-ۓ]+")

LEVEL_ORDER = ["a1", "a2", "b1", "b1plus", "b2", "b2plus", "c1", "c2"]


def load_level_vocab(level_id):
    f = os.path.join(ROOT, f"data/emirati-src/{level_id}.json")
    if not os.path.exists(f):
        return set()
    d = json.load(open(f, encoding="utf-8"))
    vocab = set()
    for lesson in d.get("lessons", []):
        for item in lesson.get("items", []):
            vocab.update(TOKEN_RE.findall(item.get("ar", "")))
        for p in lesson.get("paragraphs", []):
            vocab.update(TOKEN_RE.findall(p.get("ar", "")))
    return vocab


def load_researched_vocab():
    f = os.path.join(ROOT, "data/emirati-research/researched_vocab.json")
    if not os.path.exists(f):
        return set(), None
    d = json.load(open(f, encoding="utf-8"))
    vocab = set(d.get("words", {}).keys())
    for verb, info in d.get("verbs", {}).items():
        if not isinstance(info, dict):
            continue
        vocab.update(info.get("present", {}).values())
        vocab.update(info.get("past", {}).values())
        vocab.update(TOKEN_RE.findall(info.get("root", "")))
    return vocab, d.get("available_from_level")


RESEARCHED_VOCAB, RESEARCHED_AVAILABLE_FROM = load_researched_vocab()


def load_confirmed_vocab():
    vocab = set()
    for lvl in LEVEL_ORDER:
        vocab |= load_level_vocab(lvl)
    vocab |= RESEARCHED_VOCAB
    return vocab


def load_cumulative_vocab(up_to_level):
    vocab = set()
    reached_researched_level = RESEARCHED_AVAILABLE_FROM is None
    for lvl in LEVEL_ORDER:
        vocab |= load_level_vocab(lvl)
        if lvl == RESEARCHED_AVAILABLE_FROM:
            reached_researched_level = True
        if lvl == up_to_level:
            break
    if reached_researched_level:
        vocab |= RESEARCHED_VOCAB
    return vocab


CONFIRMED_VOCAB = load_confirmed_vocab()

POSSESSIVE_SUFFIXES = ["ها", "هم", "كم", "ني", "نا", "ي", "ك", "ه"]


def check_definite_article(word, vocab):
    return word.startswith("ال") and check_word(word[2:], vocab)


def check_wa_prefix(word, vocab):
    return word.startswith("و") and len(word) > 2 and check_word(word[1:], vocab)


def check_possessive_suffix(word, vocab):
    for suf in POSSESSIVE_SUFFIXES:
        if not (word.endswith(suf) and len(word) > len(suf)):
            continue
        base = word[: -len(suf)]
        if check_word(base, vocab):
            return True
        if base.endswith("ت") and (base[:-1] + "ة") in vocab:
            return True
        if base.endswith("ا") and check_word(base[:-1] + "ى", vocab):
            return True
    return False


def check_sound_plural_yn(word, vocab):
    return word.endswith("ين") and len(word) > 2 and check_word(word[:-2], vocab)


def check_fem_dual(word, vocab):
    """Feminine dual: -ة becomes -تين (sayyaara -> sayyaaratayn)."""
    return word.endswith("تين") and len(word) > 3 and check_word(word[:-3] + "ة", vocab)


def check_sound_plural_aat(word, vocab):
    """Regular feminine sound plural: strip -ات, re-add ة, check the
    already-confirmed singular (tayyaara -> tayyaaraat)."""
    return word.endswith("ات") and len(word) > 3 and check_word(word[:-2] + "ة", vocab)


def check_feminine_ta_marbuta(word, vocab):
    """Regular masc->fem adjective/noun agreement: base + ة (kabeer -> kabeera)."""
    return word.endswith("ة") and len(word) > 1 and word[:-1] in vocab


def check_reverse_feminine(word, vocab):
    """The masc counterpart of an already-confirmed fem -ة form (thaanya
    confirmed -> thaani also safe), the mirror image of the check above."""
    return (word + "ة") in vocab


def check_feminine_afal_color(word, vocab):
    """CaCCaa' fem of the 'af3al color/defect-adjective pattern
    (azraq -> zarqaa', a7mar -> 7amraa'): strip اء, re-add أ, check vocab."""
    return word.endswith("اء") and len(word) > 3 and ("أ" + word[:-2]) in vocab


def check_bare_of_definite(word, vocab):
    """The flip side of check_definite_article: if 'al-X' is already
    confirmed, the bare noun X is the same lexeme, not a new word."""
    return ("ال" + word) in vocab


def check_bi_prefix(word, vocab):
    return word.startswith("ب") and len(word) > 2 and check_word(word[1:], vocab)


def check_future_1s_elision(word, vocab):
    """The future ب- marker elides the 1st-person-singular أ- present
    prefix (ب+أروح -> بروح, not بأروح) -- confirmed directly in the GO
    future paradigm; this generalizes it to every other verb's already-
    confirmed 1s present form."""
    return word.startswith("ب") and len(word) > 2 and ("أ" + word[1:]) in vocab


def check_li_prefix(word, vocab):
    return word.startswith("ل") and len(word) > 2 and check_word(word[1:], vocab)


def check_fa_prefix(word, vocab):
    return word.startswith("ف") and len(word) > 2 and check_word(word[1:], vocab)


def check_ha_demonstrative_prefix(word, vocab):
    """Colloquial 'this' clitic: ها + definite noun (halfluus = 'this
    money', literally 'ha-al-fluus')."""
    return word.startswith("ها") and len(word) > 3 and check_word(word[2:], vocab)


def check_word(word, vocab=None):
    vocab = vocab if vocab is not None else CONFIRMED_VOCAB
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
    if check_sound_plural_aat(word, vocab):
        return True
    if check_fem_dual(word, vocab):
        return True
    if check_feminine_ta_marbuta(word, vocab):
        return True
    if check_reverse_feminine(word, vocab):
        return True
    if check_feminine_afal_color(word, vocab):
        return True
    if check_bare_of_definite(word, vocab):
        return True
    if check_bi_prefix(word, vocab):
        return True
    if check_li_prefix(word, vocab):
        return True
    if check_fa_prefix(word, vocab):
        return True
    if check_future_1s_elision(word, vocab):
        return True
    if check_ha_demonstrative_prefix(word, vocab):
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
