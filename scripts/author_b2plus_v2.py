#!/usr/bin/env python3
"""Full rewrite of B2+ Khaleeji Arabic content -- "lazim ma" (shouldn't)
themed, same repetition fix, built on the very large confirmed vocabulary
from A1 through B2.
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
    lesson(1, "You Shouldn't Drink, You Shouldn't Go", "لازم ما تشرب، لازم ما تروح", [
        item("لازم ما تشرب قهوة كثير، تخليك متوتر طول اليوم", "You shouldn't drink too much coffee, it makes you nervous all day", "laazim ma tishrab gahwa katheer"),
        item("لازم ما تروح السوق بدون فلوس كافية، بترجع بدون شي", "You shouldn't go to the market without enough money, you'll return without anything", "laazim ma truuH es-suug bidoon fluus kaafya"),
        item("لازم ما تشربين مويه باردة بعد الرياضة", "You (f) shouldn't drink cold water right after exercise", "laazim ma tishrabeen moya baarda ba3d er-riyaada"),
        item("لازم ما يروح المجلس متأخر، الكل ينتظره ويصير متضايق", "He shouldn't go to the majlis late, everyone waits for him and he feels embarrassed", "laazim ma yruuH el-majlis mit'akhkhir"),
    ], topicId="b2plus-lazim-ma"),

    lesson(2, "She Shouldn't, We Shouldn't", "لازم ما تروح، لازم ما نروح", [
        item("لازم ما تسافر لوحدها بدون ما تتصل بأهلها أول", "She shouldn't travel alone without informing her family first", "laazim ma tsaafir liwaHdaha bidoon ma tkhabbir ahlaha awwal"),
        item("لازم ما نصرف كل فلوسنا في يوم وحد، لازم نصرفها شوي شوي", "We shouldn't spend all our money in one day, we should distribute it well", "laazim ma nisrif kil fluusana fi yoom waaHid"),
        item("لازم ما تروحون بيت جدكم بدون ما تتصلون أول", "You all shouldn't go to your grandfather's house without calling first", "laazim ma truu7oon bayt jiddikum bidoon ma tittasiloon awwal"),
        item("لازم ما يشربون قهوة قبل النوم، ما بينامون زين", "They shouldn't drink coffee before sleep, they won't sleep well", "laazim ma yishrabuun gahwa gabl en-nawm"),
    ]),

    lesson(3, "You Shouldn't Want, You Shouldn't Know", "لازم ما تبغى، لازم ما تدري", [
        item("لازم ما تبغى كل شي مرة وحدة، الصبر مهم في الحياة", "You shouldn't want everything at once, patience is important in life", "laazim ma tibgha kil shay marra waHda"),
        item("لازم ما تدري كل شي، بعض الأشياء أزيان لو ما تدريها", "You shouldn't know everything, some things are better if you don't know them", "laazim ma tadri kil shay, ba3d el-ashyaa azyan law ma daraytha"),
        item("لازم ما تبغى بيت أكبر من دخلك، هذا بيخليك متضايق بعدين", "You shouldn't want a house bigger than your income, this will make you upset", "laazim ma tibgha bayt akbar min dakhlak"),
        item("لازم ما تدري كل شي عن أصحابك، فيه أشياء خاصة", "You shouldn't know everything about your friends, there are personal things", "laazim ma tadri kil shay 3an as7aabak"),
    ]),

    lesson(4, "Not Because You're Tired, But Because Busy", "مب لأنك تعبان، بس لأنك مشغول", [
        item("لازم ما ترفض العرس مب لأنك تعبان، بس لأنك مشغول بشغل مهم", "You shouldn't decline the wedding not because you're tired, but because you're busy with important work", "laazim ma tirfid el-3urs mub li-annak ta3baan"),
        item("مب لأنه غالي رفضنا البيت، بس لأن موقعه مب زين", "It's not because it's expensive that we declined the house, but because its location isn't good", "mub li-annah ghaali rafadhna el-bayt"),
        item("لازم ما تلوم نفسك مب لأن الوضع صعب، بس لأنك سويت كل اللي تقدر عليه", "You shouldn't blame yourself not because the situation is hard, but because you did all you could", "laazim ma tloom nafsak"),
        item("ما نجحت مب لأن الامتحان صعب، بس لأني ما درست كافي", "I didn't succeed not because the exam was hard, but because I didn't study enough", "ma najaHt mub li-ann el-imtiHaan sa3ib"),
    ]),

    lesson(5, "Review: Lazim Ma", "مراجعة: لازم ما", [
        item("لازم ما تصرف كل فلوسك على العرس، وفر شي للسفر بعدين", "You shouldn't spend all your money on the wedding, leave something for travel later", "laazim ma tisrif kil fluusak 3alal-3urs"),
        item("لازم ما تدري كل شي عن أخوك، بعض الأشياء خاصة فيه", "You shouldn't know everything about your brother, some things are private to him", "laazim ma tadri kil shay 3an akheek, ba3d el-ashyaa khaassa feeh"),
        item("مب لأنه بعيد ما رحنا، بس لأننا كنا متعبين من السفر", "It's not because it's far that we didn't go, but because we were tired from the trip", "mub li-annah ba3eed ma riHna"),
        item("لازم ما تروح لوحدك بالليل، لازم يروح حد وياك أزيان", "You shouldn't go alone at night, take someone with you for safety", "laazim ma truuH liwaHdak bil-layl"),
    ]),

    lesson(6, "You Shouldn't Go to the Hospital", "لازم ما تروح المستشفى", [
        item("لازم ما تروح المستشفى بدون موعد، بتنتظر ساعات طويلة", "You shouldn't go to the hospital without an appointment, you'll wait for long hours", "laazim ma truuH el-mustashfa bidoon maw3id"),
        item("لازم ما تاخذ الدوا بدون ما تسأل الطبيب أول", "You shouldn't take the medicine without asking the doctor first about the dose", "laazim ma taakhudh ed-dawa bidoon ma tis'al eT-Tabeeb awwal"),
        item("لازم ما ترجع الشغل قبل ما تتحسن كامل، الجسم يحتاج وقت", "You shouldn't return to work before you fully recover, the body needs time", "laazim ma tirja3 esh-shaghal gabl ma titHassan kaamil"),
        item("لازم ما تنسى ألم الظهر، لازم تشوف طبيب زين", "You shouldn't neglect the back pain, you should see a specialist doctor", "laazim ma tuhmil alam edh-dhahr"),
    ]),

    lesson(7, "You Shouldn't Go to Your Brother's House", "لازم ما تروح بيت أخوك", [
        item("لازم ما تروح بيت أخوك بدون ما تتصل، ممكن يكون مشغول", "You shouldn't go to your brother's house without calling, he might be busy", "laazim ma truuH bayt akhook bidoon ma tittasil"),
        item("لازم ما تلوم أختك على كل شي، هي تسوي اللي تقدر عليه", "You shouldn't blame your sister for everything, she does what she can", "laazim ma tloom ukhtak 3ala kil shay"),
        item("لازم ما تقارن بين أولادك، كل واحد فيهم مختلف عن الثاني", "You shouldn't compare between your children, each of them is different and special", "laazim ma tqaarin bayn awlaadak"),
        item("لازم ما تنسى تشكر جدك على كل اللي سواه لك", "You shouldn't forget to thank your grandfather for everything he did for you", "laazim ma tinsa tishkur jiddak 3ala kil elli sawaah lak"),
    ]),

    lesson(8, "You Shouldn't Want the Red House", "لازم ما تبغى البيت الأحمر", [
        item("لازم ما تبغى البيت الأحمر بس لأن لونه حلو، شوف موقعه وسعره أول", "You shouldn't want the red house just because its color is nice, look at its location and price first", "laazim ma tibgha el-bayt el-a7mar bas li-ann loonah 7ilu"),
        item("لازم ما تشري السيارة الغالية بدون ما تفكر بمشاكلها بعدين", "You shouldn't buy the expensive car without thinking about maintenance later", "laazim ma tishri es-sayyaara el-ghaalya bidoon ma tfakkir bis-siyaana ba3dayn"),
        item("لازم ما تختار الشغل بس على الفلوس، فكر بالراحة والوقت كمان", "You shouldn't choose the job just based on money, think about comfort and time too", "laazim ma tikhtaar esh-shughul bas 3alal-fluus"),
        item("لازم ما تختار المحل بس على شكله، شوف الأشياء فيه أول", "You shouldn't choose the shop just based on its appearance, see the things in it first", "laazim ma tikhtaar el-maHal bas 3ala shaklah, shoof el-ashyaa feeh awwal"),
    ]),

    lesson(9, "You Shouldn't Go Far", "لازم ما تروح بعيد", [
        item("لازم ما تروح بعيد بالليل بدون ما تخبر حد وين رايح", "You shouldn't go far at night without telling someone where you're going", "laazim ma truuH ba3eed bil-layl bidoon ma tkhabbir Had wein raayiH"),
        item("لازم ما تمشي بعيد عن الطريق الأصلي، ممكن ما تلقى البيت", "You shouldn't walk far from the main road, you might get lost", "laazim ma timshi ba3eed 3aniT-Tareeg el-asli"),
        item("لازم ما تسافر بعيد بدون فلوس كثير، ممكن تحتاج فلوس أكثر هناك", "You shouldn't travel far without a lot of money, you might need more than you thought", "laazim ma tsaafir ba3eed bidoon fluus katheer"),
        item("لازم ما تنسى أهلك، لازم تزورهم كل جمعة عشان تقعدون سوا", "You shouldn't forget your family, you must visit them every Friday so you sit together", "laazim ma tinsa ahlak, laazim tzoorhum kil jum3a 3ashaan tag3adoon sawa"),
    ]),

    lesson(10, "Review: B2+ Recap", "مراجعة", [
        item("لازم ما تروح المستشفى بدون موعد، ولازم ما تنسى الألم الطويل", "You shouldn't go to the hospital without an appointment, and shouldn't neglect long-lasting pain", "laazim ma truuH el-mustashfa bidoon maw3id"),
        item("لازم ما تبغى البيت بس على لونه، فكر بالموقع والسعر زين", "You shouldn't want the house just for its color, think well about the location and price", "laazim ma tibgha el-bayt bas 3ala loonah"),
        item("لازم ما تسافر بعيد بدون ما تخبر أهلك بمكانك", "You shouldn't travel far without telling your family your location", "laazim ma tsaafir ba3eed bidoon ma tkhabbir ahlak bimakaanak"),
        item("لازم ما تلوم نفسك كثير، كل واحد يغلط أحيانا وهذا طبيعي", "You shouldn't blame yourself too much, everyone makes mistakes sometimes and that's normal", "laazim ma tloom nafsak katheer"),
    ]),

    lesson(11, "You Shouldn't Eat That", "لازم ما تاكل هذا", [
        item("لازم ما تاكل هذا اللحم، صار له في الثلاجة أسبوع كامل", "You shouldn't eat this meat, it's been in the fridge for a whole week", "laazim ma taakil haadha el-la7am"),
        item("لازم ما تاكلين قبل الدوا مباشرة، انتظري نص ساعة أول", "You (f) shouldn't eat right before the medicine, wait half an hour first", "laazim ma taakleen gabl ed-dawa mubaasharatan"),
        item("لازم ما ياكلون كل الحلو مرة وحدة، بيتعبون بعدين", "They shouldn't eat all the dessert at once, their stomachs will hurt", "laazim ma yaakiloon kil el-Hilu marra waHda"),
        item("لازم ما نطبخ اللحم كثير، يصير مب لذيذ بعدين", "We shouldn't overcook the meat, it becomes tough and doesn't turn out well", "laazim ma naTbakh el-la7am katheer"),
    ]),

    lesson(12, "You All Shouldn't, They Shouldn't", "لازم ما تروحون، لازم ما يروحون", [
        item("لازم ما تروحون السوق قبل ما تفكرون بكل اللي تحتاجونه", "You all shouldn't go to the market before thinking about everything you need", "laazim ma truu7oon es-suug gabl ma tfakkroon bikil elli taHtaajoonah"),
        item("لازم ما تدفعون كل الفلوس بدون ما تتأكدون من السعر الصح", "You all shouldn't pay all the money without making sure of the right price", "laazim ma tidfa3oon kil el-fluus bidoon ma tit'akkadoon min es-si3ir es-saHH"),
        item("لازم ما يشرون البيت قبل ما يشوفونه مرة ثانية", "They shouldn't buy the house before seeing it a second time", "laazim ma yishroon el-bayt gabl ma yshoofoonah marra thaanya"),
        item("لازم ما يقررون السفر بدون ما يدرسون كل شي زين", "They shouldn't decide on the trip without studying all the details well", "laazim ma yqarriroon es-safar bidoon ma yadrusoon kil shay zayn"),
    ]),

    lesson(13, "You Shouldn't Go on Friday", "لازم ما تروح يوم الجمعة", [
        item("لازم ما تروح البنك يوم الجمعة، هو مسكر يومها", "You shouldn't go to the bank on Friday, it's closed that day", "laazim ma truuH el-bank yoom el-jum3a"),
        item("لازم ما تسوي شي مهم يوم الاثنين، الزحمة قوية يومها", "You shouldn't do anything important on Monday, the traffic is heavy that day", "laazim ma tsawwi shay muhim yoom el-ithnayn"),
        item("لازم ما تسافر يوم الخميس مساء، المطار يكون مليان ناس", "You shouldn't travel Thursday evening, the airport is full of people", "laazim ma tsaafir yoom el-khamees masaa"),
        item("لازم ما تحجز موعد الطبيب آخر الأسبوع، بينتظرون كل الناس", "You shouldn't book the doctor's appointment at the end of the week, everyone will be waiting", "laazim ma tiHjiz maw3id eT-Tabeeb aakhir el-isboo3"),
    ]),

    lesson(14, "You Shouldn't Have Nine", "لازم ما يكون عندك تسعة", [
        item("لازم ما يكون عندك أكثر من عشرة قمصان، هذا كثير عليك", "You shouldn't have more than ten shirts, that's too many for you", "laazim ma ykoon 3indak akthar min 3ashara gumsaan"),
        item("لازم ما تصرف أكثر من نص فلوسك على البيت", "You shouldn't spend more than half your salary on rent", "laazim ma tisrif akthar min nus raatbak 3alal-eejaar"),
        item("لازم ما يكون عندك عشرين موعد بنفس اليوم، هذا كثير عليك", "You shouldn't have twenty appointments on the same day, that's impossible", "laazim ma ykoon 3indak 3ishreen maw3id binafs el-yoom"),
        item("لازم ما تحط أكثر من كيلوين في الشنطة الصغيرة", "You shouldn't carry more than two kilos in the small bag", "laazim ma tHummil akthar min keelowayn fish-shanTa es-sagheera"),
    ]),

    lesson(15, "Review: Lazim Ma with Food, Days, Numbers", "مراجعة", [
        item("لازم ما تاكل أكثر من صحن وحد، الأكل كثير مب زين للجسم", "You shouldn't eat more than one plate, too much food isn't good for the body", "laazim ma taakil akthar min Tabag waaHid"),
        item("لازم ما تروح البنك يوم الجمعة لأنه مسكر، روح يوم السبت بدل", "You shouldn't go to the bank on Friday because it's closed, go on Saturday instead", "laazim ma truuH el-bank yoom el-jum3a li-annah mub maftooH"),
        item("لازم ما يكون عندك فلوس كثير بالبيت، حطها بالبنك أزيان", "You shouldn't have excess money at home, put it in the bank instead", "laazim ma ykoon 3indak fluus zaayida bil-bayt"),
        item("لازم ما تشتري عشرة أشياء ما تحتاجها بس لأن السعر رخيص", "You shouldn't buy ten things you don't need just because the price is cheap", "laazim ma tishtiri 3ashara ashyaa ma taHtaajha bas li-annes-si3ir rakhees"),
    ]),

    lesson(16, "You Shouldn't Be Upset", "لازم ما تزعل", [
        item("لازم ما تزعل منه بسرعة، هو ما يبغى يخليك متضايق", "You shouldn't get upset with him quickly, he doesn't want to bother you at all", "laazim ma tiz3al minnah bisur3a, huwa ma yibgha ydaayigak abadan"),
        item("لازم ما تزعلين من كل شي يقولونه، بعض الناس بس يتكلمون كذا دايما", "You (f) shouldn't get upset at everything they say, some people just talk without meaning it", "laazim ma tiz3aleen min kil shay yguuloonah"),
        item("لازم ما نقلق كثير على النتيجة، سوينا كل اللي نقدر عليه", "We shouldn't worry too much about the result, we did all we could", "laazim ma niqlaq katheer 3alan-nateeja"),
        item("لازم ما يتوترون قبل الاجتماع، لو يدرسون زين، كل شي بيصير أسهل", "They shouldn't get nervous before the meeting, good preparation makes everything easier", "laazim ma yitwattaroon gabl el-ijtimaa3"),
    ]),

    lesson(17, "You Shouldn't Go to the Doctor Tired", "لازم ما تروح الطبيب تعبان", [
        item("لازم ما تروح الطبيب وانت تعبان كثير، خذ راحة يوم أول", "You shouldn't go to the doctor while you're extremely tired, take a day of rest first", "laazim ma truuH eT-Tabeeb wa inta ta3baan jiddan"),
        item("لازم ما تسوق وانت متعب، مب زين عليك وعلى الناس الثانية", "You shouldn't drive while you're tired, it's dangerous for you and others", "laazim ma tsoog wa inta mut3ab"),
        item("لازم ما تدرس وانت جوعان، ما بتقدر تفهم زين", "You shouldn't study while you're hungry, you won't be able to focus well", "laazim ma tadrus wa inta joo3aan"),
        item("لازم ما تقرر شي مهم وانت زعلان، انتظر لين تصير زين", "You shouldn't decide anything important while you're upset, wait until you calm down", "laazim ma tqarrir shay muhim wa inta za3laan"),
    ]),

    lesson(18, "You Shouldn't Go Right", "لازم ما تروح يمين", [
        item("لازم ما تروح يمين هناك، الطريق مسكر اليوم", "You shouldn't go right there, the road is closed because of maintenance", "laazim ma truuH yameen hinaak"),
        item("لازم ما تاخذ الطريق القديم، الجديد أسرع وأسهل بكثير", "You shouldn't take the old road, the new one is much faster and easier", "laazim ma taakhudh eT-Tareeg el-gadeem"),
        item("لازم ما توقف قدام البيت مباشرة، وقف شوي بعيد", "You shouldn't stop right in front of the house, stop a bit farther away", "laazim ma toogaf guddaam el-bayt mubaasharatan"),
        item("لازم ما تدخل من الباب الثاني، هذا الباب زين ومفتوح دايما", "You shouldn't enter from the other door, this door is good and always open", "laazim ma tudkhul minal-baab eth-thaani"),
    ]),

    lesson(19, "You Shouldn't Want the Old House", "لازم ما تبغى البيت القديم", [
        item("لازم ما تبغى البيت القديم بس لأنه رخيص، شوف البيت زين أول", "You shouldn't want the old house just because it's cheap, check its condition first", "laazim ma tibgha el-bayt el-gadeem bas li-annah rakhees"),
        item("لازم ما تبغى كل الأشياء القديمة، بعضها ما تحتاجه أبدا", "You shouldn't want all the old things, some of them you never need", "laazim ma tibgha kil el-ashyaa el-gadeema"),
        item("لازم ما تقارن سيارتك القديمة بسيارة صاحبك الجديدة", "You shouldn't compare your old car to your friend's new car", "laazim ma tqaarin sayyaaratak el-gadeema bisayyaarat saaHbak el-jideeda"),
        item("لازم ما تبغى الطريقة القديمة لو فيه طريقة أزيان وأسرع", "You shouldn't want the old way if there's a better and faster way", "laazim ma tibgha eT-Tareega el-gadeema"),
    ]),

    lesson(20, "Review: B2+ Recap 2", "مراجعة", [
        item("لازم ما تروح الطبيب وانت تعبان، ولازم ما تسوق وانت متعب", "You shouldn't go to the doctor while tired, and shouldn't drive while exhausted", "laazim ma truuH eT-Tabeeb wa inta ta3baan"),
        item("لازم ما تبغى البيت القديم بس لأنه رخيص، شكله أهم من السعر", "You shouldn't want the old house just because it's cheap, condition matters more than price", "laazim ma tibgha el-bayt el-gadeem bas li-annah rakhees"),
        item("لازم ما تزعل من كل كلمة، الحياة فيها أشياء كثير ما تستاهل الزعل", "You shouldn't get upset at every word, life has a lot of talk that isn't worth getting upset over", "laazim ma tiz3al min kil kilma"),
        item("لازم ما تدخل من الباب الثاني وانت ما تعرف صاحب البيت زين", "You shouldn't enter from the back door if you don't know the house owner well", "laazim ma tudkhul minal-baab el-khalfi"),
    ]),

    lesson(21, "You Shouldn't Go to Your Sister's House Tired", "لازم ما تروح بيت أختك تعبان", [
        item("لازم ما تروح بيت أختك وانت تعبان، خذ راحة أول وبعدين روح لها", "You shouldn't go to your sister's house while tired, rest first and then visit her", "laazim ma truuH bayt ukhtak wa inta ta3baan"),
        item("لازم ما تتكلمين مع خالتك وانتي زعلانة، انتظري تصيرين زينة أول", "You (f) shouldn't talk to your maternal aunt while upset, wait until you calm down first", "laazim ma titkallmeen ma3 khaaltik wa inti za3laana"),
        item("لازم ما نقرر شي عن الأولاد واحنا زعلانين، لازم نصير زينين أول", "We shouldn't decide anything about the children while we're upset, we must be fine first", "laazim ma nqarrir shay 3anil-awlaad wa niHna za3laaneen"),
        item("لازم ما يزورون جدهم وهم مستعجلين، هو يحب يقعد وياهم وقت طويل", "They shouldn't visit their grandfather while in a hurry, he loves long sittings", "laazim ma yzooroon jiddahum wa hum musta3jileen"),
    ]),

    lesson(22, "You Shouldn't Want Your Brother's Car", "لازم ما تبغى سيارة أخوك", [
        item("لازم ما تبغى سيارة أخوك، اشتغل وشري سيارتك الخاصة", "You shouldn't want your brother's car, work and get your own car", "laazim ma tibgha sayyaarat akhook"),
        item("لازم ما تقارن شغلك بشغل صديقك، كل واحد له طريقه", "You shouldn't compare your job to your friend's job, each one has their own path", "laazim ma tqaarin shughlak bishughul saaHbak"),
        item("لازم ما تزعلين من أختك لأنها نجحت، لازم تكونين مبسوطة لها", "You (f) shouldn't be upset with your sister because she succeeded, you should be happy for her", "laazim ma tiz3aleen min ukhtik li-annaha najHat, laazim tkooneen mabsoota laha"),
        item("لازم ما تبغى بيت مثل بيت الجيران، بيتك زين ويناسبك", "You shouldn't want a house like the neighbors' house, your house is good and suits you", "laazim ma tibgha bayt mithil bayt el-jeeraan"),
    ]),

    lesson(23, "I Don't Need to Know", "ما أحتاج أدري", [
        item("ما أحتاج أدري كل التفاصيل، بس أدري النتيجة كافي لي", "I don't need to know all the details, just knowing the result is enough for me", "ma aHtaaj adri kil shay"),
        item("ما تحتاجين تدرين كل شي عنه، هو صار شخص ثاني الحين", "You (f) don't need to know everything about him, he became a different person now", "ma taHtaajeen tadreen kil shay 3annah, huwa saar shakhs thaani el-heen"),
        item("ما نحتاج ندري السبب الحقيقي، بس نقبل قراره", "We don't need to know the real reason, we just respect his decision", "ma naHtaaj nadri es-sabab el-Hageeqi"),
        item("ما يحتاجون يدرون كل شي، بس المهم يكفيهم", "They don't need to know our whole plan, just the important part is enough for them", "ma yaHtaajoon yidroon kil khiTTatna"),
    ]),

    lesson(24, "A Full Day of Lazim Ma", "يوم كامل من لازم ما", [
        item("لازم ما تصحى متأخر، ولازم تاكل فطورك، ولازم ما تتأخر عن الشغل", "You shouldn't wake up late, shouldn't skip breakfast, and shouldn't be late for work", "laazim ma tSHa mit'akhkhir"),
        item("لازم ما تدرس طول الليل بدون راحة، ولازم ما تنسى تاكل بين الدروس", "You shouldn't study all night without rest, and shouldn't forget to eat between lessons", "laazim ma tadrus Tool el-layl bidoon raaHa"),
        item("لازم ما تطبخ وانت مستعجل، ولازم ما تنسى شي بالمطبخ قبل ما تطلع", "You shouldn't cook while in a hurry, and shouldn't forget anything in the kitchen before you leave", "laazim ma taTbakh wa inta musta3jil"),
        item("لازم ما تسافر بدون راحة كافية، ولازم ما تنسى محفظتك ومفتاحك", "You shouldn't travel without enough rest, and shouldn't forget your important papers", "laazim ma tsaafir bidoon raaHa kaafya"),
    ]),

    lesson(25, "Review: Lazim Ma with Family, Know, Drink", "مراجعة", [
        item("لازم ما تدري كل شي عن العائلة، بعض الأشياء أزيان لو ما تدريها", "You shouldn't know everything about the family, some things are better if you don't know them", "laazim ma tadri kil shay 3anil-ahl"),
        item("لازم ما تشرب قهوة كثير وانت متوتر، هذا بيخليك متوتر أكثر بس", "You shouldn't drink a lot of coffee while nervous, this only increases the nervousness", "laazim ma tishrab gahwa katheer wa inta mutawattir"),
        item("لازم ما تلوم جدتك على طريقتها القديمة، هي من زمان ثاني", "You shouldn't blame your grandmother for her old-fashioned way, she's from another era", "laazim ma tloom jiddatak 3ala Tareegatha el-gadeema"),
        item("لازم ما نحكم على أحد قبل ما نعرف قصته كاملة", "We shouldn't judge someone before knowing his whole story", "laazim ma naHkum 3ala aHad gabl ma na3rif gissatah kaamila"),
    ]),

    lesson(26, "Another Full Day", "يوم كامل ثاني", [
        item("لازم ما تقعد طول اليوم بدون ما تمشي، لازم تمشي شوي كل ساعة", "You shouldn't sit all day without movement, you should walk a bit every hour", "laazim ma tag3ad Tool el-yoom bidoon Haraka"),
        item("لازم ما تشتغل بدون فطور، الجسم يحتاج أكل عشان يشتغل زين", "You shouldn't work without breakfast, the body needs energy in order to focus", "laazim ma tashtaghil bidoon futoor"),
        item("لازم ما تروح النوم وانت زعلان، افهم المشكلة قبل ما تنام", "You shouldn't go to sleep while upset, understand the problem before you sleep", "laazim ma truuH en-nawm wa inta za3laan"),
        item("لازم ما تفكر بيوم بكرا بدون ما تخلص شغل اليوم أول", "You shouldn't think about tomorrow's day without finishing today's work first", "laazim ma tfakkir biyoom bukra bidoon ma tkhallis shughul el-yoom awwal"),
    ]),

    lesson(27, "Places and Lazim Ma", "الأماكن ولازم ما", [
        item("لازم ما تروح المطار بدون ما تتأكد من وقت الطيارة الصح", "You shouldn't go to the airport without making sure of the flight's correct time", "laazim ma truuH el-mataar bidoon ma tit'akkad min wagt er-riHla es-saHH"),
        item("لازم ما توقف بالسيارة قدام باب المسجد، وقف بعيد شوي أزيان", "You shouldn't stop the car in front of the mosque door, stop a bit farther away, better", "laazim ma toogaf bis-sayyaara guddaam baab el-masjid"),
        item("لازم ما تدخل المطبخ وانت وسخ من الشغل الطويل", "You shouldn't enter the kitchen while dirty from outdoor work", "laazim ma tudkhul el-matbakh wa inta wisikh min esh-shughul el-khaariji"),
        item("لازم ما تروح المجلس بدون ما تسلم على كل واحد فيه", "You shouldn't go to the majlis without greeting everyone in it", "laazim ma truuH el-majlis bidoon ma tsallim 3ala kil waaHid feeh"),
    ]),

    lesson(28, "Lazim Ma with Money", "لازم ما مع الفلوس", [
        item("لازم ما تصرف كل فلوسك بيوم وحد، وفر شي دايما", "You shouldn't spend all your money in one day, always save something", "laazim ma tisrif kil fluusak biyoom waaHid"),
        item("لازم ما تدفع قبل ما تشوف الشي وتتأكد إنه زين", "You shouldn't pay before seeing the item and making sure it's good", "laazim ma tidfa3 gabl ma tshoof esh-shay wa tit'akkad innah zayn"),
        item("لازم ما تنسى تدري كل الفلوس قبل ما تقرر السعر", "You shouldn't forget to calculate all the money before setting the price", "laazim ma tinsa tHassib kil el-fluus gabl ma tHaddid es-si3ir"),
        item("لازم ما تشري كل شي غالي بس عشان أصحابك يشرونه", "You shouldn't buy everything expensive just because your friends buy it", "laazim ma tishri kil shay ghaali bas 3ashaan as7aabak yishroonah"),
    ]),

    lesson(29, "Lazim Ma with Feelings", "لازم ما مع المشاعر", [
        item("لازم ما تحس متضايق من قرار سويته وانت تدري الوضع زين", "You shouldn't feel bad about a decision you made while understanding the situation well", "laazim ma tHiss mutadaayig min qaraar sawwaytah"),
        item("لازم ما تخاف من الامتحان الصعب، درست زين وتقدر عليه", "You shouldn't fear the difficult exam, you studied well and you can handle it", "laazim ma tkhaaf minal-imtiHaan es-sa3ib"),
        item("لازم ما تقارن نفسك بالثانيين طول الوقت، كل واحد له طريقه", "You shouldn't compare yourself to others all the time, each person has their own path", "laazim ma tqaarin nafsak bith-thaanyeen Tool el-wagt"),
        item("لازم ما تقعد وحدك مع مشكلتك، تكلم مع صاحبك أو أهلك", "You shouldn't always suppress your feelings, talk to your friend or your family", "laazim ma tiktum mashaa3irak dayman, tkallam ma3 saaHbak aw ahlak"),
    ]),

    lesson(30, "Review: B2+ Final Recap", "مراجعة نهائية", [
        item("لازم ما تصرف كل فلوسك بيوم وحد، ولازم ما تنسى تدري كل شي زين", "You shouldn't spend all your money in one day, and shouldn't forget to calculate everything well", "laazim ma tisrif kil fluusak biyoom waaHid"),
        item("لازم ما تخاف من الامتحان، ولازم ما تقارن نفسك بالثانيين", "You shouldn't fear the exam, and shouldn't compare yourself to others", "laazim ma tkhaaf minal-imtiHaan, wa laazim ma tqaarin nafsak bith-thaanyeen"),
        item("لازم ما تحكم على أحد بسرعة، اسأله ليش سوى كذا أول", "You shouldn't judge someone quickly, ask him why he did that first", "laazim ma taHkum 3ala aHad bisur3a"),
        item("لازم ما تنسى إن العائلة أهم من أي شي ثاني", "You shouldn't forget that family is more important than anything else", "laazim ma tinsa inn el-ahl ahamm min ay shay thaani"),
    ]),

    lesson(31, "Stress and Feelings", "التوتر والمشاعر", [
        item("متوتر كثير قبل الامتحان، بس أفكر بأشياء زينة عشان أرتاح", "I'm very nervous before the exam, but I try to think of things that relax me", "mutawattir katheer gabl el-imtiHaan"),
        item("قلقانة على ابنها، بس ما تبين قلقها له", "She's worried about her son, but she tries not to show her worry to him", "galgaana 3ala waladha"),
        item("متضايقين من الشغل الكثير، بس نرتاح كل جمعة زين", "We're upset about the excessive work, but we try to rest every Friday", "mutadaayigeen minesh-shughul el-katheer"),
        item("فخورين كثير لأن السنة كانت صعبة وصبرنا زين", "We're proud of ourselves because we got through a very difficult year", "fakhooreen bi-anfusna li-annana tjaawazna sana sa3ba katheer"),
    ]),

    lesson(32, "Clothes, Shouldn't Want", "الملابس، لازم ما تبغى", [
        item("لازم ما تبغى ملابس غالية بس عشان اسمها زين", "You shouldn't want expensive clothes just because their name is famous", "laazim ma tibgha malaabis ghaalya bas 3ashaan ismha mash-hoor"),
        item("لازم ما تشرين عباية جديدة كل شهر، وفري فلوسك أزيان", "You shouldn't buy a new abaya every month, save your money instead", "laazim ma tishreen 3abaaya jideeda kil shahar"),
        item("لازم ما تلبس نفس القميص كل يوم للاجتماعات", "You shouldn't wear the same shirt every day for meetings", "laazim ma tilbas nafs el-gamees kil yoom lil-ijtimaa3aat"),
        item("لازم ما تحكم على الناس من ملابسهم بس، شوف شنو فيهم", "You shouldn't judge people just by their clothes, look at their heart", "laazim ma taHkum 3alan-naas min malaabishum bas"),
    ]),

    lesson(33, "Clothes, Shouldn't Want II", "الملابس، لازم ما تبغى ٢", [
        item("لازم ما تبغى جوتي جديد كل شهر، الجوتي الزين يبقى زين سنين", "You shouldn't want new shoes every month, good shoes last for years", "laazim ma tibgha jooti jideed kil shahar"),
        item("لازم ما تشري غترة غالية بدون ما تقارن الأسعار بمحلات ثانية", "You shouldn't buy an expensive headdress without comparing prices at other shops", "laazim ma tishri ghitra ghaalya bidoon ma tqaarin el-as3aar bima7allaat thaanya"),
        item("لازم ما تبغى بس لون واحد بملابسها، عندها ألوان جديدة كثير", "She shouldn't want only one color for her clothes, she has a lot of new colors", "laazim ma tibgha bas loon waaHid bimalaabisha"),
        item("لازم ما نشري ملابس كثير للعرس، البسيط أحيانا أزيان وأنيق", "We shouldn't overdo the clothes for the wedding, the simple is sometimes better and more elegant", "laazim ma nbaalig fil-malaabis lil-3urs"),
    ]),

    lesson(34, "Food, Shouldn't Want", "الأكل، لازم ما تبغى", [
        item("لازم ما تبغى أكل جاهز كل يوم، الأكل البيتي أزيان وألذ", "You shouldn't want ready-made food every day, home-cooked food is better and tastier", "laazim ma tibgha akal jaahiz kil yoom"),
        item("لازم ما تبغى أكل غالي بس عشان اسم المطعم مشهور", "You (f) shouldn't want expensive food just because the restaurant's name is famous", "laazim ma tibgheen akal ghaali bas 3ashaan ism el-mat3am mash-hoor"),
        item("لازم ما نطلب أكل كثير للعرس بدون ما نفكر بعدد الضيوف", "We shouldn't order too much food for the wedding without thinking about the number of guests", "laazim ma niTlub akal katheer lil-3urs bidoon ma nfakkir bi3adad edh-dhuyoof"),
        item("لازم ما يبغى حلو بعد كل وجبة، هذا مب زين له", "They shouldn't want dessert after every meal, this isn't good for them", "laazim ma yibghoon Hilu ba3d kil wajba"),
    ]),

    lesson(35, "Food, Shouldn't Want II", "الأكل، لازم ما تبغى ٢", [
        item("لازم ما تبغى تجرب كل أكلة جديدة مرة وحدة، جرب شوي شوي", "You shouldn't want to try every new dish at once, try little by little", "laazim ma tibgha tjarrib kil akla jideeda marra waHda"),
        item("لازم ما تطبخين للضيوف أكل ما تعرفينه، جربيه على العائلة أول", "You (f) shouldn't cook food you don't know for the guests, try it on the family first", "laazim ma taTbakheen lidh-dhuyoof akal ma ta3rifeenah"),
        item("لازم ما نأكل بسرعة في العرس، خذ وقتك زين", "We shouldn't eat quickly at the wedding, take your time", "laazim ma na'kul bisur3a fil-3urs, khudh wagtak zayn"),
        item("لازم ما تشري تمر كثير بدون ما تسأل عن تاريخه", "You shouldn't buy a lot of dates without asking about their date", "laazim ma tishri tamur katheer bidoon ma tis'al 3an taareekhah"),
    ]),
]


def main():
    numbers = [l["number"] for l in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1)), "lesson numbers must be sequential"
    old = json.loads((ROOT / "data/emirati-src/b2plus.json").read_text(encoding="utf-8"))
    grammar_topics = old.get("grammarTopics", {})
    out = {"level": "b2plus", "grammarTopics": grammar_topics, "lessons": LESSONS}
    out_path = ROOT / "data/emirati-src/b2plus.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    total_items = sum(len(l["items"]) for l in LESSONS)
    print(f"Wrote {len(LESSONS)} lessons, {total_items} items, {len(SEEN)} unique sentences -> {out_path}")


if __name__ == "__main__":
    main()
