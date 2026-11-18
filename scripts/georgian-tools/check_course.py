import json, os, collections
R = os.path.expanduser("~/muhkam/data")
ka = json.load(open(f"{R}/courses-georgian.json", encoding="utf-8"))["course"]
ps = json.load(open(f"{R}/courses-pashto.json", encoding="utf-8"))["course"]
man = json.load(open(f"{R}/audio-georgian/manifest.json", encoding="utf-8"))
need = set()
for lv in ka["levels"]:
    for l in lv["lessons"]:
        for p in (l.get("readingPassage") or {}).get("paragraphs", []): need.add(p["native"])
        for ex in l["exercises"]:
            if ex.get("direction") == "ka-en": need.add(ex["prompt"])
            if "native" in ex: need.add(ex["native"])
            for pr in ex.get("pairs", []): need.add(pr["native"])
for t in ka["grammarTopics"].values():
    for d in t["dialogue"]: need.add(d["native"])
missing = [t for t in need if t not in man or not os.path.exists(f"{R}/audio-georgian/{man[t]['file']}")]
print("audio needed:", len(need), "missing:", len(missing), missing[:5])
print("top-level keys differ:", set(ps) ^ set(ka))
def ex_keys(c):
    k = collections.defaultdict(set)
    for lv in c["levels"]:
        for l in lv["lessons"]:
            for ex in l["exercises"]: k[ex["type"]].add(tuple(sorted(ex)))
    return k
kk, pk = ex_keys(ka), ex_keys(ps)
for t in kk:
    print(f"  {t:16s} georgian {sorted(kk[t])[0]}" + ("" if t not in pk else ("  == pashto" if kk[t] <= pk[t] or kk[t] == pk[t] else f"  pashto {sorted(pk[t])[0]}")))
ids = [l["id"] for lv in ka["levels"] for l in lv["lessons"]]
print("lessons", len(ids), "unique ids", len(set(ids)), "topics referenced but missing:",
      [l.get("topicId") for lv in ka["levels"] for l in lv["lessons"] if l.get("topicId") and l["topicId"] not in ka["grammarTopics"]])
