"""Generate audio for every Tatar string in data/tatar-src (lesson items, reading paragraphs, grammar dialogues)
with facebook/mms-tts-tat. The text goes through ttlib.tts_text() first: the model only knows the old
font-hack letters (ѳ њ ћ ђ for ө ң һ җ) and lowercase. Incremental: skips texts already in the manifest whose
file exists. Files: <sha1[:16]>.m4a (ffmpeg AAC 64k; afconvert can't read MMS's 16 kHz WAV)."""
import glob, hashlib, json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ttlib
import torch, scipy.io.wavfile as wavfile
from transformers import VitsModel, AutoTokenizer
ROOT = os.path.expanduser("~/muhkam")
OUT = os.path.join(ROOT, "data", "audio-tatar")
MAN = os.path.join(OUT, "manifest.json")
def texts():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "tatar-src", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for l in d["lessons"]:
            out += [it["tt"] for it in l.get("items", [])] + [p["tt"] for p in l.get("paragraphs", [])]
        for t in d.get("grammarTopics", {}).values():
            out += [x["native"] for x in t["dialogue"]]
    return list(dict.fromkeys(out))
def main():
    os.makedirs(OUT, exist_ok=True)
    man = json.load(open(MAN, encoding="utf-8")) if os.path.exists(MAN) else {}
    todo = [t for t in texts() if not (t in man and os.path.exists(os.path.join(OUT, man[t]["file"])))]
    print(f"{len(todo)} to generate, {len(man)} already in manifest", flush=True)
    if not todo: return
    tok = AutoTokenizer.from_pretrained("facebook/mms-tts-tat"); model = VitsModel.from_pretrained("facebook/mms-tts-tat").eval()
    vocab = tok.get_vocab(); fails = []
    for i, text in enumerate(todo, 1):
        prep = ttlib.tts_text(text)
        bad = sorted({c for c in prep if c not in vocab and c not in " .,!?:;-–"})
        if bad: fails.append((text, f"chars not in TTS vocab: {bad}")); continue
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]; fn = h + ".m4a"
        torch.manual_seed(int(h[:8], 16))
        with torch.no_grad(): wav = model(**tok(prep, return_tensors="pt")).waveform[0].numpy()
        with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
            wavfile.write(tmp.name, model.config.sampling_rate, wav)
            r = subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp.name, "-c:a", "aac", "-b:a", "64k", os.path.join(OUT, fn)])
        if r.returncode: fails.append((text, "ffmpeg failed")); continue
        man[text] = {"file": fn, "voice": "mms-tts-tat"}
        if i % 25 == 0 or i == len(todo):
            json.dump(man, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=0); print(f"  {i}/{len(todo)}", flush=True)
    json.dump(man, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"done: manifest {len(man)} entries, {len(fails)} failures")
    for t, e in fails[:10]: print("  FAIL", t, e)
    sys.exit(1 if fails else 0)
main()
