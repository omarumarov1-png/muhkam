#!/usr/bin/env python3
"""Full rewrite of C2 Khaleeji Arabic content -- the densest chained
sentences (4+ clauses), same repetition fix, mastery register. Written
very conservatively against the now-huge confirmed vocabulary built up
across A1 through C1, reusing constructions already validated there.
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
    lesson(1, "Going Home, Dense Chain", "الرواح البيت، متسلسل كثيف", [
        item("رحت البيت بدري لأني كنت تعبان، وقعدت أرتاح، وشربت شاي، وبعدين نمت زين", "I went home early because I was tired, sat resting, drank tea, and then slept well", "riHt el-bayt badri li-anni kint ta3baan"),
        item("راح جدي المجلس لأنه يحب أصحابه، وقعد يشرب قهوة، وحكى قصص، وضحك كثير معهم", "My grandfather went to the majlis because he loves his friends, sat drinking coffee, told stories, and laughed a lot with them", "raaH jiddi el-majlis li-annah yiHibb as7aabah"),
        item("رحنا السوق لأن أختي تبغى غترة، وشفنا محلات كثير، وشرينا لها وحدة زينة، ورجعنا مبسوطين", "We went to the market because my sister wants a headdress, saw a lot of shops, bought her a nice one, and returned happy", "riHna es-suug li-ann ukhti tibgha ghitra"),
        item("راحو المطار لأن جدهم راجع، ووصلو بدري، وانتظرو ساعة، وشافوه أخيرا وكانو مبسوطين كثير", "They went to the airport because their grandfather is returning, arrived early, waited an hour, and finally saw him and were very happy", "raaHaw el-mataar li-ann jiddahum raaji3"),
    ], topicId="c2-chain"),

    lesson(2, "Drinking, Dense Chain", "الشرب، متسلسل كثيف", [
        item("أشرب قهوة كل صباح لأني أحبها، وأشرب شاي بعد العصر، وأشرب مويه طول اليوم", "I drink coffee every morning because I love it, drink tea after the afternoon, and drink water all day", "ashrab gahwa kil sabaaH li-anni aHibbha"),
        item("تشرب مويه بارده بعد الرياضة لأن جسمها يحتاجها، وترتاح، وبعدين تشرب قهوة زينة", "She drinks cold water after exercise because her body needs it, rests, and then drinks good coffee", "tishrab moya baarda ba3d er-riyaada"),
        item("نشرب قهوة في المجلس كل جمعة، ونتكلم عن أخبار الأسبوع، ونضحك، ونحس بالراحة كثير", "We drink coffee in the majlis every Friday, talk about the week's news, laugh, and feel very relaxed", "nishrab gahwa fil-majlis kil jum3a"),
        item("يشربون شاي بالحليب لأنهم يحبونه، وياكلون تمر معه، ويقعدون يتكلمون لين المغرب", "They drink tea with milk because they love it, eat dates with it, and sit talking until sunset", "yishrabuun shaay bil-Haleeb li-annahum yiHibboonah"),
    ]),

    lesson(3, "Wanting, Dense Chain", "الرغبة، متسلسل كثيف", [
        item("أبغى بيت أكبر لأن عائلتي كبرت، وأبغى غرف أكثر، وأبغى مطبخ كبير، وأبغى موقع قريب من الشغل", "I want a bigger house because my family grew, want more rooms, want a big kitchen, and want a location near work", "abgha bayt akbar li-ann 3aa'ilti kubrat"),
        item("تبغى تدرس في جامعة زينة، وتبغى تصير مهندسة، وتبغى تساعد ناس كثير، وتبغى تفتح مكتبها الخاص", "She wants to study at a good university, wants to become an engineer, wants to help a lot of people, and wants to open her own office", "tibgha tadrus fi jaami3a zeena"),
        item("أبغى أسافر للكويت، وأبغى أزور أهلي هناك، وأبغى أشوف أماكن جديدة، وأبغى أرجع قبل العيد", "I want to travel to Kuwait, want to visit my family there, want to see new places, and want to return before Eid", "abgha asaafir lil-kuwayt"),
        item("يبغى يشتغل في مكتب كبير، ويبغى راتب زين، ويبغى يتعلم أشياء جديدة، ويبغى يصير صاحب مكتبه الخاص", "He wants to work in a big office, wants a good salary, wants to learn new things, and wants to become the owner of his own office", "yibgha yashtaghil fi maktab kabeer"),
    ]),

    lesson(4, "Knowing, Dense Chain", "المعرفة، متسلسل كثيف", [
        item("أدري وين البيت لأني رحت له قبل، وأدري الطريق زين، وأدري إنه بعيد شوي، وأدري متى نوصل", "I know where the house is because I went there before, know the way well, know it's a bit far, and know when we'll arrive", "adri wein el-bayt li-anni riHt lah gabl"),
        item("تدري السعر الصح لأنها سألت في محلات كثير، وتدري وين أرخص شي، وتدري متى الأسعار أرخص", "She knows the right price because she asked at a lot of shops, knows where the cheapest thing is, and knows when prices are cheapest", "tadri es-si3ir es-saHH li-annaha sa'alat fi ma7allaat katheer"),
        item("ندري متى العرس، وندري وين بالضبط، وندري عدد الضيوف، وندري شنو نلبس", "We know when the wedding is, know exactly where, know the number of guests, and know what to wear", "nadri mita el-3urs, wa nadri wein biD-Dabt"),
        item("يدرون كل شي عن السفر لأنهم سافرو قبل، ويدرون شنو يحتاجون، ويدرون وين يروحون، ويدرون كم يصرفون", "They know everything about the trip because they've traveled before, know what they need, know where to go, and know how much they'll spend", "yidroon kil shay 3anis-safar li-annahum saafaraw gabl"),
    ]),

    lesson(5, "Review: Dense Chains", "مراجعة: المتسلسلات الكثيفة", [
        item("رحت السوق لأني أبغى غترة، وشفت محلات كثير، وشريت وحدة زينة، ورجعت مبسوط", "I went to the market because I want a headdress, saw a lot of shops, bought a nice one, and returned happy", "riHt es-suug li-anni abgha ghitra"),
        item("تشرب قهوة كل يوم، بس ما تشربها بالليل، وتشرب شاي بدل، عشان تنام زين وترتاح", "She drinks coffee every day, but doesn't drink it at night, and drinks tea instead, in order to sleep well and rest", "tishrab gahwa kil yoom, bas ma tishrabha bil-layl"),
        item("ندري وين المسجد، وندري متى الصلاة، وندري منو يروح معنا، وندري شلون نوصل بسرعة", "We know where the mosque is, know when the prayer is, know who's going with us, and know how to arrive quickly", "nadri wein el-masjid, wa nadri mita es-salaa"),
        item("كل واحد فيهم يبغى يسافر هالصيف لأنه تعب، ويبغى يرتاح، ويبغى يشوف أماكن جديدة، ويبغى يرجع مبسوط", "Each one of them wants to travel this summer because he got tired, wants to relax, wants to see new places, and wants to return happy", "kil waaHid feehum yibgha ysaafir has-sayf li-annah ti3ab"),
    ]),

    lesson(6, "Not Going, Dense Chain", "عدم الرواح، متسلسل كثيف", [
        item("ما رحت الشغل أمس لأني كنت مريض، بس اليوم أنا زين، ورجعت الشغل، وخلصت كل شي بسرعة", "I didn't go to work yesterday because I was sick, but today I'm well, returned to work, and finished everything quickly", "ma riHt esh-shaghal ams li-anni kint mareed"),
        item("ما راحت العرس لأن عندها امتحان، بس اتصلت فيهم، وقالت مبروك، وقالت بتزورهم بعدين", "She didn't go to the wedding because she has an exam, but she called them, said congratulations, and said she'll visit them later", "ma raaHat el-3urs li-ann 3indaha imtiHaan"),
        item("ما رحنا المطعم الجديد لأنه غالي، بس سمعنا إنه لذيذ، وقررنا نروح له مرة ثانية، ونجرب الأكل هناك", "We didn't go to the new restaurant because it's expensive, but we heard it's delicious, decided to go again, and try the food there", "ma riHna el-mat3am el-jideed li-annah ghaali"),
        item("ما راحو المسجد يوم الجمعة لأنهم كانو في السفر، بس صلو بالبيت، وقرو، وفكرو بالأهل هناك", "They didn't go to the mosque on Friday because they were traveling, but they prayed at home, read, and thought about the family there", "ma raaHaw el-masjid yoom el-jum3a li-annahum kaanaw fis-safar"),
    ]),

    lesson(7, "Not Wanting, Dense Chain", "عدم الرغبة، متسلسل كثيف", [
        item("ما أبغى أشتغل بعيد عن البيت لأن السفر يتعبني، بس ما عندي شغل ثاني، فلازم أشتغل فيه بالصبر", "I don't want to work far from home because the commute tires me, but I have no other job, so I must work at it with patience", "ma abgha ashtaghil ba3eed 3anil-bayt li-ann es-safar yta3ibni"),
        item("ما تبغى تسافر لوحدها لأنها ما تعرف اللغة، بس أختها بتروح معها، وبتساعدها، وبتحس بأمان أكثر", "She doesn't want to travel alone because she doesn't know the language, but her sister will go with her, help her, and she'll feel safer", "ma tibgha tsaafir liwaHdaha li-annaha ma ta3rif el-lugha"),
        item("ما أبغى أشري البيت الغالي لأن ما عندي فلوس كافية، بس أوفر كل شهر، وبعد سنين بقدر أشريه", "I don't want to buy the expensive house because I don't have enough money, but I save every month, and after years I'll be able to buy it", "ma abgha ashri el-bayt el-ghaali li-ann ma 3indi fluus kaafya"),
        item("ما يبغى يروح المستشفى لأنه ما يحبها، بس لازم يروح، وشافه الطبيب، وعطاه دوا، ورجع زين", "He doesn't want to go to the hospital because he doesn't like it, but he must go, the doctor saw him, gave him medicine, and he returned well", "ma yibgha yruuH el-mustashfa li-annah ma yiHibbha"),
    ]),

    lesson(8, "Health, Dense Chain", "الصحة، متسلسل كثيف", [
        item("رحت الطبيب لأن راسي كان يوجعني، وشافني، وقال لازم أرتاح، واخذت الدوا، والحمد لله صرت أزيان", "I went to the doctor because my head was hurting, he examined me, said I must rest, I took the medicine, and thank God I got better", "riHt eT-Tabeeb li-ann raasi kaan yoowja3ni"),
        item("أحس بتحسن لأني اخذت الدوا، ونمت زين، وشربت مويه كثير، وارتحت يومين كاملين", "I feel better because I took the medicine, slept well, drank a lot of water, and rested two whole days", "aHiss bitaHassun li-anni akhadht ed-dawa"),
        item("لازم أرتاح كامل أسبوع لأن الطبيبة قالت كذا، بس عندي شغل كثير، فقررت أرتاح ثلاثة أيام بس", "I must rest a whole week because the doctor said so, but I have a lot of work, so I decided to rest just three days", "laazim artaaH kaamil isboo3 li-anniT-Tabeeba gaalat kadha"),
        item("جدي في المستشفى لأن ظهره يوجعه من زمان، بس يتكلم، ويضحك، وياكل زين، والحمد لله الوضع تحسن كثير", "My grandfather is in the hospital because his back has hurt for a long time, but he talks, laughs, eats well, and thank God the situation improved a lot", "jiddi fil-mustashfa li-ann dhahrah yoowja3ah min zamaan"),
    ]),

    lesson(9, "Family, Dense Chain", "العائلة، متسلسل كثيف", [
        item("جدي يحب المجلس لأنه يقعد فيه مع أصحابه، ويحكي لهم قصص عن زمان، ويشرب قهوة، ويحس بالراحة", "My grandfather loves the majlis because he sits there with his friends, tells them stories from the old days, drinks coffee, and feels relaxed", "jiddi yiHibb el-majlis li-annah yig3ad feeh ma3 as7aabah"),
        item("خالتي تحب السفر لأنها تحب تشوف أماكن جديدة، وتحب تجرب أكل جديد، وتحب تتعلم أشياء، وترجع مبسوطة", "My maternal aunt loves traveling because she loves seeing new places, loves trying new food, loves learning things, and returns happy", "khaalti tHibb es-safar li-annaha tHibb tshoof amaakin jideeda"),
        item("أخوي يحب شغله لأنه يساعد ناس كثير، ويحس إنه يسوي شي مهم، ويتعلم كل يوم، ويحب أصحابه بالشغل", "My brother loves his job because he helps a lot of people, feels he's doing something important, learns every day, and loves his work friends", "akhooy yiHibb shughlah li-annah ysaa3id naas katheer"),
        item("أختي تحب أولادها كثير، فتقعد وياهم كل ما تقدر، وتساعدهم بدروسهم، وتطبخ لهم أكل يحبونه", "My sister loves her children a lot, so she sits with them whenever she can, helps them with their lessons, and cooks food they love", "ukhti tHibb awlaadha katheer, fa-tag3ad wiyaahum kil ma tigdar"),
    ]),

    lesson(10, "Review: C2 Recap", "مراجعة", [
        item("جدي يحب المجلس، ويقعد مع أصحابه، ويحكي قصص، ويشرب قهوة، وأنا أحب أسمعه كثير", "My grandfather loves the majlis, sits with his friends, tells stories, drinks coffee, and I love listening to him a lot", "jiddi yiHibb el-majlis, wa yig3ad ma3 as7aabah, wa yiHki gisas"),
        item("ما رحنا العرس لأن عندنا شغل، بس اتصلنا فيهم، وقلنا مبروك، وقررنا نزورهم الجمعة الجاية", "We didn't go to the wedding because we had work, but we called them, said congratulations, and decided to visit them next Friday", "ma riHna el-3urs li-ann 3indana shughul"),
        item("ما عندي فلوس كافية للسفر، فقررت أوفر أكثر، وأشتغل شغلين، وأسافر السنة الجاية بفلوس أكثر", "I don't have enough money to travel, so I decided to save more, work two jobs, and travel next year with more money", "ma 3indi fluus kaafya lis-safar, fa-garrart awaffir akthar"),
        item("أختي تحب أولادها، وتساعدهم، وتطبخ لهم، وتحس إنهم أهم شي في حياتها", "My sister loves her children, helps them, cooks for them, and feels they're the most important thing in her life", "ukhti tHibb awlaadha, wa tsaa3idhum, wa taTbakh lahum"),
    ]),

    lesson(11, "Places, Dense Chain", "الأماكن، متسلسل كثيف", [
        item("رحنا المطعم القريب لأنه سريع، بس الأكل مب لذيذ، فقررنا ما نرجع له مرة ثانية أبدا", "We went to the nearby restaurant because it's fast, but the food isn't delicious, so we decided never to return there", "riHna el-mat3am el-gareeb li-annah saree3"),
        item("البيت قريب من الشغل لأننا اخترناه بسبب هذا، وناسبنا زين، بس السعر كان غالي شوي أول", "The house is near work because we chose it for this reason, it suited us well, but the price was a bit expensive at first", "el-bayt gareeb minesh-shughul li-annana ikhtarnaah bisabab haadha"),
        item("المسجد قريب من بيتنا لأنه في نفس الحي، فنروح له كل صلاة، ونشوف جيراننا هناك، ونتكلم شوي", "The mosque is near our house because it's in the same neighborhood, so we go there every prayer, see our neighbors there, and talk a bit", "el-masjid gareeb min baytna li-annah fi nafs el-Hayy"),
        item("السوق بعيد عن بيتنا لأننا سكنا هنا جديد، بس البنك قريب زين، والمستشفى قريبة كمان، ونحس بالراحة من هذا", "The market is far from our house because we moved here recently, but the bank is quite near, the hospital is also near, and we feel comforted by this", "es-suug ba3eed 3an baytna li-annana sakanna hina jideed"),
    ]),

    lesson(12, "Colors, Dense Chain", "الألوان، متسلسل كثيف", [
        item("أبغى هذا البيت الأحمر لأنه قريب من المدرسة، وفيه غرف كثير، وأحب لونه، وسعره مناسب", "I want this red house because it's near the school, has a lot of rooms, I love its color, and its price is suitable", "abgha haadha el-bayt el-a7mar li-annah gareeb minal-madrasa"),
        item("شريت السيارة الزرقاء لأنها كانت أرخص من الحمراء، وناسبت فلوسي، وحبيت لونها، وهي سريعة زين", "I bought the blue car because it was cheaper than the red one, suited my money, I loved its color, and it's quite fast", "sharayt es-sayyaara ez-zarqaa li-annaha kaanat arkhas minal-Hamraa"),
        item("لبست القميص الأخضر لأنه يناسب البنطلون، ولأني أحب هاللون، ولأن أختي قالت زين، فلبسته بسرعة", "I wore the green shirt because it matches the pants, because I love this color, and because my sister said it's good, so I wore it quickly", "libast el-gamees el-akhdar li-annah ynaasib el-bantaloon"),
        item("اخترنا الغترة البيضاء لأنها تناسب العباية السوداء، وكانت زينة، ورخيصة، وناسبت العرس زين", "We chose the white headdress because it matches the black abaya, was nice, cheap, and suited the wedding well", "ikhtarna el-ghitra el-baydaa li-annaha tnaasib el-3abaaya es-sawdaa"),
    ]),

    lesson(13, "Days, Dense Chain", "الأيام، متسلسل كثيف", [
        item("يوم الجمعة زين لأننا نقعد مع الأهل، ونشرب قهوة، ونتكلم، ونضحك، ونحس بالراحة كثير", "Friday is good because we sit with the family, drink coffee, talk, laugh, and feel very relaxed", "yoom el-jum3a zayn li-annana nag3ad ma3al-ahl"),
        item("يوم السبت أروح الشغل، وأشتغل لين العصر، وأرجع البيت، وأرتاح، وأقرى شوي قبل ما أنام", "Saturday I go to work, work until afternoon, return home, rest, and read a bit before sleeping", "yoom es-sabt aruuH esh-shaghal, wa ashtaghil leen el-3asir"),
        item("الأسبوع الماضي كان صعب لأن عندنا شغل كثير، بس هالأسبوع أسهل، وقدرنا نرتاح، ونزور الأهل", "Last week was difficult because we had a lot of work, but this week is easier, we were able to rest, and visit the family", "el-isboo3 el-maadi kaan sa3ib li-ann 3indana shughul katheer"),
        item("الشهر الجاي عندنا عرس لأن ابن عمي بيتزوج، وكل العائلة بتجي، وبنطبخ كثير، وبنقعد كلنا مبسوطين", "Next month we have a wedding because my paternal cousin is getting married, the whole family will come, we'll cook a lot, and we'll all sit happily", "esh-shahar el-jaay 3indana 3urs li-ann ibin 3ammi baytizawwaj"),
    ]),

    lesson(14, "Feelings, Dense Chain", "المشاعر، متسلسل كثيف", [
        item("أنا مبسوط لأن أخوي راجع، بس تعبان شوي من الشغل الكثير، فقررت أرتاح اليوم كامل وأنام بدري", "I'm happy because my brother is back, but a bit tired from too much work, so I decided to rest all day today and sleep early", "ana mabsoot li-ann akhooy raaji3"),
        item("هي قلقانة على الامتحان لأنها ما درست كافي، بس تفكر تدرس طول الليلة، وتشرب قهوة، وتفهم كل شي", "She's worried about the exam because she didn't study enough, but she's thinking of studying all night, drinking coffee, and understanding everything", "hiya galgaana 3alal-imtiHaan li-annaha ma darasat kaafi"),
        item("احنا فخورين بجدنا لأنه سوى كل هالشي بنفسه، وما يحب الكلام عن هذا، بس احنا نعرف تعبه زين", "We're proud of our grandfather because he did all this himself, doesn't like talking about it, but we know his effort well", "iHna fakhooreen bijiddana li-annah sawa kil hash-shay binafsah"),
        item("هم متضايقين من الجو لأنه حار كثير، بس ما يقدرون يسوون شي، فيقعدون بالبيت، ويشربون مويه بارده", "They're upset about the weather because it's very hot, but they can't do anything, so they stay home and drink cold water", "hum mutadaayigeen minal-jaww li-annah Haarr katheer"),
    ]),

    lesson(15, "Review: Places, Colors, Days, Feelings", "مراجعة", [
        item("رحنا المجلس القريب يوم الجمعة، وشربنا قهوة، وتكلمنا، وضحكنا، وحسينا بالراحة والمحبة", "We went to the nearby majlis on Friday, drank coffee, talked, laughed, and felt relaxed and loved", "riHna el-majlis el-gareeb yoom el-jum3a"),
        item("شريت البيت الأخضر لأنه قريب من الشغل، بس السعر كان غالي شوي، فوفرت أكثر، وأخيرا دفعت كل شي", "I bought the green house because it's near work, but the price was a bit expensive, so I saved more, and finally paid for everything", "sharayt el-bayt el-akhdar li-annah gareeb minesh-shughul"),
        item("أنا مبسوط اليوم لأن الجو زين، والشغل خلص بدري، فقررت أزور جدي، ونشرب قهوة، ونتكلم كثير", "I'm happy today because the weather is nice, work finished early, so I decided to visit my grandfather, drink coffee, and talk a lot", "ana mabsoot el-yoom li-ann el-jaww zayn"),
        item("هي قلقانة على الشهر الجاي لأن عندها امتحانات كثير، بس تدرس كل يوم، وتفهم زين، وبتنجح انشاالله", "She's worried about next month because she has a lot of exams, but she studies every day, understands well, and will succeed God willing", "hiya galgaana 3alash-shahar el-jaay li-ann 3indaha imtiHaanaat katheer"),
    ]),

    lesson(16, "Numbers, Dense Chain", "الأرقام، متسلسل كثيف", [
        item("درست ستين صفحة لأن الامتحان صعب، وبقت أربعين بس، وقررت أدرسها الليلة، وأنام بدري بعدها", "I studied sixty pages because the exam is hard, only forty remained, and I decided to study them tonight and sleep early after", "darast sitteen safHa li-ann el-imtiHaan sa3ib"),
        item("دفعنا مية على العشاء لأننا كنا عشرة، وكان الأكل لذيذ، وشربنا قهوة بعده، وقعدنا نتكلم لين المغرب", "We paid a hundred for dinner because we were ten, the food was delicious, we drank coffee after, and sat talking until sunset", "dafa3na miya 3alal-3ashaa li-annana kinna 3ashara"),
        item("عندي عشرين سنة أشتغل في هالمكتب لأني أحب شغلي، وما أبغى أشتغل بمكان ثاني، وأحس إني في بيتي", "I've worked at this office for twenty years because I love my job, never want to work anywhere else, and feel like I'm at home", "3indi 3ishreen sana ashtaghil fi hal-maktab li-anni aHibb shughli"),
        item("شرينا سبعين كيلو تمر للعيد لأن الأهل كثير هالسنة، وكل واحد ياخذ شوي، ويبقى منه للضيوف كمان", "We bought seventy kilos of dates for Eid because there's a lot of family this year, everyone takes a bit, and some remains for guests too", "sharayna sab3een keelo tamur lil-3eed li-ann el-ahl katheer has-sana"),
    ]),

    lesson(17, "Negation, Dense Chain", "النفي، متسلسل كثيف", [
        item("ما شريت هذا القميص لأنه غالي، ومب زين، ومب لونه اللي أبغاه، فرحت محل ثاني ولقيت أزيان", "I didn't buy this shirt because it's expensive, isn't good, and isn't the color I want, so I went to another shop and found a better one", "ma sharayt haadha el-gamees li-annah ghaali"),
        item("مب هذا البيت اللي أبغاه، فما رحت أشوفه، وما اتصلت بصاحبه، ورحت أشوف بيت ثاني بدل", "It's not this house I want, so I didn't go see it, didn't call its owner, and went to look at another house instead", "mub haadha el-bayt elli abghaah"),
        item("ما تشرب قهوة الليل لأنها تخليها متوترة، وما تنام زين، فتشرب شاي بدل، وتنام مرتاحة", "She doesn't drink coffee at night because it makes her nervous and she doesn't sleep well, so she drinks tea instead and sleeps relaxed", "ma tishrab gahwa el-layl li-annaha tkhalleeha mutawattira"),
        item("ما نروح المحل الثاني لأنه بعيد، ومب أرخص، فنفضل هذا المحل القريب، ونشري منه كل شي نحتاجه", "We don't go to the other shop because it's far and not cheaper, so we prefer this nearby shop and buy everything we need from it", "ma nruuH el-maHal eth-thaani li-annah ba3eed"),
    ]),

    lesson(18, "A Full Day, Dense Chain", "يوم كامل، متسلسل كثيف", [
        item("صحيت بدري، شربت قهوة، رحت الشغل، اشتغلت لين العصر، رجعت البيت، وقعدت أرتاح لين المغرب", "I woke up early, drank coffee, went to work, worked until afternoon, returned home, and sat resting until sunset", "SiHeet badri, sharabt gahwa, riHt esh-shaghal, ishtaghalt leen el-3asir"),
        item("طبخنا الفطور، نظفنا البيت، رحنا السوق، شرينا أشياء للعرس، رجعنا نلبس ملابسنا، وطلعنا مبسوطين", "We cooked breakfast, cleaned the house, went to the market, bought things for the wedding, returned to dress, and went out happy", "Tabakhna el-futoor, nadhdhafna el-bayt, riHna es-suug"),
        item("درست الصبح، اشتغلت الظهر، قعدت مع الأهل الليل، شربنا قهوة، وقبل ما أنام قريت شوي وفكرت باليوم الجاي", "I studied in the morning, worked at noon, sat with the family at night, we drank coffee, and before sleeping I read a bit and thought about tomorrow", "darast es-sub7, ishtaghalt edh-dhuhur, ga3adt ma3al-ahl el-layl"),
        item("سافرنا الصبح، وصلنا الظهر، زرنا الأهل هناك، قعدنا نشرب قهوة، أكلنا معهم، ورجعنا الليل متعبين بس مبسوطين", "We traveled in the morning, arrived at noon, visited the family there, sat drinking coffee, ate with them, and returned at night tired but happy", "saafarna es-sub7, wisalna edh-dhuhur, zirna el-ahl hinaak"),
    ]),

    lesson(19, "Another Full Day, Dense Chain", "يوم كامل ثاني، متسلسل كثيف", [
        item("اشتغلت من الصبح لين العصر بدون راحة، وتعبت كثير، فرجعت البيت، ونمت بدري، وصحيت زين بكرا", "I worked from morning until afternoon without a break, got very tired, so I returned home, slept early, and woke up well the next day", "ishtaghalt min es-sub7 leen el-3asir bidoon raaHa"),
        item("درسنا للامتحان طول اليوم، وفهمنا كل شي، وقعدنا نرتاح شوي، وأكلنا، ونمنا بدري", "We studied for the exam all day, understood everything, sat resting a bit, ate, and slept early", "darasna lil-imtiHaan Tool el-yoom"),
        item("زرنا المستشفى الصبح، وشرينا أشياء من السوق الظهر، وطبخنا العشاء، وقعدنا نتكلم عن يومنا لين المغرب", "We visited the hospital in the morning, bought things from the market at noon, cooked dinner, and sat talking about our day until sunset", "zirna el-mustashfa es-sub7"),
        item("تكلمت مع أخوي طول الطريق، وفهمنا كل شي أخيرا، وضحكنا كثير، ووصلنا مبسوطين ومرتاحين", "I talked with my brother the whole way, we finally understood everything, laughed a lot, and arrived happy and relaxed", "tkallamt ma3 akhooy Tool eT-Tareeg"),
    ]),

    lesson(20, "Review: C2 Recap 2", "مراجعة", [
        item("صحيت بدري ورحت الشغل، لأن عندي اجتماع مهم، وخلصت الشغل قبل الظهر، ورجعت البيت مرتاح", "I woke up early and went to work because I have an important meeting, finished the work before noon, and returned home relaxed", "SiHeet badri wa riHt esh-shaghal li-ann 3indi ijtimaa3 muhim"),
        item("ما رحت العرس مب لأني تعبان، بس لأن عندي شغل مهم، ولازم أخلصه، فقعدت أشتغل كل اليوم", "I didn't go to the wedding not because I'm tired, but because I have important work, must finish it, so I sat working all day", "ma riHt el-3urs mub li-anni ta3baan"),
        item("جدي في المستشفى، بس يتكلم زين، ويضحك، وياكل زين، والحمد لله الوضع تحسن كثير كل يوم", "My grandfather is in the hospital, but he talks well, laughs, eats well, and thank God the situation improves every day", "jiddi fil-mustashfa, bas yitkallam zayn, wa yiDHak, wa yaakil zayn"),
        item("سافرنا ووصلنا وزرنا الأهل وقعدنا نشرب قهوة ونتكلم، وكان يوم زين كثير، ورجعنا مبسوطين", "We traveled, arrived, visited the family, sat drinking coffee and talking, and it was a very good day, and we returned happy", "saafarna wa wisalna wa zirna el-ahl wa ga3adna nishrab gahwa"),
    ]),

    lesson(21, "Lazim, Dense Chain", "لازم، متسلسل كثيف", [
        item("لازم أروح البنك لأن فلوس البيت لازم تدفع اليوم، وبعدين أروح السوق، وأشري أشياء للعشاء", "I must go to the bank because the house money must be paid today, then I go to the market, and buy things for dinner", "laazim aruuH el-bank li-ann fluus el-bayt laazim tidfa3 el-yoom"),
        item("لازم تدرس أكثر لأن الامتحان قريب، ولازم تنام زين، ولازم تفهم كل شي، ولازم تسأل لو ما فهمتي", "You must study more because the exam is near, must sleep well, must understand everything, and must ask if you don't understand", "laazim tadrus akthar li-ann el-imtiHaan gareeb"),
        item("لازم نساعد جدتنا لأنها كبيرة في السن، ولازم نزورها كل جمعة، ولازم نتصل فيها كل يوم لأنها تحب هذا", "We must help our grandmother because she's elderly, must visit her every Friday, and must call her every day because she loves this", "laazim nsaa3id jiddatna li-annaha kabeera fis-sin"),
        item("لازم يدفعون الحساب لأنهم اكلو كثير، ولازم يشكرون صاحب المطعم، ولازم يرجعون له مرة ثانية", "They must pay the bill because they ate a lot, must thank the restaurant owner, and must return again", "laazim yidfa3oon el-Hisaab li-annahum akalaw katheer"),
    ]),

    lesson(22, "Lazim Ma, Dense Chain", "لازم ما، متسلسل كثيف", [
        item("لازم ما تشرب قهوة كثير لأنها تخليك متوتر، بس فنجان بالصبح زين، وفنجان بعد العشاء ممكن كمان", "You shouldn't drink too much coffee because it makes you nervous, but one cup in the morning is fine, and one after dinner is also possible", "laazim ma tishrab gahwa katheer li-annaha tkhalleek mutawattir"),
        item("لازم ما تروح لوحدك بالليل لأنه مب زين، بس مع أخوك ما فيه مشكلة، ويقدر يساعدك لو احتجت شي", "You shouldn't go alone at night because it's not good, but with your brother there's no problem, and he can help you if you need anything", "laazim ma truuH liwaHdak bil-layl li-annah mub zayn"),
        item("لازم ما تصرف كل فلوسك لأنك بتحتاجها بعدين، بس تشري أشياء تحتاجها زين، وتوفر باقي الفلوس", "You shouldn't spend all your money because you'll need it later, but buying things you need is fine, and save the rest of the money", "laazim ma tisrif kil fluusak li-annak batHtaajha ba3dayn"),
        item("لازم ما تقارن نفسك بالثانيين لأن كل واحد مختلف، بس تقدر تتعلم منهم، وتتحسن، وتصير أزيان كل يوم", "You shouldn't compare yourself to others because everyone is different, but you can learn from them, improve, and become better every day", "laazim ma tqaarin nafsak bith-thaanyeen li-ann kil waaHid mukhtalif"),
    ]),

    lesson(23, "Knowing, Dense Chain", "المعرفة، متسلسل كثيف ٢", [
        item("أدري إنه مشغول لأنه ما رد علي، بس بيتصل فيني بعدين، وأدري إنه ما ينساني، وأنا صابر", "I know he's busy because he didn't answer me, but he'll call me later, I know he doesn't forget me, and I'm patient", "adri innah mashghool li-annah ma radd 3alay"),
        item("تدري إن الطريق طويل لأنها سافرته قبل، بس تحب السفر بالسيارة، وتحب تشوف الطريق، وتحس بالراحة طول الوقت", "She knows the road is long because she's traveled it before, but she loves traveling by car, loves seeing the road, and feels comfortable the whole time", "tadri inn eT-Tareeg Taweel li-annaha saafarat-tah gabl"),
        item("ندري إن العرس بيكون كبير لأن العائلتين كبار، بس ما ندري بالضبط كم ضيف، واحنا جاهزين لكل شي", "We know the wedding will be big because both families are big, but we don't know exactly how many guests, and we're ready for everything", "nadri inn el-3urs baykoon kabeer li-ann el-3aa'ilatayn kubaar"),
        item("يدرون إن الشغل صعب لأنهم جربو قبل، بس يحبونه لأنه يستاهل، ويحسون بالفرح كل ما يخلصون مشروع", "They know the work is hard because they've tried before, but they love it because it's worth it, and they feel joy every time they finish a project", "yidroon inn esh-shughul sa3ib li-annahum jarrabaw gabl"),
    ]),

    lesson(24, "Wanting, Dense Chain", "الرغبة، متسلسل كثيف ٢", [
        item("أبغى أسافر بعيد لأني أحب أشوف أماكن جديدة، بس ما عندي وقت كافي، فقررت أسافر الشهر الجاي بدل", "I want to travel far because I love seeing new places, but I don't have enough time, so I decided to travel next month instead", "abgha asaafir ba3eed li-anni aHibb ashoof amaakin jideeda"),
        item("تبغى تدرس شي ثاني لأنها ما تحب شغلها، بس تخاف تبدأ من جديد، فتفكر وتدرس شوي شوي عن هالموضوع", "She wants to study something else because she doesn't like her job, but she's afraid to start over, so she thinks and studies this topic little by little", "tibgha tadrus shay thaani li-annaha ma tHibb shughulha"),
        item("أبغى أشري بيت أكبر لأن عائلتي كبرت، بس السعر غالي، فأوفر كل شهر، وبعد سنتين بقدر أشريه انشاالله", "I want to buy a bigger house because my family grew, but the price is expensive, so I save every month, and after two years I'll be able to buy it God willing", "abgha ashri bayt akbar li-ann 3aa'ilti kubrat"),
        item("يبغى يفتح محل جديد لأنه يحب البيع والشراء، بس يحتاج فلوس أكثر، فيشتغل شغلين، ويوفر بسرعة", "He wants to open a new shop because he loves buying and selling, but he needs more money, so he works two jobs and saves quickly", "yibgha yiftaH maHal jideed li-annah yiHibb el-bay3 wash-shiraa"),
    ]),

    lesson(25, "Review: Lazim, Know, Want", "مراجعة", [
        item("لازم أدرس أكثر لأن الامتحان قريب، وأبغى أنجح لأني تعبت هالفصل، وأدري إني أقدر لو جربت زين", "I must study more because the exam is near, want to succeed because I worked hard this semester, and know I can if I try well", "laazim adrus akthar li-ann el-imtiHaan gareeb"),
        item("لازم ما تشرب قهوة كثير لأنها تخليك متوتر، وأدري إن هذا صعب عليك، بس تقدر تتعلم تشرب أقل", "You shouldn't drink too much coffee because it makes you nervous, and I know this is hard for you, but you can learn to drink less", "laazim ma tishrab gahwa katheer li-annaha tkhalleek mutawattir"),
        item("أبغى أساعد جدتي لأنها كبيرة، وأعرف إنها تحتاجني، فأزورها كل جمعة، وأتصل فيها كل يوم", "I want to help my grandmother because she's elderly, know she needs me, so I visit her every Friday, and call her every day", "abgha asaa3id jiddati li-annaha kabeera"),
        item("تبغى تسافر لأنها تحب هالشي، بس لازم تخلص شغلها أول، وتدري إن الصبر مهم قبل السفر", "She wants to travel because she loves this, but she must finish her work first, and knows patience is important before travel", "tibgha tsaafir li-annaha tHibb hash-shay"),
    ]),

    lesson(26, "Colors and Directions, Dense Chain", "الألوان والاتجاهات، متسلسل كثيف", [
        item("رحنا يمين لأن البيت الأحمر هناك، وبعدين رحنا يسار عشان نلقى البنك، ووصلنا أخيرا بعد وقت طويل", "We went right because the red house is there, then went left in order to find the bank, and finally arrived after a long time", "riHna yameen li-ann el-bayt el-a7mar hinaak"),
        item("البيت الأزرق قدام المسجد، والبيت الأخضر وراه، وبينهم بيت أصفر صغير، وكلهم قريبين من بعض", "The blue house is in front of the mosque, the green house is behind it, between them is a small yellow house, and they're all near each other", "el-bayt el-azrag guddaam el-masjid, wal-bayt el-akhdar waraah"),
        item("مشيت يمين لين لقيت المحل، وشريت غترة بيضاء، وبعدين رجعت يسار للسيارة، وطلعنا للبيت مباشرة", "I walked right until I found the shop, bought a white headdress, then went back left to the car, and we went home directly", "misheet yameen leen ligeet el-maHal"),
        item("السيارة الحمراء قريبة من البنك، والسيارة الصفراء بعيدة شوي وراها، وسيارتي الزرقاء بينهم بالضبط", "The red car is near the bank, the yellow car is a bit far behind it, and my blue car is exactly between them", "es-sayyaara el-Hamraa gareeba minal-bank"),
    ]),

    lesson(27, "A Story, Dense Chain", "قصة، متسلسل كثيف", [
        item("جدي كان يشتغل في الغوص أيام زمان، وكان يروح البحر شهور طويلة، وكان صعب، بس تعلم منه أشياء كثير", "My grandfather used to work in pearl diving in the old days, would go to the sea for long months, it was hard, but he learned a lot from it", "jiddi kaan yashtaghil fil-ghaws ayyaam zamaan"),
        item("خالي سافر للكويت وهو صغير، درس هناك سنين طويلة، رجع بعدها، وصار مهندس زين، وفتح مكتبه الخاص", "My maternal uncle traveled to Kuwait when he was young, studied there for many years, returned after, became a good engineer, and opened his own office", "khaali saafar lil-kuwayt wa huwa sagheer"),
        item("جدتي طبخت للعائلة كل جمعة سنين طويلة، وتعلمنا منها كل الوصفات، ولسا نطبخها لين الحين، ونفكر فيها كل مرة", "My grandmother cooked for the family every Friday for many years, we learned all the recipes from her, still cook them until now, and think of her every time", "jiddati Tabakhat lil-3aa'ila kil jum3a sineen Taweela"),
        item("أخوي بدأ شغل صغير، اشتغل عليه كثير، وبعد سنين صار محل كبير ومشهور، وصار فخور بنفسه كثير", "My brother started a small business, worked on it hard, and after years it became a big and famous shop, and he became very proud of himself", "akhooy bida shughul sagheer, ishtaghal 3alayh katheer"),
    ]),

    lesson(28, "Money, Dense Chain", "الفلوس، متسلسل كثيف", [
        item("وفرت فلوس كثير سنتين، شريت بيها بيت صغير، وصار عندي بيت ثاني، وأحس إني نجحت أخيرا", "I saved a lot of money for two years, bought a small house with it, had a second house, and feel I finally succeeded", "waffart fluus katheer santeen, sharayt beeha bayt sagheer"),
        item("اشتغل شغلين عشان يوفر فلوس أكثر، وبعد سنة قدر يشري سيارة جديدة، وكان مبسوط كثير بهذا", "He worked two jobs in order to save more money, and after a year he was able to buy a new car, and was very happy with this", "ishtaghal shughlayn 3ashaan ywaffir fluus akthar"),
        item("دفعنا نص الفلوس أول، وبعدين دفعنا النص الثاني بعد شهرين، وخلصنا كل شي، وارتحنا من هالموضوع", "We paid half the money first, then paid the other half after two months, finished everything, and relaxed about this matter", "dafa3na nus el-fluus awwal, wa ba3dayn dafa3na en-nus eth-thaani ba3d shahrayn"),
        item("صرفت فلوس كثير على السفر، فقررت أوفر أكثر، وبعد كذا رجعت أسافر مرة ثانية، وصرت أوفر فلوسي زين", "I spent a lot of money on travel, so I decided to save more, and after that I traveled again, and I became better at saving my money", "saraft fluus katheer 3ales-safar, fa-garrart awaffir akthar"),
    ]),

    lesson(29, "Feelings, Dense Chain", "المشاعر، متسلسل كثيف", [
        item("كنت متوتر قبل الامتحان، بس درست زين، وفهمت كل شي، ودخلت، ونجحت أخيرا، وحسيت بفرح كثير", "I was nervous before the exam, but I studied well, understood everything, went in, finally succeeded, and felt a lot of joy", "kint mutawattir gabl el-imtiHaan, bas darast zayn, wa fihimt kil shay"),
        item("كانت قلقانة على ابنها أول، بس اتصل فيها وقال إنه زين، فارتاحت، وضحكت، وحست بأمان كثير", "She was worried about her son at first, but he called her and said he's fine, so she relaxed, laughed, and felt very safe", "kaanat galgaana 3ala ibnaha awwal, bas ittasal feeha"),
        item("كنا متضايقين من الشغل الكثير، بس اخذنا إجازة، وارتحنا، ورجعنا نشتغل مبسوطين، وأزيان من قبل بكثير", "We were upset about the excessive work, but we took a vacation, rested, returned to work happier, and much better than before", "kinna mutadaayigeen minesh-shughul el-katheer"),
        item("كان زعلان من صاحبه أول، بس تكلمو مع بعض، وفهمو بعض، وصارو أصحاب زين مرة ثانية، وضحكو كثير", "He was upset with his friend at first, but they talked to each other, understood each other, became good friends again, and laughed a lot", "kaan za3laan min saaHbah awwal, bas tkallamaw ma3 ba3ad"),
    ]),

    lesson(30, "Review: C2 Final Recap", "مراجعة نهائية", [
        item("جدي اشتغل في الغوص أيام زمان، وتعبت العائلة، بس ما زعلو، وصار عندنا بيت زين أخيرا، والحمد لله", "My grandfather worked in pearl diving in the old days, the family struggled, but didn't get upset, and we finally got a good house, thank God", "jiddi ishtaghal fil-ghaws ayyaam zamaan"),
        item("وفرنا فلوس سنين طويلة، وشرينا بيت أكبر، وصرنا نقعد فيه مع كل العائلة، ونشرب قهوة، ونحس بالفخر", "We saved money for many years, bought a bigger house, and now sit in it with the whole family, drink coffee, and feel proud", "waffarna fluus sineen Taweela, wa sharayna bayt akbar"),
        item("كنت متوتر من الشغل الجديد أول، بس تعلمت زين، وصرت أحبه، وأحس إني أزيان كل يوم فيه", "I was nervous about the new job at first, but I learned well, started loving it, and feel better every day in it", "kint mutawattir minesh-shughul el-jideed awwal"),
        item("رحنا يمين وبعدين يسار، ولقينا البيت الأخضر أخيرا، وكان يستاهل كل هالتعب، وحسينا بفخر كبير", "We went right and then left, finally found the green house, it was worth all this effort, and we felt great pride", "riHna yameen wa ba3dayn yasaar, wa ligeena el-bayt el-akhdar akheeran"),
    ]),

    lesson(31, "Stress, Dense Chain", "التوتر، متسلسل كثيف", [
        item("متوتر كثير قبل الامتحان، بس أفكر بأشياء زينة عشان أرتاح، وأدرس زين، وأحس إني جاهز، وأدخل مرتاح", "I'm very nervous before the exam, but I think of good things in order to relax, study well, feel ready, and go in relaxed", "mutawattir katheer gabl el-imtiHaan"),
        item("قلقانة على ابنها، بس ما تبين قلقها له، وتساعده، وتقعد وياه، وتحس بفخر كل ما يتعلم شي جديد", "She's worried about her son, but doesn't show her worry to him, helps him, sits with him, and feels proud every time he learns something new", "galgaana 3ala ibnaha, bas ma tbayyin galagha lah"),
        item("متضايقين من الشغل الكثير، بس نرتاح كل جمعة، ونزور الأهل، ونشرب قهوة، ونحس بالراحة أكثر", "We're upset about the excessive work, but we rest every Friday, visit the family, drink coffee, and feel more relaxed", "mutadaayigeen minesh-shughul el-katheer"),
        item("فخورين كثير لأن السنة كانت صعبة، وصبرنا زين، وتعلمنا أشياء كثير، ورجعنا أزيان من قبل بكثير", "We're very proud because the year was difficult, we were patient, learned a lot of things, and became much better than before", "fakhooreen katheer li-ann es-sana kaanat sa3ba"),
    ]),

    lesson(32, "Clothes, Dense Chain", "الملابس، متسلسل كثيف", [
        item("رحت السوق، شفت قميص أزرق زين، جربته، وناسبني، فشريته، ولبسته، وحسيت إني أنيق كثير اليوم", "I went to the market, saw a nice blue shirt, tried it on, it suited me, so I bought it, wore it, and felt very elegant today", "riHt es-suug, shift gamees azrag zayn, jarrabtah"),
        item("شرت عباية جديدة للعرس، وغترة بيضاء تناسبها، وجوتي أسود يناسبها زين، وكانت أنيقة كثير", "She bought a new abaya for the wedding, a white headdress that matches it, black shoes that suit it well, and she looked very elegant", "sharat 3abaaya jideeda lil-3urs, wa ghitra baydaa tnaasibha"),
        item("لبسنا ملابس دافية لأن الجو بارد، وطلعنا نمشي، وحسينا بالزين طول الوقت، ورجعنا مبسوطين كثير", "We wore warm clothes because the weather is cold, went out to walk, felt good the whole time, and returned very happy", "libasna malaabis daafya li-ann el-jaww baarid"),
        item("غسلت القميص الوسخ، نظفته زين، وبعدين لبسته للاجتماع المهم، وحسيت إني جاهز لكل شي", "I washed the dirty shirt, cleaned it well, then wore it to the important meeting, and felt ready for everything", "ghasalt el-gamees el-wisikh, nadhdhaftah zayn"),
    ]),

    lesson(33, "Clothes, Dense Chain II", "الملابس، متسلسل كثيف ٢", [
        item("جربت قميص أحمر وقميص أصفر، بس اخترت الأزرق لأنه ناسبني أكثر، وحسيت فيه أزيان من كل شي ثاني", "I tried a red shirt and a yellow shirt, but chose the blue one because it suited me more, and felt better in it than anything else", "jarrabt gamees aHmar wa gamees asfar, bas ikhtart el-azrag"),
        item("شرينا جوتي جديد لكل الأولاد قبل العيد، وكانو مبسوطين كثير فيه، ولبسوه كل يوم من العيد", "We bought new shoes for all the children before Eid, they were very happy with them, and wore them every day of Eid", "sharayna jooti jideed likil el-awlaad gabl el-3eed"),
        item("لبست غترة جديدة اليوم لأن القديمة صارت وسخة، وحسيت إني أنيق، ومبسوط، وجاهز ليومي", "I wore a new headdress today because the old one became dirty, and felt elegant, happy, and ready for my day", "libast ghitra jideeda el-yoom li-ann el-gadeema saarat wisikha"),
        item("قارنت الأسعار بمحلات كثير، ولقيت غترة زينة بسعر مناسب، فشريتها بسرعة، وحسيت إني وفرت فلوس كثير", "I compared prices at a lot of shops, found a nice headdress at a suitable price, bought it quickly, and felt I saved a lot of money", "qaarant el-as3aar bima7allaat katheer, wa ligeet ghitra zeena bisi3ir munaasib"),
    ]),

    lesson(34, "Food, Dense Chain", "الأكل، متسلسل كثيف", [
        item("طبخت لحم وسلطة وأرز للضيوف، وحطيت تمر وقهوة بعدها، وعطيناه للضيوف، وكل واحد اكل كثير ومبسوط", "I cooked meat, salad, and rice for the guests, put out dates and coffee after, gave it to the guests, and everyone ate a lot and was happy", "Tabakht la7am wa salata wa aruz lidh-dhuyoof"),
        item("جربنا مطعم جديد، طلبنا أكل خليجي، وكان لذيذ، فقررنا نرجع له مرة ثانية، ونجرب أكلات ثانية منه", "We tried a new restaurant, ordered Khaleeji food, it was delicious, so we decided to return again, and try other dishes from it", "jarrabna mat3am jideed, Talabna akal khaleeji"),
        item("سوت جدتي أكل زين كل جمعة، وكل العائلة تجي تاكل معها، ويقعدون يتكلمون، ويحسون بالمحبة والفرح", "My grandmother makes good food every Friday, the whole family comes to eat with her, sits talking, and feels love and joy", "sawwat jiddati akal zayn kil jum3a"),
        item("شرينا تمر كثير للعيد، وحطينا شوي في كل صحن، وعطيناه للضيوف مع القهوة، وكلهم كانو مبسوطين", "We bought a lot of dates for Eid, put some in each plate, gave it to the guests with coffee, and they were all happy", "sharayna tamur katheer lil-3eed, wa HaTTayna shway fi kil saHan"),
    ]),

    lesson(35, "Food, Dense Chain II", "الأكل، متسلسل كثيف ٢", [
        item("طلبنا لحم وسمك وسلطة، واكلنا كل شي، وشربنا قهوة بعدها، وقعدنا نتكلم، وكان يوم زين كثير", "We ordered meat, fish, and salad, ate everything, drank coffee after, sat talking, and it was a very good day", "Talabna la7am wa samak wa salata, wa akalna kil shay"),
        item("جربت أكل جديد اليوم، ما عرفته أول، بس اكلته، وحبيته كثير، وقررت أطبخه بنفسي بعدين", "I tried new food today, didn't know it at first, but ate it, loved it a lot, and decided to cook it myself later", "jarrabt akal jideed el-yoom, ma 3iraftah awwal, bas akaltah"),
        item("طبخنا للأهل كلهم، وأكل الكل كثير، وقعدنا نشرب قهوة ونتكلم لين المغرب، وحسينا بالمحبة والراحة", "We cooked for the whole family, everyone ate a lot, we sat drinking coffee and talking until sunset, and felt love and comfort", "Tabakhna lil-ahl killahum, wa akal el-kil katheer"),
        item("شريت لحم وسلطة من السوق، طبخت أكل زين، والعائلة كلها اكلت وكانت مبسوطة، وشكرتني جدتي كثير", "I bought meat and salad from the market, cooked good food, the whole family ate and was happy, and my grandmother thanked me a lot", "sharayt la7am wa salata mines-suug, wa Tabakht akal zayn"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/c2.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "c2", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/c2.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
