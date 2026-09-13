#!/usr/bin/env python3
"""Full rewrite of B1+ Khaleeji Arabic content -- same repetition fix,
built on the now much larger confirmed vocabulary from A1/A2/B1, with
genuinely varied لازم ("must") constructions plus new body-parts/health
vocabulary instead of one reused template.
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
    lesson(1, "I Must Go", "لازم أروح", [
        item("لازم أروح المستشفى الحين لأن جدي مريض", "I must go to the hospital now because my grandfather is sick", "laazim aruuH el-mustashfa el-heen li-ann jiddi mareed"),
        item("لازم تروح الشغل بدري بكرا عشان الاجتماع المهم", "You must go to work early tomorrow because of the important meeting", "laazim truuH esh-shaghal badri bukra 3ashaan el-ijtimaa3 el-muhim"),
        item("لازم تروحين المدرسة، عندك امتحان اليوم", "You (f) must go to school, you have an exam today", "laazim truuHeen el-madrasa, 3indik imtiHaan el-yoom"),
        item("لازم يروح البنك قبل ما يسكرون", "He must go to the bank before it closes", "laazim yruuH el-bank gabl ma yiskiroon"),
    ], topicId="b1plus-lazim"),

    lesson(2, "She Must, We Must", "لازم تروح، لازم نروح", [
        item("لازم تروح السوق تشري أشياء للعرس بكرا", "She must go to the market to buy things for tomorrow's wedding", "laazim truuH es-suug tishri ashyaa lil-3urs bukra"),
        item("لازم نروح نزور خالتي قبل ما تسافر", "We must go visit my maternal aunt before she travels", "laazim nruuH nzoor khaalti gabl ma tsaafir"),
        item("لازم تروحون المطار بدري عشان الزحمة", "You all must go to the airport early because of traffic", "laazim truu7oon el-mataar badri 3ashaan ez-za7ma"),
        item("لازم يروحون المدرسة كل يوم إلا الجمعة", "They must go to school every day except Friday", "laazim yruu7oon el-madrasa kil yoom illa el-jum3a"),
    ]),

    lesson(3, "I Must Drink", "لازم أشرب", [
        item("لازم أشرب مويه كثير لأن الجو حار اليوم", "I must drink a lot of water because the weather is hot today", "laazim ashrab moya katheer li-ann el-jaww Haarr el-yoom"),
        item("لازم تشرب دوا قبل الأكل، قال الطبيب كذا", "You must drink medicine before eating, the doctor said so", "laazim tishrab dawa gabl el-akal"),
        item("لازم ما تشربين قهوة الليل لأن عندك امتحان بكرا", "You (f) must not drink coffee at night because you have an exam tomorrow", "laazim ma tishrabeen gahwa el-layl"),
        item("لازم يشرب مويه بارده بعد الشغل الطويل", "He must drink cold water after the long work", "laazim yishrab moya baarda ba3d esh-shaghal eT-Taweel"),
    ]),

    lesson(4, "We Must Drink", "لازم نشرب", [
        item("لازم نشرب قهوة قبل ما نطلع، الجو بارد كثير", "We must drink coffee before we leave, the weather is very cold", "laazim nishrab gahwa gabl ma nTla3"),
        item("لازم تشربون شاي بالحليب، جدتي سوته بيدها", "You all must drink tea with milk, my grandmother made it by hand", "laazim tishrabuun shaay bil-Haleeb"),
        item("لازم يشربون مويه كثير في الصيف عشان ما يتعبون", "They must drink a lot of water in the summer so they don't get tired", "laazim yishrabuun moya katheer fis-sayf"),
        item("ما لازم نشرب قهوة كثير، مب زين للمعدة", "We shouldn't drink too much coffee, it's not good for the stomach", "ma laazim nishrab gahwa katheer, mub zayn lil-mi3ida"),
    ]),

    lesson(5, "Review: Lazim with Verbs", "مراجعة: لازم مع الأفعال", [
        item("لازم أدرس اليوم وأنام بدري عشان أصحى زين بكرا", "I must study today and sleep early in order to wake up well tomorrow", "laazim adrus el-yoom wa anaam badri"),
        item("لازم نروح ونشوف الطبيب قبل ما يصير الوضع أصعب", "We must go and see the doctor before the situation gets harder", "laazim nruuH wa nshoof eT-Tabeeb"),
        item("لازم يدفعون الحساب قبل لا يطلعون من المطعم", "They must pay the bill before they leave the restaurant", "laazim yidfa3oon el-Hisaab gabl la yiTla3oon"),
        item("ما لازم تتأخر، الاجتماع يبدأ الساعة تسعة بالضبط", "You shouldn't be late, the meeting starts at exactly nine o'clock", "ma laazim tit'akhkhar"),
    ]),

    lesson(6, "Days and Must", "الأيام ولازم", [
        item("يوم الاثنين لازم أروح البنك، ويوم الثلاثاء لازم أدرس للامتحان", "On Monday I must go to the bank, and on Tuesday I must study for the exam", "yoom el-ithnayn laazim aruuH el-bank"),
        item("يوم الجمعة ما لازم نشتغل، بس لازم نزور جدي في المجلس", "On Friday we don't have to work, but we must visit my grandfather in the majlis", "yoom el-jum3a ma laazim nashtaghil"),
        item("الأسبوع الجاي لازم نسافر، عندنا عرس في الكويت", "Next week we must travel, we have a wedding in Kuwait", "el-isboo3 el-jaay laazim nsaafir"),
        item("يوم السبت لازم تروح تشري غترة جديدة قبل العرس", "On Saturday you must go buy a new headdress before the wedding", "yoom es-sabt laazim truuH tishri ghitra jideeda"),
    ]),

    lesson(7, "Money and Must", "الفلوس ولازم", [
        item("لازم أدفع فلوس البيت قبل آخر الشهر", "I must pay the house money before the end of the month", "laazim adfa3 fluus el-bayt gabl aakhir esh-shahar"),
        item("لازم توفر فلوس عشان تقدر تسافر هالصيف", "You must save money in order to be able to travel this summer", "laazim twaffir fluus 3ashaan tigdar tsaafir has-sayf"),
        item("لازم ما تصرف كل فلوسك على أشياء مب مهمة", "You shouldn't spend all your money on unimportant things", "laazim ma tisrif kil fluusak 3ala ashyaa mub muhimma"),
        item("لازم ندفع نص الفلوس الحين والنص الثاني بعدين", "We must pay half the money now and the other half later", "laazim nidfa3 nus el-fluus el-heen"),
    ]),

    lesson(8, "Feelings and Must", "المشاعر ولازم", [
        item("أنا تعبان كثير، لازم أرتاح شوي قبل ما أرجع الشغل", "I'm very tired, I must rest a bit before going back to work", "ana ta3baan katheer, laazim artaaH shway"),
        item("هي متوترة لأن عندها امتحان، لازم نساعدها تدرس", "She's nervous because she has an exam, we must help her study", "hiya mutawattira li-ann 3indaha imtiHaan"),
        item("احنا قلقانين على جدي، لازم نتصل فيه الحين", "We're worried about my grandfather, we must call him now", "iHna galgaaneen 3ala jiddi, laazim nittasil feeh el-heen"),
        item("لازم ما تزعل، كل شي بيصير زين انشاالله", "You shouldn't be upset, everything will be fine God willing", "laazim ma tiz3al, kil shay baysir zayn"),
    ]),

    lesson(9, "Directions and Must", "الاتجاهات ولازم", [
        item("لازم تروح يمين وبعدين يسار عشان توصل البنك", "You must go right and then left in order to reach the bank", "laazim truuH yameen wa ba3dayn yasaar"),
        item("لازم نوقف قدام المسجد لأن السيارة ما تدخل الشارع", "We must stop in front of the mosque because the car can't enter the street", "laazim niwgaf guddaam el-masjid"),
        item("لازم تمشي شوي لين تلقى المحل، هو قريب من هنا", "You must walk a bit until you find the shop, it's near from here", "laazim timshi shway leen tilga el-maHal"),
        item("لازم ما تروح بعيد لأن الجو بيصير حار كثير بعدين", "You shouldn't go far because the weather will become very hot later", "laazim ma truuH ba3eed"),
    ]),

    lesson(10, "Review: Lazim Recap", "مراجعة شاملة", [
        item("لازم أروح البنك وأدفع الفلوس قبل ما أرجع البيت", "I must go to the bank and pay the money before returning home", "laazim aruuH el-bank wa adfa3 el-fluus"),
        item("لازم نساعد جدتي لأنها ما تقدر تروح السوق لوحدها", "We must help my grandmother because she can't go to the market alone", "laazim nsaa3id jiddati li-annaha ma tigdar truuH es-suug liwaHdaha"),
        item("لازم ما ننسى نتصل فيهم قبل ما يوصلون المطار", "We shouldn't forget to call them before they arrive at the airport", "laazim ma ninsa nittasil feehum"),
        item("يوم الجمعة لازم نقعد في المجلس ونشرب قهوة مع الأهل كلهم", "On Friday we must sit in the majlis and drink coffee with all the family", "yoom el-jum3a laazim nag3ad fil-majlis"),
    ]),

    lesson(11, "I Must Know", "لازم أدري", [
        item("لازم أدري السعر قبل ما أشري عشان ما يغشونني", "I must know the price before I buy so they don't cheat me", "laazim adri es-si3ir gabl ma ashri"),
        item("لازم تدري وين البيت قبل ما تروح، السوق كبير", "You must know where the house is before you go, the market is big", "laazim tadri wein el-bayt gabl ma truuH"),
        item("لازم ندري شنو الوضع قبل ما نقرر شي", "We must know what the situation is before we decide anything", "laazim nadri shinu el-wad3"),
        item("ما تدرين وين خالتك؟ لازم تدرين، هي وياك اليوم", "You (f) don't know where your maternal aunt is? You must know, she's with you today", "ma tidreen wein khaaltik?"),
    ]),

    lesson(12, "She and They Must Know", "لازم تدري، لازم يدرون", [
        item("لازم تدري إنه ما يقدر يجي بسبب الشغل", "She must know that he can't come because of work", "laazim tadri innah ma yigdar yiji bisabab esh-shaghal"),
        item("لازم يدرون وين المجلس قبل ما يروحون العرس", "They must know where the majlis is before they go to the wedding", "laazim yidroon wein el-majlis gabl ma yruu7oon el-3urs"),
        item("لازم تدرون وقت العرس بالضبط عشان ما تتأخرون", "You all must know the exact time of the wedding so you're not late", "laazim tidroon wagt el-3urs biD-Dabt"),
        item("جدي يدري كل شي عن الغوص والصحراء أيام زمان", "My grandfather knows everything about pearl diving and the desert from the old days", "jiddi yadri kil shay 3an el-ghaws wes-sa7raa"),
    ]),

    lesson(13, "What I Want and the Price", "شنو أبغى والسعر", [
        item("أبغى أدري كم سعر هالسيارة قبل ما أقرر", "I want to know the price of this car before I decide", "abgha adri kam si3ir has-sayyaara"),
        item("السعر غالي كثير على شي بسيط مثل هذا", "The price is very high for something simple like this", "es-si3ir ghaali katheer 3ala shay baseet mithil haadha"),
        item("تبغى تدري السعر قبل ما تشري، صح؟", "You want to know the price before you buy, right?", "tibgha tadri es-si3ir gabl ma tishri, sa77?"),
        item("السعر أرخص هنا من المحل الثاني بعشرين", "The price is cheaper here than the other shop by twenty", "es-si3ir arkhas hina min el-maHal eth-thaani bi3ishreen"),
    ]),

    lesson(14, "This Red House", "هذا البيت الأحمر", [
        item("أبغى هذا البيت الأحمر لأنه قريب من الشغل والمدرسة", "I want this red house because it's near work and school", "abgha haadha el-bayt el-a7mar li-annah gareeb min esh-shaghal wal-madrasa"),
        item("هذا القميص الأزرق أزيان من الأخضر، بس أغلى شوي", "This blue shirt is nicer than the green one, but a bit more expensive", "haadha el-gamees el-azrag azyan minal-akhdar"),
        item("هذي السيارة الصفراء رخيصة، بس ما أحبها كثير", "This yellow car is cheap, but I don't like it much", "haadhi es-sayyaara es-safraa rakheesa"),
        item("هذا الجوتي الأسود يناسب العباية زين كثير", "These black shoes match the abaya very well", "haadha el-jooti el-aswad ynaasib el-3abaaya zayn katheer"),
    ]),

    lesson(15, "Review: Know, Want, Colors", "مراجعة", [
        item("أبغى أدري وين شريت هالغترة الحمراء الجميلة", "I want to know where you bought this beautiful red headdress", "abgha adri wein sharayt hal-ghitra el-Hamraa el-jameela"),
        item("لازم تدرون السعر الصح قبل ما تشرون شي", "You all must know the right price before you buy anything", "laazim tidroon es-si3ir es-saHH gabl ma tishroon shay"),
        item("هذا البيت الأزرق أزيان من الأصفر، وأنا أدري ليش", "This blue house is nicer than the yellow one, and I know why", "haadha el-bayt el-azrag azyan minal-asfar"),
        item("تبغى تشري السيارة الحمراء ولا الزرقاء؟ أنا ما أدري", "Do you want to buy the red car or the blue one? I don't know", "tibgha tishri es-sayyaara el-Hamraa wala ez-zarqaa?"),
    ]),

    lesson(16, "The Family and Must", "العائلة ولازم", [
        item("لازم نساعد جدي وجدتي لأنهم كبار في السن الحين", "We must help my grandfather and grandmother because they're elderly now", "laazim nsaa3id jiddi wa jiddati li-annahum kubaar fis-sin el-heen"),
        item("لازم نزور خالي في العيد حتى لو بيته بعيد شوي", "We must visit my maternal uncle at Eid even if his house is a bit far", "laazim nzoor khaali fil-3eed Hatta law baytah ba3eed shway"),
        item("لازم أختي تدرس أكثر عشان تنجح في الجامعة", "My sister must study more in order to succeed at university", "laazim ukhti tadrus akthar 3ashaan tanjaH fil-jaami3a"),
        item("لازم الأهل كلهم يجتمعون في العرس، ما حد يتأخر", "The whole family must gather at the wedding, no one should be late", "laazim el-ahl killahum yijtami3oon fil-3urs"),
    ]),

    lesson(17, "Food, Drink, and Must", "الأكل والشرب ولازم", [
        item("لازم نطبخ أكل كثير لأن عندنا ضيوف الليلة", "We must cook a lot of food because we have guests tonight", "laazim naTbakh akal katheer li-ann 3indana dhuyoof el-layla"),
        item("لازم تاكل قبل الدوا، قال الطبيب كذا صباح ومساء", "You must eat before the medicine, the doctor said so morning and evening", "laazim taakil gabl ed-dawa"),
        item("لازم نشري تمر وقهوة قبل ما يوصل الضيوف", "We must buy dates and coffee before the guests arrive", "laazim nishtiri tamur wa gahwa gabl ma yoosal edh-dhuyoof"),
        item("ما لازم تاكل كثير قبل النوم، مب زين للمعدة", "You shouldn't eat a lot before sleep, it's not good for the stomach", "ma laazim taakil katheer gabl en-nawm"),
    ]),

    lesson(18, "Places and Must", "الأماكن ولازم", [
        item("لازم نروح المستشفى الحين، جدي تعبان كثير", "We must go to the hospital now, my grandfather is very sick", "laazim nruuH el-mustashfa el-heen"),
        item("لازم تروح البنك وتصرف شيكك قبل يوم الخميس", "You must go to the bank and cash your check before Thursday", "laazim truuH el-bank"),
        item("لازم نلقى مطعم زين قريب من المسجد للعشاء", "We must find a good restaurant near the mosque for dinner", "laazim nilga mat3am zayn gareeb minal-masjid"),
        item("لازم يوصلون المجلس قبل صلاة المغرب", "They must arrive at the majlis before the sunset prayer", "laazim yoosaloon el-majlis gabl salaat el-maghrib"),
    ]),

    lesson(19, "Numbers and Must", "الأرقام ولازم", [
        item("لازم أدرس أربعين صفحة قبل الامتحان بعد يومين", "I must study forty pages before the exam in two days", "laazim adrus arba3een safHa gabl el-imtiHaan ba3d yoomayn"),
        item("لازم ندفع سبعين على الحساب، كنا سبعة أشخاص", "We must pay seventy for the bill, we were seven people", "laazim nidfa3 sab3een 3alal-Hisaab"),
        item("لازم نشري مية كيلو تمر عشان العيد قريب", "We must buy a hundred kilos of dates because Eid is near", "laazim nishri miya keelo tamur 3ashaan el-3eed gareeb"),
        item("لازم يوصلون قبل الساعة عشرة، بعدها يسكرون الباب", "They must arrive before ten o'clock, after that they close the door", "laazim yoosaloon gabl es-saa3a 3ashara"),
    ]),

    lesson(20, "Review: Family, Food, Places, Time", "مراجعة", [
        item("لازم نطبخ للعرس ونوصل المجلس قبل صلاة المغرب بشوي", "We must cook for the wedding and arrive at the majlis a bit before the sunset prayer", "laazim naTbakh lil-3urs wa noosal el-majlis"),
        item("لازم أدفع فلوس المستشفى قبل ما نطلع من هناك", "I must pay the hospital money before we leave from there", "laazim adfa3 fluus el-mustashfa"),
        item("لازم أختي وأخوي يوصلون بدري عشان يساعدون بالطبخ", "My sister and brother must arrive early to help with the preparation", "laazim ukhti wa akhooy yoosaloon badri"),
        item("لازم ندري كم شخص جاي عشان نطبخ أكل يكفي الكل", "We must know how many people are coming so we cook the right amount", "laazim nadri kam shakhs jaay"),
    ]),

    lesson(21, "I Must Go to the Doctor", "لازم أروح الطبيب", [
        item("لازم أروح الطبيب لأن راسي يوجعني من أمس", "I must go to the doctor because my head has been hurting since yesterday", "laazim aruuH eT-Tabeeb li-ann raasi yoowja3ni min ams"),
        item("لازم تروح المستشفى، الوضع صار أصعب من قبل", "You must go to the hospital, the situation has become more dangerous than before", "laazim truuH el-mustashfa, el-wad3 saar akhtar min gabl"),
        item("لازم تروحين تشوفين الطبيبة قبل ما يصير الوضع أصعب", "You (f) must go see the doctor before the situation gets worse", "laazim truuHeen tshoofeen eT-Tabeeba"),
        item("لازم يروح المستشفى، رجله توجعه من أمس", "He must go to the hospital, his leg has been swollen since yesterday", "laazim yruuH el-mustashfa, rijlah mitwarrima min ams"),
    ]),

    lesson(22, "We Must Go to the Doctor", "لازم نروح الطبيب", [
        item("لازم نروح الطبيب سوا عشان ندري الوضع زين", "We must go to the doctor together in order to make sure about the situation", "laazim nruuH eT-Tabeeb sawa 3ashaan niTma'in 3alal-wad3"),
        item("لازم تروحون المستشفى الحين، ما ننتظر أكثر من كذا", "You all must go to the hospital now, we won't wait more than this", "laazim truu7oon el-mustashfa el-heen"),
        item("لازم يروحون يشوفون الطبيب قبل السفر عشان يدرون كل شي زين", "They must go see the doctor before the trip in order to reassure themselves", "laazim yruu7oon yshoofoon eT-Tabeeb gabl es-safar"),
        item("ما لازم نتأخر، الطبيبة زينة وما تلقاها كل وقت", "We shouldn't be late, the doctor is good and you don't find her any time", "ma laazim nit'akhkhar"),
    ]),

    lesson(23, "How Do You Feel Today?", "شلونك تحس اليوم؟", [
        item("شلونك تحس اليوم؟ أزيان من أمس، الحمد لله", "How do you feel today? Better than yesterday, thank God", "shlonak taHiss el-yoom? azyan min ams, alhamdulillah"),
        item("أحس بألم في راسي وظهري من الصبح", "I feel pain in my head and back since the morning", "aHiss bi-alam fi raasi wa dhahri min es-sub7"),
        item("تحسين بتحسن؟ نعم، الدوا ساعدني كثير", "Do you (f) feel improvement? Yes, the medicine helped me a lot", "taHisseen bitaHassun? na3am"),
        item("هو يحس بتعب كثير من السفر الطويل أمس", "He feels severe tiredness from yesterday's long trip", "huwa yiHiss bita3ab shadeed min es-safar eT-Taweel ams"),
    ]),

    lesson(24, "I Need Rest", "أحتاج راحة", [
        item("أحتاج راحة يومين قبل ما أرجع الشغل", "I need two days of rest before returning to work", "aHtaaj raaHa yoomayn gabl ma arja3 esh-shaghal"),
        item("تحتاجين تنامين أكثر، انتي تعبانة كثير هالأيام", "You (f) need to sleep more, you're very tired these days", "taHtaajeen tnaameen akthar"),
        item("نحتاج مساعدة عشان ننظف البيت قبل العرس", "We need help in order to clean the house before the wedding", "naHtaaj musaa3ada 3ashaan nanadhdhif el-bayt gabl el-3urs"),
        item("يحتاجون وقت أكثر عشان يفهمون الدرس زين", "They need more time in order to understand the lesson well", "yaHtaajoon wagt akthar 3ashaan yifhamoon ed-dars zayn"),
    ]),

    lesson(25, "Review: Health and Feelings", "مراجعة", [
        item("أحس بتعب كثير، أفكر لازم أروح الطبيب بكرا", "I feel severe tiredness, I think I must go to the doctor tomorrow", "aHiss bita3ab shadeed"),
        item("أحتاج راحة كافية عشان أقدر أرجع الشغل نشيط", "I need enough rest in order to be able to return to work with energy", "aHtaaj raaHa kaafya 3ashaan agdar arja3 esh-shaghal biguwwa"),
        item("جدتي تحس بتحسن بعد الدوا، الحمد لله كثير", "My grandmother feels improvement after the medicine, thank God so much", "jiddati taHiss bitaHassun ba3d ed-dawa"),
        item("لازم تحس بأزيان قبل السفر، لو ما تحس بأزيان لازم نرجع", "You must feel better before the trip, if you don't feel better we must go back", "laazim taHiss bi-azyan gabl es-safar"),
    ]),

    lesson(26, "A Full Day", "يوم كامل", [
        item("صحيت بدري، شربت قهوة، ورحت الشغل قبل الزحمة", "I woke up early, drank coffee, and went to work before the traffic", "SiHeet badri, sharabt gahwa"),
        item("درست الصبح، اشتغلت الظهر، وقعدت مع الأهل الليل", "I studied in the morning, worked at noon, and sat with the family at night", "darast es-sub7, ishtaghalt edh-dhuhur"),
        item("طبخنا الفطور، نظفنا البيت، وبعدين رحنا نزور جدي", "We cooked breakfast, cleaned the house, and then went to visit my grandfather", "Tabakhna el-futoor, nadhdhafna el-bayt"),
        item("سافرت الصبح، وصلت الظهر، وقعدت أرتاح لين المغرب", "I traveled in the morning, arrived at noon, and rested until sunset", "saafart es-sub7, wisalt edh-dhuhur"),
    ]),

    lesson(27, "Another Full Day", "يوم كامل ثاني", [
        item("اشتغلت من الصبح لين العصر بدون راحة", "I worked from morning until afternoon without taking a break", "ishtaghalt min es-sub7 leen el-3asir bidoon ma aakhudh raaHa"),
        item("درسنا للامتحان طول اليوم، وبعدين قعدنا نرتاح", "We studied for the exam all day, and then we sat resting", "darasna lil-imtiHaan Tool el-yoom"),
        item("زرنا المستشفى الصبح، وشرينا أشياء السوق الظهر", "We visited the hospital in the morning, and bought market things at noon", "zirna el-mustashfa es-sub7"),
        item("تكلمت مع أخوي طول الطريق، وفهمنا كل شي أخيرا", "I talked with my brother the whole way, and we finally understood everything", "tkallamt ma3 akhooy Tool eT-Tareeg"),
    ]),

    lesson(28, "Money and Feelings", "الفلوس والمشاعر", [
        item("مبسوط كثير لأني وفرت فلوس كافية للسفر هالصيف", "I'm very happy because I saved enough money to travel this summer", "mabsoot katheer li-anni waffart fluus kaafya lis-safar has-sayf"),
        item("قلقانة من الفلوس لأن الشغل صار أصعب هالسنة", "She's worried about money because work has become harder this year", "galgaana minal-fluus li-ann esh-shaghal saar as3ab has-sana"),
        item("فخور بنفسي لأني دفعت القرض كله أخيرا", "I'm proud of myself because I finally paid off all the debts", "fakhoor binafsi li-anni dafa3t kil ed-dyoon akheeran"),
        item("متضايق لأن دفعت فلوس كثير على شي ما يستاهل", "I'm upset because I paid a lot of money for something not worth it", "mutadaayig li-anni dafa3t fluus katheer 3ala shay ma yistaahil"),
    ]),

    lesson(29, "Family, Friends, and Feelings", "العائلة والأصحاب والمشاعر", [
        item("مبسوط كثير لأن كل أصحابي ياو للعرس أخيرا", "I'm very happy because all my friends finally came to the wedding", "mabsoot katheer li-ann kil as7aabi yaw lil-3urs akheeran"),
        item("فخورة بأختي لأنها نجحت في الجامعة زين كثير", "I'm proud of my sister because she succeeded at university with the best grades", "fakhoora bi-ukhti li-annaha najHat fil-jaami3a"),
        item("متعب من كل الشغل، بس أصحابي ساعدوني كثير هالأسبوع", "I'm exhausted from all the work, but my friends helped me a lot this week", "mut3ab min kil esh-shaghal"),
        item("زعلان من صاحبي لأنه ما اتصل فيني من زمان", "I'm upset with my friend because he hasn't called me in a long time", "za3laan min saaHbi li-annah ma ittasal feeni min zamaan"),
    ]),

    lesson(30, "Review: B1+ Recap", "مراجعة شاملة", [
        item("لازم أروح الطبيب لأن راسي يوجعني، بس أحس بتحسن شوي", "I must go to the doctor because my head hurts, but I feel a bit of improvement", "laazim aruuH eT-Tabeeb li-ann raasi yoowja3ni"),
        item("لازم نساعد جدي وجدتي، وأنا فخور بعائلتي كثير", "We must help my grandfather and grandmother, and I'm very proud of my family", "laazim nsaa3id jiddi wa jiddati, wa ana fakhoor bi-3aa'ilti katheer"),
        item("أحتاج راحة كافية قبل الامتحان عشان أقدر أفكر زين", "I need enough rest before the exam in order to be able to think well", "aHtaaj raaHa kaafya gabl el-imtiHaan"),
        item("مبسوطين لأن كل شي زين هالسنة، والحمد لله كثير", "We're happy because everything is good this year, thank God so much", "mabsooteen li-ann kil shay zayn has-sana"),
    ]),

    lesson(31, "Professions Must Go", "المهن ولازم يروح", [
        item("لازم المهندسة تروح المكتب الجديد تشوف المشروع", "The engineer must go to the new office to see the project", "laazim el-muhandisa truuH el-maktab el-jideed"),
        item("لازم المترجم يروح الاجتماع لأنه يعرف لغتين", "The translator must go to the meeting because he knows two languages", "laazim el-mutarjim yruuH el-ijtimaa3"),
        item("لازم التاجر يروح البنك يدفع فلوس المحل الجديد", "The merchant must go to the bank to pay for the new merchandise", "laazim et-taajir yruuH el-bank"),
        item("لازم المدرس يروح المدرسة بدري عشان يدرّس زين", "The teacher must go to school early in order to prepare the lesson", "laazim el-mudarris yruuH el-madrasa badri"),
    ]),

    lesson(32, "Clothes and Must", "الملابس ولازم", [
        item("لازم ألبس شي زين للاجتماع، هذا مهم كثير", "I must wear something nice for the meeting, this is very important", "laazim albas shay zayn lil-ijtimaa3"),
        item("لازم تلبسين عباية دافية، الجو بارد كثير اليوم", "You (f) must wear a warm abaya, the weather is very cold today", "laazim tilbaseen 3abaaya daafya"),
        item("لازم يلبسون ملابس مريحة عشان السفر طويل", "They must wear comfortable clothes because the trip is long", "laazim yilbasoon malaabis mureeHa"),
        item("ما لازم تلبس الجوتي الضيق، رجلك بتوجعك", "You shouldn't wear the tight shoes, your foot will hurt", "ma laazim tilbas el-jooti ed-dayyig"),
    ]),

    lesson(33, "At the Hospital", "في المستشفى", [
        item("الطبيبة قالت لازم أرتاح أسبوع كامل بدون شغل", "The doctor said I must rest a whole week without work", "eT-Tabeeba gaalat laazim artaaH isboo3 kaamil bidoon shughul"),
        item("جدي في المستشفى، بس الحمد لله الوضع تحسن كثير", "My grandfather is in the hospital, but thank God the situation improved a lot", "jiddi fil-mustashfa, bas alhamdulillah el-wad3 taHassan katheer"),
        item("زرناه في المستشفى وشفناه يتكلم زين، والحمد لله على هذا", "We visited him in the hospital and saw him talking well, thank God for this", "zirnaah fil-mustashfa wa shifnaah yitkallam zayn"),
        item("الدكتور قال إنه بيطلع من المستشفى بكرا انشاالله", "The doctor said he'll leave the hospital tomorrow God willing", "ed-doktoor gaal innah bayiTla3 minal-mustashfa bukra inshaallah"),
    ]),

    lesson(34, "Food, Must Have", "الأكل، لازم يكون عندنا", [
        item("لازم يكون عندنا تمر وقهوة دايما في البيت للضيوف", "We must always have dates and coffee for unexpected guests", "laazim ykoon 3indana tamur wa gahwa dayman lidh-dhuyoof"),
        item("لازم يكون عندك أكل كافي قبل ما تروح الشغل الصبح", "You must have enough food before you start the diet", "laazim ykoon 3indak akal kaafi"),
        item("لازم يكون عندهم لحم وسلطة وأرز للعشاء الليلة", "They must have meat, salad, and rice for tonight's dinner", "laazim ykoon 3indahum la7am wa salata wa aruz lil-3ashaa el-layla"),
        item("لازم يكون عندنا مويه كافية قبل السفر الطويل", "We must have enough water before the long trip", "laazim ykoon 3indana moya kaafya gabl es-safar eT-Taweel"),
    ]),

    lesson(35, "Food, Must Have II", "الأكل، لازم يكون عندنا ٢", [
        item("لازم يكون عندك خبز طازة كل صباح مع الفطور", "You must have fresh bread every morning with breakfast", "laazim ykoon 3indak khubz Taaza kil sabaaH"),
        item("لازم يكون فيه أكل يناسب كل الضيوف، بعضهم ما ياكل لحم", "There must be food suitable for all the guests, some of them don't eat meat", "laazim ykoon feeh akal ynaasib kil edh-dhuyoof"),
        item("لازم نطبخ أكل كافي لأن أكثر الأهل جايين هالمرة", "We must cook enough food because most of the family is coming this time", "laazim naTbakh akal kaafi li-ann akthar el-ahl jaayeen hal-marra"),
        item("لازم يكون عندنا حلو بعد العشاء، الأطفال يحبونه كثير", "We must have dessert after dinner, the children love it a lot", "laazim ykoon 3indana Hilu ba3d el-3ashaa"),
    ]),

    lesson(36, "Weather and Must", "الجو ولازم", [
        item("لازم تاخذ مظلة معاك، الجو غائم كثير بعدين", "You must take an umbrella with you, the weather is cloudy and it'll rain later", "laazim taakhudh midhalla ma3aak"),
        item("لازم نلبس ملابس دافية لأن الرطوبة والريح قوية اليوم", "We must wear warm clothes because the humidity and wind are strong today", "laazim nilbas malaabis daafya"),
        item("لازم نقعد بالبيت اليوم، فيه عاصفة قوية في الطريق", "We must stay home today, there's a strong storm on the way", "laazim nag3ad bil-bayt el-yoom, feeh 3aasifa gawiyya fiT-Tareeg"),
        item("ما لازم تطلع الحين، الجو حار كثير وقت الظهر", "You shouldn't go out now, the weather is very hot at noon", "ma laazim tiTla3 el-heen"),
    ]),

    lesson(37, "Sleeping", "النوم", [
        item("لازم أنام بدري عشان أصحى نشيط بكرا الصبح", "I must sleep early in order to wake up energetic tomorrow morning", "laazim anaam badri 3ashaan aSHa nasheeT bukra es-sub7"),
        item("ما نامت زين أمس، فهي متعبة كثير اليوم", "She didn't sleep well yesterday, so she's very tired today", "ma naamat zayn ams, fahiya mut3aba katheer el-yoom"),
        item("الأطفال نامو بدري لأنهم تعبو من اللعب طول اليوم", "The children slept early because they got tired from playing all day", "el-aTfaal naamaw badri li-annahum ti3baw minal-la3ib Tool el-yoom"),
        item("ما أقدر أنام لين أفكر بكل مشاكل الشغل", "I can't sleep until I think about all the work problems", "ma agdar anaam leen afakkir bikil mashaakil esh-shaghal"),
    ]),

    lesson(38, "I Must Cook", "لازم أطبخ", [
        item("لازم أطبخ للعرس، عندي وصفات جديدة كثير أبغى أجربها", "I must cook for the wedding, I have a lot of new recipes I want to try", "laazim aTbakh lil-3urs"),
        item("لازم تطبخين شي بسيط اليوم، ما عندنا وقت كثير", "You (f) must cook something simple today, we don't have much time", "laazim taTbakheen shay baseet el-yoom"),
        item("لازم نطبخ أكل خليجي لذيذ للضيوف هالمرة", "We must cook authentic Khaleeji food for the foreign guests this time", "laazim naTbakh akal khaleeji lidh-dhuyoof"),
        item("لازم يطبخون قبل ما يوصل الأهل، الوقت ضيق كثير", "They must cook before the family arrives, the time is very tight", "laazim yaTbakhoon gabl ma yoosal el-ahl"),
    ]),

    lesson(39, "Body Parts", "أجزاء الجسم", [
        item("عيني تعبانة من الشغل الطويل طول اليوم", "My eye is tired from working on the computer all day", "3ayni ta3baana minesh-shughul 3alal-kombyootar Tool el-yoom"),
        item("يدي توجعني من الشغل الطويل في البيت أمس", "My hand hurts from the long work at home yesterday", "yiddi toowja3ni minesh-shughul eT-Taweel"),
        item("راسه يوجعه من الشغل الكثير هالأسبوع كله", "His head hurts from lack of sleep this whole week", "raasah yoowja3ah min gillat en-nawm hal-isboo3 killah"),
        item("رجلها متعبة من الوقفة الطويلة في المطبخ", "Her foot is tired from the long standing in the kitchen", "rijilha mut3aba minal-wagfa eT-Taweela fil-matbakh"),
    ]),

    lesson(40, "Lazim with Objects", "لازم مع الأشياء", [
        item("لازم عندنا مفتاح ثاني للبيت، ما ندري وين الأول", "We must have a second key for the house, we don't know where the first one is", "laazim 3indana miftaaH thaani lil-bayt, ma nadri wein el-awwal"),
        item("لازم اخذ محفظتي ونظارتي قبل ما أطلع من البيت", "I must take my wallet and glasses before I leave the house", "laazim aakhudh maH-fadhti wa nadhdhaarti"),
        item("لازم يكون عندك مظلة في السيارة، الجو غائم دايما هالفصل", "You must have an umbrella in the car, the weather is always cloudy this season", "laazim ykoon 3indak midhalla fis-sayyaara"),
        item("لازم نشري كتب جديدة للطلاب قبل ما يبدأ الفصل", "We must buy new books for the students before the semester starts", "laazim nishri kutub jideeda liT-Tullaab"),
    ]),

    lesson(41, "Polite Requests, Because", "طلبات مؤدبة ولأن", [
        item("ممكن تساعدني شوي لأن الشنطة ثقيلة علي كثير", "Could you help me a bit because the bag is too heavy for me", "mumkin tsaa3idni shway li-ann esh-shanTa thageela 3alay katheer"),
        item("لو سمحت، ممكن تقول لي وين البنك لأني ما أدري الطريق", "Excuse me, could you tell me where the bank is because I'm lost", "law sama7t, mumkin tguul li wein el-bank li-anni daayi3"),
        item("من فضلك، ممكن تنتظر شوي لأن أخوي بيوصل بعد دقيقة", "Please, could you wait a bit because my brother will arrive in a minute", "min fadlak, mumkin tintadhir shway li-ann akhooy bayoosal ba3d dageega"),
        item("ممكن تعطيني فنجان قهوة ثاني لأن الأول كان لذيذ كثير", "Could you give me another cup of coffee because the first one was very delicious", "mumkin ta3teeni finjaan gahwa thaani"),
    ]),

    lesson(42, "Comparatives, Because", "المقارنة ولأن", [
        item("هذا البيت أكبر من الثاني لأن فيه غرف أكثر", "This house is bigger than the other one because it has more rooms", "haadha el-bayt akbar minath-thaani li-ann feeh ghuraf akthar"),
        item("القهوة هنا أزيان لأنهم يحطون هيل زين فيها", "The coffee here is better because they put good cardamom in it", "el-gahwa hina azyan li-annahum yiHiTToon heel zayn feeha"),
        item("هذا الجوتي أغلى من الثاني لأنه أزيان كثير", "These shoes are more expensive than the other pair because they're imported from abroad", "haadha el-jooti aghla minath-thaani li-annah mustawrad min barra"),
        item("القطار أسرع من الباص لأنه ما يوقف كثير في الطريق", "The train is faster than the bus because it doesn't stop much along the way", "el-gitaar asra3 minal-baas li-annah ma yoogaf katheer fiT-Tareeg"),
    ]),

    lesson(43, "Time, Chained", "الوقت المتسلسل", [
        item("أول ما أصحى، أشرب قهوة، وبعدين أنظف البيت، وبعدين أروح الشغل", "First when I wake up, I drink coffee, then I clean the house, then I go to work", "awwal ma aSHa, ashrab gahwa"),
        item("قبل النوم أقرى شوي، وبعدين أفكر باليوم الجاي، وبعدين أنام", "Before sleep I read a bit, then I think about tomorrow, then I sleep", "gabl en-nawm agra shway"),
        item("لين نوصل السوق، نشري الأكل، وبعدين نروح المطعم، وبعدين نرجع البيت", "Until we reach the market, we buy the food, then we go to the restaurant, then we return home", "leen noosal es-suug"),
        item("أول نصلي، وبعدين نشرب قهوة، وبعدين نقعد في المجلس لين المغرب", "First we pray, then we drink coffee, then we sit in the majlis until sunset", "awwal nsalli, wa ba3dayn nishrab gahwa"),
    ]),

    lesson(44, "Back, Knee, Nose", "الظهر والركبة والخشم", [
        item("ظهري يوجعني من الوقفة الطويلة في المطبخ أمس", "My back hurts from the long standing in the kitchen yesterday", "dhahri yoowja3ni minal-wagfa eT-Taweela fil-matbakh ams"),
        item("ركبته توجعه لأنه يمشي كثير كل يوم للشغل", "His knee hurts him from how much he walks every day to work", "rukbatah toowja3ah min kithir ma yimshi kil yoom lish-shughul"),
        item("خشمها حساس من البخور، فما تقدر تقعد بالمجلس كثير", "Her nose is sensitive to incense, so she can't sit in the majlis for long", "khashimha Hassaas minal-bukhoor"),
        item("لازم أروح الطبيب لأن ظهري يوجعني من أسبوع كامل", "I must go to the doctor because my back has been hurting for a whole week", "laazim aruuH eT-Tabeeb li-ann dhahri yoowja3ni min isboo3 kaamil"),
    ]),

    lesson(45, "Buying and Paying, Because", "الشراء والدفع ولأن", [
        item("شريت جوتي جديد لأن القديم صار ضيق على رجلي", "I bought new shoes because the old ones became tight on my foot", "sharayt jooti jideed li-ann el-gadeem saar dayyig 3ala rijli"),
        item("ما دفعت كل الفلوس مرة وحدة لأن السعر كان عالي", "I didn't pay all the money at once because the price was high", "ma dafa3t kil el-fluus marra waHda li-ann es-si3ir kaan 3aali"),
        item("لازم تسأل عن السعر قبل ما تدفع عشان ما يغشونك", "You must ask about the price before you pay so they don't cheat you", "laazim tis'al 3anis-si3ir gabl ma tidfa3"),
        item("دفعنا أرخص سعر بالسوق لأننا شفنا محلات كثير قبل ما نقرر", "We paid the cheapest price in the market because we saw a lot of shops before deciding", "dafa3na arkhas si3ir bis-suug li-annana shifna ma7allaat katheer gabl ma niqarrir"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/b1plus.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "b1plus", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/b1plus.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
