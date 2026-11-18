"""Georgian helpers: tokenizer, dictionary verification, national-system romanization.

Dictionary: download https://kaikki.org/dictionary/Georgian/kaikki.org-dictionary-Georgian.jsonl into a folder,
run `python3 build_index.py <that.jsonl> <folder>`, and point KA_DICT at the folder (it must hold ka_forms.json + ka_lemmas.json).
Content scripts import `author.Course`, which refuses to save a lesson file unless every Georgian word passes `known()`."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
DICT = os.environ.get("KA_DICT", os.path.join(HERE, "..", "ka-dict"))
_F = None
def forms():
    global _F
    if _F is None: _F = json.load(open(os.path.join(DICT, "ka_forms.json"), encoding="utf-8"))
    return _F
# Clitics/particles attach to fully inflected words; strip them only to look up the host word.
CLITICS = ["ც", "ო", "ვე", "ღა"]
# Words that are standard grammar but missing as surface forms in the dump; each needs a documented reason.
ALLOW = {}
def allow(word, why): ALLOW[word] = why
# Documented gaps: regular forms whose paradigm siblings are attested in the dump.
allow("მქვია", "1sg of ჰქვია 'be called'; 2sg გქვია and 3sg ჰქვია are attested; მ-/გ-/ჰ- object markers as in attested მიყვარს/გიყვარს/უყვარს")
allow("გაგიმარჯოთ", "plural/polite of the attested reply გაგიმარჯოს; plural -თ as in attested გაქვს/გაქვთ")
allow("ტკივა", "3sg of მტკივა 'it hurts me'; 1sg მტკივა and 2sg გტკივა attested, 3sg has no object prefix (cf. აქვს, უნდა)")
allow("დაჯექით", "polite/plural imperative of attested დაჯექი; plural -თ as in attested წადით")
allow("შხარა", "proper name: Shkhara, Georgia's highest mountain")
TOK = re.compile(r"[ა-ჿ]+(?:-[ა-ჿ]+)*")
def tokens(s): return TOK.findall(s)
VOW = set("აეიოუ")
def base_known(w):
    F = forms()
    if w in F or w in ALLOW or dative_postposition(w): return True
    for c in CLITICS:
        if w.endswith(c) and len(w) > len(c) + 1 and (w[:-len(c)] in F or w[:-len(c)] in ALLOW): return True
    return False
def copula(w):
    """Enclitic -ა 'is' (short for არის): consonant-stem nouns drop -ი (ექიმი → ექიმია), vowel-final words add -ა (დედა → დედაა)."""
    if len(w) > 3 and w.endswith("ია") and base_known(w[:-1]): return True
    if len(w) >= 3 and w.endswith("ა") and w[-2] in VOW and base_known(w[:-1]): return True
    return False
_LEM = None
def lemmas():
    global _LEM
    if _LEM is None: _LEM = json.load(open(os.path.join(DICT, "ka_lemmas.json"), encoding="utf-8"))
    return _LEM
def attributive(w):
    """Attributive form of an -ი-final numeral/adjective before a noun in the dative/ergative drops -ი
    (ორი → ორ საათზე, ქართული → ქართულ ენას, attested); accepted only when w+'ი' is a confirmed numeral or adjective."""
    return any(x["pos"] in ("num", "adj") for x in lemmas().get(w + "ი", []))
DAT_POST = ["ს", "ში", "ზე", "თან"]
def dative_postposition(w):
    """Regular dative -ს and the postpositions built on it (-ში in, -ზე on, -თან at) attach to the full stem
    with no syncope (attested tables: ვახშამში, ვახშამზე, იანვარში, სექტემბერთან). Accepted only on a confirmed noun/name;
    -ი-final stems drop -ი (მაისი → მაისში), other vowels keep it (მეტრო → მეტროში). Not applied to -მდე/-დან/-ით, which can syncopate."""
    L = lemmas()
    for e in DAT_POST:
        if w.endswith(e) and len(w) > len(e) + 1:
            stem = w[:-len(e)]
            for cand in (stem + "ი", stem):
                if any(x["pos"] in ("noun", "name") for x in L.get(cand, [])) and (cand.endswith("ი") or cand == stem): return True
    return False
def known(w):
    F = forms()
    if len(w) == 1: return True  # a single letter shown on its own (alphabet lessons)
    if attributive(w): return True
    if dative_postposition(w): return True
    if w in F or w in ALLOW or copula(w): return True
    for c in CLITICS:
        if w.endswith(c) and len(w) > len(c) + 1 and (w[:-len(c)] in F or w[:-len(c)] in ALLOW): return True
    if "-" in w: return all(known(p) for p in w.split("-"))
    return False
def unknown(s): return [w for w in tokens(s) if not known(w)]
# National system of romanization (2002), ejectives with apostrophe.
ROM = dict(zip("აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ",
  ["a","b","g","d","e","v","z","t","i","k'","l","m","n","o","p'","zh","r","s","t'","u","p","k","gh","q'","sh","ch","ts","dz","ts'","ch'","kh","j","h"]))
def is_name(w):
    a = forms().get(w)
    return bool(a) and all(x[1] == "name" for x in a)
def romanize(s):
    out = re.sub(r"[\u10d0-\u10ff]+", lambda m: (lambda r: r[:1].upper() + r[1:] if is_name(m.group(0)) else r)("".join(ROM.get(c, c) for c in m.group(0))), s)
    return re.sub(r"(^|[.!?]\s+|[«\"—]\s*)([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
GEO_OK = set("აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
def bad_chars(s):
    """Any letter that is not one of the 33 modern Mkhedruli letters (catches Mtavruli, archaic letters, Latin/Cyrillic lookalikes inside words)."""
    out = []
    for w in re.findall(r"\w+", s):
        if any(c in GEO_OK for c in w) and any(c not in GEO_OK for c in w): out.append(w)
        for c in w:
            if "Ⴀ" <= c <= "ჿ" and c not in GEO_OK: out.append(c)
    return out
