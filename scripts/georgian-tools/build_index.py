"""Build ka_forms.json: every surface form in the Georgian Wiktionary dump -> list of (lemma, pos, tags), and ka_lemmas.json: lemma -> glosses."""
import json, sys, collections
src, outdir = sys.argv[1], sys.argv[2]
forms = collections.defaultdict(list); lemmas = collections.defaultdict(list)
GEO = lambda s: s and all(("ა" <= c <= "ჿ") or c in "- " for c in s) and any("ა" <= c <= "ჿ" for c in s)
for line in open(src, encoding="utf-8"):
    e = json.loads(line); w = e.get("word"); p = e.get("pos")
    if p == "character" or not GEO(w): continue
    gl = [g for s in e.get("senses", []) for g in (s.get("glosses") or [])]
    lemmas[w].append({"pos": p, "glosses": gl[:6]})
    forms[w].append([w, p, ["lemma"]])
    for f in e.get("forms") or []:
        s = f.get("form", "")
        for part in s.split(" / "):
            part = part.strip()
            if GEO(part) and " " not in part:
                forms[part].append([w, p, f.get("tags", [])[:4]])
json.dump(forms, open(outdir + "/ka_forms.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(lemmas, open(outdir + "/ka_lemmas.json", "w", encoding="utf-8"), ensure_ascii=False)
print("surface forms:", len(forms), "lemmas:", len(lemmas))
