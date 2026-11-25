#!/usr/bin/env python3
"""Kazakh audio via Microsoft Edge neural TTS (kk-KZ-AigulNeural).
Collects every item / paragraph / grammar-dialogue line from data/kazakh-src,
writes data/audio-kazakh/<sha1[:16]>.mp3 and manifest.json {text: {file, voice}}.
Incremental: texts already in the manifest with an existing file are skipped."""
import asyncio, glob, hashlib, json, os, sys
import edge_tts
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "data", "kazakh-src")
OUT = os.path.join(ROOT, "data", "audio-kazakh")
VOICE = "kk-KZ-AigulNeural"
CONC = 6

def texts():
    seen = []
    for f in sorted(glob.glob(os.path.join(SRC, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for l in d.get("lessons", []):
            for it in l.get("items", []) + l.get("paragraphs", []):
                seen.append(it["kk"])
        topics = d.get("grammarTopics") or {}
        for t in (topics.values() if isinstance(topics, dict) else topics):
            for turn in t.get("dialogue", []) or []:
                if turn.get("native"): seen.append(turn["native"])
    out, s = [], set()
    for t in seen:
        t = t.strip()
        if t and t not in s: s.add(t); out.append(t)
    return out

async def synth(text, path, sem, fails):
    async with sem:
        for attempt in range(4):
            try:
                await edge_tts.Communicate(text, VOICE, rate="-5%").save(path + ".tmp")
                if os.path.getsize(path + ".tmp") < 800: raise RuntimeError("tiny file")
                os.replace(path + ".tmp", path); return True
            except Exception as e:
                err = e; await asyncio.sleep(2 * (attempt + 1))
        fails.append((text, str(err))); return False

async def main():
    os.makedirs(OUT, exist_ok=True)
    mp = os.path.join(OUT, "manifest.json")
    man = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
    todo = []
    for t in texts():
        fn = hashlib.sha1(t.encode("utf-8")).hexdigest()[:16] + ".mp3"
        if t in man and os.path.exists(os.path.join(OUT, man[t]["file"])): continue
        todo.append((t, fn))
    print(f"{len(todo)} to generate", flush=True)
    sem, fails = asyncio.Semaphore(CONC), []
    for i in range(0, len(todo), 60):
        chunk = todo[i:i + 60]
        res = await asyncio.gather(*[synth(t, os.path.join(OUT, fn), sem, fails) for t, fn in chunk])
        for (t, fn), ok in zip(chunk, res):
            if ok: man[t] = {"file": fn, "voice": VOICE}
        json.dump(man, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print(f"  {min(i + 60, len(todo))}/{len(todo)}", flush=True)
    print(f"done: manifest {len(man)} entries, {len(fails)} failures")
    for t, e in fails[:10]: print("  FAIL", t, e)

asyncio.run(main())
