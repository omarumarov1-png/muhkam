#!/usr/bin/env python3
"""Full rewrite of B2 Khaleeji Arabic content -- negation (ma/mub) themed,
same repetition fix, built on the large confirmed vocabulary from
A1/A2/B1/B1+ to minimize new-word overhead while keeping real sentence
complexity and topical variety.
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
    lesson(1, "I Don't Drink, I Don't Go", "ما أشرب، ما أروح", [
        item("ما أشرب قهوة الليل لأنها تخليني ما أنام", "I don't drink coffee at night because it keeps me from sleeping", "ma ashrab gahwa el-layl li-annaha tkhalleeni ma anaam"),
        item("ما تروح السوق يوم الجمعة لأن كل المحلات مسكرة", "You don't go to the market on Friday because all the shops are closed", "ma truuH es-suug yoom el-jum3a"),
        item("ما تشربين شاي بارد، تحبين قهوة حارة بس", "You (f) don't drink cold tea, you only like hot coffee", "ma tishrabeen shaay baarid"),
        item("ما يروح المجلس بدون ما يشرب قهوة أول", "He doesn't go to the majlis without drinking coffee first", "ma yruuH el-majlis bidoon ma yishrab gahwa awwal"),
    ], topicId="b2-ma"),

    lesson(2, "She Doesn't, We Don't", "ما تروح، ما نروح", [
        item("ما تشرب قهوة بالحليب، تحب القهوة بدون حليب بس", "She doesn't drink coffee with milk, she only likes it plain", "ma tishrab gahwa bil-Haleeb"),
        item("ما نروح المطعم الجديد لأن الأكل هناك ما يستاهل السعر", "We don't go to the new restaurant because the food there isn't worth the price", "ma nruuH el-mat3am el-jideed"),
        item("ما تروحون البنك بعد الظهر لأنه يسكر الساعة وحدة", "You all don't go to the bank after noon because it closes at one o'clock", "ma truu7oon el-bank ba3d edh-dhuhur"),
        item("ما يشربون قهوة قبل الفطور، الأكل أول عندهم دايما", "They don't drink coffee before breakfast, food always comes first for them", "ma yishrabuun gahwa gabl el-futoor"),
    ]),

    lesson(3, "Not This, Not That", "مب هذا، مب هذاك", [
        item("مب هذا البيت اللي أبغاه، أبغى بيت أكبر وأقرب من الشغل", "It's not this house that I want, I want a bigger house closer to work", "mub haadha el-bayt elladhi abghaah"),
        item("هذا مب سعر عادل، السعر الصح أرخص من كذا بكثير", "This isn't a fair price, the right price is much cheaper than this", "haadha mub si3ir 3aadil"),
        item("مب هذاك القميص اللي أبغاه، أبغى الأزرق مب الأحمر", "It's not that shirt I want, I want the blue one not the red one", "mub haadhaak el-gamees elli abghaah"),
        item("هذي مب الطريقة الصح تسوي فيها القهوة، فيه طريقة أزيان", "This isn't the right way to make coffee, there's a better way", "haadhi mub eT-Tareega es-saHH tsawwi feeha el-gahwa"),
    ]),

    lesson(4, "Not Because, But Because", "مب لأن، بس لأن", [
        item("ما رحت لأني تعبان، رحت لأن جدي طلب مني", "I didn't go because I'm tired, I went because my grandfather asked me to", "ma riHt li-anni ta3baan, riHt li-ann jiddi Talab minni"),
        item("مب لأنه غالي ما شريته، بس لأنه ما يناسبني", "It's not because it's expensive that I didn't buy it, but because it doesn't suit me", "mub li-annah ghaali ma sharaytah, bas li-annah ma ynaasibni"),
        item("ما نجحت لأن الامتحان سهل، نجحت لأني درست كثير", "I didn't succeed because the exam was easy, I succeeded because I studied a lot", "ma najaHt li-ann el-imtiHaan sahil, najaHt li-anni darast katheer"),
        item("مب لأني ما أحبه ما رحت العرس، بس لأن عندي شغل مهم", "It's not because I don't like him that I didn't go to the wedding, but because I had important work", "mub li-anni ma aHibbah ma riHt el-3urs"),
    ]),

    lesson(5, "Review: Negation", "مراجعة: النفي", [
        item("ما شريت هذا القميص لأنه غالي، بس لأنه مب زين", "I didn't buy this shirt because it's expensive, but because it's not nice", "ma sharayt haadha el-gamees li-annah ghaali, bas li-annah mub zayn"),
        item("مب هذا البيت اللي أبغاه، وما رحت أشوفه أبدا", "It's not this house I want, and I never went to see it", "mub haadha el-bayt elli abghaah, wa ma riHt ashoofah abadan"),
        item("ما تشرب قهوة الليل، ومب لأنها مرة، بس عشان تنام زين", "She doesn't drink coffee at night, and not because it's bitter, but so she sleeps well", "ma tishrab gahwa el-layl"),
        item("ما نروح المحل الثاني لأنه بعيد، بس لأن هذا أرخص وأزيان", "We don't go to the other shop because it's far, but because this one is cheaper and better", "ma nruuH el-maHal eth-thaani li-annah ba3eed"),
    ]),

    lesson(6, "Negation and Money", "النفي والفلوس", [
        item("ما دفعت الحساب كله لأن نص الفلوس كافي الحين", "I didn't pay the whole bill because half the money is enough for now", "ma dafa3t el-Hisaab killah li-ann nus el-fluus kaafi Haaliyan"),
        item("ما عندي فلوس كافية أشري بيت الحين، بس أوفر كل شهر", "I don't have enough money to buy a house now, but I save every month", "ma 3indi fluus kaafya ashri bayt el-heen"),
        item("ما نصرف كل الفلوس على أشياء ما نحتاجها", "We don't spend all our money on things we don't need", "ma nisrif kil el-fluus 3ala ashyaa ma naHtaajha"),
        item("مب لأن الفلوس قليلة ما سافرنا، بس لأن ما عندنا وقت", "It's not because we have little money that we didn't travel, but because we don't have time", "mub li-ann el-fluus galeela ma saafarna"),
    ]),

    lesson(7, "Negation and Family", "النفي والعائلة", [
        item("ما زارنا خالي من زمان لأنه مشغول بشغله الجديد", "My maternal uncle hasn't visited us in a long time because he's busy with his new job", "ma zaarna khaali min zamaan li-annah mashghool bishughlah el-jideed"),
        item("ما تدري جدتي شنو صار بالضبط، بس تحس إن الوضع تحسن", "My grandmother doesn't know exactly what happened, but she feels the situation improved", "ma tadri jiddati shinu saar biD-Dabt"),
        item("ما قدرو يخلون خالي يروح الطبيب، هو ما يحب المستشفى أبدا", "They couldn't get my maternal uncle to go to the doctor, he never likes the hospital", "ma gidaraw ykhalloon khaali yruuH eT-Tabeeb"),
        item("مب لأننا ما نحب أهلنا ما نزورهم كثير، بس السفر بعيد ومتعب", "It's not because we don't love our family that we don't visit them often, but the trip is far and tiring", "mub li-annana ma niHibb ahlana ma nzoorhum katheer"),
    ]),

    lesson(8, "Negation and Colors", "النفي والألوان", [
        item("ما شريت السيارة الحمراء لأني ما أحب هذا اللون كثير", "I didn't buy the red car because I don't like this color much", "ma sharayt es-sayyaara el-Hamraa li-anni ma aHibb haadha el-loon katheer"),
        item("العباية مب سوداء ومب زرقاء، هي بين اللونين", "The abaya isn't black and isn't blue, it's between the two colors", "el-3abaaya mub sawdaa wa mub zarqaa"),
        item("ما تبغى الغترة البيضاء لأنها تصير وسخة بسرعة", "She doesn't want the white headdress because it gets dirty quickly", "ma tibgha el-ghitra el-baydaa li-annaha twassikh bisur3a"),
        item("مب كل بيت أخضر أزيان من البيت الأصفر، السعر مهم كمان", "Not every green house is better than the yellow house, the price matters too", "mub kil bayt akhdar azyan minal-bayt el-asfar"),
    ]),

    lesson(9, "Negation and Places", "النفي والأماكن", [
        item("ما رحنا المستشفى لأن الوضع ما كان صعب، بس رحنا زيارة بس", "We didn't go to the hospital because the situation wasn't difficult, but we went just for a visit", "ma riHna el-mustashfa li-ann el-wad3 ma kaan sa3ib"),
        item("ما نلقى مطاعم زينة قريبة من هنا، كلها بعيدة شوي", "We can't find good restaurants near here, they're all a bit far", "ma nilga maTaa3im zeena gareeba min hina"),
        item("مب كل مسجد قريب من بيتنا زين، فنفضل المسجد الكبير", "Not every mosque near our house is good, so we prefer the big mosque", "mub kil masjid gareeb min baytna zayn"),
        item("ما وصلنا السوق قبل ما يسكرون، فرجعنا البيت بدون شي", "We didn't arrive at the market before it closed, so we returned home without anything", "ma wisalna es-suug gabl ma yiskiroon"),
    ]),

    lesson(10, "Review: B2 Recap", "مراجعة", [
        item("ما شريت البيت الأخضر لأنه بعيد، مب لأني ما أحبه", "I didn't buy the green house because it's far, not because I didn't like it", "ma sharayt el-bayt el-akhdar li-annah ba3eed"),
        item("ما زرنا خالي من زمان لأن السفر متعب، بس بنزوره بكرا", "We haven't visited my maternal uncle in a long time because the trip is tiring, but we'll visit him tomorrow", "ma zirna khaali min zamaan li-ann es-safar mut3ib"),
        item("مب كل شي غالي زين، وما كل شي رخيص وسخ", "Not everything expensive is good, and not everything cheap is bad", "mub kil shay ghaali zayn"),
        item("ما نصرف على أشياء ما نحتاجها، عشان نوفر للسفر هالصيف", "We don't spend on things we don't need, in order to save for this summer's trip", "ma nisrif 3ala ashyaa ma naHtaajha"),
    ]),

    lesson(11, "I'm Not Sick", "أنا مب مريض", [
        item("أنا مب مريض، بس تعبان شوي من النوم القليل", "I'm not sick, just a bit tired from lack of sleep", "ana mub mareed, bas ta3baan shway"),
        item("هي مب متضايقة من الشغل، هي متضايقة من صديقتها", "She's not upset about work, she's upset with her friend", "hiya mub mutadaayiga minesh-shughul"),
        item("احنا مب قلقانين على النتيجة، نفكر إنها بتصير زينة", "We're not worried about the result, we think it'll be good", "iHna mub galgaaneen 3alan-nateeja, nfakkir innaha baytseer zeena"),
        item("هم مب متأخرين، وصلو قبل خمس دقايق بس ما شفناهم", "They're not late, they arrived five minutes ago but we didn't see them", "hum mub mit'akhkhireen"),
    ]),

    lesson(12, "Not Tired, Not Happy", "مب تعبان، مب مبسوط", [
        item("مب تعبان اليوم، بس ما أبغى أروح الشغل اليوم", "I'm not tired today, but I don't feel enthusiasm for work", "mub ta3baan el-yoom, bas ma aHiss biHamaas lish-shughul"),
        item("مب مبسوطة بنتيجة الامتحان، كانت أصعب من اللي درسته", "She's not happy with the exam result, it was harder than what she studied", "mub mabsoota binateejat el-imtiHaan"),
        item("ما كانو زعلانين من القرار، بس كانو متضايقين شوي", "They weren't upset about the decision, but they were a bit annoyed", "ma kaanaw za3laaneen minal-qaraar, bas kaanaw mutadaayigeen shway"),
        item("مب فخور بهذا الشغل، أقدر أسويه أزيان من كذا بكثير", "I'm not proud of this work, I can do it much better than this", "mub fakhoor bihaadha esh-shughul"),
    ]),

    lesson(13, "Not One, Not Two", "مب واحد، مب اثنين", [
        item("مب واحد بس اللي نجح، أكثر الصف نجح هالمرة", "It's not just one who succeeded, most of the class succeeded this time", "mub waaHid bas elli najaH, akthar es-saff najaH hal-marra"),
        item("ما عندي عشرة بس، عندي خمسة عشر بالضبط", "I don't have just ten, I have about fifteen", "ma 3indi 3ashara bas, 3indi khamsata3ash tagreeban"),
        item("مب مية درهم كان السفر، كانت أرخص من كذا بكثير", "The trip wasn't a hundred dirhams, it was much cheaper than that", "mub miya dirham kaanat er-riHla"),
        item("ما دفعنا سبعين على العشاء، دفعنا أقل من خمسين", "We didn't pay seventy for dinner, we paid less than fifty", "ma dafa3na sab3een 3alal-3ashaa, dafa3na agall min khamseen"),
    ]),

    lesson(14, "Not Today, Not Friday", "مب اليوم، مب الجمعة", [
        item("مب اليوم عندي امتحان، امتحاني يوم الاثنين الجاي", "My exam isn't today, my exam is next Monday", "mub el-yoom 3indi imtiHaan, imtiHaani yoom el-ithnayn el-jaay"),
        item("ما نسافر يوم الجمعة، نسافر يوم السبت الصبح بدري", "We're not traveling on Friday, we're traveling early Saturday morning", "ma nsaafir yoom el-jum3a"),
        item("مب أمس رحت المستشفى، رحت أول أمس مع خالتي", "It wasn't yesterday I went to the hospital, I went the day before yesterday with my maternal aunt", "mub ams riHt el-mustashfa"),
        item("ما بيوصل بكرا، بيوصل بعد يومين لأن سفره طويل", "He won't arrive tomorrow, he'll arrive in two days because his trip is long", "ma bayoosal bukra, bayoosal ba3d yoomayn"),
    ]),

    lesson(15, "Review: Negation with Health, Numbers, Days", "مراجعة", [
        item("مب مريض كثير، بس لازم أرتاح يوم أو يومين بس", "I'm not very sick, but I need to rest just a day or two", "mub mareed katheer, bas laazim artaaH yoom aw yoomayn bas"),
        item("ما عندي عشرين سنة أشتغل هنا، عندي خمس عشرة بس", "I haven't worked here for twenty years, I've worked here for just fifteen", "ma 3indi 3ishreen sana ashtaghil hina"),
        item("مب يوم الخميس العرس، العرس يوم الجمعة الجاية", "The wedding isn't on Thursday, the wedding is next Friday", "mub yoom el-khamees el-3urs, el-3urs yoom el-jum3a el-qaadima"),
        item("ما كانت متضايقة من النتيجة، كانت مبسوطة كثير بالعكس", "She wasn't upset about the result, she was surely very happy", "ma kaanat mutadaayiga minan-nateeja"),
    ]),

    lesson(16, "Not Expensive, Not Cheap", "مب غالي، مب رخيص", [
        item("هذا السعر مب غالي ولا رخيص، هو سعر عادل ومناسب", "This price isn't expensive or cheap, it's a fair and reasonable price", "haadha es-si3ir mub ghaali wala rakhees"),
        item("الجوتي مب غالي زين، بس مب زين مثل السعر", "The shoes aren't very expensive, but the quality isn't worth the price", "el-jooti mub ghaali zayn"),
        item("مب كل شي رخيص وسخ، بعض الأشياء الرخيصة زينة كثير", "Not everything cheap is bad, some cheap things are very good", "mub kil shay rakhees wisikh"),
        item("ما دفعنا سعر غالي على البيت، دفعنا سعر يناسب دخلنا", "We didn't pay a high price for the house, we paid a price that suits our income", "ma dafa3na si3ir ghaali 3alal-bayt"),
    ]),

    lesson(17, "Not My Brother, My Sister", "مب أخوي، أختي", [
        item("مب أخوي اللي سافر، أختي هي اللي سافرت للكويت", "It wasn't my brother who traveled, it was my sister who traveled to Kuwait", "mub akhooy elli saafar, ukhti hiya elli saafarat lil-kuwayt"),
        item("مب جدي اللي حكى لي القصة، جدتي هي اللي حكتها", "It wasn't my grandfather who told me the story, my grandmother is the one who told it", "mub jiddi elli Haka li el-gissa, jiddati hiya elli Hakatha"),
        item("ما خالي اللي زارنا أمس، عمي هو اللي زارنا", "It wasn't my maternal uncle who visited us yesterday, my paternal uncle is the one who visited us", "ma khaali elli zaarna ams, 3ammi huwa elli zaarna"),
        item("مب ابن عمي اللي نجح في الجامعة، ابن خالي هو اللي نجح", "It wasn't my paternal cousin who succeeded at university, my maternal cousin is the one who succeeded", "mub ibin 3ammi elli najaH fil-jaami3a"),
    ]),

    lesson(18, "Not Near, Not Far", "مب قريب، مب بعيد", [
        item("البيت مب قريب من الشغل، فلازم أطلع بدري كل يوم", "The house isn't near work, so I have to leave early every day", "el-bayt mub gareeb minesh-shughul"),
        item("المستشفى مب بعيد كثير، بيوصلونه في عشر دقايق بالسيارة", "The hospital isn't very far, they'll reach it in ten minutes by car", "el-mustashfa mub ba3eed katheer"),
        item("مب قريب المطعم من هنا، لازم نروح بالسيارة مب مشي", "The restaurant isn't near here, we need to go by car not on foot", "mub gareeb el-mat3am min hina"),
        item("ما البنك بعيد، بس الزحمة تخلي الطريق طويل كثير", "The bank isn't far, but the traffic makes the way take a long time", "ma el-bank ba3eed, bas ez-za7ma tkhalli eT-Tareeg yTool katheer"),
    ]),

    lesson(19, "Not Red, Not Blue", "مب أحمر، مب أزرق", [
        item("القميص مب أحمر، هو أصفر غامق يبين أحمر من بعيد", "The shirt isn't red, it's dark yellow that looks red from far away", "el-gamees mub aHmar, huwa asfar ghaamiq"),
        item("مب أزرق البيت، هو أخضر غامق يبين أزرق بالليل", "The house isn't blue, it's dark green that looks blue at night", "mub azraq el-bayt, huwa akhdar ghaamiq"),
        item("ما السيارة صفراء، هي بيضاء بس فيها غبار كثير", "The car isn't yellow, it's white but it has a lot of dust on it", "ma es-sayyaara safraa, hiya baydaa"),
        item("مب أسود جوتيها، هو بني غامق كثير يبين أسود", "Her shoes aren't black, they're very dark brown that looks black", "mub aswad jootiiha, huwa bunni ghaamiq"),
    ]),

    lesson(20, "Review: B2 Recap", "مراجعة", [
        item("مب أخوي اللي شرى البيت الأخضر، أنا اللي شريته", "It wasn't my brother who bought the green house, I'm the one who bought it", "mub akhooy elli shara el-bayt el-akhdar, ana elli sharaytah"),
        item("البيت مب بعيد ولا قريب، هو بين البنك والمسجد بالضبط", "The house isn't far or near, it's exactly between the bank and the mosque", "el-bayt mub ba3eed wala gareeb, huwa bayn el-bank wal-masjid biD-Dabt"),
        item("ما دفعنا سعر غالي على السيارة الحمراء، دفعنا سعر عادل", "We didn't pay a high price for the red car, we paid a fair price", "ma dafa3na si3ir ghaali 3ales-sayyaara el-Hamraa"),
        item("مب اليوم بيوصلون، بيوصلون بكرا لأن سفرهم تأخر", "They're not arriving today, they'll arrive tomorrow because their trip was delayed", "mub el-yoom bayoosaloon"),
    ]),

    lesson(21, "You Don't Have to Go", "ما لازم تروح", [
        item("ما لازم تروح الشغل بكرا لأنه يوم إجازة رسمية", "You don't have to go to work tomorrow because it's an official holiday", "ma laazim truuH esh-shaghal bukra li-annah yoom ijaaza rasmiyya"),
        item("ما لازم تدفع الحساب كله الحين، تقدر تدفع نصه بس", "You don't have to pay the whole bill now, you can pay just half of it", "ma laazim tidfa3 el-Hisaab killah el-heen"),
        item("ما لازم تلبس شي رسمي للمجلس، الملابس العادية زينة", "You don't have to wear anything formal for the majlis, regular clothes are fine", "ma laazim tilbas shay rasmi lil-majlis"),
        item("ما لازم تدرس كل الكتاب، بس الدروس الأولى للامتحان", "You don't have to study the whole book, just the first chapters for the exam", "ma laazim tadrus kil el-kitaab"),
    ]),

    lesson(22, "She Doesn't Have To, You All Don't Have To", "ما لازم تروح، ما لازم تروحون", [
        item("ما لازم تروح خالتي معنا، تقدر تجي بعدين لو تبغى", "My maternal aunt doesn't have to go with us, she can come later if she wants", "ma laazim truuH khaalti ma3ana"),
        item("ما لازم تروحون المطار كلكم، واحد بس يكفي يستقبله", "You all don't have to go to the airport, just one of you is enough to receive him", "ma laazim truu7oon el-mataar killkum"),
        item("ما لازم تدفعون كل الفلوس هالشهر، تقدرون تدفعون شوي شوي", "You all don't have to pay all the money this month, you can pay in installments", "ma laazim tidfa3oon kil el-fluus hash-shahar"),
        item("ما لازم تتصلون كل يوم، تتصلون كل أسبوع بس يكفي", "You all don't have to call every day, calling every week is enough", "ma laazim tittasiloon kil yoom, tittasiloon kil isboo3 bas yikfi"),
    ]),

    lesson(23, "I Don't Know, You Don't Want", "ما أدري، ما تبغى", [
        item("ما أدري وين المفتاح، شفت البيت كله وما لقيته", "I don't know where the key is, I looked through the whole house and didn't find it", "ma adri wein el-miftaaH, shift el-bayt killah wa ma ligeetah"),
        item("ما تبغى تسافر الحين، تبغى تخلص شغلك أول", "You don't want to travel now, you want to finish your work first", "ma tibgha tsaafir el-heen"),
        item("ما أدري ليش هو زعلان، ما قال لي شي عن السبب", "I don't know why he's upset, he didn't tell me anything about the reason", "ma adri leish huwa za3laan"),
        item("ما تبغى تروح لوحدها، تبغى حد يروح وياها", "She doesn't want to go alone, she wants someone to go with her", "ma tibgha truuH liwaHdaha, tibgha Had yruuH wiyaaha"),
    ]),

    lesson(24, "They Don't Know, We Don't Want", "ما يدرون، ما نبغى", [
        item("ما يدرون كم الساعة الحين لأن ساعاتهم كلها وقفت", "They don't know what time it is now because all their watches stopped", "ma yidroon kam es-saa3a el-heen"),
        item("ما لازم نتأخر على العرس، فلازم نطلع من الحين", "We must not be late to the wedding, so we must leave now", "ma laazim nit'akhkhar 3alal-3urs, fa-laazim nTla3 minal-heen"),
        item("ما يدرون وين يروحون هالصيف، يفكرون بأماكن كثير بس ما قررو", "They don't know where to go this summer, they're thinking of a lot of places but haven't decided", "ma yidroon wein yruu7oon has-sayf"),
        item("ما لازم نصرف كل فلوسنا على السفر، لازم نوفر شي عشان بعدين", "We shouldn't spend all our money on travel, we must save something for the future", "ma laazim nisrif kil fluusana 3ales-safar"),
    ]),

    lesson(25, "Review: Negation with Lazim, Know, Want", "مراجعة", [
        item("ما لازم تدري كل شي الحين، بس لازم تدري المهم بس", "You don't have to know all the details now, but you must know the important ones", "ma laazim tadri kil et-tafaaseel el-heen"),
        item("أبغى كل العائلة تجي معنا، مب أروح لوحدي", "I want the whole family to come with us, not go alone", "abgha kil el-ahl tiji ma3ana, mub aruuH liwaHdi"),
        item("ما يدرون ليش تأخرنا، ما قدرنا نتصل فيهم بسبب الجوال", "They don't know why we're late, we couldn't call them because of the phone", "ma yidroon leish ta'akhkharna"),
        item("ما لازم تبغى كل شي دفعة وحدة، بعض الأشياء تاخذ وقت", "You don't have to want everything at once, some things take time", "ma laazim tibgha kil shay daf3a waHda"),
    ]),

    lesson(26, "A Day of Negation", "يوم من النفي", [
        item("ما صحيت بدري اليوم، ما رحت الشغل، وما درست للامتحان", "I didn't wake up early today, I didn't go to work, and I didn't study for the exam", "ma SiHeet badri el-yoom"),
        item("ما طبخنا اليوم لأننا كنا متعبين، طلبنا من المطعم بدل", "We didn't cook today because we were tired, we ordered from the restaurant instead", "ma Tabakhna el-yoom li-annana kinna mut3ibeen"),
        item("ما اتصلو فينا اليوم، بس ما قلقنا لأنهم مشغولين دايما", "They didn't call us today, but we didn't worry because they're always busy", "ma ittasalaw feena el-yoom"),
        item("ما نظفت البيت اليوم، بكرا انشاالله عندي وقت أكثر", "I didn't clean the house today, tomorrow God willing I'll have more time", "ma nadhdhaft el-bayt el-yoom, bukra inshaallah 3indi wagt akthar"),
    ]),

    lesson(27, "Another Day of Negation", "يوم ثاني من النفي", [
        item("ما زرنا جدي هالأسبوع لأننا كنا مشغولين، بس بنزوره الجمعة", "We didn't visit my grandfather this week because we were busy, but we'll visit him on Friday", "ma zirna jiddi hal-isboo3"),
        item("ما سافرنا هالصيف لأن الفلوس ما كانت كافية، بس بنسافر الجاي", "We didn't travel this summer because the money wasn't enough, but we'll travel next", "ma saafarna has-sayf li-ann el-fluus ma kaanat kaafya"),
        item("ما شرينا شي جديد هالشهر، نوفر عشان نشري بيت أكبر", "We didn't buy anything new this month, we're saving to buy a bigger house", "ma sharayna shay jideed hash-shahar"),
        item("ما رحنا العرس لأننا كنا في السفر، بس اتصلنا فيهم من هناك", "We didn't go to the wedding because we were traveling, but we sent a gift", "ma riHna el-3urs li-annana kinna fis-safar"),
    ]),

    lesson(28, "Not Happy, Not Sad", "مب مبسوط، مب زعلان", [
        item("مب مبسوط ولا زعلان بالنتيجة، هي عادية مثل ما فكرت", "I'm neither happy nor sad about the result, it's normal like I expected", "mub mabsoot wala za3laan binateeja"),
        item("ما كانت مبسوطة بالعرس، بس ما كانت زعلانة كمان، كانت عادية", "She wasn't happy at the wedding, but she wasn't sad either, she was neutral", "ma kaanat mabsoota bil-3urs"),
        item("مب زعلانين من القرار، بس مستغربين شوي لأنه كان سريع", "We're not upset about the decision, but we're a bit surprised because it was fast", "mub za3laaneen minal-qaraar"),
        item("ما هو مبسوط بالشغل الجديد، بس ما هو زعلان، هو مستغرب بس", "He's not happy with the new job, but he's not upset either, he's confused", "ma huwa mabsoot bish-shughul el-jideed"),
    ]),

    lesson(29, "Friends, Family, and Negation", "الأصحاب والعائلة والنفي", [
        item("ما كل أصحابي ياو للعرس، بس أهم واحد يا وهذا يكفيني", "Not all my friends came to the wedding, but the most important one came and that's enough for me", "ma kil as7aabi yaw lil-3urs"),
        item("مب كل أهلي يعرفون بالخبر لسا، بنقول لهم شوي شوي", "Not all my family knows the news yet, we'll tell them little by little", "mub kil ahli ya3rifoon bil-khabar lissa"),
        item("ما صاحبي اتصل فيني، أنا اللي اتصلت فيه أول", "My friend didn't call me, I'm the one who called him first", "ma saaHbi ittasal feeni, ana elli ittasalt feeh awwal"),
        item("مب كل قريب زين مثل الأهل الحقيقيين، بس العائلة أهم من كل شي", "Not every relative is as good as the real family, but blood is more precious", "mub kil qareeb zayn mithil el-ahl el-Hageeqiyeen"),
    ]),

    lesson(30, "Review: B2 Recap", "مراجعة شاملة", [
        item("ما لازم تدري كل شي عن السفر، بس لازم تدري وين ومتى", "You don't have to know everything about the trip, but you must know where and when", "ma laazim tadri kil shay 3anis-safar"),
        item("مب مبسوط ولا زعلان، بس تعبان من كل هالشغل هالأسبوع", "I'm neither happy nor sad, just tired from all this work this week", "mub mabsoot wala za3laan, bas ta3baan min kil hash-shughul hal-isboo3"),
        item("ما كل أصحابي يدرون بالخبر، بس بيدرون قريب انشاالله", "Not all my friends know the news, but they'll know soon God willing", "ma kil as7aabi yidroon bil-khabar"),
        item("مب أخوي اللي قرر يسافر، أختي هي اللي قررت أول", "It wasn't my brother who decided to travel, my sister is the one who decided first", "mub akhooy elli qarrar ysaafir"),
    ]),

    lesson(31, "Professions, No Work Today", "المهن، ما فيه شغل اليوم", [
        item("المهندسة ما تشتغل اليوم لأنه يوم إجازة رسمية بالبلد", "The engineer isn't working today because it's an official holiday in the country", "el-muhandisa ma tashtaghil el-yoom"),
        item("المترجم ما عنده اجتماعات اليوم، فقرر يرتاح شوي بالبيت", "The translator doesn't have meetings today, so he decided to rest a bit at home", "el-mutarjim ma 3indah ijtimaa3aat el-yoom"),
        item("التاجر ما فتح محله اليوم لأنه سافر يشري أشياء جديدة للمحل", "The merchant didn't open his shop today because he traveled to buy new things for the shop", "et-taajir ma fataH maHallah el-yoom"),
        item("المدرسة ما درّست اليوم لأن الطلاب عندهم امتحان ثاني اليوم", "The teacher didn't teach today because the students have an exam in another subject", "el-mudarrisa ma darrasat el-yoom"),
    ]),

    lesson(32, "Not Wanting Food", "ما أبغى أكل", [
        item("ما أبغى أكل الحين، اكلت كثير بالفطور ولسا شبعان", "I don't want to eat now, I ate a lot at breakfast and I'm still full", "ma abgha akal el-heen"),
        item("ما تبغى اللحم اليوم، تبغى سلطة وشي خفيف بس", "She doesn't want meat today, she wants salad and something light only", "ma tibgha el-la7am el-yoom"),
        item("أبغى أطلب من المطعم اليوم، مب أطبخ، عشان أرتاح", "I want to order from the restaurant today, not cook, in order to rest", "abgha aTlub minal-mat3am el-yoom, mub aTbakh, 3ashaan artaaH"),
        item("ما يبغى قهوة ثانية، شرب كثير من الصبح", "He doesn't want another coffee, he drank a lot since morning", "ma yibgha gahwa thaanya, sharab katheer mines-sub7"),
    ]),

    lesson(33, "Clothes, Not Having", "الملابس، ما عندي", [
        item("ما عندي قميص يناسب هالعرس، لازم أروح أشري واحد جديد", "I don't have a shirt that suits this wedding, I need to go buy a new one", "ma 3indi gamees ynaasib hal-3urs"),
        item("ما عندها عباية سوداء، عندها بس الأزرق والأخضر", "She doesn't have a black abaya, she only has blue and green", "ma 3indaha 3abaaya sawdaa"),
        item("ما عندهم جوتي يناسب الشتاء، لازم يشرون قبل ما يصير الجو بارد", "They don't have shoes suitable for winter, they need to buy before the weather gets cold", "ma 3indahum jooti ynaasib esh-shita"),
        item("ما عندي غترة نظيفة اليوم، لازم أغسل واحدة بسرعة", "I don't have a clean headdress today, I need to wash one quickly", "ma 3indi ghitra nadheefa el-yoom"),
    ]),

    lesson(34, "Clothes, Not Having II", "الملابس، ما عندي ٢", [
        item("ما عندنا ملابس دافية كافية للأطفال هالشتاء", "We don't have enough warm clothes for the children this winter", "ma 3indana malaabis daafya kaafya lil-aTfaal hash-shita"),
        item("ما عنده قحفية تناسب الغترة الجديدة، لازم يشري ثانية", "He doesn't have a skull cap that matches the new headdress, he needs to buy another", "ma 3indah ga7fiyya tnaasib el-ghitra el-jideeda"),
        item("ما عندها دلاغات نظيفة، كلها وسخة من أمس", "She doesn't have clean socks, they're all in the washer since yesterday", "ma 3indaha dallaghaat nadheefa"),
        item("ما عندنا وقت نشري ملابس جديدة قبل السفر، بنشري هناك", "We don't have time to buy new clothes before the trip, we'll buy there", "ma 3indana wagt nishri malaabis jideeda gabl es-safar"),
    ]),

    lesson(35, "Not Eating", "ما آكل", [
        item("ما آكل لحم كثير، أفضل السمك والسلطة أكثر", "I don't eat a lot of meat, I prefer fish and salad more", "ma aakil la7am katheer"),
        item("ما تاكل قبل الرياضة، تحس بتعب لو اكلت", "She doesn't eat before exercise, she feels tired if she eats", "ma taakil gabl er-riyaada"),
        item("ما يحبون الأكل بسرعة، يحبون ياخذون وقتهم زين", "They don't like eating quickly, they like taking their time", "ma yiHibboon el-akal bisur3a"),
        item("ما أكلنا في المطعم أمس، طبخنا بالبيت لأنه أرخص وألذ", "We didn't eat at the restaurant yesterday, we cooked at home because it's cheaper and tastier", "ma akalna fil-mat3am ams"),
    ]),

    lesson(36, "Not Working", "ما أشتغل", [
        item("ما أشتغل يوم السبت هالأسبوع لأن عندي إجازة", "I'm not working on Saturday this week because I have a vacation", "ma ashtaghil yoom es-sabt hal-isboo3"),
        item("ما تشتغل من البيت، تفضل تروح المكتب كل يوم", "She doesn't work from home, she prefers to go to the office every day", "ma tashtaghil minal-bayt"),
        item("ما نشتغل سوا بنفس المشروع، كل واحد له مشروعه", "We don't work together on the same project, each one has their own project", "ma nashtaghil sawa binafs el-mashroo3"),
        item("ما يشتغلون بعد المغرب، الشركة تسكر الساعة خمسة", "They don't work after sunset, the company closes its doors at five o'clock", "ma yashtaghiloon ba3d el-maghrib"),
    ]),

    lesson(37, "Not This, But That", "مب هذا، بس هذاك", [
        item("مب هذا اللي طلبته، طلبت قهوة بدون سكر وهذي فيها سكر", "This isn't what I ordered, I ordered coffee without sugar and this has sugar", "mub haadha elli Talabtah"),
        item("مب هذي الطريق الصح للمطار، الطريق الصح من هناك", "This isn't the right way to the airport, the right way is from there", "mub haadhi eT-Tareeg es-saHH lil-mataar"),
        item("مب هذا السعر الصح، السعر الصح أرخص بعشرين", "This isn't the right price, the right price is cheaper by twenty", "mub haadha es-si3ir es-saHH"),
        item("مب هذي المشكلة الحقيقية، المشكلة الحقيقية إننا ما تكلمنا زين", "This isn't the real problem, the real problem is that we didn't communicate well", "mub haadhi el-mushkila el-Hageeqiyya"),
    ]),

    lesson(38, "Not Coming", "ما بيجي", [
        item("ما بيجي أخوي للعرس لأنه سافر لبلد ثاني هالأسبوع", "My brother isn't coming to the wedding because he's traveling outside the country this week", "ma bayiji akhooy lil-3urs"),
        item("ما تجي خالتي معنا اليوم، عندها موعد ثاني في نفس الوقت", "My maternal aunt isn't coming with us today, she has another appointment at the same time", "ma tiji khaalti ma3ana el-yoom"),
        item("ما ييت للاجتماع أمس لأني كنت مريض، بس اتصلت فيهم بعدين", "I didn't come to the meeting yesterday because I was sick, but I sent a report", "ma yeet lil-ijtimaa3 ams li-anni kint mareed"),
        item("ما ياو المدرسة أمس، الجو كان سيء كثير وسكرو المدرسة", "They didn't come to school yesterday, the weather was very bad and they closed the school", "ma yaaw el-madrasa ams"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/b2.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "b2", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/b2.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
