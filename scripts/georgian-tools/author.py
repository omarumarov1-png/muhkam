"""Authoring helper for Muhkam Georgian source files.
Usage in a write script:
    from author import Course
    c = Course("a1", "a1-script")
    c.T("id", title, pattern, explanation, fact, [("A", ka, en), ...])
    c.L(1, "Title", "ქართული სათაური", [(ka, en), ...], topic="id")
    c.save()
save() refuses to write if any Georgian word fails the dictionary check, a non-Mkhedruli letter sneaks in,
a lesson has fewer than 6 items, or a sentence duplicates one already in another source file."""
import json, os, sys, glob
import kalib as k
SRC = os.path.expanduser("~/muhkam/data/georgian-src")
class Course:
    def __init__(self, level, name):
        self.level, self.path = level, os.path.join(SRC, name + ".json")
        self.lessons, self.topics, self.problems = [], {}, []
    def _check(self, where, ka):
        u = k.unknown(ka); b = k.bad_chars(ka)
        if u: self.problems.append(f"{where}: unknown {u} in «{ka}»")
        if b: self.problems.append(f"{where}: bad characters {b} in «{ka}»")
    def T(self, tid, title, pattern, explanation, fact, dialogue):
        assert dialogue, "every grammar topic needs a dialogue (app crashes otherwise)"
        # Georgian quoted inside the explanation is checked too; 1–3 letter tokens are affixes being discussed (-ში, -დან).
        for fld in (title, pattern, explanation, fact):
            u = [w for w in k.unknown(fld) if len(w) > 3]
            if u: self.problems.append(f"topic {tid} text: unknown {u}")
        for sp, ka, en in dialogue: self._check(f"topic {tid}", ka)
        self.topics[tid] = {"title": title, "pattern": pattern, "explanation": explanation, "fact": fact,
                            "dialogue": [{"sp": sp, "native": ka, "en": en} for sp, ka, en in dialogue]}
    def L(self, number, title, title_ka, items, topic=None):
        self._check(f"L{number} title", title_ka)
        if len(items) < 6: self.problems.append(f"L{number}: only {len(items)} items")
        out = []
        for ka, en in items:
            self._check(f"L{number}", ka)
            out.append({"ka": ka, "en": en, "translit": k.romanize(ka)})
        les = {"number": number, "title": title, "titleNative": title_ka, "items": out}
        if topic: les["topicId"] = topic
        self.lessons.append(les)
    def R(self, number, title, title_ka, context, paragraphs, questions):
        self._check(f"R{number} title", title_ka)
        for ka, en in paragraphs: self._check(f"R{number}", ka)
        for q in questions: assert 0 <= q[2] < len(q[1]) == 4, f"R{number}: bad question {q}"
        self.lessons.append({"number": number, "title": title, "titleNative": title_ka, "context": context,
            "paragraphs": [{"ka": ka, "en": en} for ka, en in paragraphs],
            "questions": [{"question": q, "options": o, "answerIndex": a} for q, o, a in questions]})
    def save(self):
        nums = [l["number"] for l in self.lessons]
        if len(nums) != len(set(nums)): self.problems.append("duplicate lesson numbers")
        seen = {}
        for f in glob.glob(os.path.join(SRC, "*.json")):
            if os.path.abspath(f) == os.path.abspath(self.path): continue
            for l in json.load(open(f, encoding="utf-8"))["lessons"]:
                for it in l.get("items", []): seen[it["ka"]] = os.path.basename(f)
        mine = set()
        for l in self.lessons:
            for it in l.get("items", []):
                if it["ka"] in seen: self.problems.append(f"L{l['number']}: duplicate of {seen[it['ka']]}: «{it['ka']}»")
                if it["ka"] in mine: self.problems.append(f"L{l['number']}: duplicate inside file: «{it['ka']}»")
                mine.add(it["ka"])
        if self.problems:
            print("NOT SAVED —", len(self.problems), "problem(s):"); [print("  " + p) for p in self.problems]; sys.exit(1)
        os.makedirs(SRC, exist_ok=True)
        doc = {"level": self.level, "lessons": self.lessons}
        if self.topics: doc["grammarTopics"] = self.topics
        json.dump(doc, open(self.path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = sum(len(l.get("items", [])) for l in self.lessons)
        print(f"saved {os.path.basename(self.path)}: {len(self.lessons)} lessons, {n} sentences, {len(self.topics)} grammar notes")
