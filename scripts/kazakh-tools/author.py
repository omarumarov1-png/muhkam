"""Authoring helper for Muhkam Kazakh source files (data/kazakh-src).
    from author import Course
    c = Course("a1", "a1")
    c.T("id", title, pattern, explanation, fact, [("A", tt, en), ...])
    c.L(1, "Title", "Татарча исем", [(tt, en), ...], topic="id")
    c.R(101, "Title", "Исем", context, [(tt, en), ...], [(question, [4 options], answerIndex), ...])
    c.save()
save() refuses to write if any Tatar word is unknown to the Apertium analyser / attested corpus / allow-list,
a lookalike (Latin, Kazakh, Serbian) letter sneaks in, a lesson has fewer than 4 items, or a sentence repeats
one from another source file. Sentences taken from Tatoeba are counted for the attribution line."""
import json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kklib as ttlib
SRC = os.path.expanduser("~/muhkam/data/kazakh-src")
MIN_ITEMS = 4
class Course:
    def __init__(self, level, name):
        self.level, self.path = level, os.path.join(SRC, name + ".json")
        self.lessons, self.topics, self.problems = [], {}, []
    def _check(self, where, tt):
        for p in ttlib.check(tt): self.problems.append(f"{where}: {p} in «{tt}»")
        if any(ch in "\u200b\u200c\u200d\ufeff\u00ad" for ch in tt): self.problems.append(f"{where}: invisible character in «{tt}»")
        if "title" not in where and any(ch.isdigit() for ch in tt): self.problems.append(f"{where}: digits (TTS can't read them) in «{tt}»")
    def T(self, tid, title, pattern, explanation, fact, dialogue):
        assert dialogue, "every grammar topic needs a dialogue (the app crashes otherwise)"
        for sp, tt, en in dialogue: self._check(f"topic {tid}", tt)
        self.topics[tid] = {"title": title, "pattern": pattern, "explanation": explanation, "fact": fact,
                            "dialogue": [{"sp": sp, "native": tt, "en": en} for sp, tt, en in dialogue]}
    def L(self, number, title, title_tt, items, topic=None):
        self._check(f"L{number} title", title_tt)
        if len(items) < MIN_ITEMS: self.problems.append(f"L{number}: only {len(items)} items")
        for tt, en in items: self._check(f"L{number}", tt)
        les = {"number": number, "title": title, "titleNative": title_tt, "items": [{"kk": tt, "en": en} for tt, en in items]}
        if topic: les["topicId"] = topic
        self.lessons.append(les)
    def R(self, number, title, title_tt, context, paragraphs, questions):
        self._check(f"R{number} title", title_tt)
        for tt, en in paragraphs: self._check(f"R{number}", tt)
        for q in questions: assert 0 <= q[2] < len(q[1]) == 4, f"R{number}: bad question {q}"
        self.lessons.append({"number": number, "title": title, "titleNative": title_tt, "context": context,
            "paragraphs": [{"kk": tt, "en": en} for tt, en in paragraphs],
            "questions": [{"question": q, "options": o, "answerIndex": a} for q, o, a in questions]})
    def save(self):
        nums = [l["number"] for l in self.lessons]
        if len(nums) != len(set(nums)): self.problems.append("duplicate lesson numbers")
        missing = [t for t in {l.get("topicId") for l in self.lessons} if t and t not in self.topics]
        if missing: self.problems.append(f"lessons point to grammar topics not defined in this file: {missing}")
        seen = {}
        for f in glob.glob(os.path.join(SRC, "*.json")):
            if os.path.abspath(f) == os.path.abspath(self.path): continue
            for l in json.load(open(f, encoding="utf-8"))["lessons"]:
                for it in l.get("items", []) + l.get("paragraphs", []): seen[it["kk"]] = os.path.basename(f)
        mine = set()
        for l in self.lessons:
            for it in l.get("items", []) + l.get("paragraphs", []):
                if it["kk"] in seen: self.problems.append(f"L{l['number']}: duplicate of {seen[it['kk']]}: «{it['kk']}»")
                if it["kk"] in mine: self.problems.append(f"L{l['number']}: duplicate inside file: «{it['kk']}»")
                mine.add(it["kk"])
        if self.problems:
            print("NOT SAVED —", len(self.problems), "problem(s):"); [print("  " + p) for p in self.problems[:60]]; sys.exit(1)
        os.makedirs(SRC, exist_ok=True)
        doc = {"level": self.level, "lessons": self.lessons}
        if self.topics: doc["grammarTopics"] = self.topics
        json.dump(doc, open(self.path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = sum(len(l.get("items", [])) for l in self.lessons)
        print(f"saved {os.path.basename(self.path)}: {len(self.lessons)} lessons, {n} sentences, {len(self.topics)} grammar notes")
