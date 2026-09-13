#!/usr/bin/env python3
"""Full rewrite of A1 Khaleeji Arabic content: fixes the filler-word
repetition problem (every old sentence padded with اليوم/زين/كثير
regardless of relevance) by hand-authoring natural, topically-varied
sentences instead of templated ones. See scripts/verify_emirati_vocab.py
for the vocab guard and data/emirati-research/researched_vocab.json for
the newly expanded (Khaleeji-wide) vocabulary/verb paradigms this draws on.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import verify_emirati_vocab as V  # noqa: E402

SEEN = set()


def item(ar, en, translit=None):
    if ar in SEEN:
        raise ValueError(f"DUPLICATE sentence: {ar!r}")
    SEEN.add(ar)
    ok, bad = V.check_sentence(ar)
    if not ok:
        raise ValueError(f"Unconfirmed words {bad} in: {ar!r}")
    d = {"ar": ar, "en": en}
    if translit:
        d["translit"] = translit
    return d


def lesson(number, title, titleNative, items, topicId=None):
    d = {"number": number, "title": title, "titleNative": titleNative, "items": items}
    if topicId:
        d["topicId"] = topicId
    return d


LESSONS = [
    lesson(1, "Hello and Peace", "السلام والتحية", [
        item("السلام عليكم", "Peace be upon you", "as-salaamu alaykum"),
        item("وعليكم السلام", "And peace be upon you", "wa alaykum as-salaam"),
        item("مرحبا، هلا والله", "Hello, welcome", "marhaba, hala wallah"),
        item("تشرفت فيك", "Nice to meet you", "tasharraft feek"),
    ], topicId="a1-greetings"),

    lesson(2, "How Are You?", "شلونك؟", [
        item("شلونك؟", "How are you?", "shlonak?"),
        item("زين، الحمد لله", "Good, thank God", "zayn, alhamdulillah"),
        item("وانت، شلونك؟", "And you, how are you?", "wa inta, shlonak?"),
        item("أنا مبسوط الحين", "I'm happy right now", "ana mabsoot el-heen"),
    ]),

    lesson(3, "Thank You and Sorry", "شكراً وآسف", [
        item("شكراً", "Thank you", "shukran"),
        item("العفو، ما في مشكلة", "You're welcome, no problem", "el-3afw, maa fee mushkila"),
        item("آسف", "Sorry", "aasif"),
        item("يعطيك العافية", "Thank you (lit. may God give you strength)", "ya3teek el-3aafya"),
    ]),

    lesson(4, "Yes, No, Okay", "نعم، لا، تمام", [
        item("نعم، تمام", "Yes, okay", "na3am, tamaam"),
        item("لا، آسف", "No, sorry", "laa, aasif"),
        item("خلاص", "Done, that's settled", "khalaas"),
        item("ممكن؟", "Is that possible? May I?", "mumkin?"),
    ]),

    lesson(5, "Meeting Someone", "التعارف", [
        item("هلا والله، من وين انت؟", "Welcome, where are you from?", "hala wallah, min wein inta?"),
        item("أنا من هنا", "I'm from here", "ana min hina"),
        item("وانتي، من وين انتي؟", "And you (f), where are you from?", "wa inti, min wein inti?"),
        item("أنا من هناك", "I'm from there", "ana min hinaak"),
    ]),

    lesson(6, "Morning and Evening", "الصباح والمساء", [
        item("صباح الخير", "Good morning", "sabaah el-khayr"),
        item("مساء الخير", "Good evening", "masaa el-khayr"),
        item("الصبح أشرب قهوة", "In the morning I drink coffee", "es-sub7 ashrab gahwa"),
        item("الليل أروح البيت", "At night I go home", "el-layl aruu7 el-bayt"),
    ]),

    lesson(7, "No Problem and Possible", "ما في مشكلة وممكن", [
        item("ما في مشكلة", "No problem", "maa fee mushkila"),
        item("ممكن أبغى قهوة؟", "May I have coffee?", "mumkin abgha gahwa?"),
        item("خلاص، تمام", "Alright, okay", "khalaas, tamaam"),
        item("لا مشكلة، طبعا", "No problem, of course", "laa mushkila, taba3an"),
    ]),

    lesson(8, "Pronouns: I, You, He, She", "الضمائر", [
        item("أنا هنا", "I am here", "ana hina"),
        item("انت تعبان", "You (m) are tired", "inta ta3baan"),
        item("هو هناك", "He is there", "huwa hinaak"),
        item("هي تشرب قهوة", "She drinks coffee", "hiya tishrab gahwa"),
    ]),

    lesson(9, "Pronouns: We, You All, They", "الضمائر: احنا، انتوا، هم", [
        item("احنا هنا", "We are here", "i7na hina"),
        item("انتوا هناك", "You all are there", "intu hinaak"),
        item("هم مبسوطين", "They are happy", "humma mabsooteen"),
        item("هم يشربون شاي", "They drink tea", "humma yishrabuun shaay"),
    ]),

    lesson(10, "Review: Greetings and Pronouns", "مراجعة: التحية والضمائر", [
        item("السلام عليكم، شلونك؟", "Peace be upon you, how are you?", "as-salaamu alaykum, shlonak?"),
        item("زين، الحمد لله، وانت؟", "Good, thank God, and you?", "zayn, alhamdulillah, wa inta?"),
        item("احنا مبسوطين اليوم", "We are happy today", "i7na mabsooteen el-yoom"),
        item("هم زين، شكراً", "They are well, thank you", "humma zayn, shukran"),
    ]),

    lesson(11, "Numbers 1-5", "الأرقام ١-٥", [
        item("واحد، اثنين، ثلاثة", "One, two, three", "waahid, ithnayn, thalaatha"),
        item("أربعة وخمسة", "Four and five", "arba3a wa khamsa"),
        item("أبغى ثلاثة", "I want three", "abgha thalaatha"),
        item("كم هذا؟ خمسة", "How much is this? Five", "kam hatha? khamsa"),
    ]),

    lesson(12, "Numbers 6-10", "الأرقام ٦-١٠", [
        item("ستة وسبعة", "Six and seven", "sitta wa sab3a"),
        item("ثمانية وتسعة", "Eight and nine", "thamaanya wa tis3a"),
        item("هذا عشرة", "This is ten", "hatha 3ashara"),
        item("كم هذا؟ سبعة", "How much is this? Seven", "kam hatha? sab3a"),
    ]),

    lesson(13, "Colors", "الألوان", [
        item("هذا أحمر", "This is red", "hatha ahmar"),
        item("السيارة زرقاء", "The car is blue", "es-sayyaara zarqaa"),
        item("القميص أصفر", "The shirt is yellow", "el-gamees asfar"),
        item("البيت أخضر", "The house is green", "el-bayt akhdar"),
    ]),

    lesson(14, "Family", "العائلة", [
        item("هذا أبويه", "This is dad", "hatha abooyah"),
        item("هذي يمة", "This is mom", "hathi yumma"),
        item("هذا أخو", "This is brother", "hatha akhu"),
        item("الأهل زين، الحمد لله", "The family is well, thank God", "el-ahl zayn, alhamdulillah"),
    ]),

    lesson(15, "I Want", "أبغى", [
        item("أبغى قهوة", "I want coffee", "abgha gahwa"),
        item("أبغى شاي، مب قهوة", "I want tea, not coffee", "abgha shaay, mub gahwa"),
        item("أبغى مويه بارده", "I want cold water", "abgha moya baarda"),
        item("أبغى أكل الحين", "I want food right now", "abgha akal el-heen"),
    ]),

    lesson(16, "I Drink, You Drink", "أشرب، تشرب", [
        item("أشرب قهوة الصبح", "I drink coffee in the morning", "ashrab gahwa es-sub7"),
        item("تشرب شاي، وأنا أشرب قهوة", "You (m) drink tea, and I drink coffee", "tishrab shaay, wa ana ashrab gahwa"),
        item("تشربين مويه؟", "Do you (f) drink water?", "tishrabeen moya?"),
        item("هو يشرب قهوة، وهي تشرب شاي", "He drinks coffee, and she drinks tea", "yishrab gahwa, wa tishrab shaay"),
    ], topicId="a1-present-shirib"),

    lesson(17, "We Drink, They Drink", "نشرب، يشربون", [
        item("نشرب قهوة كل صباح", "We drink coffee every morning", "nishrab gahwa kil sabaah"),
        item("انتوا تشربون شاي؟", "Do you all drink tea?", "intu tishrabuun shaay?"),
        item("هم يشربون مويه بعد الأكل", "They drink water after the food", "humma yishrabuun moya ba3d el-akal"),
        item("ما نشرب قهوة الليل", "We don't drink coffee at night", "ma nishrab gahwa el-layl"),
    ], topicId="a1-present-shirib"),

    lesson(18, "Question Words", "أدوات الاستفهام", [
        item("شنو هذا؟", "What is this?", "shinu hatha?"),
        item("وين البيت؟", "Where is the house?", "wein el-bayt?"),
        item("ليش انت تعبان؟", "Why are you tired?", "leish inta ta3baan?"),
        item("متى الأكل؟", "When is the food?", "mita el-akal?"),
    ]),

    lesson(19, "Feelings", "المشاعر", [
        item("أنا تعبان الحين", "I am tired right now", "ana ta3baan el-heen"),
        item("هو مبسوط اليوم", "He is happy today", "huwa mabsoot el-yoom"),
        item("أنا جوعان، أبغى أكل", "I am hungry, I want food", "ana joo3aan, abgha akal"),
        item("أنا عطشان، أبغى مويه", "I am thirsty, I want water", "ana 3atshaan, abgha moya"),
    ]),

    lesson(20, "Review: Numbers, Colors, Family, Feelings", "مراجعة", [
        item("الأهل عندهم بيت كبير وجديد", "The family has a big new house", "el-ahl 3indahum bayt kabeer wa jideed"),
        item("البيت أحمر وأخضر", "The house is red and green", "el-bayt ahmar wa akhdar"),
        item("الأهل مبسوطين اليوم", "The family is happy today", "el-ahl mabsooteen el-yoom"),
        item("أنا جوعان، وين الأكل؟", "I'm hungry, where's the food?", "ana joo3aan, wein el-akal?"),
    ]),

    lesson(21, "Days of the Week", "أيام الأسبوع", [
        item("اليوم الأحد", "Today is Sunday", "el-yoom el-a7ad"),
        item("بكرا الاثنين", "Tomorrow is Monday", "bukra el-ithnayn"),
        item("يوم الجمعة أروح المسجد", "On Friday I go to the mosque", "yoom el-jum3a aruu7 el-masjid"),
        item("يوم السبت أنا مب مشغول", "On Saturday I'm not busy", "yoom es-sabt ana mub mashghool"),
    ]),

    lesson(22, "Big and Small", "كبير وصغير", [
        item("هذا بيت كبير", "This is a big house", "hatha bayt kabeer"),
        item("هذي سيارة صغيرة", "This is a small car", "hathi sayyaara sagheera"),
        item("البيت الجديد كبير", "The new house is big", "el-bayt el-jideed kabeer"),
        item("القميص القديم صغير", "The old shirt is small", "el-gamees el-gadeem sagheer"),
    ]),

    lesson(23, "I Don't Want / I'm Not", "ما أبغى / أنا مب", [
        item("ما أبغى قهوة، أبغى شاي", "I don't want coffee, I want tea", "ma abgha gahwa, abgha shaay"),
        item("أنا مب تعبان، أنا مبسوط", "I'm not tired, I'm happy", "ana mub ta3baan, ana mabsoot"),
        item("ما أشرب شاي بارد", "I don't drink cold tea", "ma ashrab shaay baarid"),
        item("البيت مب كبير، صغير", "The house isn't big, it's small", "el-bayt mub kabeer, sagheer"),
    ], topicId="a1-negation"),

    lesson(24, "I Go, You Go", "أروح، تروح", [
        item("أروح الشغل الصبح", "I go to work in the morning", "aruu7 esh-shaghal es-sub7"),
        item("تروح السوق بكرا؟", "Are you going to the market tomorrow?", "truu7 es-suug bukra?"),
        item("تروحين المدرسة؟", "Are you (f) going to school?", "truu7een el-madrasa?"),
        item("هو يروح المطعم كل جمعة", "He goes to the restaurant every Friday", "yruu7 el-mat3am kil jum3a"),
    ]),

    lesson(25, "She Goes, We Go, They Go", "تروح، نروح، يروحون", [
        item("هي تروح السوق مع يمة", "She goes to the market with mom", "truu7 es-suug ma3 yumma"),
        item("نروح المسجد يوم الجمعة", "We go to the mosque on Friday", "nruu7 el-masjid yoom el-jum3a"),
        item("انتوا تروحون وين بكرا؟", "Where are you all going tomorrow?", "intu truu7oon wein bukra?"),
        item("هم يروحون المطعم كل يوم", "They go to the restaurant every day", "yruu7oon el-mat3am kil yoom"),
    ]),

    lesson(26, "Places: Here, There, Near, Far", "هنا، هناك، قريب، بعيد", [
        item("المطعم هنا", "The restaurant is here", "el-mat3am hina"),
        item("المستشفى هناك", "The hospital is there", "el-mustashfa hinaak"),
        item("السوق قريب من البيت", "The market is near the house", "es-suug gareeb min el-bayt"),
        item("بيت جدي بعيد من هنا", "My grandfather's house is far from here", "bayt jiddi ba3eed min hina"),
    ]),

    lesson(27, "Directions: Right, Left, In Front, Behind", "يمين، يسار، قدام، ورا", [
        item("السوق يمين", "The market is to the right", "es-suug yameen"),
        item("المستشفى يسار", "The hospital is to the left", "el-mustashfa yasaar"),
        item("البيت قدّام المسجد", "The house is in front of the mosque", "el-bayt guddaam el-masjid"),
        item("السيارة ورا البيت", "The car is behind the house", "es-sayyaara wara el-bayt"),
    ]),

    lesson(28, "Car and Taxi", "سيارة وتاكسي", [
        item("عندي سيارة جديدة", "I have a new car", "3indi sayyaara jideeda"),
        item("التاكسي بعيد الحين", "The taxi is far away right now", "et-taaksi ba3eed el-heen"),
        item("أروح الشغل بالسيارة", "I go to work by car", "aruu7 esh-shaghal bis-sayyaara"),
        item("تبغى تاكسي؟", "Do you want a taxi?", "tibgha taaksi?"),
    ]),

    lesson(29, "Money: How Much?", "كم؟", [
        item("كم هذا؟", "How much is this?", "kam hatha?"),
        item("هذا غالي كثير", "This is very expensive", "hatha ghaali katheer"),
        item("هذا رخيص، زين", "This is cheap, good", "hatha rakhees, zayn"),
        item("وين الفلوس؟", "Where's the money?", "wein el-fluus?"),
    ]),

    lesson(30, "Review: Directions, Places, Negation", "مراجعة", [
        item("السوق قريب، مب بعيد", "The market is near, not far", "es-suug gareeb, mub ba3eed"),
        item("البيت الجديد يمين المسجد", "The new house is to the right of the mosque", "el-bayt el-jideed yameen el-masjid"),
        item("كم هذا؟ غالي مب رخيص", "How much is this? Expensive, not cheap", "kam hatha? ghaali mub rakhees"),
        item("ما أروح هناك، بعيد كثير", "I'm not going there, it's very far", "ma aruu7 hinaak, ba3eed katheer"),
    ]),

    lesson(31, "Professions", "المهن", [
        item("أبويه مدرس", "Dad is a teacher", "abooyah mudarris"),
        item("يمة مهندسة", "Mom is an engineer", "yumma muhandisa"),
        item("أخوي دريول", "My brother is a driver", "akhooy daryool"),
        item("عندك شغل زين", "You have good work", "3indak shughul zayn"),
    ]),

    lesson(32, "Professions II", "المهن ٢", [
        item("خالي تاجر", "My maternal uncle is a merchant", "khaali taajir"),
        item("عمي ميكانيكي", "My paternal uncle is a mechanic", "3ammi mikaaniki"),
        item("هذا مترجم زين", "This is a good translator", "hatha mutarjim zayn"),
        item("هذي سكرتيرة الشغل", "This is the work secretary", "hathi sikirteera esh-shaghal"),
    ]),

    lesson(33, "Extended Family", "العائلة الكبيرة", [
        item("جدي وجدتي يروحون بيتنا كل جمعة", "My grandfather and grandmother come to our house every Friday", "jiddi wa jiddati yruu7oon baytna kil jum3a"),
        item("خالتي عندها بنت وابن", "My maternal aunt has a daughter and a son", "khaalti 3indaha bint wa ibin"),
        item("ابن العم عنده سيارة جديدة", "My paternal cousin has a new car", "ibin el-3amm 3indah sayyaara jideeda"),
        item("حفيدي مبسوط اليوم", "My grandson is happy today", "7afeedi mabsoot el-yoom"),
    ]),

    lesson(34, "Clothes Shopping", "شراء الملابس", [
        item("أبغى قميص جديد", "I want a new shirt", "abgha gamees jideed"),
        item("الغترة غالية هنا", "The headdress is expensive here", "el-ghitra ghaalya hina"),
        item("جوتيه رخيص في السوق", "Shoes are cheap in the market", "jootee rakhees fis-suug"),
        item("أبغى عباية زينة", "I want a nice abaya", "abgha 3abaaya zeena"),
    ]),

    lesson(35, "Food at the Restaurant", "الأكل في المطعم", [
        item("أبغى لحم وسلطة", "I want meat and salad", "abgha la7am wa salata"),
        item("عندهم بيض زين هنا", "They have good eggs here", "3indahum bayd zayn hina"),
        item("الأكل لذيذ في هذا المطعم", "The food is delicious at this restaurant", "el-akal latheeth fi haadha el-mat3am"),
        item("أبغى الحساب لو سمحت", "I want the bill please", "abgha el-7isaab law sama7t"),
    ]),

    lesson(36, "Weather", "الجو", [
        item("الجو حار اليوم", "The weather is hot today", "el-jaww 7aarr el-yoom"),
        item("الجو بارد الليل", "The weather is cold at night", "el-jaww baarid el-layl"),
        item("الجو مشمس بكرا", "It's sunny tomorrow", "el-jaww mishmis bukra"),
        item("فيه ريح ورطوبة اليوم", "There's wind and humidity today", "feeh reeh wa rutuuba el-yoom"),
    ]),

    lesson(37, "Around the House", "البيت", [
        item("فيه باب كبير في البيت", "There's a big door in the house", "feeh baab kabeer fil-bayt"),
        item("الدريشة نظيفة", "The window is clean", "ed-dreesha nadheefa"),
        item("الطاولة والكرسي في المطبخ", "The table and chair are in the kitchen", "et-taawla wal-kursi fil-matbakh"),
        item("الصحن وسخ، لازم أنظف الصحن", "The plate is dirty, I need to clean the plate", "es-sa7in wisikh, laazim anadhdhif es-sa7in"),
    ]),

    lesson(38, "Animals", "الحيوانات", [
        item("عندي قطوة في البيت", "I have a cat at home", "3indi gattwa fil-bayt"),
        item("شفت جلب كبير أمس", "I saw a big dog yesterday", "shift jalib kabeer ams"),
        item("خالي عنده جمل", "My maternal uncle has a camel", "khaali 3indah jamal"),
        item("شفت طير صغير الحين", "I just saw a small bird", "shift teer sagheer el-heen"),
    ]),

    lesson(39, "Numbers 13-20", "الأرقام ١٣-٢٠", [
        item("ثلاث طعش وأربع طعش", "Thirteen and fourteen", "thalaath ta3sh wa arba3 ta3sh"),
        item("خمس طعش وعشرين", "Fifteen and twenty", "khamas ta3sh wa 3ishreen"),
        item("عندنا عشرين دقيقة", "We have twenty minutes", "3indana 3ishreen dageega"),
        item("كم هذا؟ خمس طعش", "How much is this? Fifteen", "kam hatha? khamas ta3sh"),
    ]),

    lesson(40, "Eating", "الأكل", [
        item("آكل بيض كل صباح", "I eat eggs every morning", "aakil bayd kil sabaah"),
        item("تاكل لحم اليوم؟", "Are you eating meat today?", "taakil la7am el-yoom?"),
        item("ياكل سلطة قبل اللحم", "He eats salad before the meat", "yaakil salata gabl el-la7am"),
        item("اكلنا في المطعم أمس", "We ate at the restaurant yesterday", "kalayna fil-mat3am ams"),
    ]),

    lesson(41, "I Cook, You Cook", "أطبخ، تطبخ", [
        item("أطبخ لحم كل جمعة", "I cook meat every Friday", "atbakh la7am kil jum3a"),
        item("تطبخين سلطة زينة", "You (f) cook good salad", "tatbakheen salata zeena"),
        item("يطبخ بيض الصبح", "He cooks eggs in the morning", "yatbakh bayd es-sub7"),
        item("طبخنا لحم وبيض الصبح", "We cooked meat and eggs in the morning", "tabakhna la7am wa bayd es-sub7"),
    ]),

    lesson(42, "New Adjectives", "صفات جديدة", [
        item("البيت جميل", "The house is beautiful", "el-bayt jameel"),
        item("الشغل صعب اليوم", "The work is difficult today", "esh-shaghal sa3b el-yoom"),
        item("هذا سهل كثير", "This is very easy", "hatha sahil katheer"),
        item("القميص نظيف والبنطلون وسخ", "The shirt is clean and the pants are dirty", "el-gamees nadheef wal-bantaloon wisikh"),
    ]),

    lesson(43, "Things I Want", "أشياء أبغاها", [
        item("أبغى كتاب جديد", "I want a new book", "abgha kitaab jideed"),
        item("أبغى قلم وكتاب", "I want a pen and a book", "abgha galam wa kitaab"),
        item("وين مفتاح البيت؟", "Where's the house key?", "wein miftaa7 el-bayt?"),
        item("محفظتي في السيارة", "My wallet is in the car", "ma7fadhti fis-sayyaara"),
    ]),

    lesson(44, "I Clean, You Clean", "أنظف، تنظف", [
        item("أنظف البيت كل جمعة", "I clean the house every Friday", "anadhdhif el-bayt kil jum3a"),
        item("تنظف المطبخ الحين؟", "Are you cleaning the kitchen now?", "tinadhdhif el-matbakh el-heen?"),
        item("هي تنظف الدريشة", "She cleans the window", "tinadhdhif ed-dreesha"),
        item("ننظف البيت قبل العيد", "We clean the house before Eid", "nanadhdhif el-bayt gabl el-3eed"),
    ]),

    lesson(45, "Time of Day", "أوقات اليوم", [
        item("أروح المدرسة الصبح", "I go to school in the morning", "aruu7 el-madrasa es-sub7"),
        item("أشرب قهوة عصر", "I drink coffee in the afternoon", "ashrab gahwa 3asir"),
        item("لازم أروح البيت الليل", "I have to go home at night", "laazim aruu7 el-bayt el-layl"),
        item("ما أشتغل بعد الظهر", "I don't work after noon", "ma ashtaghil ba3d edh-dhuhur"),
    ]),

    lesson(46, "Polite Phrases", "عبارات مؤدبة", [
        item("من فضلك، أبغى قهوة", "Please, I want coffee", "min fadlak, abgha gahwa"),
        item("لو سمحت، وين المطعم؟", "Excuse me, where is the restaurant?", "law sama7t, wein el-mat3am?"),
        item("طبعا، ما في مشكلة", "Of course, no problem", "taba3an, maa fee mushkila"),
        item("انشاالله بكرا", "God willing, tomorrow", "inshaallah bukra"),
    ]),

    lesson(47, "Reactions", "ردود فعل", [
        item("يلا، نروح السوق", "Come on, let's go to the market", "yalla, nruu7 es-suug"),
        item("هذا حلو كثير", "This is very nice", "hatha 7ilu katheer"),
        item("مبروك! البيت الجديد زين", "Congratulations! The new house is nice", "mabruuk! el-bayt el-jideed zayn"),
        item("والله ما أدري", "By God, I don't know", "wallah ma adri"),
    ]),

    lesson(48, "The Bill and Free Things", "الحساب ومجاني", [
        item("الحساب لو سمحت", "The bill please", "el-7isaab law sama7t"),
        item("هذا مجاني اليوم", "This is free today", "hatha majjaani el-yoom"),
        item("كم الحساب كله؟", "How much is the whole bill?", "kam el-7isaab kila?"),
        item("القهوة مجانية بعد الأكل", "The coffee is free after the meal", "el-gahwa majjaaniya ba3d el-akal"),
    ]),

    lesson(49, "Arabic Coffee and Hospitality", "القهوة العربية والضيافة", [
        item("الدلة والفنجان في كل بيت خليجي", "The coffee pot and cup are in every Gulf house", "ed-dalla wal-finjaan fi kil bayt khaleeji"),
        item("عندهم قهوة وتمر زين", "They have good coffee and dates", "3indahum gahwa wa tamur zayn"),
        item("البخور زين في البيت", "The incense is nice in the house", "el-bukhoor zayn fil-bayt"),
        item("الفنجان صغير، والدلة كبيرة", "The cup is small, and the dallah is big", "el-finjaan sagheer, wad-dalla kabeera"),
    ]),

    lesson(50, "The Gulf Countries", "دول الخليج", [
        item("الإمارات والسعودية في الخليج", "The UAE and Saudi Arabia are in the Gulf", "el-imaaraat was-sa3oodiyya fil-khaleej"),
        item("الكويت وقطر والبحرين في الخليج", "Kuwait, Qatar, and Bahrain are in the Gulf", "el-kuwayt wa gatar wal-ba7rayn fil-khaleej"),
        item("عندي أهل في عمان", "I have family in Oman", "3indi ahl fi 3umaan"),
        item("هذا خليجي، وهذا مب خليجي", "This one is Khaleeji, and this one isn't", "hatha khaleeji, wa hatha mub khaleeji"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    grammar_topics = json.loads((ROOT / "data/emirati-src/a1.json").read_text(encoding="utf-8")).get("grammarTopics", {})
    out = {"level": "a1", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/a1.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
