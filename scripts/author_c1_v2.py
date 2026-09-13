#!/usr/bin/env python3
"""Full rewrite of C1 Khaleeji Arabic content -- long chained-clause
sentences (because/and/but/so/before/after), same repetition fix. Written
conservatively against the now-very-large confirmed vocabulary from A1
through B2+ to minimize new-word research overhead.
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
    lesson(1, "Going Home, Because, And", "الرواح البيت، لأن، و", [
        item("رحت البيت بدري لأني كنت تعبان، وقعدت أرتاح لين المغرب", "I went home early because I was tired, and I sat resting until sunset", "riHt el-bayt badri li-anni kint ta3baan, wa ga3adt artaaH leen el-maghrib"),
        item("راح جدي المجلس لأنه يحب يشوف أصحابه، وقعد يشرب قهوة معهم", "My grandfather went to the majlis because he loves seeing his friends, and he sat drinking coffee with them", "raaH jiddi el-majlis li-annah yiHibb yshoof as7aabah"),
        item("رحنا السوق لأن أختي تبغى غترة جديدة، وشرينا لها وحدة زينة", "We went to the market because my sister wants a new headdress, and we bought her a nice one", "riHna es-suug li-ann ukhti tibgha ghitra jideeda"),
        item("راحو المطار لأن جدهم راجع من السفر، ووصلو قبل الطيارة بشوي", "They went to the airport because their grandfather is returning from his trip, and they arrived a bit before the plane", "raaHaw el-mataar li-ann jiddahum raaji3 mines-safar"),
    ], topicId="c1-chain"),

    lesson(2, "Drinking, Because, And", "الشرب، لأن، و", [
        item("أشرب قهوة كل صباح لأني أحبها كثير، وأشرب شاي بعد العصر", "I drink coffee every morning because I love it a lot, and I drink tea after the afternoon", "ashrab gahwa kil sabaaH li-anni aHibbha katheer"),
        item("تشرب مويه بارده بعد الرياضة لأن جسمها يحتاجها، وترتاح بعدين", "She drinks cold water after exercise because her body needs it, and she rests afterward", "tishrab moya baarda ba3d er-riyaada li-ann jismha yaHtaajha"),
        item("نشرب قهوة في المجلس كل جمعة لأن جدي يحبها، ونتكلم عن أخبار الأسبوع", "We drink coffee in the majlis every Friday because my grandfather loves it, and we talk about the week's news", "nishrab gahwa fil-majlis kil jum3a li-ann jiddi yiHibbha"),
        item("يشربون شاي بالحليب لأنهم يحبونه، وياكلون تمر معه كل مرة", "They drink tea with milk because they love it, and they eat dates with it every time", "yishrabuun shaay bil-Haleeb li-annahum yiHibboonah"),
    ]),

    lesson(3, "Wanting, Because, And", "الرغبة، لأن، و", [
        item("أبغى بيت أكبر لأن عائلتي كبرت، وأبغى غرف أكثر للأولاد", "I want a bigger house because my family grew, and I want more rooms for the children", "abgha bayt akbar li-ann 3aa'ilti kubrat"),
        item("تبغى تدرس في جامعة زينة لأنها تحب العلم، وتبغى تصير مهندسة", "She wants to study at a good university because she loves knowledge, and she wants to become an engineer", "tibgha tadrus fi jaami3a zeena li-annaha tHibb el-3ilm"),
        item("أبغى أسافر للكويت لأن عندي أهل هناك، وأبغى أزورهم قبل العيد", "I want to travel to Kuwait because I have family there, and I want to visit them before Eid", "abgha asaafir lil-kuwayt li-ann 3indi ahl hinaak"),
        item("يبغى يشتغل في مكتب كبير لأنه يحب هالنوع من الشغل، ويبغى راتب زين", "He wants to work in a big office because he loves this kind of work, and he wants a good salary", "yibgha yashtaghil fi maktab kabeer li-annah yiHibb han-noo3 minesh-shughul"),
    ]),

    lesson(4, "Knowing, Because, And", "المعرفة، لأن، و", [
        item("أدري وين البيت لأني رحت له مرة قبل، وأدري الطريق زين الحين", "I know where the house is because I went there once before, and I know the way well now", "adri wein el-bayt li-anni riHt lah marra gabl"),
        item("تدري السعر الصح لأنها سألت في محلات كثير، وتدري وين أرخص شي", "She knows the right price because she asked at a lot of shops, and she knows where the cheapest thing is", "tadri es-si3ir es-saHH li-annaha sa'alat fi ma7allaat katheer"),
        item("ندري متى العرس لأن خالتي قالت لنا، وندري وين بالضبط", "We know when the wedding is because my maternal aunt told us, and we know exactly where", "nadri mita el-3urs li-ann khaalti gaalat lana"),
        item("يدرون كل شي عن السفر لأنهم سافرو قبل مرات كثير، ويدرون شنو يحتاجون", "They know everything about the trip because they've traveled many times before, and they know what they need", "yidroon kil shay 3anis-safar li-annahum saafaraw gabl marraat katheer"),
    ]),

    lesson(5, "Review: Chained Clauses", "مراجعة: الجمل المتسلسلة", [
        item("رحت السوق لأني أبغى أشري غترة، وشريت وحدة زينة ورخيصة", "I went to the market because I want to buy a headdress, and I bought a nice cheap one", "riHt es-suug li-anni abgha ashri ghitra"),
        item("تشرب قهوة كل يوم لأنها تحبها، بس ما تشربها بالليل عشان تنام زين", "She drinks coffee every day because she loves it, but she doesn't drink it at night so she sleeps well", "tishrab gahwa kil yoom li-annaha tHibbha"),
        item("ندري وين المسجد لأننا رحنا له كثير، وندري متى الصلاة بالضبط", "We know where the mosque is because we've gone there a lot, and we know exactly when the prayer is", "nadri wein el-masjid li-annana riHna lah katheer"),
        item("يبغى يسافر هالصيف لأنه تعب من الشغل، ويبغى يرتاح شوي", "He wants to travel this summer because he got tired from work, and he wants to rest a bit", "yibgha ysaafir has-sayf li-annah ti3ib minesh-shughul"),
    ]),

    lesson(6, "Not Going, Because, But", "عدم الرواح، لأن، بس", [
        item("ما رحت الشغل أمس لأني كنت مريض، بس اليوم أنا زين والحمد لله", "I didn't go to work yesterday because I was sick, but today I'm well, thank God", "ma riHt esh-shaghal ams li-anni kint mareed"),
        item("ما راحت العرس لأن عندها امتحان بكرا، بس اتصلت فيهم وقالت مبروك", "She didn't go to the wedding because she has an exam tomorrow, but she called them and said congratulations", "ma raaHat el-3urs li-ann 3indaha imtiHaan bukra"),
        item("ما رحنا المطعم الجديد لأنه غالي كثير، بس سمعنا إنه لذيذ", "We didn't go to the new restaurant because it's very expensive, but we heard it's delicious", "ma riHna el-mat3am el-jideed li-annah ghaali katheer"),
        item("ما راحو المسجد يوم الجمعة لأنهم كانو في السفر، بس صلو بالبيت", "They didn't go to the mosque on Friday because they were traveling, but they prayed at home", "ma raaHaw el-masjid yoom el-jum3a li-annahum kaanaw fis-safar"),
    ]),

    lesson(7, "Not Wanting, Because, But", "عدم الرغبة، لأن، بس", [
        item("ما أبغى أشتغل بعيد عن البيت لأن السفر يتعبني، بس ما عندي شغل ثاني", "I don't want to work far from home because the commute tires me, but I have no other choice", "ma abgha ashtaghil ba3eed 3anil-bayt li-ann es-safar yta3ibni"),
        item("ما تبغى تسافر لوحدها لأنها ما تعرف اللغة هناك، بس أختها بتروح معها", "She doesn't want to travel alone because she doesn't know the language there, but her sister will go with her", "ma tibgha tsaafir liwaHdaha li-annaha ma ta3rif el-lugha hinaak"),
        item("ما أبغى أشري البيت الغالي لأن ما عندي فلوس كافية، بس أوفر عشان بعدين", "I don't want to buy the expensive house because I don't have enough money, but I'm saving for later", "ma abgha ashri el-bayt el-ghaali li-ann ma 3indi fluus kaafya"),
        item("ما يبغى يروح المستشفى لأنه ما يحبها، بس لازم يروح عشان صحته", "He doesn't want to go to the hospital because he doesn't like it, but he must go for his health", "ma yibgha yruuH el-mustashfa li-annah ma yiHibbha"),
    ]),

    lesson(8, "Money, Because, So", "الفلوس، لأن، فـ", [
        item("ما عندي فلوس كافية اليوم، فقررت أروح السوق بكرا بدل اليوم", "I don't have enough money today, so I decided to go to the market tomorrow instead of today", "ma 3indi fluus kaafya el-yoom, fa-garrart aruuH es-suug bukra"),
        item("كان السعر غالي كثير، فرحنا محل ثاني ولقينا سعر أرخص وأزيان", "The price was very expensive, so we went to another shop and found a cheaper and better price", "kaan es-si3ir ghaali katheer, fa-riHna maHal thaani"),
        item("دفعنا فلوس كثير على السفر، فقررنا نوفر أكثر الشهر الجاي", "We paid a lot of money for the trip, so we decided to save more next month", "dafa3na fluus katheer 3ales-safar, fa-garrarna nwaffir akthar esh-shahar el-jaay"),
        item("ما دفع الحساب على وقته، فاتصلو فيه من البنك يتكلمون معه", "He didn't pay the bill on time, so they called him from the bank to talk with him", "ma dafa3 el-Hisaab 3ala wagtah, fa-ittasalaw feeh minal-bank"),
    ]),

    lesson(9, "Family, Because, And", "العائلة، لأن، و", [
        item("جدي يحب المجلس لأنه يقعد فيه مع أصحابه، ويحكي لهم قصص عن زمان", "My grandfather loves the majlis because he sits there with his friends, and he tells them stories about the old days", "jiddi yiHibb el-majlis li-annah yig3ad feeh ma3 as7aabah"),
        item("خالتي تحب السفر لأنها تحب تشوف أماكن جديدة، وتحب تجرب أكل جديد", "My maternal aunt loves traveling because she loves seeing new places, and she loves trying new food", "khaalti tHibb es-safar li-annaha tHibb tshoof amaakin jideeda"),
        item("أخوي يحب شغله لأنه يساعد ناس كثير فيه، ويحس إنه يسوي شي مهم", "My brother loves his job because he helps a lot of people in it, and he feels he's doing something important", "akhooy yiHibb shughlah li-annah ysaa3id naas katheer feeh"),
        item("أختي تحب أولادها كثير، فتقعد وياهم كل ما تقدر", "My sister loves her children a lot, so she sits with them every free time she has", "ukhti tHibb awlaadha katheer, fa-tag3ad wiyaahum kil wagt faadi 3indaha"),
    ]),

    lesson(10, "Review: C1 Recap", "مراجعة", [
        item("جدي يحب المجلس لأنه يقعد فيه مع أصحابه ويحكي قصص، وأنا أحب أسمعها", "My grandfather loves the majlis because he sits there with his friends and tells stories, and I love hearing them", "jiddi yiHibb el-majlis li-annah yig3ad feeh ma3 as7aabah wa yiHki gisas"),
        item("ما رحنا العرس لأن عندنا شغل، بس اتصلنا فيهم وقلنا مبروك", "We didn't go to the wedding because we had work, but we called them and said congratulations", "ma riHna el-3urs li-ann 3indana shughul"),
        item("ما عندي فلوس كافية للسفر هالصيف، فقررت أوفر أكثر وأسافر السنة الجاية", "I don't have enough money to travel this summer, so I decided to save more and travel next year", "ma 3indi fluus kaafya lis-safar has-sayf, fa-garrart awaffir akthar"),
        item("أختي تحب أولادها كثير، وتحس إنهم أهم شي في حياتها", "My sister loves her children a lot, and she feels they're the most important thing in her life", "ukhti tHibb awlaadha katheer, wa tHiss innahum ahamm shay fi Hayaatha"),
    ]),

    lesson(11, "The Near Place, Because, But", "المكان القريب، لأن، بس", [
        item("رحنا المطعم القريب لأنه سريع، بس الأكل هناك مب لذيذ زين", "We went to the nearby restaurant because it's fast, but the food there isn't very delicious", "riHna el-mat3am el-gareeb li-annah saree3"),
        item("البيت قريب من الشغل لأننا اخترناه بسبب هذا، بس السعر كان غالي شوي", "The house is near work because we chose it for this reason, but the price was a bit expensive", "el-bayt gareeb minesh-shughul li-annana ikhtarnaah bisabab haadha"),
        item("المسجد قريب من بيتنا لأنه في نفس الحي، بس المجلس بعيد شوي", "The mosque is near our house because it's in the same neighborhood, but the majlis is a bit far", "el-masjid gareeb min baytna li-annah fi nafs el-Hayy"),
        item("السوق بعيد عن بيتنا لأننا سكنا هنا جديد، بس البنك قريب زين", "The market is far from our house because we moved here recently, but the bank is quite near", "es-suug ba3eed 3an baytna li-annana sakanna hina Hadeeth"),
    ]),

    lesson(12, "This Red House, Because, And", "هذا البيت الأحمر، لأن، و", [
        item("أبغى هذا البيت الأحمر لأنه قريب من المدرسة، وفيه غرف كثير للعائلة", "I want this red house because it's near the school, and it has a lot of rooms for the family", "abgha haadha el-bayt el-a7mar li-annah gareeb minal-madrasa"),
        item("شريت السيارة الزرقاء لأنها كانت أرخص من الحمراء، وناسبت فلوسي زين", "I bought the blue car because it was cheaper than the red one, and it suited my money well", "sharayt es-sayyaara ez-zarqaa li-annaha kaanat arkhas minal-Hamraa"),
        item("لبست القميص الأخضر لأنه يناسب البنطلون، ولأني أحب هاللون كثير", "I wore the green shirt because it matches the pants, and because I love this color a lot", "libast el-gamees el-akhdar li-annah ynaasib el-bantaloon"),
        item("اخترنا الغترة البيضاء لأنها تناسب العباية السوداء، وكانت زينة كثير", "We chose the white headdress because it matches the black abaya, and it was very nice", "ikhtarna el-ghitra el-baydaa li-annaha tnaasib el-3abaaya es-sawdaa"),
    ]),

    lesson(13, "Days, Because, And", "الأيام، لأن، و", [
        item("يوم الجمعة زين لأننا نقعد مع الأهل كلهم، ونشرب قهوة في المجلس", "Friday is good because we sit with all the family, and we drink coffee in the majlis", "yoom el-jum3a zayn li-annana nag3ad ma3al-ahl killahum"),
        item("يوم السبت أروح الشغل لأنه يوم عادي عندنا، وأرجع البيت متأخر شوي", "Saturday I go to work because it's a normal day for us, and I return home a bit late", "yoom es-sabt aruuH esh-shaghal li-annah yoom 3aadi 3indana"),
        item("الأسبوع الماضي كان صعب لأن عندنا شغل كثير، بس هالأسبوع أسهل زين", "Last week was difficult because we had a lot of work, but this week is much easier", "el-isboo3 el-maadi kaan sa3ib li-ann 3indana shughul katheer"),
        item("الشهر الجاي عندنا عرس لأن ابن عمي بيتزوج، وكل العائلة بتجي", "Next month we have a wedding because my paternal cousin is getting married, and the whole family will gather", "esh-shahar el-jaay 3indana 3urs li-ann ibin 3ammi baytizawwaj"),
    ]),

    lesson(14, "Feelings, Because, But", "المشاعر، لأن، بس", [
        item("أنا مبسوط كثير لأن أخوي راجع من السفر، بس تعبان شوي لأني ما نمت زين", "I'm very happy because my brother is back from his trip, but a bit tired because I didn't sleep well", "ana mabsoot katheer li-ann akhooy raaji3 mines-safar"),
        item("هي قلقانة على الامتحان لأنها ما درست كافي، بس تفكر تدرس طول الليلة", "She's worried about the exam because she didn't study enough, but she's thinking of studying all night", "hiya galgaana 3alal-imtiHaan li-annaha ma darasat kaafi"),
        item("احنا فخورين بجدنا لأنه سوى كل هالشي بنفسه، بس هو ما يحب الكلام عن هذا", "We're proud of our grandfather because he did all this himself, but he doesn't like talking about it", "iHna fakhooreen bijiddana li-annah sawa kil hash-shay binafsah"),
        item("هم متضايقين من الجو لأنه حار كثير هالأيام، بس ما يقدرون يسوون شي", "They're upset about the weather because it's very hot these days, but they can't do anything", "hum mutadaayigeen minal-jaww li-annah Haarr katheer hal-ayyaam"),
    ]),

    lesson(15, "Review: Places, Colors, Days, Feelings", "مراجعة", [
        item("رحنا المجلس القريب يوم الجمعة لأننا نحب نقعد مع الأهل، وشربنا قهوة كثير", "We went to the nearby majlis on Friday because we love sitting with the family, and we drank a lot of coffee", "riHna el-majlis el-gareeb yoom el-jum3a li-annana niHibb nag3ad ma3al-ahl"),
        item("شريت البيت الأخضر لأنه قريب من الشغل، بس السعر كان أغلى من اللي فكرت فيه", "I bought the green house because it's near work, but the price was more expensive than what I thought", "sharayt el-bayt el-akhdar li-annah gareeb minesh-shughul"),
        item("أنا مبسوط اليوم لأن الجو زين والشغل خلص بدري، فقررت أزور جدي", "I'm happy today because the weather is nice and work finished early, so I decided to visit my grandfather", "ana mabsoot el-yoom li-ann el-jaww zayn wash-shughul khallas badri"),
        item("هي قلقانة على الشهر الجاي لأن عندها امتحانات كثير، بس تدرس كل يوم", "She's worried about next month because she has a lot of exams, but she studies every day", "hiya galgaana 3alash-shahar el-jaay li-ann 3indaha imtiHaanaat katheer"),
    ]),

    lesson(16, "Numbers, Because, And", "الأرقام، لأن، و", [
        item("درست ستين صفحة لأن الامتحان صعب، وبقت أربعين صفحة بس لبكرا", "I studied sixty pages because the exam is hard, and only forty pages remain for tomorrow", "darast sitteen safHa li-ann el-imtiHaan sa3ib"),
        item("دفعنا مية على العشاء لأننا كنا عشرة أشخاص، وكان الأكل لذيذ كثير", "We paid a hundred for dinner because we were ten people, and the food was very delicious", "dafa3na miya 3alal-3ashaa li-annana kinna 3ashara"),
        item("عندي عشرين سنة أشتغل في هالمكتب لأني أحب شغلي، وما أبغى أشتغل بمكان ثاني أبدا", "I've worked at this office for twenty years because I love my job, and I never want to work anywhere else", "3indi 3ishreen sana ashtaghil fi hal-maktab li-anni aHibb shughli"),
        item("شرينا سبعين كيلو تمر للعيد لأن الأهل كثير هالسنة، وكل واحد ياخذ شوي منه", "We bought seventy kilos of dates for Eid because there's a lot of family this year, and everyone takes a bit of it", "sharayna sab3een keelo tamur lil-3eed li-ann el-ahl katheer has-sana"),
    ]),

    lesson(17, "Health, Because, But", "الصحة، لأن، بس", [
        item("رحت الطبيب لأن راسي كان يوجعني، بس الحمد لله الوضع صار أزيان", "I went to the doctor because my head was hurting, but thank God the situation got better", "riHt eT-Tabeeb li-ann raasi kaan yoowja3ni"),
        item("أحس بتحسن لأني اخذت الدوا على وقته، بس لسا أحس بتعب شوي", "I feel better because I took the medicine on time, but I still feel a bit tired", "aHiss bitaHassun li-anni akhadht ed-dawa 3ala wagtah"),
        item("لازم أرتاح كامل أسبوع لأن الطبيبة قالت كذا، بس عندي شغل كثير ينتظرني", "I must rest a whole week because the doctor said so, but I have a lot of work waiting for me", "laazim artaaH kaamil isboo3 li-anniT-Tabeeba gaalat kadha"),
        item("جدي في المستشفى لأن ظهره يوجعه من زمان، بس يتكلم ويضحك زين الحمد لله", "My grandfather is in the hospital because his back has hurt for a long time, but he talks and is doing well, thank God", "jiddi fil-mustashfa li-ann dhahrah yoowja3ah min zamaan"),
    ]),

    lesson(18, "Not Because, But Because, Chained", "مب لأن، بس لأن، متسلسل", [
        item("ما شريت البيت مب لأنه غالي، بس لأن موقعه بعيد من الشغل وأتعب كل يوم", "I didn't buy the house not because it's expensive, but because its location is far from work and I'd get tired every day", "ma sharayt el-bayt mub li-annah ghaali"),
        item("ما رحت العرس مب لأني زعلان، بس لأن عندي امتحان بكرا ولازم أدرس", "I didn't go to the wedding not because I'm upset, but because I have an exam tomorrow and must study", "ma riHt el-3urs mub li-anni za3laan"),
        item("ما نجحت مب لأن الامتحان صعب كثير، بس لأني ما درست زين وما كان عندي وقت", "I didn't succeed not because the exam was too hard, but because I didn't study well and didn't have time", "ma najaHt mub li-ann el-imtiHaan sa3ib katheer"),
        item("ما اشتغل هناك مب لأن الفلوس قليلة، بس لأن الشغل بعيد وما يناسب وقته", "He didn't work there not because the money is little, but because the work is far and doesn't suit his time", "ma ishtaghal hinaak mub li-ann el-fluus galeela"),
    ]),

    lesson(19, "A Full Day, Chained", "يوم كامل، متسلسل", [
        item("صحيت بدري، شربت قهوة، رحت الشغل، اشتغلت لين العصر، وبعدين رجعت البيت أرتاح", "I woke up early, drank coffee, went to work, worked until afternoon, and then returned home to rest", "SiHeet badri, sharabt gahwa, riHt esh-shaghal"),
        item("طبخنا الفطور، نظفنا البيت، رحنا السوق، شرينا أشياء للعرس، ورجعنا نلبس ملابسنا", "We cooked breakfast, cleaned the house, went to the market, bought things for the wedding, and returned to put on our clothes", "Tabakhna el-futoor, nadhdhafna el-bayt, riHna es-suug"),
        item("درست الصبح، اشتغلت الظهر، قعدت مع الأهل الليل، وقبل ما أنام قريت شوي", "I studied in the morning, worked at noon, sat with the family at night, and before sleeping I read a bit", "darast es-sub7, ishtaghalt edh-dhuhur, ga3adt ma3al-ahl el-layl"),
        item("سافرنا الصبح، وصلنا الظهر، زرنا الأهل هناك، وقعدنا نشرب قهوة لين المغرب", "We traveled in the morning, arrived at noon, visited the family there, and sat drinking coffee until sunset", "saafarna es-sub7, wisalna edh-dhuhur, zirna el-ahl hinaak"),
    ]),

    lesson(20, "Review: C1 Recap 2", "مراجعة", [
        item("صحيت بدري ورحت الشغل لأن عندي اجتماع مهم، وخلصت الشغل قبل الظهر", "I woke up early and went to work because I have an important meeting, and I finished the work before noon", "SiHeet badri wa riHt esh-shaghal li-ann 3indi ijtimaa3 muhim"),
        item("ما رحت العرس مب لأني تعبان، بس لأن عندي شغل مهم ولازم أخلصه اليوم", "I didn't go to the wedding not because I'm tired, but because I have important work and must finish it today", "ma riHt el-3urs mub li-anni ta3baan"),
        item("جدي في المستشفى، بس يتكلم زين ويضحك، والحمد لله الوضع تحسن كثير", "My grandfather is in the hospital, but he talks well and is doing well, and thank God the situation improved a lot", "jiddi fil-mustashfa, bas yitkallam zayn"),
        item("سافرنا ووصلنا وزرنا الأهل وقعدنا نشرب قهوة، وكان يوم زين كثير", "We traveled, arrived, visited the family, and sat drinking coffee, and it was a very good day", "saafarna wa wisalna wa zirna el-ahl wa ga3adna nishrab gahwa"),
    ]),

    lesson(21, "Lazim, Because, And", "لازم، لأن، و", [
        item("لازم أروح البنك لأن فلوس البيت لازم تدفع اليوم، وبعدين أروح السوق", "I must go to the bank because the house money must be paid today, and then I go to the market", "laazim aruuH el-bank li-ann fluus el-bayt laazim tidfa3 el-yoom"),
        item("لازم تدرس أكثر لأن الامتحان قريب، ولازم تنام زين عشان تفهم أزيان", "You must study more because the exam is near, and you must sleep well in order to focus", "laazim tadrus akthar li-ann el-imtiHaan gareeb"),
        item("لازم نساعد جدتنا لأنها كبيرة في السن، ولازم نزورها كل جمعة", "We must help our grandmother because she's elderly, and we must visit her every Friday", "laazim nsaa3id jiddatna li-annaha kabeera fis-sin"),
        item("لازم يدفعون الحساب لأنهم اكلو كثير، ولازم يشكرون صاحب المطعم", "They must pay the bill because they ate a lot, and they must thank the restaurant owner", "laazim yidfa3oon el-Hisaab li-annahum akalaw katheer"),
    ]),

    lesson(22, "Lazim Ma, Because, But", "لازم ما، لأن، بس", [
        item("لازم ما تشرب قهوة كثير لأنها تخليك متوتر، بس فنجان وحد بالصبح زين", "You shouldn't drink too much coffee because it makes you nervous, but one cup in the morning is fine", "laazim ma tishrab gahwa katheer li-annaha tkhalleek mutawattir"),
        item("لازم ما تروح لوحدك بالليل لأنه مب زين، بس مع أخوك ما فيه مشكلة", "You shouldn't go alone at night because it's not safe, but with your brother there's no problem", "laazim ma truuH liwaHdak bil-layl li-annah mub zayn"),
        item("لازم ما تصرف كل فلوسك لأنك بتحتاجها بعدين، بس تشري أشياء تحتاجها زين", "You shouldn't spend all your money because you'll need it later, but buying things you need is fine", "laazim ma tisrif kil fluusak li-annak batHtaajha ba3dayn"),
        item("لازم ما تقارن نفسك بالثانيين لأن كل واحد مختلف، بس تقدر تتعلم منهم", "You shouldn't compare yourself to others because everyone is different, but you can learn from them", "laazim ma tqaarin nafsak bith-thaanyeen li-ann kil waaHid mukhtalif"),
    ]),

    lesson(23, "Knowing, Because, But", "المعرفة، لأن، بس", [
        item("أدري إنه مشغول لأنه ما رد علي، بس بيتصل فيني بعدين انشاالله", "I know he's busy because he didn't answer me, but he'll call me later God willing", "adri innah mashghool li-annah ma radd 3alay"),
        item("تدري إن الطريق طويل لأنها سافرته قبل، بس تحب السفر بالسيارة كثير", "She knows the road is long because she's traveled it before, but she loves traveling by car a lot", "tadri inn eT-Tareeg Taweel li-annaha saafarat-tah gabl"),
        item("ندري إن العرس بيكون كبير لأن العائلتين كبار، بس ما ندري بالضبط كم ضيف", "We know the wedding will be big because both families are big, but we don't know exactly how many guests", "nadri inn el-3urs baykoon kabeer li-ann el-3aa'ilatayn kubaar"),
        item("يدرون إن الشغل صعب لأنهم جربو قبل، بس يحبونه لأنه يستاهل", "They know the work is hard because they've tried before, but they love it because it's worth it", "yidroon inn esh-shughul sa3ib li-annahum jarrabaw gabl"),
    ]),

    lesson(24, "Wanting, Because, But", "الرغبة، لأن، بس", [
        item("أبغى أسافر بعيد لأني أحب أشوف أماكن جديدة، بس ما عندي وقت كافي هالسنة", "I want to travel far because I love seeing new places, but I don't have enough time this year", "abgha asaafir ba3eed li-anni aHibb ashoof amaakin jideeda"),
        item("تبغى تدرس شي ثاني لأنها ما تحب شغلها الحين، بس تخاف تبدأ من جديد", "She wants to study something else because she doesn't like her job now, but she's afraid to start over", "tibgha tadrus shay thaani li-annaha ma tHibb shughulha el-heen"),
        item("أبغى أشري بيت أكبر لأن عائلتي كبرت، بس السعر في هالحي غالي كثير", "I want to buy a bigger house because my family grew, but the price in this neighborhood is very expensive", "abgha ashri bayt akbar li-ann 3aa'ilti kubrat"),
        item("يبغى يفتح محل جديد لأنه يحب البيع والشراء، بس يحتاج فلوس أكثر أول", "He wants to open a new shop because he loves commerce, but he needs more money first", "yibgha yiftaH maHal jideed li-annah yiHibb et-tijaara"),
    ]),

    lesson(25, "Review: Lazim, Know, Want", "مراجعة", [
        item("لازم أدرس أكثر لأن الامتحان قريب، وأبغى أنجح لأني تعبت كثير هالفصل", "I must study more because the exam is near, and I want to succeed because I worked hard this semester", "laazim adrus akthar li-ann el-imtiHaan gareeb"),
        item("لازم ما تشرب قهوة كثير لأنها تخليك متوتر، وأدري إن هذا صعب عليك", "You shouldn't drink too much coffee because it makes you nervous, and I know this is hard for you", "laazim ma tishrab gahwa katheer li-annaha tkhalleek mutawattir"),
        item("أبغى أساعد جدتي لأنها كبيرة، وأعرف إنها تحتاجني كثير هالأيام", "I want to help my grandmother because she's elderly, and I know she needs me a lot these days", "abgha asaa3id jiddati li-annaha kabeera"),
        item("تبغى تسافر لأنها تحب هالشي، بس لازم تخلص شغلها أول قبل ما تروح", "She wants to travel because she loves this, but she must finish her work first before she goes", "tibgha tsaafir li-annaha tHibb hash-shay"),
    ]),

    lesson(26, "Colors and Directions, Chained", "الألوان والاتجاهات، متسلسل", [
        item("رحنا يمين لأن البيت الأحمر هناك، وبعدين رحنا يسار عشان نلقى البنك", "We went right because the red house is there, and then we went left in order to find the bank", "riHna yameen li-ann el-bayt el-a7mar hinaak"),
        item("البيت الأزرق قدام المسجد، والبيت الأخضر وراه، وبينهم بيت أصفر صغير", "The blue house is in front of the mosque, the green house is behind it, and between them is a small yellow house", "el-bayt el-azrag guddaam el-masjid"),
        item("مشيت يمين لين لقيت المحل، وشريت غترة بيضاء، وبعدين رجعت يسار للسيارة", "I walked right until I found the shop, bought a white headdress, and then went back left to the car", "misheet yameen leen ligeet el-maHal"),
        item("السيارة الحمراء قريبة من البنك، والسيارة الصفراء بعيدة شوي وراها", "The red car is near the bank, and the yellow car is a bit far behind it", "es-sayyaara el-Hamraa gareeba minal-bank"),
    ]),

    lesson(27, "A Story, Chained", "قصة، متسلسلة", [
        item("جدي كان يشتغل في الغوص أيام زمان، وكان يروح البحر شهور طويلة، وكان صعب بس زين", "My grandfather used to work in pearl diving in the old days, and he'd go to the sea for long months, and it was hard but good", "jiddi kaan yashtaghil fil-ghaws ayyaam zamaan"),
        item("خالي سافر للكويت وهو صغير، درس هناك سنين طويلة، رجع بعدها، وصار مهندس زين", "My maternal uncle traveled to Kuwait when he was young, studied there for many years, returned after, and became a good engineer", "khaali saafar lil-kuwayt wa huwa sagheer"),
        item("جدتي طبخت للعائلة كل جمعة سنين طويلة، وتعلمنا منها كل الوصفات، ولسا نطبخها لين الحين", "My grandmother cooked for the family every Friday for many years, and we learned all the recipes from her, and we still cook them until now", "jiddati Tabakhat lil-3aa'ila kil jum3a sineen Taweela"),
        item("أخوي بدأ شغل صغير، اشتغل عليه طول الوقت، وبعد سنين صار محل كبير ومشهور", "My brother started a small business, worked on it day and night, and after years it became a big and famous shop", "akhooy bida shughul sagheer, ishtaghal 3alayh layl wa nahaar"),
    ]),

    lesson(28, "Money, Chained", "الفلوس، متسلسل", [
        item("وفرت فلوس كثير سنتين، شريت بيها بيت صغير، وصار عندي بيت ثاني أخيرا", "I saved a lot of money for two years, bought a small house with it, and finally I had a second house", "waffart fluus katheer santeen, sharayt beeha bayt sagheer"),
        item("اشتغل شغلين عشان يوفر فلوس أكثر، وبعد سنة قدر يشري سيارة جديدة", "He worked two jobs in order to save more money, and after a year he was able to buy a new car", "ishtaghal shughlayn 3ashaan ywaffir fluus akthar"),
        item("دفعنا نص الفلوس أول، وبعدين دفعنا النص الثاني بعد شهرين، وخلصنا كل شي", "We paid half the money first, then we paid the other half after two months, and we finished everything", "dafa3na nus el-fluus awwal, wa ba3dayn dafa3na en-nus eth-thaani ba3d shahrayn"),
        item("صرفت فلوس كثير على السفر، فقررت أوفر أكثر، وبعد كذا رجعت أسافر مرة ثانية", "I spent a lot of money on travel, so I decided to save more, and after that I traveled again", "sarafat fluus katheer 3ales-safar, fa-garrarat twaffir akthar"),
    ]),

    lesson(29, "Feelings, Chained", "المشاعر، متسلسل", [
        item("كنت متوتر قبل الامتحان، بس درست زين، وفهمت كل شي، ونجحت أخيرا والحمد لله", "I was nervous before the exam, but I studied well, understood everything, and finally succeeded, thank God", "kint mutawattir gabl el-imtiHaan, bas darast zayn"),
        item("كانت قلقانة على ابنها أول، بس اتصل فيها وقال إنه زين، فارتاحت كثير", "She was worried about her son at first, but he called her and said he's fine, so she relaxed a lot", "kaanat galgaana 3ala waladha awwal"),
        item("كنا متضايقين من الشغل الكثير، بس اخذنا إجازة، ورجعنا نشتغل مبسوطين أكثر", "We were upset about the excessive work, but we took a vacation, and we returned to work happier", "kinna mutadaayigeen minesh-shughul el-katheer"),
        item("كان زعلان من صاحبه أول، بس تكلمو مع بعض، وفهمو بعض، وصارو أصحاب زين مرة ثانية", "He was upset with his friend at first, but they talked to each other, understood each other, and became good friends again", "kaan za3laan min saaHbah awwal"),
    ]),

    lesson(30, "Review: C1 Final Recap", "مراجعة نهائية", [
        item("جدي اشتغل في الغوص أيام زمان، وتعبت العائلة بس ما زعلو، وصار عندنا بيت زين أخيرا", "My grandfather worked in pearl diving in the old days, and the family struggled but was patient, and we finally got a good house", "jiddi ishtaghal fil-ghaws ayyaam zamaan"),
        item("وفرنا فلوس سنين طويلة، وشرينا بيت أكبر، وصرنا نقعد فيه مع كل العائلة كل جمعة", "We saved money for many years, bought a bigger house, and we sit in it with the whole family every Friday", "waffarna fluus sineen Taweela, wa sharayna bayt akbar"),
        item("كنت متوتر من الشغل الجديد أول، بس تعلمت زين، وصرت أحبه كثير الحين", "I was nervous about the new job at first, but I learned well, and now I love it a lot", "kint mutawattir minesh-shughul el-jideed awwal"),
        item("رحنا يمين وبعدين يسار، ولقينا البيت الأخضر أخيرا، وكان يستاهل كل هالتعب", "We went right and then left, and finally found the green house, and it was worth all this effort", "riHna yameen wa ba3dayn yasaar, wa ligeena el-bayt el-akhdar akheeran"),
    ]),

    lesson(31, "Professions, Chained", "المهن، متسلسل", [
        item("المهندسة درست سنين طويلة، اشتغلت في مكاتب كثير، وأخيرا فتحت مكتبها الخاص", "The engineer studied for many years, worked at a lot of offices, and finally opened her own office", "el-muhandisa darasat sineen Taweela"),
        item("المترجم تعلم لغتين وهو صغير، اشتغل مع شركات كثير، وصار مترجم زين كثير", "The translator learned two languages when he was young, worked with a lot of companies, and became one of the best translators", "el-mutarjim ta3allam lughtayn wa huwa sagheer"),
        item("التاجر بدأ محل صغير، اشتغل عليه كثير، وبعد سنين صار عنده محلات كثير", "The merchant started a small shop, worked on it hard, and after years he had a lot of shops", "et-taajir bida maHal sagheer, ishtaghal 3alayh biguwwa"),
        item("المدرس درّس سنين طويلة في نفس المدرسة، وحب كل طلابه، وهم لسا يزورونه لين الحين", "The teacher taught for many years at the same school, loved all his students, and they still visit him until now", "el-mudarris darras sineen Taweela fi nafs el-madrasa"),
    ]),

    lesson(32, "At the Hospital, Chained", "في المستشفى، متسلسل", [
        item("جدي راح المستشفى لأن ظهره يوجعه، شافه الطبيب، وعطاه دوا، ورجع البيت وارتاح", "My grandfather went to the hospital because his back hurts him, the doctor saw him, gave him medicine, and he returned home relaxed", "jiddi raaH el-mustashfa li-ann dhahrah yoowja3ah"),
        item("زرنا خالتي في المستشفى، شفناها تتكلم وتضحك، وفهمنا إن الوضع تحسن كثير", "We visited my maternal aunt in the hospital, saw her talking and doing well, and understood the situation improved a lot", "zirna khaalti fil-mustashfa"),
        item("قعدت مع أخوي في المستشفى طول الليل، وصحينا الصبح، وشفنا الطبيبة تقول إنه بيتحسن قريب", "I sat with my brother in the hospital all night, we woke up in the morning, and saw the doctor say he'll recover soon", "ga3adt ma3 akhooy fil-mustashfa Tool el-layl"),
        item("رحت الطبيب، شافني، وقال لازم أرتاح، فرجعت البيت وقعدت أسبوع كامل بدون شغل", "I went to the doctor, he examined me, and said I must rest, so I returned home and stayed a whole week without work", "riHt eT-Tabeeb, shaafni, wa gaal laazim artaaH"),
    ]),

    lesson(33, "Train Rides, Chained", "رحلات القطار، متسلسل", [
        item("رحنا القطار بدري، سافرنا فيه، وصلنا بعد ساعة، وطلعنا للسوق مباشرة", "We went to the train early, traveled on it, arrived after an hour, and went to the market directly", "riHna el-gitaar badri, saafarna feeh"),
        item("سافرت بالقطار للكويت، شفت أماكن جديدة كثير، وقعدت أفكر طول الطريق", "I traveled by train to Kuwait, saw a lot of new places, and sat thinking the whole way", "saafart bil-gitaar lil-kuwayt, shift amaakin jideeda katheer"),
        item("القطار أسرع من الباص، بس الباص أرخص، فقررنا نروح بالقطار ونرجع بالباص", "The train is faster than the bus, but the bus is cheaper, so we decided to go by train and return by bus", "el-gitaar asra3 minal-baas, bas el-baas arkhas"),
        item("وصل القطار متأخر، فانتظرنا ساعة كاملة، وبعدين ركبنا وصلنا زين أخيرا", "The train arrived late, so we waited a whole hour, and then we boarded and finally arrived well", "wisal el-gitaar mit'akhkhir, fa-intadharna saa3a kaamila"),
    ]),

    lesson(34, "Clothes, Chained", "الملابس، متسلسل", [
        item("رحت السوق، شفت قميص أزرق زين، جربته، وناسبني كثير، فشريته مباشرة", "I went to the market, saw a nice blue shirt, tried it on, and it suited me a lot, so I bought it directly", "riHt es-suug, shift gamees azrag zayn"),
        item("شرت عباية جديدة للعرس، وغترة بيضاء تناسبها، وجوتي أسود يناسبها زين", "She bought a new abaya for the wedding, a white headdress that matches it, and black shoes that complete the look", "sharat 3abaaya jideeda lil-3urs"),
        item("لبسنا ملابس دافية لأن الجو بارد، وطلعنا نمشي، وحسينا بالزين طول الوقت", "We wore warm clothes because the weather is cold, went out to walk, and felt comfortable the whole time", "libasna malaabis daafya li-ann el-jaww baarid"),
        item("غسلت القميص الوسخ، نظفته زين، وبعدين لبسته للاجتماع المهم", "I washed the dirty shirt, cleaned it well, and after it dried I wore it to the important meeting", "ghasalt el-gamees el-wisikh, nadhdhaftah zayn"),
    ]),

    lesson(35, "Clothes, Chained II", "الملابس، متسلسل ٢", [
        item("جربت قميص أحمر وقميص أصفر، بس اخترت الأزرق لأنه ناسبني أكثر", "I tried a red shirt and a yellow shirt, but I chose the blue one because it suited me more", "jarrabt gamees aHmar wa gamees asfar, bas ikhtart el-azrag"),
        item("شرينا جوتي جديد لكل الأولاد قبل العيد، وكانو مبسوطين كثير فيه", "We bought new shoes for all the children before Eid, and they were very happy with them", "sharayna jooti jideed likil el-awlaad gabl el-3eed"),
        item("لبست غترة جديدة اليوم لأن القديمة صارت وسخة، وحسيت إني أنيق كثير", "I wore a new headdress today because the old one became dirty, and I felt very elegant", "libast ghitra jideeda el-yoom li-ann el-gadeema saarat wisikha"),
        item("قارنت الأسعار بمحلات كثير، ولقيت غترة زينة بسعر مناسب، فشريتها بسرعة", "I compared prices at a lot of shops, found a nice headdress at a suitable price, and bought it quickly", "qaarant el-as3aar bima7allaat katheer, wa ligeet ghitra zeena bisi3ir munaasib"),
    ]),

    lesson(36, "Food, Chained", "الأكل، متسلسل", [
        item("طبخت لحم وسلطة وأرز للضيوف، وحطيت تمر وقهوة بعدها، وكل واحد أكل كثير", "I cooked meat, salad, and rice for the guests, put out dates and coffee after, and everyone ate a lot", "Tabakht la7am wa salata wa aruz lidh-dhuyoof"),
        item("جربنا مطعم جديد، طلبنا أكل خليجي، وكان لذيذ كثير، فقررنا نرجع له مرة ثانية", "We tried a new restaurant, ordered Khaleeji food, and it was very delicious, so we decided to go back again", "jarrabna mat3am jideed, Talabna akal khaleeji"),
        item("سوت جدتي أكل زين كل جمعة، وكل العائلة تجي تاكل معها، ويقعدون يتكلمون طويل", "My grandmother makes good food every Friday, and the whole family comes to eat with her, and they sit talking for a long time", "sawwat jiddati akal zayn kil jum3a"),
        item("شرينا تمر كثير للعيد، وحطينا شوي في كل صحن، وعطيناه للضيوف مع القهوة", "We bought a lot of dates for Eid, put some in each plate, and served it to the guests with coffee", "sharayna tamur katheer lil-3eed, wa HaTTayna shway fi kil saHan"),
    ]),

    lesson(37, "Food, Chained II", "الأكل، متسلسل ٢", [
        item("طلبنا لحم وسمك وسلطة، وأكلنا كل شي، وشربنا قهوة بعدها، وكان يوم زين", "We ordered meat, fish, and salad, ate everything, drank coffee after, and it was a good day", "Talabna la7am wa samak wa salata"),
        item("جربت أكل جديد اليوم، ما عرفته أول، بس أكلته وحبيته كثير", "I tried new food today, I didn't know it at first, but I ate it and loved it a lot", "jarrabt akal jideed el-yoom, ma 3iraftah awwal"),
        item("طبخنا للأهل كلهم، وأكل الكل كثير، وقعدنا نشرب قهوة ونتكلم لين المغرب", "We cooked for the whole family, everyone ate until they were full, and we sat drinking coffee and talking until sunset", "Tabakhna lil-ahl killahum"),
        item("شريت لحم وسلطة من السوق، طبخت أكل زين، والعائلة كلها اكلت وكانت مبسوطة", "I bought meat and salad from the market, cooked good food, and the whole family ate and was happy", "sharayt la7am wa salata mines-suug"),
    ]),

    lesson(38, "Why I Love It", "ليش أحبه", [
        item("أحب المجلس لأن فيه أصحابي، ونتكلم ونضحك، وأحس زين كل ما أروح له", "I love the majlis because my friends are there, we talk and laugh, and I feel relaxed every time I go there", "aHibb el-majlis li-ann feeh as7aabi"),
        item("أحب هالبيت لأني كبرت فيه، وأحبه من زمان، وأهلي كلهم يحبونه مثلي", "I love this house because it has a lot of memories, I grew up in it, and my whole family loves it like me", "aHibb hal-bayt li-annah feeh dhikrayaat katheer"),
        item("تحب شغلها لأنها تساعد ناس كثير، وتصير فخورة كل ما تخلص مشروع", "She loves her job because she helps a lot of people, and she feels proud every time she finishes a project", "tHibb shughulha li-annaha tsaa3id naas katheer"),
        item("نحب السفر لأننا نشوف أماكن جديدة، ونتعلم أشياء كثير، ونرجع مبسوطين كثير", "We love traveling because we see new places, learn a lot of things, and return with good memories", "niHibb es-safar li-annana nshoof amaakin jideeda"),
    ]),

    lesson(39, "Weather, Chained", "الجو، متسلسل", [
        item("الجو حار كثير هالأيام، فنقعد بالبيت أكثر، ونشرب مويه بارده طول الوقت", "The weather is very hot these days, so we stay home more, and drink cold water all the time", "el-jaww Haarr katheer hal-ayyaam, fa-nag3ad bil-bayt akthar"),
        item("كان الجو غائم الصبح، بس صار صافي بعد الظهر، فطلعنا نمشي شوي", "The weather was cloudy in the morning, but it became clear after noon, so we went out to walk a bit", "kaan el-jaww ghaayim es-sub7, bas saar saafi ba3d edh-dhuhur"),
        item("فيه ريح ورطوبة اليوم، فحسينا بتعب أكثر من العادي، وقعدنا نرتاح كثير", "There's wind and humidity today, so we felt more tired than usual, and we sat resting a lot", "feeh reeH wa rutuuba el-yoom"),
        item("الشتاء بارد هذي السنة أكثر من كل سنة، فلبسنا ملابس دافية كثير", "Winter is colder this year than usual, so we wore a lot of warm clothes", "esh-shita baarid haadhi es-sana akthar minal-3aada"),
    ]),

    lesson(40, "Body Parts, Because", "أجزاء الجسم، لأن", [
        item("راسي يوجعني لأني ما نمت زين أمس، فقررت أنام بدري الليلة", "My head hurts because I didn't sleep well yesterday, so I decided to sleep early tonight", "raasi yoowja3ni li-anni ma nimt zayn ams"),
        item("ظهرها يوجعها لأنها تشتغل طول اليوم بدون قعدة، فلازم ترتاح أكثر", "Her back hurts because she works standing all day, so she must rest more", "dhahrha yoowja3ha li-annaha tashtaghil Tool el-yoom waagfa"),
        item("ركبته توجعه لأنه يمشي كثير كل يوم، بس الطبيب قال هذا زين لصحته", "His knee hurts because he walks a lot every day, but the doctor said this is good for his health", "rukbatah toowja3ah li-annah yimshi katheer kil yoom"),
        item("عيني تعبانة لأني قعدت أدرس طول الليل، فلازم أرتاحها شوي بكرا", "My eye is tired because I sat studying all night, so I must rest it a bit tomorrow", "3ayni ta3baana li-anni ga3adt adrus Tool el-layl"),
    ]),

    lesson(41, "Weather, Chained II", "الجو، متسلسل ٢", [
        item("الجو مشمس اليوم، فقررنا نطلع نمشي في الصحراء ونشوف الجمال هناك", "The weather is sunny today, so we decided to go out and walk in the desert and see the camels there", "el-jaww mishmis el-yoom, fa-garrarna nTla3 nimshi fis-sa7raa"),
        item("صارت عاصفة قوية بالليل، فقعدنا بالبيت، وشربنا شاي وقهوة كثير", "A strong storm happened at night, so we stayed home, and drank tea and coffee until it ended", "saarat 3aasifa gawiyya bil-layl, fa-ga3adna bil-bayt"),
        item("الرطوبة عالية كثير في الصيف عندنا، فنحب نقعد بالبيت أكثر من السوق", "The humidity is very high in the summer for us, so we love staying home more than the market", "er-rutuuba 3aalya katheer fis-sayf 3indana"),
        item("كان الجو بارد ومطير أمس، بس اليوم صار صافي وحلو، فطلعنا نمشي ونحس بالجو الزين", "The weather was cold and rainy yesterday, but today it became clear and nice, so we went out to enjoy the weather", "kaan el-jaww baarid wa maTeer ams, bas el-yoom saar saafi wa Hilu"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/c1.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "c1", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/c1.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
