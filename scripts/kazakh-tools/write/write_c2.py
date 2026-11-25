# -*- coding: utf-8 -*-
"""Kazakh C2: proverbs (мақал-мәтелдер) from Common Voice Kazakh text (CC0), English translations ours."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
HERE = os.path.dirname(os.path.abspath(__file__))
items = json.load(open(os.path.join(HERE, "c2_data.json"), encoding="utf-8"))
c = Course("c2", "c2")
T = c.T
T("kk-c2-friends", "Proverbs of Friendship", "Досыңа … , дұшпаныңа … · … болсаң, …",
  "Kazakh proverbs about friends and enemies are built as mirrored pairs: Досыңның мың болғанына мақтан, дұшпаның жалғыз болса да сақтан. "
  "The conditional -са/-се sets up the image and the -ар/-ер future draws the lesson: Жақсымен жолдас болсаң, жетерсің мұратқа.",
  "Kazakh has two words for enemy: жау (an enemy in war) and дұшпан (a personal foe). Proverbs prefer дұшпан.",
  [("A", "Жаңа досың қалай?", "How's your new friend?"), ("B", "Жақсы, бірақ ескі дос естен кетпейді ғой.", "Good, but an old friend is never forgotten, you know."), ("A", "Дұрыс айтасың.", "You're right.")])
T("kk-c2-words", "Proverbs about Speech", "Айтылған сөз — атылған оқ · сөз · тіл · ауыз",
  "Few cultures prize the spoken word like the Kazakhs, whose oral poets (ақындар) and orators (шешендер) were famous across the steppe. "
  "These proverbs warn and teach: a word, once spoken, cannot be called back. Note the dash for is: Тұз — астың дәмі.",
  "Айтыс, a live duel of improvising poets, is still a popular televised event in Kazakhstan.",
  [("A", "Неге үндемей отырсың?", "Why are you sitting in silence?"), ("B", "Айтылған сөз — атылған оқ, дейді ғой.", "A word spoken is a bullet fired, as they say."), ("A", "Онда ойланып сөйле.", "Then think before you speak.")])
T("kk-c2-wisdom", "Proverbs of Knowledge", "білім · ақыл · ғалым · надан",
  "Knowledge (білім), reason (ақыл) and the scholar (ғалым) stand against ignorance (надандық) in dozens of sayings. "
  "Comparatives are often made without -рақ, by setting two things side by side: Білімнен қымбат досың жоқ — no friend dearer than knowledge.",
  "Abai Kunanbaev, the national poet, wrote in his Words of Edification that learning is the path out of a people's misfortune.",
  [("A", "Бұл сұрақтың жауабын білмеймін.", "I don't know the answer to this question."), ("B", "Білмегеніңді үлкендерден сұра.", "Ask your elders what you don't know."), ("A", "Солай істеймін.", "I'll do that.")])
T("kk-c2-work", "Proverbs of Work and Wealth", "еңбек · мал · бай · кедей",
  "Herding culture shows in proverbs about wealth: мал (livestock) is the old word for property itself. "
  "Work (еңбек) is praised and laziness (жалқаулық) mocked; many sayings use the -ған participle as a noun: еңбек қуған — the one who pursues labour.",
  "Еңбек етсең ерінбей, тояды қарның тіленбей — if you work without laziness, you'll eat without begging — is one of Abai's best-known lines.",
  [("A", "Шаршадым, демалғым келеді.", "I'm tired, I want to rest."), ("B", "Еңбек етсең ерінбей, тояды қарның тіленбей.", "Work without laziness, and you'll eat without begging."), ("A", "Жарайды, тағы бір сағат істеймін.", "All right, I'll work one more hour.")])
T("kk-c2-kin", "Proverbs of Family and Kin", "ағайын · туыс · бала · әке",
  "Kinship (ағайын, туыс) is the backbone of traditional Kazakh society, and proverbs describe both its comfort and its quarrels. "
  "Watch for the genitive-possessive pairs: атаның баласы, ағайынның өкпесі.",
  "Kazakhs traditionally knew their ancestors back seven generations (жеті ата), and marriage within those seven was not allowed.",
  [("A", "Ағайындарың көп пе?", "Do you have many relatives?"), ("B", "Иә, көп. Олар әрқашан көмектеседі.", "Yes, many. They always help."), ("A", "Бақытты адамсың.", "You're a lucky person.")])
T("kk-c2-character", "Proverbs of Character", "жақсы · жаман · ер · батыр",
  "The constant pair жақсы — жаман (good — bad person) runs through these sayings, along with ер (a real man, a hero) and батыр (a warrior). "
  "Imperatives give advice to the listener: Жақсымын деп мақтанба. Ask yourself which half of each proverb is the image and which is the lesson.",
  "Many proverbs here were collected in nineteenth-century anthologies, but most are still heard in everyday speech today.",
  [("A", "Ол өзін өте жақсы деп мақтайды.", "He boasts that he's very good."), ("B", "Жақсымын деп мақтанба, халық айтсын.", "Don't boast that you're good; let the people say it."), ("A", "Иә, ол мұны білмейді.", "Yes, he doesn't know that.")])
L = c.L
from collections import OrderedDict
by = OrderedDict()
MAP = {"school": "character"}
for tp, kk, en in items: by.setdefault(MAP.get(tp, tp), []).append((kk, en))
for k in by: by[k].sort(key=lambda x: len(x[0]))
chunks, left = {}, []
for tp, xs in by.items():
    n = len(xs) // 4 * 4; chunks[tp] = [xs[i:i + 4] for i in range(0, n, 4)]; left += xs[n:]
for j, x in enumerate(left): chunks["character"][j % len(chunks["character"])].append(x)
order, it = [], {k: list(v) for k, v in chunks.items()}
while any(it.values()):
    for k in list(it):
        if it[k]: order.append((k, it[k].pop(0)))
NAMES = {"friends": ("Friends and Foes", "Дос пен дұшпан"), "words": ("The Spoken Word", "Сөз құдіреті"), "wisdom": ("Knowledge", "Білім мен ақыл"),
         "work": ("Work and Wealth", "Еңбек пен байлық"), "kin": ("Family and Kin", "Ағайын-туыс"), "character": ("Character", "Мінез")}
cnt = {}
for i, (top, its) in enumerate(order, 1):
    cnt[top] = cnt.get(top, 0) + 1
    en, kk = NAMES[top]
    L(i, f"{en} {cnt[top]}", f"{kk} {cnt[top]}", its, "kk-c2-" + top)
c.save()
