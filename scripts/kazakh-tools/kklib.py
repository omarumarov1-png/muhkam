"""Kazakh (Cyrillic) helpers (adapted from tatar-tools/ttlib.py) for the Muhkam course.

check(text)      -> list of problems (unknown words, Latin/other lookalike letters, bad chars)
tts_text(text)   -> text prepared for facebook/mms-tts-tat (lowercase + legacy letters:
                    ө→ѳ, ң→њ, һ→ћ, җ→ђ; the model was trained on that old font encoding and
                    has no tokens for the real Tatar letters)
Words are checked against the Apertium Tatar analyser (tat.automorf.hfst, path in TT_ANALYZER),
the Tatoeba Tatar sentences we use (TT_CORPUS: a set of attested word forms) and allow.txt
(one word per line, with a reason after #). Never ship a word none of them accepts.
"""
import os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяәғқңөұүһі"
WORD = re.compile(r"[" + LETTERS + LETTERS.upper() + r"]+(?:-[" + LETTERS + LETTERS.upper() + r"]+)*")
# characters that look like Tatar letters but are not (Latin/Kazakh/Bashkir/Serbian lookalikes)
LOOKALIKE = {}
BAD = set('ǝəɵäöüҥњћђѳҗ') | set('iI') | set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
_an = None; _corpus = None; _allow = None
def analyser():
    global _an
    if _an is None:
        import hfst
        p = os.environ.get('KK_ANALYZER') or os.path.join(HERE, 'kaz.automorf.hfst')
        _an = hfst.HfstInputStream(p).read()
    return _an
def corpus():
    global _corpus
    if _corpus is None:
        p = os.environ.get('KK_CORPUS') or os.path.join(HERE, 'kk_corpus_words.txt')
        _corpus = set(open(p, encoding='utf-8').read().split()) if os.path.exists(p) else set()
    return _corpus
def allowed():
    global _allow
    if _allow is None:
        p = os.path.join(HERE, 'allow.txt'); _allow = set()
        if os.path.exists(p):
            for l in open(p, encoding='utf-8'):
                w = l.split('#')[0].strip().lower()
                if w: _allow.add(w)
    return _allow
_cache = {}
def known(w):
    lw = w.lower()
    if lw in _cache: return _cache[lw]
    a = analyser()
    ok = lw in allowed() or lw in corpus() or bool(a.lookup(w)) or bool(a.lookup(lw)) or bool(a.lookup(lw[:1].upper() + lw[1:]))
    if not ok and '-' in lw: ok = all(known(p) for p in lw.split('-'))
    _cache[lw] = ok
    return ok
def words(text): return WORD.findall(text)
def check(text):
    probs = []
    for ch in text:
        if ch in BAD: probs.append(f"lookalike/latin char {ch!r} U+{ord(ch):04X} {unicodedata.name(ch, '?')}")
    for w in words(text):
        if not known(w): probs.append(f"unknown word: {w}")
    return probs
