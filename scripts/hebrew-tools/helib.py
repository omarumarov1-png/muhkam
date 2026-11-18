"""Hebrew nikkud checker: every pointed word must match a fully pointed spelling in the Hebrew Wiktionary dump
(canonical headword forms + pointed inflected forms), modulo mark order, meteg and cantillation."""
import json, os, re, unicodedata
DICT = os.environ.get("HE_DICT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "he-dict"))
LET = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
CANT = re.compile("[֑-ֽ֯׀׃]")       # cantillation, meteg, paseq, sof pasuq
DAGESH = "ּ"
def norm(w):
    w = CANT.sub("", unicodedata.normalize("NFD", w))
    return unicodedata.normalize("NFC", w)
def skeleton(w):
    return "".join(c for c in w if c in LET)
_P = None
def pointed():
    global _P
    if _P is None:
        path = os.path.join(DICT, "he_pointed.json")
        if not os.path.exists(path):
            S = set()
            for line in open(os.path.join(DICT, "hebrew.jsonl"), encoding="utf-8"):
                e = json.loads(line)
                for f in e.get("forms", []):
                    s = f.get("form", "")
                    for part in re.split(r"[\s,/]+", s):
                        if any("ְ" <= c <= "ׇ" for c in part) and any(c in LET for c in part):
                            S.add(norm(part.strip("־-")))
            json.dump(sorted(S), open(path, "w", encoding="utf-8"), ensure_ascii=False)
        _P = set(json.load(open(path, encoding="utf-8")))
    return _P
# pointed one-letter prefixes (article, and, in, to, from, that, like), each optionally stacked: וְהַ, וּבַ, שֶׁבַּ…
PREFIXES = [norm(p) for p in ["הַ","הָ","הֶ","וְ","וּ","וַ","בְּ","בַּ","בָּ","בִּ","לְ","לַ","לָ","לִ","מִ","מֵ","שֶׁ","כְּ","כַּ","כָּ"]]
def _drop_first_dagesh(w):
    # the article/prefix doubles the first letter with a dagesh; dictionary forms don't have it
    m = re.match(r"^(.)([ְ-ׇ]*)", w)
    if not m: return w
    return m.group(1) + m.group(2).replace(DAGESH, "", 1) + w[m.end():]
def _add_first_dagesh(w):
    # after וּ / וְ etc. a word-initial ב כ פ (and ג ד ת) loses its dot; the dictionary form has it
    if w and w[0] in "בגדכפת" and DAGESH not in w[:3]:
        return unicodedata.normalize("NFC", w[0] + DAGESH + w[1:])
    return w
def known(word, depth=0):
    w = norm(word)
    P = pointed()
    if w in P or _drop_first_dagesh(w) in P: return True
    # וְ + יְ… merges into וִי… (וִירָקוֹת = וְ + יְרָקוֹת)
    for pre in ("וִי", "בִּי", "לִי", "כִּי", "בַּי", "לַי"):  # prefix + יְ… fuses: וִירָקוֹת, בִּירוּשָׁלַיִם
        if w.startswith(norm(pre)) and known(norm("יְ") + w[len(norm(pre)):], depth + 1): return True
    if depth < 2:
        for p in PREFIXES:
            if w.startswith(p) and len(skeleton(w)) > 1:
                rest = w[len(p):]
                if known(rest, depth + 1) or known(_drop_first_dagesh(rest), depth + 1) or known(_add_first_dagesh(rest), depth + 1): return True
    return False
TOK = re.compile(r"[ְ-תװ-״ּ]+")
def tokens(s): return [t.strip("־") for t in re.split(r"[\s\-–—,.!?:;\"«»()־/·→=+']+", s) if any(c in LET for c in t)]
def unknown(s):
    return [t for t in tokens(s) if len(skeleton(t)) > 1 and not known(t)]
def bad_chars(s):
    """Letters/marks outside modern Hebrew + nikkud (catches Yiddish digraphs, presentation forms, Latin/Cyrillic lookalikes)."""
    out = []
    for ch in s:
        o = ord(ch)
        if 0xFB1D <= o <= 0xFB4F: out.append(f"presentation form U+{o:04X}")
        if 0x05F0 <= o <= 0x05F2: out.append(f"Yiddish ligature U+{o:04X}")
    return out
_H = None
def headwords():
    """Unpointed headwords (how Hebrew is normally written)."""
    global _H
    if _H is None:
        _H = set()
        for line in open(os.path.join(DICT, "hebrew.jsonl"), encoding="utf-8"):
            w = json.loads(line).get("word", "")
            if w and all(c in LET for c in w): _H.add(w)
    return _H
NIKKUD = re.compile("[ְ-ׇ]")
def known_any(t):
    return known(t) if NIKKUD.search(t) else (skeleton(t) in headwords())
def unknown(s):
    return [t for t in tokens(s) if len(skeleton(t)) > 1 and not known_any(t)]
