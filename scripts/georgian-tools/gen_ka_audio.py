"""Generate Microsoft neural audio for every Georgian string in data/georgian-src (lesson items, reading paragraphs, grammar dialogues).
Incremental: skips texts already in the manifest whose file exists. Voice is chosen deterministically per text (Eka / Giorgi by hash parity)."""
import asyncio, glob, hashlib, json, os, sys
import edge_tts
ROOT = os.path.expanduser("~/muhkam")
OUT = os.path.join(ROOT, "data", "audio-georgian")
MAN = os.path.join(OUT, "manifest.json")
VOICES = ["ka-GE-EkaNeural", "ka-GE-GiorgiNeural"]
def texts():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "georgian-src", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for l in d["lessons"]:
            out += [it["ka"] for it in l.get("items", [])] + [p["ka"] for p in l.get("paragraphs", [])]
        for t in d.get("grammarTopics", {}).values():
            out += [x["native"] for x in t["dialogue"]]
    return list(dict.fromkeys(out))
async def one(text, sem, man, fails):
    h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]
    voice = VOICES[int(h, 16) % 2]; fn = h + ".mp3"; path = os.path.join(OUT, fn)
    async with sem:
        for attempt in range(4):
            try:
                await edge_tts.Communicate(text, voice).save(path + ".part")
                if os.path.getsize(path + ".part") < 2000: raise RuntimeError("tiny file")
                os.replace(path + ".part", path); man[text] = {"file": fn, "voice": voice}; return
            except Exception as e:
                err = e; await asyncio.sleep(2 * (attempt + 1))
        fails.append((text, repr(err)[:120]))
async def main():
    os.makedirs(OUT, exist_ok=True)
    man = json.load(open(MAN, encoding="utf-8")) if os.path.exists(MAN) else {}
    todo = [t for t in texts() if not (t in man and os.path.exists(os.path.join(OUT, man[t]["file"])))]
    print(f"{len(todo)} to generate, {len(man)} already in manifest", flush=True)
    sem, fails = asyncio.Semaphore(4), []
    for i in range(0, len(todo), 40):
        await asyncio.gather(*(one(t, sem, man, fails) for t in todo[i:i + 40]))
        json.dump(man, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print(f"  {min(i + 40, len(todo))}/{len(todo)}", flush=True)
    keep = set(texts()); stale = [t for t in man if t not in keep]
    print(f"done: manifest {len(man)} entries, {len(fails)} failures, {len(stale)} manifest entries no longer in source")
    for t, e in fails[:10]: print("  FAIL", t, e)
    sys.exit(1 if fails else 0)
asyncio.run(main())
