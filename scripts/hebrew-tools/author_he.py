"""Authoring helper for the Hebrew alef-bet unit. save() refuses to write on any unverified word."""
import json, os, sys
import helib as h
SRC = os.path.expanduser("~/muhkam/data/hebrew-src")
class Course:
    def __init__(self, level, name):
        self.level, self.path, self.lessons, self.topics, self.problems = level, os.path.join(SRC, name + ".json"), [], {}, []
    def _check(self, where, s):
        u, b = h.unknown(s), h.bad_chars(s)
        if u: self.problems.append(f"{where}: not in dictionary {u} in «{s}»")
        if b: self.problems.append(f"{where}: {b} in «{s}»")
    def T(self, tid, title, pattern, explanation, fact, dialogue):
        assert dialogue
        for fld in (title, pattern, explanation, fact):  # 1–2 letter tokens in notes are syllables/letters being shown
            u = [w for w in h.unknown(fld) if len(h.skeleton(w)) > 2]
            if u: self.problems.append(f"topic {tid} text: not in dictionary {u}")
        for sp, he, en in dialogue: self._check(f"topic {tid}", he)
        self.topics[tid] = {"title": title, "pattern": pattern, "explanation": explanation, "fact": fact,
                            "dialogue": [{"sp": sp, "native": he, "en": en} for sp, he, en in dialogue]}
    def L(self, number, title, title_he, items, topic=None):
        self._check(f"L{number} title", title_he)
        if len(items) < 6: self.problems.append(f"L{number}: only {len(items)} items")
        out, ens = [], set()
        for it in items:
            he, en, tr = it[:3]
            if len(it) <= 3: self._check(f"L{number}", he)   # syllable drills (with their own options) aren't words
            else:
                b = h.bad_chars(he)
                if b: self.problems.append(f"L{number}: {b} in «{he}»")
            if en in ens: self.problems.append(f"L{number}: duplicate English «{en}» (breaks matching)")
            ens.add(en)
            d = {"he": he, "en": en, "translit": tr}
            if len(it) > 3: del d["translit"]   # in a drill the transliteration IS the answer
            if len(it) > 3:
                w = it[3]
                if len(w) != 3 or len(set(w + [en])) != 4: self.problems.append(f"L{number}: bad wrong-options for «{he}»: {w}")
                d["wrong"] = w
            out.append(d)
        les = {"number": number, "title": title, "titleNative": title_he, "items": out}
        if topic: les["topicId"] = topic
        self.lessons.append(les)
    def R(self, number, title, title_he, context, paragraphs, questions):
        self._check(f"R{number} title", title_he)
        for he, en in paragraphs: self._check(f"R{number}", he)
        self.lessons.append({"number": number, "title": title, "titleNative": title_he, "context": context,
            "paragraphs": [{"he": he, "en": en} for he, en in paragraphs],
            "questions": [{"question": q, "options": o, "answerIndex": a} for q, o, a in questions]})
    def save(self):
        # lessons are numbered in the order they are written (readings keep 101+), so practice lessons can be inserted anywhere
        n = 0
        for l in self.lessons:
            if "items" in l:
                n += 1; l["number"] = n
        seen = set()
        for l in self.lessons:
            for it in l.get("items", []):
                if "wrong" in it: continue          # drills may repeat a syllable on purpose (spaced review)
                if it["he"] in seen: self.problems.append(f"L{l['number']}: duplicate «{it['he']}»")
                seen.add(it["he"])
        if self.problems:
            print("NOT SAVED —", len(self.problems), "problem(s):"); [print("  " + p) for p in self.problems]; sys.exit(1)
        doc = {"level": self.level, "lessons": self.lessons}
        if self.topics: doc["grammarTopics"] = self.topics
        json.dump(doc, open(self.path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"saved {os.path.basename(self.path)}: {len(self.lessons)} lessons, {sum(len(l.get('items',[])) for l in self.lessons)} items, {len(self.topics)} notes")
