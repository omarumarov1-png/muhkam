# -*- coding: utf-8 -*-
"""Everyday Kazakh: extra lessons from Tatoeba kaz-eng (CC BY 2.0 FR), appended to A1, A2, B1."""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "everyday_data.json"), encoding="utf-8"))
START = {"a1": 46, "a2": 53, "b1": 90}
for level, items in DATA.items():
    random.Random(7).shuffle(items)
    n = len(items) // 4
    chunks = [items[i * 4:(i + 1) * 4] for i in range(n)]
    for j, extra in enumerate(items[n * 4:]):
        chunks[j].append(extra)
    c = Course(level, f"{level}-everyday")
    for k, ch in enumerate(chunks):
        c.L(START[level] + k, f"Everyday Kazakh {k + 1}", f"Күнделікті сөйлесу {k + 1}", [tuple(x) for x in ch])
    c.save()
