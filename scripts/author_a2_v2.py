#!/usr/bin/env python3
"""Full rewrite of A2 Khaleeji Arabic content -- same fix as A1: real
topical variety and natural information content instead of one template
("X home yesterday, saw the family, good") copy-pasted across every
person/lesson. Draws on the newly expanded verb paradigms in
data/emirati-research/researched_vocab.json (VISIT/STUDY/UNDERSTAND/
DO_MAKE/THINK/TEACH/TRAVEL, plus upgraded SLEEP/LOVE/CLEAN/SEE_PRESENT).
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
    lesson(1, "I Went, You Went", "رحت، رحت", [
        item("رحت السوق أمس", "I went to the market yesterday", "riHt es-suug ams"),
        item("رحت المستشفى أمس؟", "Did you (m) go to the hospital yesterday?", "riHt el-mustashfa ams?"),
        item("رحتي المطعم أمس", "You (f) went to the restaurant yesterday", "riHti el-mat3am ams"),
        item("راح بيت خاله أمس", "He went to his maternal uncle's house yesterday", "raaH bayt khaalah ams"),
    ], topicId="a2-past-raah"),

    lesson(2, "She Went, We Went, They Went", "راحت، رحنا، راحو", [
        item("راحت المدرسة أمس", "She went to school yesterday", "raaHat el-madrasa ams"),
        item("رحنا المسجد يوم الجمعة", "We went to the mosque on Friday", "riHna el-masjid yoom el-jum3a"),
        item("رحتو وين أمس؟", "Where did you all go yesterday?", "riHtaw wein ams?"),
        item("راحو بيت جدهم أمس", "They went to their grandfather's house yesterday", "raaHaw bayt jiddahum ams"),
    ]),

    lesson(3, "Where Did You Go Yesterday?", "وين رحت أمس؟", [
        item("وين رحت أمس؟ رحت السوق", "Where did you go yesterday? I went to the market", "wein riHt ams? riHt es-suug"),
        item("وين راح خالك أمس؟ راح الشغل", "Where did your uncle go yesterday? He went to work", "wein raaH khaalak ams? raaH esh-shaghal"),
        item("وين راحت يمك أمس؟ راحت السوق", "Where did your mom go yesterday? She went to the market", "wein raaHat yummak ams? raaHat es-suug"),
        item("وين راحو أهلك أمس؟ راحو بيت جدهم", "Where did your family go yesterday? They went to their grandfather's house", "wein raaHaw ahlak ams? raaHaw bayt jiddahum"),
    ]),

    lesson(4, "Going Tomorrow", "رايح بكرا", [
        item("بروح المطعم بكرا", "I'll go to the restaurant tomorrow", "baruuH el-mat3am bukra"),
        item("بتروح الشغل بكرا؟", "Will you go to work tomorrow?", "batruuH esh-shaghal bukra?"),
        item("بيروح السوق بكرا", "He'll go to the market tomorrow", "bayruuH es-suug bukra"),
        item("بنروح بيت جدي بكرا", "We'll go to my grandfather's house tomorrow", "banruuH bayt jiddi bukra"),
    ], topicId="a2-future-b"),

    lesson(5, "Review: Past Tense of Raah", "مراجعة: راح", [
        item("رحت المسجد، وشفت خالي هناك", "I went to the mosque, and I saw my uncle there", "riHt el-masjid, wa shift khaali hinaak"),
        item("راحت السوق، وشرت غترة جديدة", "She went to the market, and bought a new headdress", "raaHat es-suug, wa ishtarat ghitra jideeda"),
        item("راحو المطعم أمس، والأكل كان لذيذ", "They went to the restaurant yesterday, and the food was delicious", "raaHaw el-mat3am ams, wal-akal kaan latheeth"),
        item("ما رحنا الشغل يوم الجمعة", "We didn't go to work on Friday", "ma riHna esh-shaghal yoom el-jum3a"),
    ]),

    lesson(6, "I Saw, You Saw", "شفت، شفت", [
        item("شفت جدي أمس في السوق", "I saw my grandfather yesterday at the market", "shift jiddi ams fis-suug"),
        item("شفت سيارة جديدة أمس؟", "Did you (m) see a new car yesterday?", "shift sayyaara jideeda ams?"),
        item("شفتي البيت الجديد؟", "Did you (f) see the new house?", "shifti el-bayt el-jideed?"),
        item("شاف صديقه في المطعم أمس", "He saw his friend at the restaurant yesterday", "shaaf sadeegah fil-mat3am ams"),
    ], topicId="a2-past-shaaf"),

    lesson(7, "She Saw, We Saw, They Saw", "شافت، شفنا، شافو", [
        item("شافت طبيبة زينة في المستشفى", "She saw a good doctor at the hospital", "shaafat tabeeba zeena fil-mustashfa"),
        item("شفنا جمل كبير في الصحراء", "We saw a big camel in the desert", "shifna jamal kabeer fis-sa7raa"),
        item("شفتو الجو أمس؟ كان بارد", "Did you all see the weather yesterday? It was cold", "shiftaw el-jaww ams? kaan baarid"),
        item("شافو بيت خالتهم الجديد", "They saw their maternal aunt's new house", "shaafaw bayt khaaltahum el-jideed"),
    ]),

    lesson(8, "What Did You See?", "شنو شفت؟", [
        item("شنو شفت في السوق؟ شفت غترة زينة", "What did you see at the market? I saw a nice headdress", "shinu shift fis-suug? shift ghitra zeena"),
        item("منو شفت في المطعم؟ شفت خالي", "Who did you see at the restaurant? I saw my uncle", "minu shift fil-mat3am? shift khaali"),
        item("وين شفتها؟ شفتها في المدرسة", "Where did you see her? I saw her at school", "wein shiftaha? shiftaha fil-madrasa"),
        item("شفت طيرين في السماء", "I saw two birds in the sky", "shift tayreen fis-samaa"),
    ]),

    lesson(9, "Combining Raah and Shaaf", "راح وشاف", [
        item("راح المطار وشاف الطيارة", "He went to the airport and saw the airplane", "raaH el-mataar wa shaaf et-tayyaara"),
        item("رحت المستشفى وشفت الطبيب", "I went to the hospital and saw the doctor", "riHt el-mustashfa wa shift et-tabeeb"),
        item("راحت المطعم وشافت صديقتها هناك", "She went to the restaurant and saw her friend there", "raaHat el-mat3am wa shaafat sadeegtaha hinaak"),
        item("رحنا السوق وشفنا أشياء زينة كثير", "We went to the market and saw a lot of nice things", "riHna es-suug wa shifna ashyaa zeena katheer"),
    ]),

    lesson(10, "Review: Past Tense of Shaaf", "مراجعة: شاف", [
        item("شفت الجو أمس، كان حار كثير", "I saw the weather yesterday, it was very hot", "shift el-jaww ams, kaan Haarr katheer"),
        item("ما شفنا أحد في البيت أمس", "We didn't see anyone at the house yesterday", "ma shifna a7ad fil-bayt ams"),
        item("شافو القمر أمس بالليل", "They saw the moon last night", "shaafaw el-gamar ams bil-layl"),
        item("شفتي مدرستك الجديدة؟", "Did you (f) see your new school?", "shifti madrastik el-jideeda?"),
    ]),

    lesson(11, "I Didn't Go, I Didn't See", "ما رحت، ما شفت", [
        item("ما رحت الشغل أمس، كنت تعبان", "I didn't go to work yesterday, I was tired", "ma riHt esh-shaghal ams, kint ta3baan"),
        item("ما شفت الأهل أمس، كانو مشغولين", "I didn't see the family yesterday, they were busy", "ma shift el-ahl ams, kaanaw mashghooleen"),
        item("ما راح المدرسة يوم الجمعة", "He didn't go to school on Friday", "ma raaH el-madrasa yoom el-jum3a"),
        item("ما شافت خالتها الأسبوع الماضي", "She didn't see her maternal aunt last week", "ma shaafat khaaltaha el-isboo3 el-maadi"),
    ], topicId="a2-past-negation"),

    lesson(12, "She Didn't, We Didn't", "ما راحت، ما رحنا", [
        item("ما راحت السوق، كانت مريضة", "She didn't go to the market, she was sick", "ma raaHat es-suug, kaanat mareeda"),
        item("ما رحنا المطعم أمس، طبخنا بالبيت", "We didn't go to the restaurant yesterday, we cooked at home", "ma riHna el-mat3am ams, tabakhna bil-bayt"),
        item("ما راحو المسجد يوم الجمعة", "They didn't go to the mosque on Friday", "ma raaHaw el-masjid yoom el-jum3a"),
        item("ما شفنا الطيارة، كانت بعيدة", "We didn't see the airplane, it was far", "ma shifna et-tayyaara, kaanat ba3eeda"),
    ]),

    lesson(13, "Yesterday and Tomorrow", "أمس وبكرا", [
        item("أمس رحت المستشفى، وبكرا بروح المدرسة", "Yesterday I went to the hospital, and tomorrow I'll go to school", "ams riHt el-mustashfa, wa bukra baruuH el-madrasa"),
        item("شفت خالي أمس، وبكرا بشوف عمي", "I saw my uncle yesterday, and tomorrow I'll see my paternal uncle", "shift khaali ams, wa bukra bashoof 3ammi"),
        item("أمس كان الجو حار، وبكرا بارد انشاالله", "Yesterday the weather was hot, and tomorrow it'll be cold, God willing", "ams kaan el-jaww Haarr, wa bukra baarid inshaallah"),
        item("طبخنا لحم أمس، وبكرا بنطبخ سلطة", "We cooked meat yesterday, and tomorrow we'll cook salad", "tabakhna la7am ams, wa bukra bantbakh salata"),
    ]),

    lesson(14, "Family and Past Tense", "العائلة والماضي", [
        item("جدي راح المسجد كل جمعة", "My grandfather goes to the mosque every Friday", "jiddi raaH el-masjid kil jum3a"),
        item("خالتي شافت الطبيبة أمس", "My maternal aunt saw the doctor yesterday", "khaalti shaafat et-tabeeba ams"),
        item("أخوي راح السوق وشرى جوتي جديد", "My brother went to the market and bought new shoes", "akhooy raaH es-suug wa ishtara jooti jideed"),
        item("حفيدي شاف الجمل أول مرة أمس", "My grandson saw a camel for the first time yesterday", "Hafeedi shaaf el-jamal awwal marra ams"),
    ]),

    lesson(15, "Review: Past Tense Negation", "مراجعة: النفي في الماضي", [
        item("ما رحت السوق أمس، كنت مشغول", "I didn't go to the market yesterday, I was busy", "ma riHt es-suug ams, kint mashghool"),
        item("شفت الأهل، بس ما شفت خالي", "I saw the family, but I didn't see my uncle", "shift el-ahl, bas ma shift khaali"),
        item("راحت المدرسة، بس ما شافت صديقتها", "She went to school, but she didn't see her friend", "raaHat el-madrasa, bas ma shaafat sadeegtaha"),
        item("ما راحو المطعم أمس، طبخو بالبيت", "They didn't go to the restaurant yesterday, they cooked at home", "ma raaHaw el-mat3am ams, Tabakhaw bil-bayt"),
    ]),

    lesson(16, "Numbers and Past Tense", "الأرقام والماضي", [
        item("شفت ثلاث طيارات في المطار", "I saw three airplanes at the airport", "shift thalaath tayyaaraat fil-mataar"),
        item("راح خمسة من الأهل للمطعم أمس", "Five of the family went to the restaurant yesterday", "raaH khamsa min el-ahl lil-mat3am ams"),
        item("شريت عشرة جوتيات من السوق", "I bought ten pairs of shoes from the market", "ishtarayt 3ashara jootiyaat min es-suug"),
        item("رحنا سبعة أيام للسفر", "We went for seven days of travel", "riHna sab3a ayyaam lis-safar"),
    ]),

    lesson(17, "Colors and Past Tense", "الألوان والماضي", [
        item("شريت قميص أحمر أمس", "I bought a red shirt yesterday", "ishtarayt gamees a7mar ams"),
        item("شفت سيارة زرقاء في السوق", "I saw a blue car at the market", "shift sayyaara zarqaa fis-suug"),
        item("راحت وشرت غترة بيضاء", "She went and bought a white headdress", "raaHat wa ishtarat ghitra baydaa"),
        item("خالي عنده سيارة صفراء جديدة", "My maternal uncle has a new yellow car", "khaali 3indah sayyaara safraa jideeda"),
    ]),

    lesson(18, "Feelings and Past Tense", "المشاعر والماضي", [
        item("كنت تعبان أمس، بس اليوم زين", "I was tired yesterday, but today I'm good", "kint ta3baan ams, bas el-yoom zayn"),
        item("كانت مبسوطة أمس في العرس", "She was happy at the wedding yesterday", "kaanat mabsoota ams fil-3urs"),
        item("كانو جوعانين بعد السفر", "They were hungry after the trip", "kaanaw joo3aaneen ba3d es-safar"),
        item("كنا زعلانين لأن ما شفنا الأهل", "We were sad because we didn't see the family", "kinna za3laaneen li-ann ma shifna el-ahl"),
    ]),

    lesson(19, "Money and Past Tense", "الفلوس والماضي", [
        item("دفعت فلوس كثير في السوق أمس", "I spent a lot of money at the market yesterday", "sarafit fluus katheer fis-suug ams"),
        item("كان القميص غالي، بس شريته", "The shirt was expensive, but I bought it", "kaan el-gamees ghaali, bas ishtaraytah"),
        item("دفعنا الحساب وطلعنا من المطعم", "We paid the bill and left the restaurant", "difa3na el-Hisaab wa Tala3na min el-mat3am"),
        item("كانت الجوتي رخيصة، فشريت اثنين", "The shoes were cheap, so I bought two", "kaanat el-jooti rakheesa, fa-ishtarayt ithnayn"),
    ]),

    lesson(20, "Review: Numbers, Colors, Feelings, Money", "مراجعة", [
        item("دفعت خمسة على القميص الأحمر", "I paid five for the red shirt", "dafa3t khamsa 3alal-gamees el-a7mar"),
        item("كنا مبسوطين لأن الفلوس رخيصة", "We were happy because the prices were cheap", "kinna mabsooteen li-ann el-as3aar rakheesa"),
        item("دفعنا عشرة على الأكل أمس", "We spent ten on food yesterday", "sarafna 3ashara 3ala el-akal ams"),
        item("كانت السيارة الزرقاء غالية كثير", "The blue car was very expensive", "kaanat es-sayyaara ez-zarqaa ghaalya katheer"),
    ]),

    lesson(21, "Days with Past Tense", "الأيام والماضي", [
        item("يوم الأحد رحت الشغل، ويوم الاثنين رحت المدرسة", "On Sunday I went to work, and on Monday I went to school", "yoom el-a7ad riHt esh-shaghal, wa yoom el-ithnayn riHt el-madrasa"),
        item("يوم الجمعة الماضي شفنا الأهل كلهم", "Last Friday we saw all the family", "yoom el-jum3a el-maadi shifna el-ahl killahum"),
        item("يوم السبت طبخت لحم للأهل", "On Saturday I cooked meat for the family", "yoom es-sabt Tabakht la7am lil-ahl"),
        item("الأسبوع الماضي سافرنا للكويت", "Last week we traveled to Kuwait", "el-isboo3 el-maadi saafarna lil-kuwayt"),
    ], topicId="a2-days-past"),

    lesson(22, "Places with Past Tense", "الأماكن والماضي", [
        item("رحت السوق، وبعدين رحت المطعم", "I went to the market, and then I went to the restaurant", "riHt es-suug, wa ba3dayn riHt el-mat3am"),
        item("طلعنا من البيت وقعدنا في المسجد", "We left the house and sat in the mosque", "Tala3na min el-bayt wa ga3adna fil-masjid"),
        item("راح المطار الصبح ورجع الليل", "He went to the airport in the morning and returned at night", "raaH el-mataar es-sub7 wa raja3 el-layl"),
        item("زرت جدي في بيته أمس", "I visited my grandfather at his house yesterday", "zirt jiddi fi baytah ams"),
    ]),

    lesson(23, "Money and Shopping in the Past", "الفلوس والتسوق في الماضي", [
        item("شريت غترة وقميص من السوق", "I bought a headdress and a shirt from the market", "ishtarayt ghitra wa gamees min es-suug"),
        item("دفعت خمسين على العباية", "I paid fifty for the abaya", "dafa3t khamseen 3ala el-3abaaya"),
        item("كانت الجوتي بأربعين، فشريتها", "The shoes were at forty, so I bought them", "kaanat el-jooti bi-arba3een, fa-ishtaraytaha"),
        item("طلع من السوق وما شرى شي", "He left the market and didn't buy anything", "Tala3 min es-suug wa ma shara shay"),
    ]),

    lesson(24, "Big and Small in the Past", "كبير وصغير في الماضي", [
        item("البيت القديم كان صغير، والجديد كبير", "The old house was small, and the new one is big", "el-bayt el-gadeem kaan sagheer, wal-jideed kabeer"),
        item("كانت السيارة كبيرة وغالية كثير", "The car was big and very expensive", "kaanat es-sayyaara kabeera wa ghaalya katheer"),
        item("شرى غترة صغيرة لابنه", "He bought a small headdress for his son", "ishtara ghitra sagheera li-ibnah"),
        item("كان الفنجان صغير، بس الدلة كبيرة", "The cup was small, but the dallah was big", "kaan el-finjaan sagheer, bas ed-dalla kabeera"),
    ]),

    lesson(25, "Review: Days, Places, Money, Size", "مراجعة", [
        item("يوم الجمعة رحت المسجد وزرت جدي بعدين", "On Friday I went to the mosque and then visited my grandfather", "yoom el-jum3a riHt el-masjid wa zirt jiddi ba3dayn"),
        item("دفعت فلوس كثير على البيت الكبير", "I paid a lot of money for the big house", "dafa3t fluus katheer 3ala el-bayt el-kabeer"),
        item("رحنا السوق الصغير لأنه قريب", "We went to the small market because it's near", "riHna es-suug es-sagheer li-annah gareeb"),
        item("طلعنا من المطعم ورحنا بيت خالي", "We left the restaurant and went to my uncle's house", "Tala3na min el-mat3am wa riHna bayt khaali"),
    ]),

    lesson(26, "I Drank and I Saw", "شربت وشفت", [
        item("شربت قهوة وشفت جدي في المجلس", "I drank coffee and saw my grandfather in the majlis", "sharabt gahwa wa shift jiddi fil-majlis"),
        item("شربنا شاي وشفنا القمر من الدريشة", "We drank tea and saw the moon from the window", "sharabna shaay wa shifna el-gamar min ed-dreesha"),
        item("شربت مويه بعد ما رحت الشغل", "I drank water after I went to work", "sharabt moya ba3d ma riHt esh-shaghal"),
        item("شربو قهوة وشافو الطيور في السماء", "They drank coffee and saw the birds in the sky", "sharabaw gahwa wa shaafaw et-tuyoor fis-samaa"),
    ]),

    lesson(27, "Feelings Yesterday and Today", "المشاعر أمس واليوم", [
        item("كنت زعلان أمس، بس اليوم مبسوط", "I was sad yesterday, but today I'm happy", "kint za3laan ams, bas el-yoom mabsoot"),
        item("كانت تعبانة أمس، واليوم زينة", "She was tired yesterday, and today she's good", "kaanat ta3baana ams, wal-yoom zeena"),
        item("كنا جوعانين بعد السفر، واليوم شبعانين", "We were hungry after the trip, and today we're full", "kinna joo3aaneen ba3d es-safar, wal-yoom shab3aaneen"),
        item("كان مريض الأسبوع الماضي، واليوم زين", "He was sick last week, and today he's well", "kaan mareed el-isboo3 el-maadi, wal-yoom zayn"),
    ]),

    lesson(28, "Family Recombined", "العائلة من جديد", [
        item("خالي وعمي راحو السفر مع بعض", "My maternal uncle and paternal uncle traveled together", "khaali wa 3ammi raaHaw es-safar ma3 ba3ad"),
        item("جدتي طبخت للعائلة كلها أمس", "My grandmother cooked for the whole family yesterday", "jiddati Tabakhat lil-3aa'ila killaha"),
        item("حفيدتي درست في المدرسة الجديدة", "My granddaughter studied at the new school", "Hafeedati darasat fil-madrasa el-jideeda"),
        item("ابن عمي زارنا الأسبوع الماضي", "My paternal cousin visited us last week", "ibin 3ammi zaarna el-isboo3 el-maadi"),
    ]),

    lesson(29, "Questions About the Past", "أسئلة عن الماضي", [
        item("متى رحت السوق؟ رحت أمس", "When did you go to the market? I went yesterday", "mita riHt es-suug? riHt ams"),
        item("كم دفعت على القميص؟ دفعت ثلاثين", "How much did you pay for the shirt? I paid thirty", "kam dafa3t 3ala el-gamees? dafa3t thalaatheen"),
        item("منو زار جدك أمس؟ زاره عمي", "Who visited your grandfather yesterday? My paternal uncle visited him", "minu zaar jiddak ams? zaarah 3ammi"),
        item("ليش ما رحت الشغل أمس؟ كنت مريض", "Why didn't you go to work yesterday? I was sick", "leish ma riHt esh-shaghal ams? kint mareed"),
    ]),

    lesson(30, "Review: A2 Recap", "مراجعة شاملة", [
        item("رحت السوق أمس وشريت غترة حمراء", "I went to the market yesterday and bought a red headdress", "riHt es-suug ams wa ishtarayt ghitra Hamraa"),
        item("ما شفنا خالتنا الأسبوع الماضي، بنزورها بكرا", "We didn't see our maternal aunt last week, we'll visit her tomorrow", "ma shifna khaaltana el-isboo3 el-maadi, banzooraha bukra"),
        item("كان السفر زين، وشفنا أشياء جديدة كثير", "The trip was good, and we saw a lot of new things", "kaan es-safar zayn, wa shifna ashyaa jideeda katheer"),
        item("طبخنا وأكلنا وبعدين رحنا المسجد", "We cooked and ate, and then we went to the mosque", "Tabakhna wa akalna wa ba3dayn riHna el-masjid"),
    ]),

    lesson(31, "Professions Yesterday", "المهن أمس", [
        item("أبويه اشتغل في المكتب أمس", "Dad worked at the office yesterday", "abooyah ishtaghal fil-maktab ams"),
        item("المهندسة زارت المكتب الجديد أمس", "The engineer visited the new office yesterday", "el-muhandisa zaarat el-maktab el-jideed ams"),
        item("الدريول راح المطار مرة ثانية أمس", "The driver went to the airport again yesterday", "ed-daryool raaH el-mataar marra thaanya ams"),
        item("الطبيبة شافت مرضى كثير أمس", "The doctor saw a lot of patients yesterday", "et-tabeeba shaafat marda katheer ams"),
    ]),

    lesson(32, "Professions Yesterday II", "المهن أمس ٢", [
        item("المترجم فهم كل شي في المكتب", "The translator understood everything at the office", "el-mutarjim fihim kil shay fil-maktab"),
        item("التاجر شرى أشياء كثير من السوق أمس", "The merchant bought a lot of things from the market yesterday", "et-taajir shara ashyaa katheer min es-suug ams"),
        item("المدرس درّس الطلاب درس جديد", "The teacher taught the students a new lesson", "el-mudarris darras et-tullaab dars jideed"),
        item("السكرتيرة نظفت المكتب الصبح", "The secretary cleaned the office in the morning", "es-sikirteera nadhdhafat el-maktab es-sub7"),
    ]),

    lesson(33, "Getting Around by Train", "بالقطار", [
        item("سافرنا بالقطار للسعودية", "We traveled by train to Saudi Arabia", "saafarna bil-gitaar lis-sa3oodiyya"),
        item("القطار أسرع من الباص", "The train is faster than the bus", "el-gitaar asra3 min el-baas"),
        item("رحنا بالباص لأن القطار كان بعيد", "We went by bus because the train was far", "riHna bil-baas li-ann el-gitaar kaan ba3eed"),
        item("وصل القطار متأخر أمس", "The train arrived late yesterday", "wisal el-gitaar mit'akhkhir ams"),
    ]),

    lesson(34, "Clothes, Wanting", "الملابس، أبغى", [
        item("أبغى قميص أزرق للشغل", "I want a blue shirt for work", "abgha gamees azraq lish-shaghal"),
        item("خالتي تبغى عباية جديدة للعرس", "My maternal aunt wants a new abaya for the wedding", "khaalti tibgha 3abaaya jideeda lil-3urs"),
        item("يبغى غترة بيضاء زينة", "He wants a nice white headdress", "yibgha ghitra baydaa zeena"),
        item("أبغى جوتي مريح للسفر", "I want comfortable shoes for the trip", "abgha jooti mureeH lis-safar"),
    ]),

    lesson(35, "Clothes, Wanting II", "الملابس، أبغى ٢", [
        item("ما أبغى بنطلون غالي، أبغى رخيص", "I don't want expensive pants, I want cheap ones", "ma abgha bantaloon ghaali, abgha rakhees"),
        item("تبغى قحفية جديدة لابنك؟", "Do you want a new skull cap for your son?", "tibgha ga7fiyya jideeda li-ibnak?"),
        item("أبغى دلاغات دافية للشتاء", "I want warm socks for winter", "abgha dallaghaat daafya lish-shita"),
        item("عمتي تبغى عباية سوداء وقميص أبيض", "My paternal aunt wants a black abaya and a white shirt", "3ammati tibgha 3abaaya sawdaa wa gamees abyad"),
    ]),

    lesson(36, "Food, Wanting", "الأكل، أبغى", [
        item("أبغى تمر وقهوة بعد الأكل", "I want dates and coffee after the meal", "abgha tamur wa gahwa ba3d el-akal"),
        item("تبغى سلطة زينة مع اللحم؟", "Do you want a nice salad with the meat?", "tibgha salata zeena ma3 el-la7am?"),
        item("يبغى بيض ولحم للفطور", "He wants eggs and meat for breakfast", "yibgha bayd wa la7am lil-futoor"),
        item("أبغى أكل لذيذ في المطعم الجديد", "I want delicious food at the new restaurant", "abgha akal latheeth fil-mat3am el-jideed"),
    ]),

    lesson(37, "Food, Wanting II", "الأكل، أبغى ٢", [
        item("أبغى فنجان قهوة وشوي تمر", "I want a cup of coffee and a bit of dates", "abgha finjaan gahwa wa shway tamur"),
        item("ما أبغى أكل غالي، أبغى شي رخيص ولذيذ", "I don't want expensive food, I want something cheap and delicious", "ma abgha akal ghaali, abgha shay rakhees wa latheeth"),
        item("يبغى سلطة وبيض كل صباح", "He wants salad and eggs every morning", "yibgha salata wa bayd kil sabaaH"),
        item("تبغى قهوة ثانية؟ تفضل", "Do you want a second coffee? Please, go ahead", "tibgha gahwa thaanya? tfaddal"),
    ]),

    lesson(38, "Furniture", "الأثاث", [
        item("شرينا طاولة وكراسي جديدة للمطبخ", "We bought a new table and chairs for the kitchen", "ishtarayna Taawla wa karaasi jideeda lil-matbakh"),
        item("الكرسي القديم صغير ومب مريح", "The old chair is small and not comfortable", "el-kursi el-gadeem sagheer wa mub mureeH"),
        item("الصحون فوق الطاولة", "The plates are on top of the table", "es-suHoon fooq eT-Taawla"),
        item("الباب الجديد أزيان من القديم", "The new door is nicer than the old one", "el-baab el-jideed azyan min el-gadeem"),
    ]),

    lesson(39, "Numbers 30-60", "الأرقام ٣٠-٦٠", [
        item("عندي ثلاثين درس هذا الأسبوع", "I have thirty lessons this week", "3indi thalaatheen dars haadha el-isboo3"),
        item("دفعت أربعين على الجوتي", "I paid forty for the shoes", "dafa3t arba3een 3ala el-jooti"),
        item("سافرنا خمسين دقيقة بالسيارة", "We traveled fifty minutes by car", "saafarna khamseen dageega bis-sayyaara"),
        item("خالي عنده ستين كتاب في بيته", "My maternal uncle has sixty books in his house", "khaali 3indah sitteen kitaab fi baytah"),
    ]),

    lesson(40, "Numbers 70-100", "الأرقام ٧٠-١٠٠", [
        item("شرينا سبعين كيلو تمر للعيد", "We bought seventy kilos of dates for Eid", "ishtarayna sab3een keelo tamur lil-3eed"),
        item("عندهم ثمانين طالب في المدرسة", "They have eighty students at the school", "3indahum thamaaneen Taalib fil-madrasa"),
        item("دفعنا تسعين على العشاء أمس", "We paid ninety for dinner yesterday", "dafa3na tis3een 3ala el-3ashaa ams"),
        item("عندي مية درهم بس", "I only have a hundred", "3indi miya bas"),
    ]),

    lesson(41, "She Cooks, We Cook", "تطبخ، نطبخ", [
        item("تطبخ سلطة زينة كل يوم", "She cooks good salad every day", "tatbakh salata zeena kil yoom"),
        item("نطبخ للعائلة كلها يوم الجمعة", "We cook for the whole family on Friday", "natbakh lil-3aa'ila killaha yoom el-jum3a"),
        item("انتوا تطبخون أكل خليجي؟", "Do you all cook Khaleeji food?", "intu tatbakhoon akal khaleeji?"),
        item("يطبخون لحم وتمر للضيوف", "They cook meat and dates for the guests", "yatbakhoon la7am wa tamur lidh-dhuyoof"),
    ]),

    lesson(42, "I Cooked, You Cooked", "طبخت، طبخت", [
        item("طبخت للأهل كلهم أمس", "I cooked for the whole family yesterday", "Tabakht lil-ahl killahum ams"),
        item("طبخت سلطة زينة أمس؟", "Did you (m) cook a good salad yesterday?", "Tabakht salata zeena ams?"),
        item("طبخ لحم وبيض للفطور", "He cooked meat and eggs for breakfast", "Tabakh la7am wa bayd lil-futoor"),
        item("طبخنا للضيوف كل شي في البيت", "We cooked everything for the guests at home", "Tabakhna lidh-dhuyoof kil shay fil-bayt"),
    ]),

    lesson(43, "Loving Things", "أحب", [
        item("أحب القهوة العربية كثير", "I love Arabic coffee a lot", "aHibb el-gahwa el-3arabiyya katheer"),
        item("تحبين السفر؟ أحبه كثير", "Do you (f) love travel? I love it a lot", "tiHibbeen es-safar? aHibbah katheer"),
        item("يحب البحر أكثر من الصحراء", "He loves the sea more than the desert", "yiHibb el-baHar akthar min es-sa7raa"),
        item("نحب نزور جدي كل جمعة", "We love visiting my grandfather every Friday", "niHibb nzoor jiddi kil jum3a"),
    ]),

    lesson(44, "More Adjectives", "صفات أكثر", [
        item("القطار سريع، والباص بطيء", "The train is fast, and the bus is slow", "el-gitaar saree3, wal-baas baTee"),
        item("الدرس سهل، بس الامتحان صعب", "The lesson is easy, but the exam is difficult", "ed-dars sahil, bas el-imtiHaan sa3ib"),
        item("اللحم لذيذ، والسلطة طازة", "The meat is delicious, and the salad is fresh", "el-la7am latheeth, was-salata Taaza"),
        item("الكرسي قوي، بس الطاولة ضعيفة", "The chair is strong, but the table is weak", "el-kursi qawi, bas eT-Taawla da3eefa"),
    ]),

    lesson(45, "Things I Have", "أشياء عندي", [
        item("عندي كتاب ودفتر للمدرسة", "I have a book and a notebook for school", "3indi kitaab wa daftar lil-madrasa"),
        item("عندها محفظة ونظارة جديدة", "She has a wallet and new glasses", "3indaha maH-fadha wa nadhdhaara jideeda"),
        item("عندنا مظلة للمطر", "We have an umbrella for the rain", "3indana midhalla lil-maTar"),
        item("عندهم بيت وسيارتين", "They have a house and two cars", "3indahum bayt wa sayyaaratayn"),
    ]),

    lesson(46, "I See, I Saw", "أشوف، شفت", [
        item("أشوف جدي كل جمعة في المجلس", "I see my grandfather every Friday in the majlis", "ashoof jiddi kil jum3a fil-majlis"),
        item("تشوف الجو زين من الدريشة", "You can see the weather well from the window", "tshoof el-jaww zayn min ed-dreesha"),
        item("شفته أمس بس ما شفته اليوم", "I saw him yesterday but I didn't see him today", "shiftah ams bas ma shiftah el-yoom"),
        item("نشوف القمر زين في الصحراء", "We can see the moon well in the desert", "nshoof el-gamar zayn fis-sa7raa"),
    ]),

    lesson(47, "I Cleaned, You Cleaned", "نظفت، نظفت", [
        item("نظفت البيت كله قبل العيد", "I cleaned the whole house before Eid", "nadhdhaft el-bayt killah gabl el-3eed"),
        item("نظفتي غرفتك أمس؟", "Did you (f) clean your room yesterday?", "nadhdhafti ghurftik ams?"),
        item("نظف السيارة الصبح", "He cleaned the car in the morning", "nadhdhaf es-sayyaara es-sub7"),
        item("نظفنا المطبخ والصحون بعد الأكل", "We cleaned the kitchen and the plates after eating", "nadhdhafna el-matbakh wa es-suHoon ba3d el-akal"),
    ]),

    lesson(48, "Telling Time", "قول الوقت", [
        item("كم الساعة؟ الساعة عشرة", "What time is it? It's ten o'clock", "kam es-saa3a? es-saa3a 3ashara"),
        item("أروح الشغل الساعة سبعة", "I go to work at seven o'clock", "aruuH esh-shaghal es-saa3a sab3a"),
        item("الدرس بعد عشرين دقيقة", "The lesson is in twenty minutes", "ed-dars ba3d 3ishreen dageega"),
        item("وصلنا الساعة خمسة عصر", "We arrived at five in the afternoon", "wisalna es-saa3a khamsa 3asir"),
    ]),

    lesson(49, "Bus, Market, and Sky", "الباص والسوق والسماء", [
        item("رحت السوق بالباص الصبح", "I went to the market by bus in the morning", "riHt es-suug bil-baas es-sub7"),
        item("السوق مليان أشياء زينة كثير", "The market is full of a lot of nice things", "es-suug malyaan ashyaa zeena katheer"),
        item("السماء صافية والقمر واضح الليل", "The sky is clear and the moon is visible tonight", "es-samaa saafya wal-gamar waadiH el-layl"),
        item("شفنا نجوم كثير في الصحراء", "We saw a lot of stars in the desert", "shifna nujoom katheer fis-sa7raa"),
    ]),

    lesson(50, "Comparatives", "المقارنة", [
        item("بيت جدي أكبر من بيتنا", "My grandfather's house is bigger than our house", "bayt jiddi akbar min baytna"),
        item("هذا القميص أصغر من الثاني", "This shirt is smaller than the second one", "haadha el-gamees asghar min eth-thaani"),
        item("القهوة هنا أزيان من هناك", "The coffee here is better than there", "el-gahwa hina azyan min hinaak"),
        item("هذا المطعم أغلى من المطعم الجديد", "This restaurant is more expensive than the new restaurant", "haadha el-mat3am aghla min el-mat3am el-jideed"),
    ]),

    lesson(51, "First, Again, Never", "أول، ثانية، أبدا", [
        item("هذا أول مرة أروح السعودية", "This is the first time I go to Saudi Arabia", "haadha awwal marra aruuH es-sa3oodiyya"),
        item("بنزور جدي مرة ثانية بكرا", "We'll visit my grandfather again tomorrow", "banzoor jiddi marra thaanya bukra"),
        item("ما شفت شي مثل هذا أبدا", "I've never seen anything like this", "ma shift shay mithil haadha abadan"),
        item("أول شي نشرب قهوة، وبعدين نتكلم", "First we drink coffee, and then we talk", "awwal shay nishrab gahwa, wa ba3dayn nitkallam"),
    ]),

    lesson(52, "Quantifiers", "كل وبعض", [
        item("كل الأهل ياو للعرس", "All the family came to the wedding", "kil el-ahl yaaw lil-3urs"),
        item("بعض الطلاب فهمو الدرس", "Some of the students understood the lesson", "ba3d et-Tullaab fihmaw ed-dars"),
        item("كل يوم أشرب قهوة الصبح", "Every day I drink coffee in the morning", "kil yoom ashrab gahwa es-sub7"),
        item("بعض الأكل كان لذيذ، وبعضه مب زين", "Some of the food was delicious, and some of it wasn't good", "ba3d el-akal kaan latheeth, wa ba3dah mub zayn"),
    ]),

    lesson(53, "Leaving", "الطلوع", [
        item("طلعت من البيت الساعة سبعة", "I left the house at seven o'clock", "Tala3t min el-bayt es-saa3a sab3a"),
        item("طلعنا من المطعم بعد الأكل", "We left the restaurant after eating", "Tala3na min el-mat3am ba3d el-akal"),
        item("طلعو من المسجد وراحو بيت جدهم", "They left the mosque and went to their grandfather's house", "Tala3aw min el-masjid wa raaHaw bayt jiddahum"),
        item("طلعت من الشغل متأخر أمس", "I left work late yesterday", "Tala3t min esh-shaghal mit'akhkhir ams"),
    ]),

    lesson(54, "Coming", "المجيء", [
        item("يجي كل جمعة يزور جدي", "He comes every Friday to visit my grandfather", "yiji kil jum3a yzoor jiddi"),
        item("تجي معنا للمطعم الليلة؟", "Are you coming with us to the restaurant tonight?", "tiji ma3ana lil-mat3am el-layla?"),
        item("متى يجي أخوك؟ يجي بعد العصر", "When is your brother coming? He's coming after the afternoon", "mita yiji akhook? yiji ba3d el-3asir"),
        item("ما يجي الشغل يوم الجمعة", "He doesn't come to work on Friday", "ma yiji esh-shaghal yoom el-jum3a"),
    ]),

    lesson(55, "I Came, You Came", "ييت، ييت", [
        item("ييت من الشغل متأخر أمس", "I came from work late yesterday", "yeet min esh-shaghal mit'akhkhir ams"),
        item("ييتي على وقتك اليوم، زين", "You (f) came on time today, good", "yeeti 3ala wagtik el-yoom, zayn"),
        item("يا من السفر أمس بالليل", "He came from the trip last night", "yaa min es-safar ams bil-layl"),
        item("يينا للعرس مع كل الأهل", "We came to the wedding with the whole family", "yeena lil-3urs ma3 kil el-ahl"),
    ]),

    lesson(56, "She Came, We Came", "يات، يينا", [
        item("يات خالتي من السفر أمس", "My maternal aunt came from her trip yesterday", "yaat khaalti min es-safar ams"),
        item("يينا نزور جدي بعد الشغل", "We came to visit my grandfather after work", "yeena nzoor jiddi ba3d esh-shaghal"),
        item("ييتو على وقتكم، زين كثير", "You all came on time, very good", "yeetoo 3ala wagtikum, zayn katheer"),
        item("ياو من السوق بأشياء كثير", "They came from the market with a lot of things", "yaaw min es-suug bi-ashyaa katheer"),
    ]),

    lesson(57, "Sitting", "القعود", [
        item("قعد في المجلس يشرب قهوة", "He sat in the majlis drinking coffee", "ga3ad fil-majlis yishrab gahwa"),
        item("قعدنا نتكلم عن السفر كثير", "We sat talking about the trip for a long time", "ga3adna nitkallam 3an es-safar katheer"),
        item("قعد في المطعم لين المغرب مع صديقه", "He sat in the restaurant with his friend until sunset", "ga3ad fil-mat3am leen el-maghrib ma3 sadeegah"),
        item("جدي يحب يتكلم في المجلس", "My grandfather loves to talk in the majlis", "jiddi yiHibb yitkallam fil-majlis"),
    ]),

    lesson(58, "Shoes, Socks, and Caps", "الجوتي والدلاغات والقحفية", [
        item("شريت جوتي جديد ودلاغات دافية", "I bought new shoes and warm socks", "ishtarayt jooti jideed wa dallaghaat daafya"),
        item("القحفية تحت الغترة", "The skull cap goes under the headdress", "el-ga7fiyya taHt el-ghitra"),
        item("دلاغاتي وسخة، لازم دلاغات جديدة", "My socks are dirty, I need new socks", "dallaghaati wisikha, laazim dallaghaat jideeda"),
        item("جوتي أخوي كبير، وجوتي صغير", "My brother's shoes are big, and my shoes are small", "jootee akhooy kabeer, wa jootee sagheer"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/a2.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "a2", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/a2.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
