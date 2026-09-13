#!/usr/bin/env python3
"""Full rewrite of B1 Khaleeji Arabic content -- same repetition fix as
A1/A2, but pushed toward genuinely more complex, multi-clause sentences
(because/if/but/sequencing chains) and richer vocabulary appropriate to
B1, using the newly expanded verb paradigms (VISIT/STUDY/UNDERSTAND/
DO_MAKE/THINK/TEACH/TRAVEL/TALK/LEAVE/ARRIVE/RETURN/PAY/COPULA_PAST) that
the old templated generator never had access to.
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
    lesson(1, "I Have, You Have", "عندي، عندك", [
        item("عندي فلوس كثير لأني دفعت الأهل الأسبوع الماضي", "I have a lot of money because my family paid me last week", "3indi fluus katheer li-anni dafa3ni el-ahl el-isboo3 el-maadi"),
        item("عندك بيت كبير، بس ما عندك سيارة", "You have a big house, but you don't have a car", "3indak bayt kabeer, bas ma 3indak sayyaara"),
        item("عنده صديق زين يساعده كل وقت", "He has a good friend who helps him all the time", "3indah sadeeg zayn"),
        item("عندها فلوس، لو تبغى تشري بيت جديد", "She has money, if you want to buy a new house", "3indaha fluus, law tibgha tishri bayt jideed"),
    ], topicId="b1-3ind"),

    lesson(2, "We Have, They Have", "عندنا، عندهم", [
        item("عندنا بيت كبير لأن الأهل كثير", "We have a big house because there are a lot of family members", "3indana bayt kabeer li-ann el-ahl katheer"),
        item("عندكم فلوس؟ نعم، بس ما عندنا وقت نروح فيه السوق", "Do you all have money? Yes, but we don't have time to go to the market", "3indakum fluus? na3am"),
        item("عندهم بيت جديد لأنهم دفعو فلوس كثير عليه", "They have a new house because they paid a lot of money for it", "3indahum bayt jideed li-annahum dafa3aw fluus katheer 3alayh"),
        item("ما عندهم فلوس اليوم، بس عندهم بيت زين وسيارتين", "They don't have money today, but they have a good house and two cars", "ma 3indahum fluus el-yoom, bas 3indahum bayt zayn wa sayyaaratayn"),
    ]),

    lesson(3, "What Do You Have?", "شنو عندك؟", [
        item("شنو عندك في السوق؟ عندي غترة وقميص جديد", "What do you have from the market? I have a headdress and a new shirt", "shinu 3indak fis-suug? 3indi ghitra wa gamees jideed"),
        item("كم عندك من الفلوس؟ عندي مية بس", "How much money do you have? I only have a hundred", "kam 3indak min el-fluus? 3indi miya bas"),
        item("منو عنده سيارة اليوم؟ عند خالي سيارة زينة", "Who has a car today? My maternal uncle has a nice car", "minu 3indah sayyaara el-yoom? 3ind khaali sayyaara zeena"),
        item("عندك وقت الحين؟ لا، عندي شغل كثير", "Do you have time now? No, I have a lot of work", "3indak wagt el-heen? la, 3indi shughul katheer"),
    ]),

    lesson(4, "I Don't Have", "ما عندي", [
        item("ما عندي فلوس كثير، بس عندي بيت وسيارة", "I don't have a lot of money, but I have a house and a car", "ma 3indi fluus katheer, bas 3indi bayt wa sayyaara"),
        item("ما عندك وقت؟ ليش؟ عندي شغل لين الليل", "You don't have time? Why? I have work until night", "ma 3indak wagt? leish? 3indi shughul leen el-layl"),
        item("ما عندها صديق هنا لأنها وصلت هذا الأسبوع بس", "She doesn't have a friend here because she only arrived this week", "ma 3indaha sadeeg hina li-annaha wisalat haadha el-isboo3 bas"),
        item("ما عندهم بيت لأن الفلوس مب كافية", "They don't have a house because the money isn't enough", "ma 3indahum bayt li-ann el-fluus mub kaafya"),
    ]),

    lesson(5, "Review: Possession", "مراجعة: التملّك", [
        item("عندي أخو يدرس في الكويت، وعندي أخت تشتغل في قطر", "I have a brother who studies in Kuwait, and I have a sister who works in Qatar", "3indi akhu yadrus fil-kuwayt, wa 3indi ukht tashtaghil fi gatar"),
        item("ما عندهم سيارة، فيروحون الشغل بالباص كل يوم", "They don't have a car, so they go to work by bus every day", "ma 3indahum sayyaara, fa-yruu7oon esh-shaghal bil-baas kil yoom"),
        item("عندنا مجلس كبير نستقبل فيه الضيوف يوم الجمعة", "We have a big majlis where we receive guests on Friday", "3indana majlis kabeer"),
        item("لو عندك فلوس زينة، تقدر تشري بيت في السوق الجديد", "If you have good money, you can buy a house in the new market area", "law 3indak fluus zeena, tigdar tishri bayt fis-suug el-jideed"),
    ]),

    lesson(6, "Because I Went", "لأني رحت", [
        item("رحت المستشفى لأني كنت مريض كثير أمس", "I went to the hospital because I was very sick yesterday", "riHt el-mustashfa li-anni kint mareed katheer ams"),
        item("راح جدي المجلس لأن أصحابه كانو هناك", "My grandfather went to the majlis because his friends were there", "raaH jiddi el-majlis li-ann as7aabah kaanaw hinaak"),
        item("رحنا السوق لأن أختي تبغى غترة جديدة للعرس", "We went to the market because my sister wants a new headdress for the wedding", "riHna es-suug li-ann ukhti tibgha ghitra jideeda lil-3urs"),
        item("راحو المطار لأن جدهم راجع من السفر اليوم", "They went to the airport because their grandfather is returning from his trip today", "raaHaw el-mataar li-ann jiddahum raaji3 min es-safar el-yoom"),
    ]),

    lesson(7, "Why Are You Tired?", "ليش تعبان؟", [
        item("ليش انت تعبان؟ لأني سافرت كل الليل وما نمت", "Why are you tired? Because I traveled all night and didn't sleep", "leish inta ta3baan? li-anni saafart kil el-layl wa ma nimt"),
        item("ليش هي زعلانة؟ لأن صديقتها ما يات للعرس", "Why is she sad? Because her friend didn't come to the wedding", "leish hiya za3laana? li-ann sadeegtaha ma yaat lil-3urs"),
        item("ليش هم مشغولين؟ لأنهم يدرسون للامتحان بكرا", "Why are they busy? Because they're studying for the exam tomorrow", "leish hum mashghooleen? li-annahum yadrusoon lil-imtiHaan bukra"),
        item("ليش انتوا متأخرين؟ لأن القطار وصل متأخر اليوم", "Why are you all late? Because the train arrived late today", "leish intu mit'akhkhireen? li-ann el-gitaar wisal mit'akhkhir el-yoom"),
    ]),

    lesson(8, "Because It's Expensive", "لأنه غالي", [
        item("ما شريت القميص لأنه غالي كثير هناك", "I didn't buy the shirt because it's very expensive there", "ma sharayt el-gamees li-annah ghaali katheer hinaak"),
        item("شرى السيارة الرخيصة لأن الغالية ما كانت زينة", "He bought the cheap car because the expensive one wasn't good", "shara es-sayyaara er-rakheesa li-ann el-ghaalya ma kaanat zeena"),
        item("ما نروح المطعم الجديد لأن الأكل هناك غالي ومب لذيذ", "We're not going to the new restaurant because the food there is expensive and not delicious", "ma nruu7 el-mat3am el-jideed li-ann el-akal hinaak ghaali wa mub latheeth"),
        item("دفعت فلوس كثير على البيت لأنه قريب من الشغل", "I paid a lot of money for the house because it's near work", "dafa3t fluus katheer 3alal-bayt li-annah gareeb min esh-shaghal"),
    ]),

    lesson(9, "With Someone", "مع أحد", [
        item("رحت السوق مع خالتي وشرينا أشياء كثير", "I went to the market with my maternal aunt and we bought a lot of things", "riHt es-suug ma3 khaalti wa sharayna ashyaa katheer"),
        item("يحب يقعد مع أصحابه في المجلس كل ليلة", "He loves to sit with his friends in the majlis every night", "yiHibb yig3ad ma3 as7aabah fil-majlis kil layla"),
        item("سافرنا مع كل العائلة، فكان السفر مبسوط ولذيذ", "We traveled with the whole family, so the trip was fun and enjoyable", "saafarna ma3 kil el-ahl, fa-kaan es-safar mabsoot wa latheeth"),
        item("تكلمت مع المدرس عن ابني، وفهمت شنو المشكلة", "I talked with the teacher about my son, and I understood what the problem was", "tkallamt ma3 el-mudarris 3an ibni, wa fihimt shinu el-mushkila"),
    ]),

    lesson(10, "Review: Possession, Because, With", "مراجعة", [
        item("ما عندي وقت أروح السوق لأني مشغول مع الشغل", "I don't have time to go to the market because I'm busy with work", "ma 3indi wagt aruu7 es-suug li-anni mashghool ma3 esh-shaghal"),
        item("عندنا ضيوف الليلة، فلازم نطبخ لحم وسلطة زينة", "We have guests tonight, so we need to cook good meat and salad", "3indana dhuyoof el-layla, fa-laazim natbakh la7am wa salata zeena"),
        item("جدي يحب يتكلم عن أيام زمان مع أصحابه في المجلس", "My grandfather loves talking about the old days with his friends in the majlis", "jiddi yiHibb yitkallam 3an ayyaam zamaan"),
        item("لو عندك وقت، يلا نزور خالتي بعد الشغل", "If you have time, let's visit my maternal aunt after work", "law 3indak wagt, yalla nzoor khaalti ba3d esh-shaghal"),
    ]),

    lesson(11, "Family Possession", "تملّك العائلة", [
        item("جدي عنده مجلس كبير، وفيه كل الأهل يقعدون يوم الجمعة", "My grandfather has a big majlis, and all the family sits there on Friday", "jiddi 3indah majlis kabeer"),
        item("أختي عندها بنت وابن، وهم يدرسون في نفس المدرسة", "My sister has a daughter and a son, and they study at the same school", "ukhti 3indaha bint wa ibin, wa hum yadrusoon fi nafs el-madrasa"),
        item("خالي وعمي عندهم شغل واحد، بس عندهم آراء مختلفة كثير", "My maternal uncle and paternal uncle have the same job, but they have very different opinions", "khaali wa 3ammi 3indahum shughul waaHid"),
        item("جدتي عندها قصص كثير عن الصحراء والغوص أيام زمان", "My grandmother has a lot of stories about the desert and pearl diving from the old days", "jiddati 3indaha gisas katheer 3an es-sa7raa wal-ghaws ayyaam zamaan"),
    ]),

    lesson(12, "Days and Possession", "الأيام والتملّك", [
        item("يوم الجمعة عندنا وقت زين نزور الأهل ونشرب قهوة سوا", "On Friday we have good time to visit the family and drink coffee together", "yoom el-jum3a 3indana wagt zayn nzoor el-ahl"),
        item("يوم السبت عندي امتحان، فلازم أدرس كل يوم الجمعة", "On Saturday I have an exam, so I need to study all Friday", "yoom es-sabt 3indi imtiHaan, fa-laazim adrus kil yoom el-jum3a"),
        item("الأسبوع الماضي ما كان عندي وقت، بس هذا الأسبوع عندي وقت كثير", "Last week I didn't have time, but this week I have a lot of time", "el-isboo3 el-maadi ma kaan 3indi wagt"),
        item("يوم الاثنين عندهم اجتماع مهم في المكتب من الصبح", "On Monday they have an important meeting at the office from the morning", "yoom el-ithnayn 3indahum ijtimaa3 muhim fil-maktab min es-sub7"),
    ]),

    lesson(13, "Feelings and Because", "المشاعر ولأن", [
        item("أنا مبسوط كثير لأن أخوي راجع من السفر بكرا", "I'm very happy because my brother is returning from his trip tomorrow", "ana mabsoot katheer li-ann akhooy raaji3 min es-safar bukra"),
        item("هي زعلانة لأنها ما فهمت الدرس، بس المدرسة بتساعدها", "She's sad because she didn't understand the lesson, but the teacher will help her", "hiya za3laana li-annaha ma fihimat ed-dars"),
        item("كنا متضايقين لأن السفر تأخر، بس الحمد لله وصلنا زين", "We were annoyed because the trip was delayed, but thank God we arrived fine", "kinna mutadaayigeen li-ann es-safar ta'akhkhar"),
        item("هو متوتر لأن عنده امتحان صعب بكرا الصبح", "He's stressed because he has a difficult exam tomorrow morning", "huwa mutawattir li-ann 3indah imtiHaan sa3ib bukra es-sub7"),
    ]),

    lesson(14, "Money and Because", "الفلوس ولأن", [
        item("ما دفعت الحساب لأني نسيت محفظتي في البيت", "I didn't pay the bill because I left my wallet at home", "ma dafa3t el-Hisaab li-anni niseet ma7fadhti fil-bayt"),
        item("شرينا بيت جديد لأن القديم صار صغير على العائلة", "We bought a new house because the old one became too small for the family", "sharayna bayt jideed li-ann el-gadeem saar sagheer 3alal-ahl"),
        item("ما عندي فلوس كافية، فقررت أشتغل شغلين", "I don't have enough money, so I decided to work two jobs", "ma 3indi fluus kaafya, fa-garrart ashtaghil shughlayn"),
        item("دفعنا فلوس كثير على السفر، بس كان يستاهل كل درهم", "We paid a lot of money for the trip, but it was worth every dirham", "dafa3na fluus katheer 3ala es-safar"),
    ]),

    lesson(15, "Review: Possession and Because", "مراجعة", [
        item("ما عندي سيارة لأني بعتها الأسبوع الماضي، والحين أروح بالباص", "I don't have a car because I sold it last week, and now I go by bus", "ma 3indi sayyaara li-anni bi3tha el-isboo3 el-maadi"),
        item("عندها بيت جميل لأن أبوها ساعدها تدفع فلوسه", "She has a beautiful house because her father helped her pay for it", "3indaha bayt jameel li-ann abooha saa3adha tidfa3 fluusah"),
        item("جدي متعب لأنه سافر يومين بدون ما يرتاح", "My grandfather is exhausted because he traveled two days without resting", "jiddi mut3ab li-annah saafar yoomayn bidoon ma yirtaaH"),
        item("لأننا فهمنا الدرس زين، ما احتجنا مدرس ثاني", "Because we understood the lesson well, we didn't need another teacher", "li-annana fihimna ed-dars zayn"),
    ]),

    lesson(16, "With Family", "مع العائلة", [
        item("قعدت مع جدي في المجلس، وحكى لي قصص عن الغوص", "I sat with my grandfather in the majlis, and he told me stories about pearl diving", "ga3adt ma3 jiddi fil-majlis"),
        item("سافرت مع أهلي للسعودية، وزرنا مسجد جميل هناك", "I traveled with my family to Saudi Arabia, and we visited a beautiful mosque there", "saafart ma3 ahli lis-sa3oodiyya"),
        item("طبخت مع يمي أكل خليجي، وتعلمت وصفات جديدة كثير", "I cooked Khaleeji food with my mom, and I learned a lot of new recipes", "Tabakht ma3 yummi akal khaleeji"),
        item("درست مع أخوي للامتحان، وفهمنا الدرس أزيان سوا", "I studied with my brother for the exam, and we understood the lesson better together", "darast ma3 akhooy lil-imtiHaan"),
    ]),

    lesson(17, "Colors and Possession", "الألوان والتملّك", [
        item("عندي سيارة زرقاء وأخوي عنده سيارة حمراء أزيان منها", "I have a blue car and my brother has a red car nicer than it", "3indi sayyaara zarqaa wa akhooy 3indah sayyaara Hamraa azyan minha"),
        item("عندها عباية سوداء وغترة بيضاء تلبسهم في العرس", "She has a black abaya and a white headdress she wears at the wedding", "3indaha 3abaaya sawdaa wa ghitra baydaa"),
        item("البيت الأخضر أغلى من البيت الأصفر لأنه أكبر", "The green house is more expensive than the yellow house because it's bigger", "el-bayt el-akhdar aghla min el-bayt el-asfar li-annah akbar"),
        item("ما عندي قميص أبيض، بس عندي قمصان حمراء وزرقاء كثير", "I don't have a white shirt, but I have a lot of red and blue shirts", "ma 3indi gamees abyad, bas 3indi gumsaan Hamraa wa zarqaa katheer"),
    ]),

    lesson(18, "Numbers and Possession", "الأرقام والتملّك", [
        item("عندي عشرة كتب، بس قريت خمسة بس لين الحين", "I have ten books, but I've only read five so far", "3indi 3ashara kutub"),
        item("عندهم ثلاثين طالب في الصف، وكلهم يحبون المدرس", "They have thirty students in the class, and they all love the teacher", "3indahum thalaatheen Taalib fis-saff"),
        item("دفعت مية على الجوتي، وأختي دفعت خمسين بس على جوتيها", "I paid a hundred for the shoes, and my sister only paid fifty for hers", "dafa3t miya 3alal-jooti"),
        item("عندنا سبعة أيام إجازة، بنسافر أربعة منها للكويت", "We have seven days of vacation, we'll travel four of them to Kuwait", "3indana sab3a ayyaam ijaaza"),
    ]),

    lesson(19, "Directions and Because", "الاتجاهات ولأن", [
        item("رحنا يمين لأن الدريول قال المطعم قريب من هناك", "We went right because the driver said the restaurant is near there", "riHna yameen li-ann ed-daryool gaal el-mat3am gareeb min hinaak"),
        item("ما رحنا يسار بسبب الزحمة الكثيرة هناك اليوم", "We didn't go left because of the heavy traffic there today", "ma riHna yasaar bisabab ez-za7ma el-katheera hinaak el-yoom"),
        item("البيت قريب من المسجد، وسهل توصله", "The house is near the mosque, and it's easy to reach", "el-bayt gareeb minal-masjid, wa sahil toosalah"),
        item("وقفنا بعيد عن السوق بسبب الزحمة القوية هناك", "We stopped far from the market because of the heavy traffic there", "wigafna ba3eed 3an es-suug bisabab ez-za7ma el-gawiyya hinaak"),
    ]),

    lesson(20, "Review: With, Colors, Numbers, Directions", "مراجعة", [
        item("رحت مع خالي يمين المسجد، وشرينا غترة حمراء وقميص أزرق", "I went with my maternal uncle to the right of the mosque, and we bought a red headdress and a blue shirt", "riHt ma3 khaali yameen el-masjid"),
        item("عندنا عشرين ضيف الليلة، فلازم نحط الكراسي كلها في المجلس", "We have twenty guests tonight, so we need to put all the chairs in the majlis", "3indana 3ishreen dayf el-layla"),
        item("البيت الجديد أكبر من القديم بس أبعد عن السوق شوي", "The new house is bigger than the old one but a bit farther from the market", "el-bayt el-jideed akbar min el-gadeem bas ab3ad 3an es-suug shway"),
        item("مع كل هالفلوس، تقدر تشري بيت أزيان وأكبر من هذا", "With all this money, you could buy a nicer and bigger house than this one", "ma3 kil hal-fluus, tigdar tishri bayt azyan wa akbar min haadha"),
    ]),

    lesson(21, "I Drink Because I Have", "أشرب لأن عندي", [
        item("أشرب قهوة كل صباح لأن عندي شغل طويل قدام", "I drink coffee every morning because I have a long day of work ahead of me", "ashrab gahwa kil sabaaH li-ann 3indi shughul Taweel guddaami"),
        item("تشرب شاي بدل القهوة لأن عندها مشكلة في معدتها", "She drinks tea instead of coffee because she has a stomach problem", "tishrab shaay badal el-gahwa li-ann 3indaha mushkila fi mi3idatha"),
        item("نشرب مويه كثير في الصيف لأن الجو حار كثير", "We drink a lot of water in the summer because the weather is very hot", "nishrab moya katheer fis-sayf li-ann el-jaww Haarr jiddan"),
        item("ما يشربون قهوة الليل لأن عندهم امتحان بكرا الصبح", "They don't drink coffee at night because they have an exam tomorrow morning", "ma yishrabuun gahwa el-layl li-ann 3indahum imtiHaan bukra es-sub7"),
    ]),

    lesson(22, "Going Because of Money", "الرواح بسبب الفلوس", [
        item("ما رحنا السفر هالسنة لأن الفلوس ما كانت كافية", "We didn't go on the trip this year because the money wasn't enough", "ma riHna es-safar has-sana li-ann el-fluus ma kaanat kaafya"),
        item("راح يشتغل شغلين لأنه يبغى يجمع فلوس للعرس", "He went to work two jobs because he wants to save money for the wedding", "raaH yishtaghil shughlayn li-annah yibgha yjammi3 fluus lil-3urs"),
        item("رحنا السوق الرخيص بدل الغالي عشان نوفر فلوس", "We went to the cheap market instead of the expensive one to save money", "riHna es-suug er-rakhees badal el-ghaali 3ashaan nwaffir fluus"),
        item("ما بيروح المطعم بكرا لأنه بيدفع فلوس كثير على العرس أول", "He won't go to the restaurant tomorrow because he'll pay a lot of money for the wedding first", "ma bayruuH el-mat3am bukra li-annah bayidfa3 fluus katheer 3alal-3urs awwal"),
    ]),

    lesson(23, "Days and Drink", "الأيام والشرب", [
        item("كل يوم جمعة نشرب قهوة في مجلس جدي بعد الصلاة", "Every Friday we drink coffee in my grandfather's majlis after the prayer", "kil yoom jum3a nishrab gahwa fi majlis jiddi"),
        item("يوم السبت شربنا شاي كثير لأن الجو كان بارد ومطير", "On Saturday we drank a lot of tea because the weather was cold and rainy", "yoom es-sabt sharabna shaay katheer li-ann el-jaww kaan baarid wa maTeer"),
        item("ما بشرب قهوة يوم الاثنين لأن عندي امتحان وما أبغى أتوتر", "I won't drink coffee on Monday because I have an exam and I don't want to get nervous", "ma bashrab gahwa yoom el-ithnayn"),
        item("كل ما نزور خالتي، تسوي لنا شاي بالحليب لذيذ", "Every time we visit my maternal aunt, she makes us delicious tea with milk", "kil ma nzoor khaalti, tsawwi lana shaay bil-Haleeb latheeth"),
    ]),

    lesson(24, "Feelings Because of Possession", "المشاعر بسبب التملّك", [
        item("مبسوط كثير لأن عندي شغل زين وبيت مريح", "I'm very happy because I have good work and a comfortable house", "mabsoot katheer li-ann 3indi shughul zayn wa bayt mureeH"),
        item("متضايقة لأن ما عندها وقت تشوف أصحابها بسبب الشغل", "She's upset because she doesn't have time to see her friends because of work", "mutadaayiga li-ann ma 3indaha wagt tshoof as7aabha"),
        item("فخورين لأن عندنا حفيد يدرس في جامعة زينة", "We're proud because we have a grandson who studies at a good university", "fakhooreen li-ann 3indana Hafeed yadrus fi jaami3a zeena"),
        item("قلقان شوي لأن ما عندي فلوس كافية للسفر هالسنة", "I'm a bit worried because I don't have enough money to travel this year", "galgaan shway li-ann ma 3indi fluus kaafya lis-safar has-sana"),
    ]),

    lesson(25, "Review: Drink, Go, Days, Feelings", "مراجعة", [
        item("كل جمعة نشرب قهوة ونتكلم عن أخبار الأسبوع في المجلس", "Every Friday we drink coffee and talk about the week's news in the majlis", "kil jum3a nishrab gahwa wa nitkallam 3an akhbaar el-isboo3"),
        item("ما رحنا العرس لأن عندنا امتحان بكرا، فقعدنا ندرس بالبيت", "We didn't go to the wedding because we have an exam tomorrow, so we stayed home studying", "ma riHna el-3urs li-ann 3indana imtiHaan bukra"),
        item("مبسوطين اليوم لأن جدنا راجع من السفر بعد شهر كامل", "We're happy today because our grandfather is back from his trip after a whole month", "mabsooteen el-yoom li-ann jiddana raaji3 min es-safar ba3d shahar kaamil"),
        item("متعبة لأني ما نمت زين أمس، بس بكرا بروح المدرسة بدري", "I'm tired because I didn't sleep well yesterday, but tomorrow I'll go to school early", "mut3aba li-anni ma nimt zayn ams"),
    ]),

    lesson(26, "Where Are You Going and Why?", "وين رايح وليش؟", [
        item("وين رايح؟ رايح المستشفى أزور جدي المريض", "Where are you going? I'm going to the hospital to visit my sick grandfather", "wein raayiH? raayiH el-mustashfa azoor jiddi el-mareed"),
        item("وين رايحة؟ رايحة السوق أشري أشياء للعرس بكرا", "Where are you (f) going? I'm going to the market to buy things for tomorrow's wedding", "wein raayHa? raayHa es-suug ashri ashyaa lil-3urs bukra"),
        item("ليش رايحين المطار؟ رايحين نستقبل خالتنا من السفر", "Why are you all going to the airport? We're going to welcome our aunt from her trip", "leish raayHeen el-mataar? raayHeen nastagbil khaaltana min es-safar"),
        item("وين رايحين هذا الصيف؟ ما قررنا لين الحين، بس نفكر بالكويت", "Where are you all going this summer? We haven't decided yet, but we're thinking of Kuwait", "wein raayHeen haadha es-sayf? ma garrarna leen el-heen"),
    ]),

    lesson(27, "Numbers and Because", "الأرقام ولأن", [
        item("درست ستين صفحة لأن الامتحان بعد يومين بس", "I studied sixty pages because the exam is in only two days", "darast sitteen safHa li-ann el-imtiHaan ba3d yoomayn bas"),
        item("دفعنا سبعين على العشاء لأن كنا عشرة أشخاص", "We paid seventy for dinner because we were ten people", "dafa3na sab3een 3alal-3ashaa li-ann kinna 3ashara"),
        item("عندي أربعين دقيقة بس لأن عندي اجتماع بعدين", "I only have forty minutes because I have a meeting afterward", "3indi arba3een dageega bas li-ann 3indi ijtimaa3 ba3dayn"),
        item("شرينا مية كيلو تمر للعيد لأن الأهل كثير هالسنة", "We bought a hundred kilos of dates for Eid because there's a lot of family this year", "sharayna miya keelo tamur lil-3eed li-ann el-ahl katheer has-sana"),
    ]),

    lesson(28, "Money, Directions, and Because", "الفلوس والاتجاهات ولأن", [
        item("رحت يمين لأن البنك هناك، ودفعت فلوس البيت", "I went right because the bank is there, and I paid the house money", "riHt yameen li-ann el-bank hinaak, wa dafa3t fluus el-bayt"),
        item("ما دفعنا الحساب هناك لأن المطعم يمين كان أرخص", "We didn't pay the bill there because the restaurant to the right was cheaper", "ma dafa3na el-Hisaab hinaak li-ann el-mat3am yameen kaan arkhas"),
        item("طلعنا يسار عشان نلقى المكتب الجديد بسرعة", "We turned left in order to find the new office quickly", "Tala3na yasaar 3ashaan nilga el-maktab el-jideed bisur3a"),
        item("قدام السوق فيه بنك كبير ومطعم زين", "In front of the market there's a big bank and a good restaurant", "guddaam es-suug feeh bank kabeer wa mat3am zayn"),
    ]),

    lesson(29, "A Full Day", "يوم كامل", [
        item("الصبح رحت الشغل، الظهر قعدت مع أصحابي، والليل درست للامتحان", "In the morning I went to work, at noon I sat with my friends, and at night I studied for the exam", "es-sub7 riHt esh-shaghal, edh-dhuhur ga3adt ma3 as7aabi"),
        item("صحيت بدري، شربت قهوة، ورحت المدرسة قبل ما يبدأ الدرس", "I woke up early, drank coffee, and went to school before the lesson started", "SiHeet badri, sharabt gahwa"),
        item("طبخنا الفطور، نظفنا البيت، وبعدين قعدنا نشرب شاي في المجلس", "We cooked breakfast, cleaned the house, and then we sat drinking tea in the majlis", "Tabakhna el-futoor, nadhdhafna el-bayt"),
        item("سافرنا الصبح، وصلنا الظهر، وقعدنا نرتاح لين المغرب", "We traveled in the morning, arrived at noon, and rested until sunset", "saafarna es-sub7, wisalna edh-dhuhur"),
    ]),

    lesson(30, "Review: B1 Recap", "مراجعة شاملة", [
        item("عندي يوم طويل بكرا: امتحان الصبح، شغل الظهر، وعرس الليل", "I have a long day tomorrow: an exam in the morning, work at noon, and a wedding at night", "3indi yoom Taweel bukra"),
        item("ما رحت العرس لأن عندي امتحان، بس أختي راحت وحكت لي كل شي", "I didn't go to the wedding because I have an exam, but my sister went and told me everything", "ma riHt el-3urs li-ann 3indi imtiHaan"),
        item("جدي عنده قصص كثير عن الغوص، ونحب نسمعها كل جمعة في المجلس", "My grandfather has a lot of stories about pearl diving, and we love hearing them every Friday in the majlis", "jiddi 3indah gisas katheer 3an el-ghaws"),
        item("لو عندك وقت وفلوس، تقدر تسافر وتشوف أشياء جديدة كثير", "If you have time and money, you can travel and see a lot of new things", "law 3indak wagt wa fluus, tigdar tsaafir wa tshoof ashyaa jideeda katheer"),
    ]),

    lesson(31, "Professions and Work", "المهن والشغل", [
        item("المهندسة تشتغل من الصبح لين العصر، وبعدين ترجع بيتها متعبة", "The engineer works from morning until afternoon, and then returns home tired", "el-muhandisa tashtaghil min es-sub7 leen el-3asir"),
        item("المترجم يشتغل مع شركات كثير لأنه يعرف لغتين زين", "The translator works with a lot of companies because he knows two languages well", "el-mutarjim yashtaghil ma3 sharikaat katheer"),
        item("التاجر يفتح مكتبه بدري عشان يستقبل الناس قبل الظهر", "The merchant opens his office early in order to receive customers before noon", "et-taajir yaftaH maktabah badri"),
        item("المدرسة تحب شغلها كثير لأنها تشوف الطلاب يفهمون ويتعلمون", "The teacher loves her job a lot because she sees the students understand and learn", "el-mudarrisa tHibb shughulha katheer"),
    ]),

    lesson(32, "Family and Because", "العائلة ولأن", [
        item("خالي زعلان لأن ابنه ما نجح في الامتحان هالسنة", "My maternal uncle is upset because his son didn't pass the exam this year", "khaali za3laan li-ann ibnah ma najaH fil-imtiHaan has-sana"),
        item("جدتي فرحانة لأن حفيدتها بتتزوج هالشهر", "My grandmother is happy because her granddaughter is getting married this month", "jiddati farHaana li-ann Hafeedatha bititzawwaj hash-shahar"),
        item("عمي فخور بابنه لأنه صار مهندس زين", "My paternal uncle is proud of his son because he became a good engineer", "3ammi fakhoor bi-ibnah li-annah saar muhandis zayn"),
        item("خالتي متضايقة من أختها لأنها ما زارتها من زمان طويل", "My maternal aunt is upset with her sister because she hasn't visited her in a long time", "khaalti mutadaayiga min ukhtha"),
    ]),

    lesson(33, "On the Phone", "على الجوال", [
        item("اتصلت فيه بس ما رد لأنه كان في اجتماع", "I called him but he didn't answer because he was in a meeting", "ittasalt feeh bas ma radd li-annah kaan fi ijtimaa3"),
        item("قال لي على الجوال بيتأخر شوي بسبب الزحمة", "He told me on the phone that he'll be a little late because of traffic", "gaal li 3alal-jawwaal innah bayit'akhkhar shway"),
        item("خطي انقطع وأنا أتكلم مع خالتي عن العرس", "My line got cut off while I was talking with my maternal aunt about the wedding", "khaTTi inqata3 wa ana atkallam ma3 khaalti 3anil-3urs"),
        item("اتصلي فيني لو وصلتو زين، عشان ما أتوتر", "Call me if you all arrive safely, so I don't worry", "ittasili feeni law wisaltaw zayn"),
    ]),

    lesson(34, "Clothes, Having", "الملابس والتملّك", [
        item("عندي عباية للعرس، بس ما عندي جوتي زين لها", "I have an abaya for the wedding, but I don't have good shoes for it", "3indi 3abaaya lil-3urs, bas ma 3indi jooti zayn laha"),
        item("عنده غترة جديدة زينة، شراها من السوق أمس بخمسين", "He has a nice new headdress, he bought it from the market yesterday for fifty", "3indah ghitra jideeda zeena, sharaaha mines-suug ams bikhamseen"),
        item("عندها قمصان كثير، بس تحب القميص الأزرق أكثر من كلهم", "She has a lot of shirts, but she likes the blue shirt more than all of them", "3indaha gumsaan katheer, bas tHibb el-gamees el-azrag akthar min killahum"),
        item("عندهم دلاغات دافية للشتاء، بس ما عندهم جوتي زين للمطر", "They have warm socks for winter, but they don't have good shoes for the rain", "3indahum dallaghaat daafya lish-shita, bas ma 3indahum jooti zayn lil-maTar"),
    ]),

    lesson(35, "Clothes, Having II", "الملابس والتملّك ٢", [
        item("لبست القميص الأحمر لأن اليوم عرس ابن عمي", "I wore the red shirt because today is my paternal cousin's wedding", "libast el-gamees el-a7mar li-ann el-yoom 3urs ibn 3ammi"),
        item("ما لبست الغترة البيضاء لأنها وسخة، لبست الثانية", "I didn't wear the white headdress because it's dirty, I wore the other one", "ma libast el-ghitra el-baydaa li-annaha wisikha, libast eth-thaanya"),
        item("لبسو أجمل ملابسهم للعرس، وكلهم كانو أنيقين كثير", "They wore their nicest clothes for the wedding, and they all looked very elegant", "libsaw ajmal malaabishum lil-3urs"),
        item("لبست عباية سوداء وجوتي أسود، تناسب بعض زين", "She wore a black abaya and black shoes, they match each other well", "libsat 3abaaya sawdaa wa jooti aswad"),
    ]),

    lesson(36, "Food, Having", "الأكل والتملّك", [
        item("عندنا لحم وسلطة وتمر، بس ما عندنا قهوة كافية للضيوف", "We have meat, salad, and dates, but we don't have enough coffee for the guests", "3indana la7am wa salata wa tamur"),
        item("عندي وصفة زينة لعشاء اليوم، تعلمتها من جدتي", "I have a good recipe for today's dinner, I learned it from my grandmother", "3indi wasfa zeena li3ashaa el-yoom"),
        item("ما عندهم أكل كافي للضيوف، فقررو يطلبون من المطعم", "They don't have enough food for the guests, so they decided to order from the restaurant", "ma 3indahum akal kaafi lidh-dhuyoof"),
        item("عندنا فطور زين كل صباح: بيض ولحم وتمر وقهوة", "We have a good breakfast every morning: eggs, meat, dates, and coffee", "3indana futoor zayn kil sabaaH"),
    ]),

    lesson(37, "Food, Having II", "الأكل والتملّك ٢", [
        item("طبخت للضيوف أكل خليجي لأنهم يحبون يجربون أشياء جديدة", "I cooked Khaleeji food for the guests because they love trying new things", "Tabakht lidh-dhuyoof akal khaleeji li-annahum yiHibboon yjarriboon ashyaa jideeda"),
        item("الأكل هنا لذيذ كثير، بس السعر أغلى من المطعم الثاني", "The food here is very delicious, but the price is more expensive than the other restaurant", "el-akal hina latheeth katheer"),
        item("ما أكلنا كل الأكل لأننا كنا شبعانين من الفطور", "We didn't eat all the food because we were already full from breakfast", "ma akalna kil eT-Ta3aam li-annana kinna shab3aaneen min el-futoor"),
        item("جدتي تطبخ أكل لذيذ يستاهل كل دقيقة", "My grandmother cooks delicious food worth every minute", "jiddati taTbakh akal latheeth yistaahil kil dageega"),
    ]),

    lesson(38, "Working", "الشغل", [
        item("أشتغل من الصبح لين العصر، وبعدين أرجع البيت أرتاح", "I work from morning until afternoon, and then I go home to rest", "ashtaghil min es-sub7 leen el-3asir"),
        item("تشتغل في مستشفى كبير، وتساعد مرضى كثير كل يوم", "She works at a big hospital, and helps a lot of patients every day", "tashtaghil fi mustashfa kabeer"),
        item("يشتغلون في مكتب واحد، بس كل واحد عنده شغل مختلف", "They work in the same office, but each one has different work", "yashtaghiloon fi maktab waaHid"),
        item("ما نشتغل يوم الجمعة لأنه يوم راحة عندنا في الخليج", "We don't work on Friday because it's a rest day for us in the Gulf", "ma nashtaghil yoom el-jum3a li-annah yoom raaHa 3indana fil-khaleej"),
    ]),

    lesson(39, "Numbers, Because", "الأرقام ولأن", [
        item("عندي عشرين سنة أشتغل في نفس الشركة لأني أحب شغلي", "I've worked at the same company for twenty years because I love my job", "3indi 3ishreen sana ashtaghil fi nafs esh-sharika"),
        item("درسنا ثلاثين درس هذا الفصل لأن المدرس سريع كثير", "We studied thirty lessons this semester because the teacher is fast at explaining", "darasna thalaatheen dars haadha el-fasl"),
        item("دفعنا تسعين على الجوتي لأنه كان أزيان نوع في المحل", "We paid ninety for the shoes because it was the best kind in the shop", "dafa3na tis3een 3alal-jooti"),
        item("عندهم مية ضيف بالعرس لأن العائلتين كبار كثير", "They have a hundred guests at the wedding because both families are very big", "3indahum miya dayf bil-3urs li-ann el-3aa'ilatayn kubaar katheer"),
    ]),

    lesson(40, "Ugly and Clean", "قبيح ونظيف", [
        item("البيت القديم صار قبيح لأن ما حد نظفه من زمان", "The old house became ugly because no one has cleaned it in a long time", "el-bayt el-gadeem saar gabee7 li-ann ma Had nadhdhafah min zamaan"),
        item("نظفت البيت كله قبل ما يوصلون الضيوف", "I cleaned the whole house before the guests arrived", "nadhdhaft el-bayt killah gabl ma yoosloon edh-dhuyoof"),
        item("القميص كان وسخ، بس بعد ما غسلت القميص صار نظيف ولذيذ الريحة", "The shirt was dirty, but after I washed it, it became clean and smelled nice", "el-gamees kaan wisikh"),
        item("مب قبيح، بس مب زين كمان، هو بس عادي", "It's not ugly, but it's not good either, it's just okay", "mub gabee7, bas mub zayn kamaan, huwa bas 3aadi"),
    ]),

    lesson(41, "More Verbs", "أفعال أكثر", [
        item("فكرت كثير قبل ما قررت أسافر لوحدي هالمرة", "I thought a lot before I decided to travel alone this time", "fakkart katheer gabl ma garrart asaafir liwaHdi hal-marra"),
        item("درّس المدرس القديم في هالمدرسة عشرين سنة قبل ما يتقاعد", "The old teacher taught at this school for twenty years before he retired", "darras el-mudarris el-gadeem fi hal-madrasa 3ishreen sana"),
        item("سوت لنا يمي أكل خليجي لذيذ مثل زمان", "My mom made us delicious Khaleeji food just like the old days", "sawwat lana yummi akal khaleeji latheeth"),
        item("زرنا جدي في المستشفى، وهو زين الحين والحمد لله", "We visited my grandfather in the hospital, and he's fine now, thank God", "zirna jiddi fil-mustashfa, wa huwa zayn el-heen wal-hamdulillah"),
    ]),

    lesson(42, "Time and Because", "الوقت ولأن", [
        item("وصلنا متأخرين لأن الساعة كانت غلط عندنا", "We arrived late because our clock was wrong", "wisalna mit'akhkhireen li-ann es-saa3a kaanat ghalat 3indana"),
        item("لازم أطلع الساعة سبعة عشان أوصل الشغل بدري", "I have to leave at seven o'clock in order to arrive at work early", "laazim aTla3 es-saa3a sab3a 3ashaan awsal esh-shaghal badri"),
        item("عندنا ربع ساعة بس، فلازم نسرع عشان ما نتأخر", "We only have fifteen minutes, so we need to hurry so we're not late", "3indana rub3 saa3a bas, fa-laazim nsari3 3ashaan ma nit'akhkhar"),
        item("من الساعة عشرة لين الساعة وحدة، عندي اجتماعات كثير", "From ten o'clock until one o'clock, I have back-to-back meetings", "min es-saa3a 3ashara leen es-saa3a waHda"),
    ]),

    lesson(43, "Always", "دايما", [
        item("دايما أشرب قهوتي قبل ما أروح الشغل عشان أصحى زين", "I always drink my coffee before going to work in order to wake up properly", "dayman ashrab gahwati gabl ma aruuH esh-shaghal"),
        item("جدتي دايما تطبخ أكل أكثر من اللازم عشان يبقى للضيوف", "My grandmother always cooks more food than needed in case guests come", "jiddati dayman taTbakh akal akthar min el-laazim"),
        item("ما دايما أفهم كل شي بسرعة، بعض الدروس صعبة علي", "I don't always understand everything quickly, some lessons are hard for me", "ma dayman afham kil shay bisur3a"),
        item("هو دايما يقول الحقيقة، حتى لو كانت صعبة", "He always tells the truth, even if it's difficult", "huwa dayman yiguul el-Hageega"),
    ]),

    lesson(44, "Quantifiers Extended", "أدوات الكمية", [
        item("كل الطلاب فهمو الدرس إلا واحد ما كان في الصف أمس", "All the students understood the lesson except one who wasn't in class yesterday", "kil eT-Tullaab fihmaw ed-dars illa waaHid ma kaan fis-saff ams"),
        item("بعض الناس يحبون القهوة مرة، وبعضهم يحبونها حلوة", "Some people love bitter coffee, and some of them love it sweet", "ba3d en-naas yiHibboon el-gahwa murra"),
        item("أكثر الأهل ياو للعرس، بس بعضهم ما قدر يوصل", "Most of the family came to the wedding, but some of them couldn't make it", "akthar el-ahl yaw lil-3urs, bas ba3dahum ma gidar yoosal"),
        item("كل شي كان زين إلا الجو، كان حار كثير هالمرة", "Everything was good except the weather, it was very hot this time", "kil shay kaan zayn illa el-jaww"),
    ]),

    lesson(45, "Last Week, Next Month", "الأسبوع الماضي، الشهر الجاي", [
        item("الأسبوع الماضي سافرنا للبحرين، والشهر الجاي بنسافر لعمان", "Last week we traveled to Bahrain, and next month we'll travel to Oman", "el-isboo3 el-maadi saafarna lil-ba7rayn"),
        item("الشهر الماضي كان صعب كثير بالشغل، بس هذا الشهر أزيان", "Last month was very difficult at work, but this month is better", "esh-shahar el-maadi kaan sa3ib katheer bish-shaghal"),
        item("الأسبوع الجاي عندي امتحانين، فبقعد أدرس كل يوم", "Next week I have two exams, so I'll be studying every day", "el-isboo3 el-jaay 3indi imtiHaneen"),
        item("من الشهر الماضي لين الحين، ما شفت خالتي ولا مرة", "From last month until now, I haven't seen my maternal aunt even once", "min esh-shahar el-maadi leen el-heen, ma shift khaalti wala marra"),
    ]),

    lesson(46, "Cousins and Grandchildren", "أولاد العم والأحفاد", [
        item("ابن عمي وبنت خالي يدرسون في نفس الجامعة الحين", "My paternal cousin and my maternal cousin study at the same university now", "ibin 3ammi wa bint khaali yadrusoon fi nafs el-jaami3a el-heen"),
        item("حفيد جدي الكبير صار مهندس، وحفيدته الصغيرة لسا تدرس", "My grandfather's oldest grandson became an engineer, and his youngest granddaughter is still studying", "Hafeed jiddi el-kabeer saar muhandis"),
        item("كل أولاد عمي وخالي يجتمعون في مجلس جدي كل جمعة", "All my paternal and maternal cousins gather in my grandfather's majlis every Friday", "kil awlaad 3ammi wa khaali yijtami3oon fi majlis jiddi kil jum3a"),
        item("عندي حفيدة صغيرة تحب تسمع قصص جدتها عن الغوص", "I have a young granddaughter who loves hearing her grandmother's stories about pearl diving", "3indi Hafeeda sagheera tHibb tisma3 gisas jiddatha 3anil-ghaws"),
    ]),

    lesson(47, "Cloudy, Storm, Humidity", "غائم وعاصفة ورطوبة", [
        item("الجو غائم اليوم، بس مب مطير كثير", "The weather is cloudy today, but not very rainy", "el-jaww ghaayim el-yoom, bas mub maTeer katheer"),
        item("صارت عاصفة قوية أمس، فما قدرنا نطلع من البيت", "There was a strong storm yesterday, so we couldn't leave the house", "saarat 3aasifa gawiyya ams, fa-ma gidarna nTla3 minal-bayt"),
        item("الرطوبة كثير هالأيام، وأنا تعبان من الجو الحين", "The humidity is a lot these days, and I'm tired from the weather right now", "er-rutuuba katheer hal-ayyaam, wa ana ta3baan minal-jaww el-heen"),
        item("لو الجو غائم بكرا، بنقعد بالمجلس بدل ما نطلع", "If the weather is cloudy tomorrow, we'll stay in the majlis instead of going out", "law el-jaww ghaayim bukra, bang3ad bil-majlis badal ma nTla3"),
    ]),

    lesson(48, "Clothes, Because", "الملابس ولأن", [
        item("لبست غترة ثانية لأن الأولى كانت وسخة من السفر", "I wore another headdress because the first one was dirty from the trip", "libast ghitra thaanya li-ann el-oola kaanat wisikha mines-safar"),
        item("ما لبست الجوتي الجديد لأنه ضيق شوي على رجلي", "I didn't wear the new shoes because they're a bit tight on my foot", "ma libast el-jooti el-jideed li-annah dayyig shway 3ala rijli"),
        item("شرت عباية جديدة لأن القديمة صارت قديمة الموضة", "She bought a new abaya because the old one became old-fashioned", "sharat 3abaaya jideeda li-ann el-gadeema saarat gadeemat el-mooda"),
        item("لبسنا ملابس دافية لأن الرطوبة والريح كانت قوية اليوم", "We wore warm clothes because the humidity and wind were strong today", "libasna malaabis daafya li-ann er-rutuuba war-reeH kaanat gawiyya el-yoom"),
    ]),

    lesson(49, "Sometimes", "أحيانا", [
        item("أحيانا أشرب قهوة بدون سكر، وأحيانا ثانية أحبها حلوة كثير", "Sometimes I drink coffee without sugar, and other times I love it very sweet", "aHyaanan ashrab gahwa bidoon sukkar"),
        item("أحيانا نزور جدي بدون ما نتصل، لأنه دايما يرحب فينا", "Sometimes we visit my grandfather without calling, because he always welcomes us", "aHyaanan nzoor jiddi bidoon ma nittasil"),
        item("أحيانا الدرس يكون سهل، وأحيانا ثانية يصير صعب كثير", "Sometimes the lesson is easy, and other times it becomes very difficult", "aHyaanan ed-dars ykoon sahil"),
        item("أحيانا أفكر إني لازم أسافر أكثر وأشوف العالم", "Sometimes I think I should travel more and see the world", "aHyaanan afakkir inni laazim asaafir akthar"),
    ]),

    lesson(50, "Buying and Paying", "الشراء والدفع", [
        item("شريت غترة وقميص ودفعت مية وخمسين على كل شي", "I bought a headdress and a shirt and paid a hundred fifty for everything", "sharayt ghitra wa gamees wa dafa3t miya wa khamseen 3ala kil shay"),
        item("قبل لا تدفع، اسأل عن السعر عشان ما يغشونك", "Before you pay, ask about the price so they don't cheat you", "gabl la tidfa3, is'al 3anis-si3ir 3ashaan ma yighshoonak"),
        item("دفعنا نص الفلوس الحين، والنص الثاني بعد ما يوصل الشي", "We paid half the money now, and the other half after the item arrives", "dafa3na nusf el-fluus el-heen"),
        item("شرى بيت جديد ودفع كل الفلوس مرة وحدة بدون قرض", "He bought a new house and paid all the money at once without a loan", "shara bayt jideed wa dafa3 kil el-fluus marra waHda bidoon gard"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/b1.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "b1", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/b1.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
