# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("c1", "c1")
T = c.T
T("c1-tale", "The Language of Folk Tales", "ни күзе белән күрсен · бара торгач · …ган, ди · инде",
  "Tatar folk tales (әкиятләр) have their own rhythm and formulas. Ни күзе белән күрсен (lit. with what eyes should he see) introduces a surprise: and what does he see! Repetition marks long journeys: Ай бара, ел бара; Баралар-баралар, бара торгач. "
  "Tales mix the present tense with the reportative past -ган, ди, and use particles like инде, бу (this one, for the hero) and икән (it turns out). Magic helpers — the div (дию), the fairy (пәри), the bald lad (Таз) — recur from story to story.",
  "Many Tatar tales were collected in the nineteenth century by Wilhelm Radloff and Kayum Nasyri, and they share plots with Kazakh, Bashkir and Turkish tales.",
  [("A", "Әкиятнең ахыры ничек?", "How does the tale end?"), ("B", "Егет кызны коткара да, алар өйләренә кайтып, рәхәтләнеп яши башлыйлар.", "The young man rescues the girl, and they go home and live happily."), ("A", "Ә дию нишли?", "And what does the div do?"), ("B", "Дию юк та була, ди.", "The div simply vanishes, they say.")])
T("c1-soc", "Society, State and History", "… буларак · … карамастан · … нәтиҗәсендә · … өлкәсендә",
  "Formal Tatar about society and history relies on postpositional phrases: милләт буларак (as a nation), авырлыкларга карамастан (despite difficulties), үзгәртеп корулар нәтиҗәсендә (as a result of reforms), мәгариф өлкәсендә (in the field of education). "
  "Historical narrative uses the present tense for vividness (Хан Сөембикәне хатын итеп ала) or the -ган past for reported facts.",
  "Kazan was the capital of an independent khanate until 1552; its fall is a central theme of Tatar historical memory and literature.",
  [("A", "Казан ханлыгы кайчан яшәгән?", "When did the Kazan Khanate exist?"), ("B", "Унбишенче гасырдан мең биш йөз илле икенче елга кадәр.", "From the fifteenth century until 1552."), ("A", "Аннары нәрсә булган?", "What happened then?"), ("B", "Иван Казанны яулап алган.", "Ivan conquered Kazan.")])
T("c1-lit", "Literature, Language and Ideas", "әсәрдә сурәтләнә · хас булган · иҗат · үзләштерү",
  "Literary criticism in Tatar strings together abstract nouns: тарихилык (historicity), камиллек (perfection), фәлсәфи фикер (philosophical thought). Verbs of depiction and revelation dominate: сурәтли, ачып бирә, гәүдәләндерә, чагылдыра. "
  "Expect long sentences in which participles stack before nouns: Халыкларны берләштергән мәңгелек рухи кыйммәтләр — the eternal spiritual values that unite peoples.",
  "The literary language of the early twentieth century, Tukay's era, was heavily Arabic and Persian; modern critics often still use that vocabulary.",
  [("A", "Бу романның төп темасы нәрсә?", "What's the main theme of this novel?"), ("B", "Ул иреккә омтылыш һәм аның бәясе турында.", "It's about the striving for freedom and its price."), ("A", "Геройларның характерлары ничек ачыла?", "How are the characters revealed?"), ("B", "Көтелмәгән сынаулар аша.", "Through unexpected trials.")])
T("c1-prov", "Longer Proverbs and Sayings", "…, …; …, … · бер — мең · …дан …",
  "Longer proverbs often have three or four parallel parts: Чүлгә кое казыган — бер саваплы, сазга күпер салган — ике саваплы, юлга агач утырткан — өч саваплы. "
  "Numbers (бер, ун, мең) and opposites (яхшы — яман, ачы — татлы, ярлы — бай) give them their shape, and ellipsis is normal: verbs are often dropped where they can be understood.",
  "Proverbs about the tongue (тел) are especially common: Дөньяда иң татлы нәрсә дә — тел, иң ачы нәрсә дә — тел.",
  [("A", "Ник алай кискен сөйләдең?", "Why did you speak so sharply?"), ("B", "Туры сүз башта зәһәр булса да, соңы шикәр.", "A straight word may be poison at first, but it's sugar in the end."), ("A", "Шулай да, йомшаграк кирәк иде.", "Even so, you should have been gentler.")])
T("c1-life", "Reflections and Experience", "… дигән сүз түгел · …ганчы · …ган саен · …дыр",
  "Reflective writing qualifies and contrasts ideas: Акча эшләү — аны теләсә ничек табу дигән сүз түгел (making money doesn't mean getting it any old way). "
  "-ганчы offers an alternative (Өметсезлеккә бирелгәнче, уйлан — before giving in to despair, think), and -дыр/-дер softens a generalisation.",
  "Tatar memoir writing often opens with childhood in the village (авылда үстем) and the contrast between then and now.",
  [("A", "Тормыштан нәрсәгә өйрәндең?", "What has life taught you?"), ("B", "Бар да бетте дип өметсезлеккә бирелмәскә.", "Not to despair thinking all is lost."), ("A", "Ә тагын?", "And what else?"), ("B", "Саулыкның иң кадерле нәрсә икәнен.", "That health is the most precious thing.")])
T("c1-folk", "Customs, Faith and Folk Belief", "ураза · корбан · Кадер кичәсе · албасты · шүрәле",
  "Many Tatar customs are tied to Islam: ураза (the Ramadan fast), Ураза бәйрәме (Eid al-Fitr), Корбан бәйрәме (Eid al-Adha), Кадер кичәсе (the Night of Power). Alongside them live older folk beliefs: the albasty, a night spirit, and the shurale of the forest. "
  "Blessings use -сын: Бәйрәм мөбарәк булсын! Иманыбызны ныгытсын!",
  "Tongue twisters (тизәйткечләр) are a living folk genre: try Җылы җәйнең көннәрендә җәймә тау итәгендә…",
  [("A", "Корбан бәйрәме кайчан?", "When is Kurban Bayram?"), ("B", "Ел саен төрле вакытта, ай календаре буенча.", "At a different time each year, by the lunar calendar."), ("A", "Бәйрәмегез мөбарәк булсын!", "Blessed holiday to you!"), ("B", "Рәхмәт, сезгә дә!", "Thank you, and to you!")])
L = c.L
S = [
('c1-lit', [
    ('Саф татар телендә андый сүз юк һәм аның кем икәнен дә белеп булмый.', "There is no such word in pure Tatar, and you can't even tell where it comes from."),
    ('Авыз эчебездәге телгә охшаган юка, очлы әйберләр шул ук тел исемен ала.', 'Thin, pointed objects shaped like the tongue in our mouth are also called tongues.'),
    ('Күңелем аны уйлый башлады исә, хәзер күземә ап-ак саф бер фәрештә күренә.', 'As soon as my heart begins to think of her, a pure, snow-white angel appears before my eyes.'),
    ('Авылда өч сыйныф укыгач, кыз урта белем алыр өчен Каратун мәктәбенә китә.', 'After three years at the village school, the girl goes to the Karatun school to get a secondary education.'),
]),
('c1-soc', [
    ('Авылдагы иң күп җир ул фермерда, малны да иң күп асраучы ул.', 'That farmer has the most land in the village, and he also keeps the most livestock.'),
    ('Нәрсәсе белән истәлекле соң бу көн, ни өчен без аны шулай зурлыйбыз?', 'What makes this day memorable, and why do we honour it so?'),
    ('Әлегә татарда күп бала табуны эчтән, тирәннән аңлап максат итеп кую юк.', 'As yet, Tatars do not set having many children as a goal that they understand deeply, from within.'),
    ('Алай да чит тел буларак төрек һәм рус телләрен укытырга белгечләр җитми.', "Even so, there aren't enough specialists to teach Turkish and Russian as foreign languages."),
]),
('c1-tale', [
    ('Син миңа фәлән кило ипи, фәлән кило ит, фәлән кило май бир.', 'Give me so many kilos of bread, so many kilos of meat and so many kilos of butter.'),
    ('Патша йокыдан торды да алманы санады: алма да юк, малай да юк.', 'The king woke up and counted the apples: no apple, and no boy.'),
    ('Инде хуш бул, егетем, мин кайту ягын карыйм, син дә өеңә кайт!', "Farewell now, young man; I'm heading home, and you go home too!"),
    ('Мулла торып эзли икән, эзли икән - өйдә беркем дә булмый икән.', "The mullah gets up and searches and searches, but there's nobody in the house."),
]),
('c1-prov', [
    ('Дөньяда иң татлы нәрсә дә — тел, иң ачы нәрсә дә — тел.', 'The sweetest thing in the world is the tongue, and the bitterest thing is the tongue too.'),
    ('Көн китә, атна китә, ай китә, ел китә, бер саплам җир китә.', 'A day goes, a week goes, a month goes, a year goes — and a patch of earth goes with them.'),
    ('Берәү бар — меңгә биргесез, берәү бар — бар икәне дә билгесез.', "Some people you wouldn't give for a thousand; others — nobody even knows they exist."),
    ('Яшь кеше җиде юл чатында тора – кайсы юлдан китүе үзеннән тора.', 'A young person stands at a crossroads of seven roads; which road he takes is up to him.'),
]),
('c1-life', [
    ('Акча эшләү дигәч тә, аны теләсә ничек табу дигән сүз түгел бит.', "Making money doesn't mean getting it any way you like, after all."),
    ('Синең белән танышканнан бирле юньләп ашый да, эчә дә, тарта да алмыйм.', "Ever since I met you, I can't eat, drink or smoke properly."),
    ('Бер гаиләдән ике талант чыгуы да сирәк очрый торган күренеш, миңа калса.', 'Two talents coming from one family is a rare thing, in my view.'),
    ('Без яшәгән бистәдә дә татарлар күп иде, татар малайлары белән уйнап үстем.', 'There were lots of Tatars in our suburb too, and I grew up playing with Tatar boys.'),
]),
('c1-folk', [
    ('Ак чалмалы, яшел чапан кигән бу зыялы шәхес игътибарны еш җәлеп итә.', 'This educated man in a white turban and a green robe often attracts attention.'),
    ('Сәгать ярымнан соң исә кичке намазлар - ястү белән тәравих вакыты керә.', 'An hour and a half later comes the time of the evening prayers, yastu and tarawih.'),
    ('Албасты, кайчагында, бик зур чүмәлә булып юлда барган кешегә ияреп тә бара.', 'The albasty sometimes follows a traveller on the road in the shape of a huge haystack.'),
    ('Рамазан аеның, чыннан да, кайсы кичәсендә булганын бер Аллаһ Үзе генә белә.', 'Only God himself knows on which night of Ramadan it truly falls.'),
]),
('c1-lit', [
    ('Автор биш мәкалә язуны күздә тоткан һәм максатына ирешкән дип әйтәсе килә.', 'One would like to say that the author meant to write five articles and achieved his aim.'),
    ('Ни өчен һәр иреккә омтылыш тагы да тирәнрәк коллыкка төшү белән тәмамлана?', 'Why does every striving for freedom end in falling into even deeper slavery?'),
    ('Чын татар культурасы өлгесе булып хезмәт итә алырлык чыгышлар иде бит алар!', 'Those were performances that could serve as a model of true Tatar culture!'),
    ('Ахыр чиктә героебыз түзми, җырлаучының янына ук бара һәм көйнең исемен сорый.', "In the end our hero can't bear it: he goes right up to the singer and asks the name of the tune."),
]),
('c1-soc', [
    ('Сафа Гәрәй хан егерме ике яшьлек тол Сөембикәне дүртенче хатын итеп ала.', 'Khan Safa Giray takes the twenty-two-year-old widow Syuyumbike as his fourth wife.'),
    ('Беренче сентябрь - халык бәйрәме, һәм ул һәрберебез өчен якын һәм кадерле.', "The first of September is a people's holiday, close and dear to each of us."),
    ('Черек күл бакчасы дигәне Казан халкының аеруча яраткан ял итү урыны булган.', 'The so-called Black Lake garden was a particularly beloved place of rest for the people of Kazan.'),
    ('Алай гына да түгел, бәлагә тарыганнар эшнең нидә булуын аңлатып бирә алмый.', "Not only that — those who have fallen into trouble can't explain what the matter is."),
]),
('c1-tale', [
    ('Төшеп китте дә бу як-ягына карана: өч якка киткән юл чаты бар.', 'He got down and looked around: there was a crossroads with roads going three ways.'),
    ('Инде бар, кызым, мунча як! - дип, ул кызны мунча ягарга җибәрә.', '"Now go, daughter, and heat the bathhouse!" she says, sending the girl off to light it.'),
    ('Әй, бу думбра бик начар икән, аны алмыйм, кирәк булса үзеңә ал!', "Oh, this dombra is very bad; I won't take it — if you need it, take it yourself!"),
    ('Мин күргәннәрне күрсәң, син дә хәер сорашып йөрер идең, - ди бу.', '"If you\'d seen what I\'ve seen, you too would be going about begging," he says.'),
]),
('c1-prov', [
    ('Яхшы сүз аркасында адәм — адәм, яман сүз аркасында адәм — әрәм.', 'Through a kind word a person stays a person; through a harsh word a person goes to waste.'),
    ('Бер сезнең урамда бәйрәм булса, бер безнең урамда бәйрәм булыр.', "If there's a festival in your street once, there'll be a festival in ours once too."),
    ('Иң акыллы кем? дигәч, юләр туктап та тормыйча — мин! — дигән ди.', "When asked, 'Who is the wisest?', the fool answered without a moment's pause: 'Me!'"),
    ('Үзенә ышанган — йокыдан торып киткән, әтәчкә ышанган ятып калган.', 'He who trusted himself got up; he who trusted the rooster overslept.'),
]),
('c1-life', [
    ('Берәүләрнең ул, үз көенә генә аккан елга кебек, тыныч кына, сиздермичә уза.', 'For some people it passes calmly and unnoticed, like a river flowing at its own pace.'),
    ('Мин дә, ачык йөзләрне бик күптән күрмәгәнгә күрә, эчемнән бик шатлана идем.', "Since I hadn't seen friendly faces for a very long time, I was very glad inside."),
    ('Үзем ялгызмын, сөйләшергә кешем юк, бер нәрсә белән күңел ачмыйча булмый бит.', "I'm on my own with nobody to talk to; I can't do without something to cheer myself up."),
    ('Гел үз фикерен генә алга сөргән кеше иртәме соңмы барыбер уңышсызлыкка юлыга.', 'Someone who always pushes only his own opinion will sooner or later meet with failure.'),
]),
('c1-folk', [
    ('Усакның болай ачы сулы түгәрәк яфраклы булып калуына менә нәрсә сәбәп булган.', 'This is why the aspen ended up with such bitter sap and round leaves.'),
    ('Корбанлык өчен пар тояклы - кәҗә, сарык, дөя, сыер кебек хайваннарны алу кирәк.', 'For the sacrifice you must take a cloven-hoofed animal such as a goat, sheep, camel or cow.'),
    ('Аллаһы Тәгалә бу кичәдә шактый күп кешене кичерер, шактыен гафу итмичә калдырыр.', 'On this night God Almighty will forgive a great many people, and leave a great many unforgiven.'),
    ('Корбан бәйрәме - ислам дөньясында иң олы, күңелләргә иң якын бәйрәмнәрнең берсе.', "Kurban Bayram is one of the greatest holidays of the Islamic world and one of the dearest to people's hearts."),
]),
('c1-lit', [
    ('Акмулла мөгаллим, сез бит үзегез дә сүзнең энҗедәй кыйммәтен тоеп иҗат итәсез.', 'Teacher Akmulla, you yourself create with a feeling for the pearl-like value of words.'),
    ('Бәлки шуңа күрәдер дә, Кәрим кунакка кайткач та атасы белән утырып сөйләшмәде.', "Perhaps that's why, even when Karim came home on a visit, he didn't sit down and talk with his father."),
    ('Бары тик кысыла төшкән күзләре генә аның эчке уйларына йотылып баруын күрсәтә.', 'Only his narrowing eyes showed that he was being swallowed up by his inner thoughts.'),
    ('Казандагы Татар дәүләт опера һәм балет академия театры Муса Җәлил исемен йөртә.', 'The Tatar State Academic Opera and Ballet Theatre in Kazan bears the name of Musa Jalil.'),
]),
('c1-soc', [
    ('Яшьләргә эшләр өчен юл ябык, аны нәкъ менә шушындый ярдәм җәмгыятьләре яба.', "The road to work is closed to young people, and it's precisely mutual-aid societies like these that open it."),
    ('Инглиз, алман телен укытуның нинди төрләре генә юк, ел саен үзгәреш, яңалык.', "There are so many ways of teaching English and German; every year there's some change, something new."),
    ('Гаять гүзәл Панаев бакчасы да Казан кешеләренең бик яраткан ял урыны саналган.', 'The beautiful Panaev Garden was also considered a favourite place of rest for the people of Kazan.'),
    ('Алай гына да түгел, белем бирү йортлары укучыларын кабул итәргә тулысынча әзер.', 'Not only that — educational institutions are fully ready to receive their students.'),
]),
('c1-tale', [
    ('Бабай караса, ни күзе белән күрсен - ауга балык бик күп эләккән.', 'The old man looks, and what does he see — a great many fish have been caught in the net.'),
    ('Урман юлы белән бара торгач, бу юл тар гына бер сукмакка әйләнә.', 'After going a while along the forest road, the road turns into a narrow path.'),
    ('Бер көн бара, өч көн бара, дүртенче көн бер елга буена туры килә.', 'He travels for one day, he travels for three, and on the fourth day he comes to a river.'),
    ('Ай бара, ел бара бу, бара торгач, караңгы бер урманга барып керә.', 'Months go by, years go by, and after a while he enters a dark forest.'),
]),
('c1-prov', [
    ('Ишәк җиде төрле йөзә белсә дә, су янына килгәч җидесен дә онытыр.', 'Even if a donkey can swim seven ways, it forgets all seven when it reaches the water.'),
    ('Күккә менсәң - аягыңнан тартыр, җиргә керсәң - колагыңнан тартыр.', "Climb to the sky and he'll pull you down by the foot; go underground and he'll pull you up by the ear."),
    ('Салкын йөзледән җылы сүз чыкмас, салкын мичтән җылы күмәч чыкмас.', 'No warm word comes from a cold face, and no warm loaf comes from a cold oven.'),
    ('Бала әйткән ди: мине берәү дә тыңламый, чөнки минем әле сакалым юк.', "The child said: nobody listens to me, because I don't have a beard yet."),
]),
('c1-life', [
    ('Бар да бетте дип өметсезлеккә бирелгәнче нәрсә дә булса эшләп булмыймы дип уйлан.', 'Before you give in to despair thinking all is lost, consider whether something can still be done.'),
    ('Адәм баласының иң кадерле, иң затлы һәм иң кыйммәтле бердәнбер нәрсәсе - саулыгы.', 'The dearest, most precious and most valuable thing a human being has is health.'),
    ('Маңгай күзе белән күрү сәләтеннән тыш, күңел күзе белән күрү мөмкинлеге дә бирелә.', 'Besides the ability to see with the eyes in your forehead, you are also given the chance to see with the eye of the heart.'),
    ('Абый, безнең хәтерне ныгыту өчен, әллә нинди күнегүләр, хәйләләр уйлап чыгара иде.', 'To strengthen our memory, my older brother would invent all kinds of exercises and tricks.'),
]),
('c1-folk', [
    ('Шүрәле алдаган кайбер кешеләр урман уртасында адашып калып һәлак тә булалар икән.', 'Some of the people Shurale tricked got lost in the middle of the forest and even perished, they say.'),
    ('Ислам галимнәре раслаганча, Кадер кичәсеннән соң иң изге кичә - Бәраәт кичәседер.', "As Islamic scholars confirm, after the Night of Power the holiest night is the Night of Bara'at."),
    ('Җылы җәйнең көннәрендә җәймә тау итәгендә җизни кызы Җәүһәрия җиләк җыя чиләгенә.', "On warm summer days, on the slope of Jayma hill, Jizni's daughter Jauhariya picks berries into her bucket. (a tongue twister on the sound җ)"),
    ('Карга әйтә: кар-кар, җирдә орлык бар-бар, урлап кына китим әле, сакчылары ялда...', "The crow says: caw-caw, there's grain on the ground, grain-grain — let me just steal some, the guards are resting..."),
]),
('c1-lit', [
    ('Алардан курантлар тавышы да, хөр рухлы шигырь дә, бурлакларның җыры да ишетелә.', 'From them you hear the chimes of the clock tower, freedom-loving poetry and the songs of the barge-haulers.'),
    ('Ике генә битлек хикәяләрендә дә ул авыл кешеләренең характерларын коеп кына куя.', 'Even in his two-page stories he captures the characters of village people perfectly.'),
    ('Инеш, Аюкөйдергән елгасы белән бер үк юнәлештә агып, Чирмешән елгасына коя икән.', 'The Inesh flows in the same direction as the Ayukoydergan river and empties into the Cheremshan.'),
    ('Ике романның икесендә дә зур урынны әнә шул укымышлылар һәм аларның хәрәкәте ала.', 'In both novels these educated people and their movement occupy a large place.'),
]),
('c1-soc', [
    ('Яңа туган балалар саны тотрыклы рәвештә арта бара, моңа шатланмый мөмкин түгел.', "The number of newborns is rising steadily, and one can't help being glad about that."),
    ('Ханлыкның бөтен гаскәре кырылып беткәч кенә, Иван изге Казан каласына килеп керә.', "Only after the khanate's entire army had been wiped out did Ivan enter the holy city of Kazan."),
    ('Аксак Тимер гаскәреннән берәр төркемнең Болгарга яу белән килгән булуы да ихтимал.', "It is also possible that some detachment of Timur's army came to Bolgar on a raid."),
    ('Рухи сәламәт илдә генә физик һәм акыл ягыннан камил яшь гражданнар тәрбияләнә шул.', 'Only in a spiritually healthy country are young citizens raised who are physically and intellectually well rounded.'),
]),
('c1-tale', [
    ('Айгыр диңгез төбеннән чыга да, Таз шул атка атланып очып та китә.', 'The stallion comes up from the bottom of the sea, and the bald lad mounts it and flies away.'),
    ('Озак көтәргә туры килми, чебен тишектән кире чыга да очып та китә.', "There's not long to wait: the fly comes back out of the hole and flies away."),
    ('Җиргә килеп чыккач, бик шатлана инде, бик күп вакыт үткән була бит.', 'When he came out onto the earth, he was overjoyed — after all, a great deal of time had passed.'),
    ('Кая киттеләр икән дип эзләп йөри-йөри дә, барып чыга бу бер шәһәргә.', 'Searching to see where they had gone, he wanders on and on and comes to a city.'),
]),
('c1-prov', [
    ('Дөреслек синең ягыңда булса, кырык мең кеше каршы булса да курыкма.', "If the truth is on your side, don't be afraid even if forty thousand people are against you."),
    ('Булыр бала ун яшендә баш була, булмас бала егерме биштә дә яшь була.', "A child who will make something of himself is a leader at ten; one who won't is still a child at twenty-five."),
    ('Егет кешенең сүзе дә, эше дә бер була, бер эшне икенче тапкыр эшләми.', "A real man's word and deed are one: he never does the same job twice."),
    ('Бер куркакның бәласе меңгә тияр, куркак белән юлдаш булсаң җаның көяр.', "One coward's trouble falls on a thousand; travel with a coward and your soul will burn."),
]),
('c1-life', [
    ('Авылга кайтканда ерактан мәчетнең айлы манарасы каршы ала һәм киткәндә озатып кала.', "When you come home to the village, the mosque's crescent-topped minaret greets you from afar, and when you leave it sees you off."),
    ('Без бу гөнаһыбызны өлкән һәм кече якыннарыбызга хөрмәт күрсәтү белән генә юа алабыз.', 'We can wash away this sin of ours only by showing respect to our loved ones, old and young.'),
    ('Тел - бер милләт вәкилләрен берләштерә торган, бербөтен итә торган ышанычлы корал ул.', 'Language is a reliable tool that unites the members of one nation and makes them whole.'),
    ('Аннан бераз вакыт узганнан соң гына җайлап, аз-азлап кына кимчелекләрен күрсәтеп була.', 'Only after some time has passed can you gently, little by little, point out shortcomings.'),
]),
('c1-folk', [
    ('Андый ук мөмкинчелеге булмаган кешеләргә бөтен гаиләгә бер корбан чалырга да ярый.', 'People without the means are also allowed to sacrifice one animal for the whole family.'),
    ('Авыл халкы сөйләшеп, килешеп, Балтай авылы халкыннан бәйрәм йоласы сатып алырга булганнар.', 'After talking it over and agreeing, the villagers decided to buy a festival custom from the people of Baltay.'),
    ('Хаҗ кылучылар тарафыннан Мәккә янындагы Гарәфә тавына бару һәм тау итәгендә намаз уку көне.', 'It is the day on which pilgrims go to Mount Arafat near Mecca and pray at the foot of the mountain.'),
    ('Җәбраил фәрештә пәйгамбәребезне җиде кат күккә хәтле алып йөрткән һәм аннан ары уза алмаган.', 'The angel Gabriel carried our Prophet up to the seventh heaven and could go no further.'),
]),
('c1-lit', [
    ('Әдип бу реаль шәхесне еш кына борынгы күренекле әдәби образларга илтеп тоташтыра.', 'The writer often links this real person to famous literary images of the past.'),
    ('Фараз итегез: дөньяның барлык бәхетләре илә тулган, хыялый бер алтын сарай булсын.', 'Imagine a dreamlike golden palace filled with all the happiness in the world.'),
    ('Берничә катлаулы чорны узган Ильяс соңгы җәендә иң аянычлы нәтиҗәләрен ясый кебек.', 'Having lived through several difficult periods, Ilyas seems to draw his saddest conclusions in his last summer.'),
    ('Әсәрдә аның һәммә эше, хәрәкәте, хәтта аның йомшаклыклары да уңай бәя белән бирелә.', 'In the work, all his deeds and actions, even his weaknesses, are presented in a positive light.'),
]),
('c1-soc', [
    ('Аларда сугышчы җайдаклар, барс, тау кәҗәсе, дөя һәм башка җәнлек сурәтләре ясалган.', 'Images of warrior horsemen, snow leopards, mountain goats, camels and other animals are depicted there.'),
    ('Авыл мәктәбендә элек-электән укытучыларга абый, апа, дип якын итеп дәшү гадәте бар.', "Village schools have a long-standing habit of addressing teachers warmly as 'abi' and 'apa'."),
    ('Авылга капитализм тирәнрәк үтеп кергән бер чорда бу катлам таркалу процессы кичерә.', 'At a time when capitalism was penetrating deeper into the countryside, this class was going through a process of disintegration.'),
    ('Акыллы кешеләр дә, табиблар да, шәкертләр дә, азанчылар да, вәгазьчеләр дә җитәрлек.', 'There are plenty of wise people, doctors, students, muezzins and preachers.'),
]),
('c1-tale', [
    ('Ялгыз җирдә торганчы, мин дә сезнең белән барыйм, - дип, ул да иярә.', '"Rather than stay alone here, let me go with you too," he says, and follows them.'),
    ('Син баргач, үзе айгыр булып сарайга ябыла ул, сине үтерергә тели ул.', 'When you go, he will shut himself in the palace as a stallion; he wants to kill you.'),
    ('Бер бик яхшы атка яхшы ияр салып, аллага тапшырып, юлга чыгып китте.', 'He put a good saddle on a fine horse, commended himself to God and set off on his way.'),
    ('Бинаны карап йөри, бер җирдә ишек тә, тишек тә юк, үзе галәмәт биек.', "He walks round looking at the building: nowhere a door or even a hole, and it's tremendously tall."),
]),
('c1-prov', [
    ('Кешене беләсең килсә, холкына кара, баланы беләсең килсә, уенына кара.', 'To know a person, look at their character; to know a child, look at how it plays.'),
    ('Вакыт акча түгел – аны саклауга куеп та, югалтсаң кире табып та булмый.', "Time isn't money: you can't save it up, and if you lose it, you can't find it again."),
    ('Җавап бирмәү дә шәп түгел, җавап бирә башласаң, аңкауны яшь бәрәңге өтә.', "Not answering isn't good either; but start answering, and the simpleton gets burned by the new potato."),
    ('Берәү кеше батканны күреп батмаска өйрәнә, берәү үзе батып карап өйрәнә.', 'One person learns not to drown by watching someone drown; another learns by drowning himself.'),
]),
('c1-life', [
    ('Үзең белән бары тик вак-төяк чыгымнарга һәм сувенирларга гына акча алырга кирәк булачак.', "You'll only need to take money with you for small expenses and souvenirs."),
    ('Иҗатта мин ирешкәннәр кемгәдер чүп кенә, ә кемгәдер могҗиза булып кына күренергә мөмкин.', "What I've achieved in my work may look like rubbish to some and a miracle to others."),
    ('Агачлардагы алмалар, әллә кайлардан ялтырап, безнең дә өзеләсе чаклар җитте, диләр кебек.', "The apples on the trees, gleaming from afar, seem to say: it's time for us to be picked too."),
    ('Мин бу акчага Әтнә базарында ак күмәч сатып алып, өйгә кайтканда, юл буе ашап кайта идем.', 'With this money I used to buy white bread at the Atnya market and eat it all the way home.'),
]),
('c1-folk', [
    ('Ак яулыклы әбиләр һәм түбәтәйле бабайлар мөнәҗәтчеләрнең чыгышын аеруча яратып кабул иттеләр.', "Grandmothers in white headscarves and grandfathers in skullcaps particularly enjoyed the munajat singers' performance."),
    ('Мондый итне үзеңә ашарга ярамый, тулысынча таратып бетерергә яисә кеше җыеп аш үткәрергә кирәк.', 'You may not eat such meat yourself; you must give all of it away or gather people for a meal.'),
    ('Ураза тотучы кеше билгеле вакытта ризыктан, судан, яман сүздән, якынлык кылудан тыелып торырга тиеш.', 'A person who is fasting must, at certain times, abstain from food, water, bad language and intimacy.'),
    ('Ураза бәйрәме иманыбызны ныгытсын, гаиләләребезгә шатлык китерсен, киләчәккә ышаныч һәм өмет иңдерсен!', 'May Eid al-Fitr strengthen our faith, bring joy to our families and give us confidence and hope for the future!'),
]),
('c1-lit', [
    ('Милләтнең хәзергесе һәм киләчәге өчен файдалы чәчмә яки тезмә берәр нәрсәгез бармы?', "Do you have anything in prose or verse that would be useful for the nation's present and future?"),
    ('Фазыл Туйкинның эшчәнлеге һәм күпчелек әсәрләре өчен хас булган сыйфат - тарихилык.', "The quality typical of Fazyl Tuykin's work and most of his writings is historicity."),
    ('Югыйсә, организмны энергия - көч-тәкать белән тәэмин итәр өчен күп азык кирәкми бит.', "Yet the body doesn't actually need much food to be supplied with energy and strength."),
    ('Нечкә тоем, тирән уй, фәлсәфи фикер, гражданлык пафосы - шагыйрь иҗатының төп асылы.', "Fine feeling, deep thought, philosophical reflection and civic passion are the essence of the poet's work."),
]),
('c1-soc', [
    ('Болгарга килүчеләр үзләрен шул изге мөселман җирендә булып кайткан кебек хис итәчәк.', 'Those who come to Bolgar will feel as if they have visited that holy Muslim land.'),
    ('Авылда дәүләт оешмаларыннан бер хезмәткәр белән клуб һәм фельдшер үзәге генә калган.', 'In the village, of all the state institutions, only one employee, the club and a medical post remain.'),
    ('Хәзерге заманда мәчет диварларын краннан башка күтәрүне күз алдына да китереп булмый.', "Nowadays it's impossible even to imagine raising the walls of a mosque without a crane."),
    ('Моннан тыш, авылда кече һәм урта эшкуарлык субъектларына бирелүче кредит күләме арта.', 'In addition, the amount of credit given to small and medium businesses in the countryside is growing.'),
]),
('c1-tale', [
    ('Син терлекләрне кара, ә мин бераз йоклап алыйм, - ди дә ятып йоклый.', '"You look after the animals, and I\'ll have a little sleep," he says, and lies down and sleeps.'),
    ('Моннан түбән бер су бар, шул су буенда минем өем бар, тегермәнче мин.', "Below here there's a river, and by that river is my house; I'm the miller."),
    ('Син инде минем өстемнән төш тә бу ком тавының аръягына чыгарга тырыш.', 'Get down off me now and try to get to the other side of this sand dune.'),
    ('Бер сукыр карчык белән сукыр карт кына бу йортта, башка беркем дә юк.', "Only a blind old woman and a blind old man live in this house; there's nobody else."),
]),
('c1-prov', [
    ('Күркә ун күкәй салса да дәшми, тавык берне салса да күрше авылга ишетелә.', 'The turkey lays ten eggs and keeps quiet; the hen lays one and the next village hears about it.'),
    ('Сиңа бирелгән ике колак, бер тел: ике тыңла, бер сөйлә, калганын үзең бел.', 'You were given two ears and one tongue: listen twice, speak once, and figure out the rest yourself.'),
    ('Бер ялганнан йөз ялган туган да ди, бер дөрес сүз йөзен дә бәреп еккан, ди.', 'From one lie a hundred lies were born, they say, but one true word knocked all hundred down.'),
    ('Тән биргән дә ана, сөт биргән дә ана, тел биргән дә ана, көй биргән дә ана.', "It's a mother who gives the body, a mother who gives milk, a mother who gives language and a mother who gives the melody."),
]),
('c1-life', [
    ('Без, ирләр өчен, хатын-кыз - сөйгән яр да, сөйкемле кәләш тә, тугрылыклы тормыш иптәше дә.', 'For us men, a woman is a beloved, a charming bride and a faithful companion in life.'),
    ('Яңа ел бәйрәмен без мандаринсыз, ак карсыз, бизәлгән чыршысыз күз алдына да китерә алмыйбыз.', "We can't even imagine New Year without tangerines, white snow and a decorated fir tree."),
    ('Язмыш кайбер вакытта бичара адәмнең өстеннән, үзенә дә сиздермичә, үтә кызганычсыз көлеп куя.', 'Sometimes fate laughs quite pitilessly at a poor human being without him even noticing.'),
    ('Икеләнү, төшенкелеккә бирелүгә әзер халәттән мине ул вакытта йөргән кызым Лилия өстерәп чыгарды.', 'At the time it was my girlfriend Liliya who pulled me out of a state of doubt and despair.'),
]),
('c1-lit', [
    ('Әгәр ташны өскә ыргыткач ул кире җиргә төшсә, димәк аңа җирнең тарту көче тәэсир итә.', "If a stone thrown upwards falls back to the ground, it means the earth's gravity is acting on it."),
    ('Аеруча галимнең җәмәгате Маһинур ханымның чыгышы бик кызыклы һәм мәгълүматка бай иде.', "The talk by the scholar's wife, Mrs Mahinur, was especially interesting and rich in information."),
    ('Боларның шактый зур өлеше күренекле композитор Рөстәм Яхин белән иҗади дуслыкта туган.', 'A large part of them was born of his creative friendship with the well-known composer Rustem Yakhin.'),
    ('Авылда берәү дә аның гөнаһлы мәхәббәт маҗараларын белмәде, хатыны, сизенсә дә, дәшмәде.', 'Nobody in the village knew about his sinful love affairs; his wife, even if she suspected, said nothing.'),
]),
('c1-soc', [
    ('Хәтта төрле әләкләр аркасында бабасының үзенең дә берничә елга сөргенгә сөрелүен яза.', 'He even writes that, because of various denunciations, his grandfather himself was exiled for several years.'),
    ('Алай гына да түгел, галимнәр, Татарстан Фәннәр Академиясе белән дә хезмәттәшлек кирәк.', 'Not only that — cooperation with scholars and with the Tatarstan Academy of Sciences is also needed.'),
    ('Әгәр киләчәктә шушы сәясәт белән барсалар, дәүләтләренең юкка чыгачагы көн кебек ачык.', "If they go on with this policy in future, it's as clear as day that their state will disappear."),
    ('Билгеләп үтик, хәзерге вакытта шәһәрдә бер мәчет тә юк, бары тик гыйбадәтханә генә бар.', "It should be noted that at present there isn't a single mosque in the town, only a church."),
]),
('c1-tale', [
    ('Безнең егет өч көн, өч төн йокламаган иде, юлда йоклап кала күрмәсен.', "Our lad hadn't slept for three days and three nights — let's hope he doesn't fall asleep on the road."),
    ('Атасы бу чәчәкнең бик еракта булуын белсә дә, алып кайтырга сүз бирә.', 'Although the father knows the flower is very far away, he promises to bring it back.'),
    ('Бер адәм кибеткә керә дә, ике стаканга йөзәр грамм аракы салдырып ала.', 'A man goes into a shop and has a hundred grams of vodka poured into each of two glasses.'),
    ('Сарайның ишеген ачып карасалар, җилләр искән, - кыз да юк, егет тә юк.', 'When they opened the palace door and looked in, the place was empty: no girl, no young man.'),
]),
('c1-prov', [
    ('Бармаган җирдә бакыр бар, күрмәгән җирдә көмеш бар, алмаган җирдә алтын бар.', "Where you haven't been there's copper, where you haven't looked there's silver, where you haven't taken there's gold."),
    ('Кырык ел кабер каравылчысы булып торган, атасы кабере кайда икәнен белмәгән.', "He was a graveyard watchman for forty years and didn't know where his father's grave was."),
    ('Акыллының чәче уйдан агара, ахмакның чәче мин дә калмыйм дип юкны уйлап агара.', "A wise man's hair turns grey from thinking; a fool's hair turns grey from worrying about nothing, so as not to be left behind."),
    ('Яхшылыкка яхшылык - һәр кешенең эшедер, яманлыкка яхшылык - ир кешенең эшедер.', "Repaying good with good is everyone's business; repaying evil with good is the business of a real man."),
]),
('c1-life', [
    ('Эт белән мәчене үзара килештерәм дип азаплану – чалбарны баш аша киергә маташуга тиң юләр гамәл.', 'Struggling to make the dog and cat get along is as foolish as trying to pull your trousers on over your head.'),
    ('Чүлгә кое казыган - бер саваплы, сазга күпер салган - ике саваплы, юлга агач утырткан - өч саваплы.', 'Dig a well in the desert — one good deed; build a bridge over a swamp — two; plant a tree by the road — three.'),
    ('Егет алты аргамакның тезген бауларын кисеп алды, калган аргамакның тезген бавын кисмәде, тартып алды.', "The young man cut the reins of six steeds; the reins of the last steed he didn't cut but pulled free."),
    ('Тагын бераз килгәннән соң, Ак бүренең урманына килеп җиттеләр дә бер бик әйбәт аланга килеп төштеләр.', "After travelling a little further, they reached the White Wolf's forest and came down into a lovely clearing."),
]),
('c1-lit', [
    ('Безнең борынгы поэзиядә еш кына сөеклеңне төштә күреп гашыйк булу очраклары тасвирлана.', "Our old poetry often describes falling in love with one's beloved after seeing them in a dream."),
    ('Автор аның аша укучы-тамашачыны үз карашлары белән таныштыра, туган төбәгенә дан җырлый.', 'Through him the author introduces the reader and viewer to his own views and sings the praises of his native region.'),
    ('Кем белә, әгәр укыса, махсус белем алган булса, бәлки шагыйрә чыккан булыр иде аннан да.', 'Who knows — if she had studied and received a special education, perhaps she too would have become a poet.'),
    ('Күп кенә атаклы каләм осталары Тукайны остаз һәм үзләренә бөек үрнәк дип таныды һәм таный.', 'Many famous writers have recognised, and still recognise, Tukay as their teacher and great example.'),
]),
('c1-soc', [
    ('Авылда калучылар аз булса да Русия буенча сибелеп яшәүче сыйныфташлар бер-берсен тапты.', 'Although few stayed in the village, classmates scattered all over Russia found one another.'),
    ('Бәйрәмгә бик күп кеше - татар җәмгыяте активистлары һәм төрле милләт вәкилләре җыелган.', 'A great many people came to the festival: activists of the Tatar community and people of various nationalities.'),
    ('Һәр кеше Болгарга килгән саен, Ак мәчетне карар һәм аның мөһимлегенә инаныр дип уйлыйм.', "I think that every time people come to Bolgar, they'll see the White Mosque and be convinced of its importance."),
    ('Сугыш һәрбер йортның бусагасын атлап керде һәм яхшылардан да иң яхшыларның гомерен алды.', 'The war crossed the threshold of every house and took the lives of the very best of the good.'),
]),
('c1-tale', [
    ('Егет моны кечкенә эш дип белеп, бик куанды, үзе генә башкарырга булды.', 'Thinking this a small task, the young man was delighted and decided to do it by himself.'),
    ('Егет белән кыз бер таш койма буена килеп җиткәч, кыз тагы ятып тыңлый.', 'When the young man and the girl reach a stone wall, the girl lies down again and listens.'),
    ('Ник елыйсың, шул адәм кушканны гына эшли алмаска, син адәм баласы бит.', "Why are you crying because you can't do what that man ordered? You're a human being, after all."),
    ('Инде тагы бер ай тулганда, юл буенда бер карача гына өйгә туры киләләр.', 'When another month had passed, they came upon a small dark hut by the road.'),
]),
('c1-prov', [
    ('Берәү бар — иделдән ил кичергән, меңнәр бар — ник туганын белми гомер кичергән.', 'One man has carried a nation across the Volga; thousands have lived their lives not knowing why they were born.'),
    ('Ун адәм салган күперне бер адәм бозар, бер адәмнең яккан утына ун адәм җылыныр.', "One man can ruin a bridge that ten men built; ten men can warm themselves by one man's fire."),
    ('Таш чүлмәккә бәрелсә дә, чүлмәк ватыла; чүлмәк ташка бәрелсә дә, чүлмәк ватыла.', "Whether the stone hits the pot or the pot hits the stone, it's the pot that breaks."),
    ('Яхшы — күргән яхшылыгын сөйләр, яман — күргән яхшылыгын да яманлык итеп сөйләр.', 'A good person tells of the good he has received; a bad one tells even the good he received as evil.'),
]),
('c1-life', [
    ('Төшендә биек коймалар белән әйләндереп алынган бер бакчада бик матур чәчәк белән уйнап йөргәнен күрә.', 'In his dream he sees himself playing with a very beautiful flower in a garden surrounded by high walls.'),
    ('Тылсымлы әкиятләрнең бер өлеше аталар һәм балалар арасындагы мөнәсәбәтләрне сурәтләүдән башланып китә.', 'Some magic tales begin by depicting the relationship between fathers and children.'),
    ('Елга бер мәртәбә була торган күркәм бәйрәмебез- Корбан гаете барчаларыбызга мөбарәк һәм хәерле булсын!', 'May our beautiful once-a-year festival of Kurban Bayram be blessed and good for all of us!'),
    ('Егерменче йөз татар поэзиясе тарихына багышланган фәнни хезмәтләр, истәлекләр, хикәяләр, романнар авторы.', 'He is the author of scholarly works, memoirs, short stories and novels devoted to the history of twentieth-century Tatar poetry.'),
]),
('c1-lit', [
    ('Әсәрдә ул Сөембикә, Казан ханлыгы белән бәйләнешле тарихи фактларга тугрылыклы булып кала.', 'In the work he stays faithful to the historical facts relating to Syuyumbike and the Kazan Khanate.'),
    ('Габдулла Тукай - үзе исән чагында ук халык шагыйренә әверелгән сирәк әдипләребезнең берсе.', "Gabdulla Tukay is one of our rare writers who became the people's poet in his own lifetime."),
    ('Нәтиҗәдә, ул хәзерге укучыга бик якын, кадерле, аңлаешлы матур образ гәүдәләндерүгә иреште.', "As a result, he succeeded in creating a beautiful image that is close, dear and understandable to today's reader."),
    ('Аларда художестволы камиллеккә, пөхтәлеккә омтылыш, югары зәвыкка исәп тотып язу көчле иде.', 'In them there was a strong drive for artistic perfection and neatness, writing with refined taste in mind.'),
]),
('c1-soc', [
    ('Татар һәм рус телләрендә архитектура буенча лекцияләр укый һәм гамәли дәресләр алып бара.', 'He gives lectures on architecture in Tatar and Russian and leads practical classes.'),
    ('Казандагы зур хоккей бәйрәме белән бүген Континенталь хоккей лигасында өченче сезон ачыла.', 'Today a great hockey celebration in Kazan opens the third season of the Kontinental Hockey League.'),
    ('Киләчәктә дә әлеге тиңсез казанышыбызның кадерен белеп, әҗерен күреп яшәргә насыйп булсын.', 'May we be granted to go on valuing this unique achievement of ours and reaping its rewards in future too.'),
    ('Еллар узган саен без Бөек Җиңүнең олуг әһәмиятен, рухи дәвамчанлыгын ачыграк аңлый барабыз.', 'As the years pass, we understand ever more clearly the great significance and spiritual legacy of the Great Victory.'),
]),
('c1-tale', [
    ('Бәдри абзый, мине өенә алып кайткач та, үзе бер эш белән Казанга китте.', 'Uncle Badri, as soon as he had taken me home, went off to Kazan on some business.'),
    ('Улым, ди, минем бер таныштан өч мең аласым бар иде, шуны алып кайт әле.', '"Son," he says, "an acquaintance owes me three thousand; go and fetch it for me."'),
    ('Ничәмә генә бәлеш кискән булса да, мәзин хатыны бу бәлешне кисә алмады.', "However many pies she had cut in her life, the muezzin's wife couldn't cut this pie."),
    ('Күптәннән бирле дошман күреп килгән бер кешем бар иде, шул талап китте.', "There was a man who had long been my enemy, and he's the one who robbed me."),
]),
('c1-prov', [
    ('Теле белән күктәге айны йөртә белгән, кулы белән казандагы майны эретә белмәгән.', "With his tongue he could move the moon in the sky, but with his hands he couldn't melt the butter in the pot."),
    ('Көзге бозның көзге калынлыгына да ышан, язгы бозның ястык калынлыгына да ышанма.', "Trust autumn ice that is as thin as a fingernail, but don't trust spring ice even when it's as thick as a pillow."),
    ('Атасы малаена алма бакчасы ясап биргән, малае атасына сыңар алма да бирә белмәгән.', "The father made his son an apple orchard, but the son couldn't even give his father a single apple."),
    ('Шомырт чәчәк аткан вакытта кызлар җилкенә, балан чәчәк аткан вакытта балык сикерә.', 'When the bird cherry blossoms, girls get restless; when the viburnum blossoms, fish leap.'),
]),
('c1-lit', [
    ('Билгеле булганча, тарихи әсәр язарга алынган язучыга талантлы каләм остасы булу гына җитми.', 'As is well known, being a talented writer is not enough for someone who sets out to write a historical work.'),
    ('Араларында җаваплы мәхәббәт булса да, әлеге пар хисләрен тануга озын-озак сынаулар аша килә.', 'Although their love is mutual, the couple comes to acknowledge their feelings only through long trials.'),
    ('Булган кадәресе, язылган һәм без укыган кадәресе, һичшиксез, соклану һәм олы ихтирамга лаек.', 'What has existed, what has been written and what we have read undoubtedly deserves admiration and deep respect.'),
    ('Эшлекле белем - стандарт керткән яңалыкның әһәмиятле эчтәлеген ачып бирүче иң гомуми төшенчә.', 'Business knowledge is the most general concept revealing the significant content of the innovation introduced by the standard.'),
]),
('c1-soc', [
    ('Бүген татарларның өчтән бере - Татарстанда, калганнары - башка төбәкләрдә, чит илләрдә яши.', 'Today a third of Tatars live in Tatarstan; the rest live in other regions and abroad.'),
    ('Корылма механикасы фәне буенча русча һәм татарча лекцияләр укый, гамәли дәресләр алып бара.', 'He lectures on structural mechanics in Russian and Tatar and leads practical classes.'),
    ('Татарстан гына да өч миллион халкыннан җиде йөз меңнән артык улын һәм кызын фронтка озатты.', 'Tatarstan alone, out of its three million people, sent more than seven hundred thousand sons and daughters to the front.'),
    ('Татарстан инде егерме елдан артык социаль-икътисади һәм сәяси үзгәртеп корулар юлыннан атлый.', 'For more than twenty years Tatarstan has been following the path of socio-economic and political reform.'),
]),
('c1-tale', [
    ('Камчы белән шундый китереп суга егет, бер савуда ун чиләк сөт бирә теге.', 'The young man strikes it so hard with the whip that it gives ten buckets of milk at one milking.'),
    ('Әгәр дә, ачу тотып, әз генә киссәгез, барыгызны да эштән азат итәчәкмен.', "If you lose your temper and cut even a little, I'll dismiss every one of you."),
    ('Берничә сәгать үткәннән соң, бу күлгә бер көтү елкылар килеп су эчәрләр.', 'A few hours later a herd of horses will come to this lake to drink.'),
    ('Егет, берничә көн үткәч, унике йөк мал төяп, кыз белән өенә кайтып керә.', 'A few days later the young man comes home with the girl, carrying twelve loads of goods.'),
]),
('c1-prov', [
    ('Бакыр зур булса да, комган төбе ямыйлар, алтын кечкенә булса да, күкрәккә кадыйлар.', "Copper may be large, but it's used to patch a kettle's bottom; gold may be small, but it's pinned to the breast."),
    ('Туры сүз башта зәһәр булса да соңы шикәр; ялган сүз башта шикәр булса да соңы зәһәр.', 'A straight word may be poison at first but sugar in the end; a false word may be sugar at first but poison in the end.'),
    ('Көзге катык, көмеш кашык - кызым белән киявемә; язгы катык, ярык кашык - улым белән киленемә.', 'Autumn yoghurt and a silver spoon for my daughter and son-in-law; spring yoghurt and a cracked spoon for my son and daughter-in-law.'),
    ('Баладан бәхетең булса, карт көнеңдә яшь итәр; баладан бәхетең булмаса, иртә яшьтән карт итәр.', "If your children bring you happiness, they'll keep you young in old age; if not, they'll make you old while you're still young."),
]),
('c1-lit', [
    ('Җыр сәнгатендә белемен камилләштерү максатыннан ул Көнчыгыш музыка техникумына да укырга керә.', 'To perfect his singing, he also enrolled at the College of Oriental Music.'),
    ('Башта ул редакциянең тәнкыйть бүлеге мөдире, соңга таба җаваплы секретарь вазифаларын башкара.', "At first he works as head of the editorial office's criticism department, and later as executive secretary."),
    ('Габдулла Тукай үткен каләмле публицист һәм журналист буларак та милләт файдасына күп хезмәт итә.', 'Gabdulla Tukay also served the nation a great deal as a sharp-penned essayist and journalist.'),
    ('Иҗат барышында аңа материалны бер үк вакытта тарихи һәм эстетик җәһәттән үзләштерергә туры килде.', 'In the course of his work he had to master the material from both a historical and an aesthetic point of view.'),
]),
('c1-soc', [
    ('Шуны истә тотарга кирәк: Россия Федерациясе - күп мәдәниятле, күп милләтле, күп динле дәүләт.', 'It must be remembered that the Russian Federation is a multicultural, multi-ethnic and multi-faith state.'),
    ('Ай дәвамында Татарстан рәссамнарының әлеге темага язылган рәсемнәре һәм яңа эшләре каралачак.', 'Over the month, paintings by Tatarstan artists on this theme and their new works will be on display.'),
    ('Төрле милләтләр һәм төрле дин тотучылар тату яши торган Татарстан бу уңайдан бер үрнәк мисал.', 'In this respect Tatarstan, where different nationalities and faiths live in harmony, is a fine example.'),
    ('Ахырда Нугайдан, Кырымнан көчле гаскәр туплап, өченче тапкыр үз урынына, Казан тәхетенә кайта.', 'In the end, gathering a strong army from the Nogais and Crimea, he returns for the third time to his place, the throne of Kazan.'),
]),
('c1-tale', [
    ('Егет бу кояш яктысын ала торган җанвар тиресен күтәреп алып кайтып китә.', 'The young man picks up the skin of the creature that takes the light of the sun and carries it home.'),
    ('Әти, нигә син фермадан кайтканда гел арбага күп итеп печән төяп кайтасың?', 'Dad, why do you always bring home a cart heaped with hay when you come back from the farm?'),
    ('Фатир хуҗабикәсе өстәлгә табагы белән эре дә, яшь тә бәрәңге китереп куя.', 'The landlady puts a dish of big new potatoes on the table.'),
    ('Барыгыз, - хәзер үк табып китерегез! - дип, өч-дүрт диюен эзләргә җибәрә.', '"Go and find it and bring it here right now!" he says, and sends three or four divs to search.'),
]),
('c1-lit', [
    ('Беренче битләреннән үк автор укучыны мавыктыргыч һәм гыйбрәтле маҗаралар дөньясына алып кереп китә.', 'From the very first pages the author draws the reader into a world of gripping and instructive adventures.'),
    ('Романның матбугат мәйданына чыгуы заманында татар матбугаты тарафыннан яхшы караш белән каршы алынды.', 'When the novel first appeared in print, it was well received by the Tatar press.'),
    ('Фаза югалып, җирнең түбәсе катлаулы-катлаулы, кара, караңгы һәм авыр болытлардан гыйбарәт булып калды.', "The phase was lost, and the earth's ceiling became nothing but layer upon layer of black, dark, heavy clouds."),
    ('Кабатланмас матур тавышка ия җырчы тиз арада ансамбльнең алдынгы башкаручыларыннан берсе булып таныла.', "The singer, who has a uniquely beautiful voice, is soon recognised as one of the ensemble's leading performers."),
]),
('c1-soc', [
    ('Авырлыкларга карамастан, алар мөселман мәхәлләсе төзүдән башлап мәчет торгызуга кадәр юлны үтә.', 'Despite the difficulties, they go all the way from founding a Muslim community to building a mosque.'),
    ('Аварларны тар-мар итә, барлык байлыкларын җыеп, каганның гаскәриләрен үзенә кушып, иленә кайта.', "He crushes the Avars, gathers all their riches, takes the khagan's warriors into his own army and returns home."),
    ('Президент белән очрашуда, офыкта киләчәге күренгән башка күргәзмәләр хакында да сүз кузгатылган.', 'At the meeting with the President, other exhibitions whose future can be seen on the horizon were also discussed.'),
    ('Ак мәчетне караганнан соң Татарстанның дин вәкилләренә дәүләт бүләкләре тапшыру тантанасы булды.', "After visiting the White Mosque, there was a ceremony presenting state awards to Tatarstan's religious figures."),
]),
('c1-tale', [
    ('Инде мин дә сезнең арттан, әтидән рөхсәт сорап, әнине эзләргә дип чыктым.', "Now I too have asked Father's permission and set out after you to look for Mother."),
    ('Карт тамагын туйдыра да, ком сахрасын үтеп, бер биек кенә тауга күтәрелә.', 'The old man eats his fill, crosses the sandy desert and climbs a high mountain.'),
    ('Әби, туфлине алып, патша кызы янына китә, күрсәтеп кайтырга бара инде бу.', "The old woman takes the slipper and goes to the king's daughter to show it to her."),
    ('Минем иремә бер уй төште, ни өчен кайгыра икән, син аннан сорап кара әле.', 'My husband has something on his mind — why is he grieving? Go and ask him.'),
]),
('c1-soc', [
    ('Республикабызда ул һәр ел саен бөек татар шагыйре Габдулла Тукайның туган көнендә билгеләп үтелә.', 'In our republic it is celebrated every year on the birthday of the great Tatar poet Gabdulla Tukay.'),
    ('Нәкъ менә шушы аңлашу күп кенә мөһим бурычларның тиз арада һәм сыйфатлы үтәлешенә мөмкинлек бирә.', 'It is precisely this understanding that allows many important tasks to be carried out quickly and well.'),
    ('Билгеле булганча, Камил хәзрәт Сәмигуллиннан башка, мөфти вазыйфасына тагын ике кеше дәгъва итте.', 'As is known, besides Kamil hazrat Samigullin, two more people sought the post of mufti.'),
    ('Көчле икътисад, хокукый дәүләт, теләктәш җәмгыять - безнең республиканың уңыш формуласы менә шул.', "A strong economy, the rule of law and a society of mutual support — that is our republic's formula for success."),
]),
('c1-tale', [
    ('Әгәр дә анаңны табып кайта алсаң, минем сараема кереп кунак булмый китмә.', "If you manage to find your mother and come back, don't leave without being a guest in my palace."),
    ('Ук килеп тию белән, теге батыр сикереп торды да укны кулына тотып йөгерде.', 'As soon as the arrow struck him, the hero leapt up and ran off with the arrow in his hand.'),
    ('Дөрес тә инде, мең хайванны ач калдырганчы, берүзем ачтан үлсәм, берни юк.', "It's true enough: better that I alone starve to death than leave a thousand animals hungry."),
    ('Көтүдән бер сыерны тоталар да сөтен савып, шул сөт белән ипиләрен ашыйлар.', 'They catch a cow from the herd, milk it, and eat their bread with that milk.'),
]),
('c1-soc', [
    ('Башка милләт вәкилләре аларны бик яратты һәм татарларның ашлары, гореф-гадәтләре белән кызыксынды.', 'People of other nationalities loved them dearly and took an interest in Tatar food and customs.'),
    ('Күпчелек фильмнар - Россия, Иран, Төркия, Франция, Һиндстан, Бөекбритания, Германия һәм Италиядән.', 'Most of the films are from Russia, Iran, Turkey, France, India, Britain, Germany and Italy.'),
    ('Кадерле татарстанлылар, сезгә тыныч күк астында бәхетле һәм мул тормыш, иҗади хезмәт шатлыгы телим.', 'Dear people of Tatarstan, I wish you a happy and prosperous life under a peaceful sky and the joy of creative work.'),
    ('Ресторан хуҗасы әйтүенчә, ул затлы ризыкны ашау өчен кешеләр әллә нинди ерак илләрдән киләләр икән.', "According to the restaurant's owner, people come from all sorts of distant countries to eat that fine dish."),
]),
('c1-tale', [
    ('Егет аптырап тормый, аюны уртага, ике бүрене ике якка җигә дә кайтып китә.', 'Without hesitating, the young man harnesses the bear in the middle and the two wolves on either side and drives home.'),
    ('Мин инде, бер кергәч, бу ак өйдән чыкмас булдым вә шунда куна да башладым.', 'Once I had gone into that white house, I never wanted to leave, and I even began spending the nights there.'),
    ('Алтын балык суда йөзеп йөри башлагач, бөтен бүлмә яп-якты булып тора икән.', 'When the golden fish began swimming in the water, the whole room became bright.'),
    ('Һич дөньяга чыкмыйча, бер шәп бакчада ята икән ул кыз иптәш кызлары белән.', 'That girl lives in a fine garden with her girlfriends, never going out into the world.'),
]),
('c1-soc', [
    ('Без барыбыз да татар милләте кешеләре һәм без милләтнең киләчәге үзебездән генә торуын аңларга тиеш.', "We are all people of the Tatar nation, and we must understand that the nation's future depends on us alone."),
    ('Бөек Болгар иле Азов буе, Донның түбәнге агымындагы һәм Таман ярымутравындагы җирләрне биләп торган.', 'Great Bulgaria occupied lands along the Sea of Azov, the lower Don and the Taman Peninsula.'),
    ('Минемчә, Министрлар Кабинетында мәгълүмат чаралары теленең сыйфаты өчен җаваплы кешеләр булырга тиеш.', 'In my view, there should be people in the Cabinet of Ministers responsible for the quality of the language used in the media.'),
    ('Бишенче чакырылыш Татарстан Республикасы Дәүләт Советы депутатларын сайлау яңа сәяси шартларда узачак.', 'The elections of deputies to the fifth convocation of the State Council of the Republic of Tatarstan will take place under new political conditions.'),
]),
('c1-tale', [
    ('Ярый, урманга барып керә бу, йөри торгач, барып чыга бу бер зур аланлыкка.', 'All right, he goes into the forest, and after wandering for a while he comes out into a large clearing.'),
    ('Күңелендә үги анасына бер усал уе юк, тик аңар миһербанлык кына тели икән.', 'In his heart he has no wicked thought towards his stepmother; he wishes her only kindness.'),
    ('Икенче көнне иртә белән аучы егет үзенең бер иптәшен алып патша янына килә.', 'The next morning the young hunter takes one of his comrades and comes to the king.'),
    ('Син андый карак кеше икәнсең, моннан ары бер шәһәргә бар, анда бер бай бар.', "So you're that kind of thief: go on to a town beyond here; there's a rich man there."),
]),
('c1-tale', [
    ('Бер елдан бу атны ярты хакына саттым да, аның урынына яңадан көрән ат алдым.', 'A year later I sold this horse for half its price and bought another bay horse in its place.'),
    ('Дию күлнең суын эчеп бетерергә тотынды да, ат тоягы эзләрендә генә калды су.', "The div set about drinking up the lake, until water remained only in the horse's hoofprints."),
    ('Кыз инә булып, егетне җеп итеп саплап, сарай түбәсеннән чыгып китәләр болар.', 'The girl turned into a needle, threaded the young man as the thread, and they slipped out through the palace roof.'),
    ('Йокыдан уянгач, алманы яңадан санап карады, элек икәү юк иде, хәзер өчәү юк.', 'When he woke up he counted the apples again: before, two were missing; now three were gone.'),
]),
('c1-tale', [
    ('Егет шуннан җәяүләп шәһәргә кереп китте дә бер картның артыннан барып җитте.', 'From there the young man walked into the city on foot and caught up with an old man.'),
    ('Күп тә үтмәгән, ни күзләре белән күрсеннәр, атка берәү атланган, чабып йөри.', 'Before long, what do they see: someone is riding a horse, galloping about.'),
    ('Урманымның теләсә кай җирендә туктап, атыңны ял иттереп, үзең теләсә ни аша.', 'Stop anywhere in my forest, let your horse rest, and eat whatever you like.'),
    ('Кыз шул минутта күлнең суын эчеп бетерә дә күлнең урыны коры җир булып кала.', 'At that very moment the girl drinks up the whole lake, and where the lake was only dry land remains.'),
]),
('c1-tale', [
    ('Абыйсы Ризаның күренекле табиб булуы да, әнисенең фатыйхасы да бик ярап куя.', "Both his older brother Riza being a well-known doctor and his mother's blessing come in very handy."),
    ('Сарай ачылгач, егет сарайның уртасында биш йөз пот авырлыгында бер шар күрде.', 'When the palace was opened, the young man saw in the middle of it a ball weighing five hundred poods.'),
    ('Доктор, авыр хәлдәге пациент үзен яхшы хис итә, аңына килде, сөйләшә башлады.', 'Doctor, the patient in serious condition is feeling well, has come round and has started talking.'),
    ('Мансурның дусты аны күрми, чуен зиндан җир белән бертигез итеп эшләнгән була.', "Mansur's friend can't see him: the cast-iron dungeon has been built level with the ground."),
]),
('c1-tale', [
    ('Кара елан шул баскычка бер орына, ике орына да искиткеч матур егеткә әверелә.', 'The black snake strikes that step once, twice, and turns into an amazingly handsome young man.'),
    ('Янә аз гына очып барганнар иде, тагын бер зур шәһәрнең турына килеп җиттеләр.', 'They had flown on a little further when they reached the sky above another great city.'),
    ('Бакчаларына чыгып, аннан да теге чәчәкне эзләп карый кыз, андый чәчәк булмый.', 'The girl goes out into their garden and looks for that flower there too, but there is no such flower.'),
    ('Син, Вәли, зинһар, бодайны калдыр, кирәк вакытында без дә ярдәм итәрбез,- ди.', '"Vali, please leave the wheat; when you need it, we\'ll help you too," they say.'),
]),
('c1-tale', [
    ('Сарай түбәсендә инә сыешлы бер тишек күрәм, шуннан чыгып булмасмы икән? - ди.', '"I can see a hole the size of a needle in the palace roof — couldn\'t we get out through it?" she says.'),
    ('Егет, мин сине күрәм, үзең күркәм, сүзең ямьле, һичбер каршы килгән җирең юк.', "Young man, I see you: you're handsome and your words are pleasant; there's nothing about you I object to."),
    ('Икмәкне бусагага куйган да, үзе баз эченә төшеп, мичкәдән бал агыза башлаган.', 'He put the bread on the threshold, went down into the cellar himself and began pouring honey from the barrel.'),
    ('Имеш, тирән бер баздан үзе дә таныш булмаган уен коралларын яктылыкка чыгара.', 'It seems he brings up from a deep cellar musical instruments that even he had never known.'),
]),
('c1-tale', [
    ('Чәчәк белән озак кына уйнагач, чәчәкне югалта бу, эзли-эзли һич тә таба алмый.', "After playing with the flower for a long time, he loses it, and however much he searches, he can't find it."),
    ('Минем дә туган илем бар: атам-анам, мине сагынып елый торгач, сукыр калганнар.', "I too have a homeland: my father and mother have wept so long missing me that they've gone blind."),
    ('Торырга йортлары да булмаган, су читендә шалаш корып, шунда гына торалар икән.', "They didn't even have a house to live in; they put up a hut by the water and lived there."),
    ('И дустым, яхшы гына, күңелле генә утырган чакта, әллә ни күңелсезләнеп киттең.', 'Oh my friend, just when we were sitting so pleasantly, you suddenly became so sad.'),
]),
('c1-tale', [
    ('Өебезгә бер карак килеп, акчабызны алып китте, менә шул каракны эзләп барамын.', "A thief came to our house and took our money; I'm going in search of that thief."),
    ('Кыз карчыкның башын караса, чәч бөртеге саен алтын да көмеш, кыйммәтле ташлар.', "When the girl looked at the old woman's head, every hair was gold and silver and precious stones."),
    ('Фәлән җирдә ике полк кавалерия тора, шуннан үзегез теләгән атны сайлап алыгыз.', 'There are two cavalry regiments in such-and-such a place; choose whatever horse you like from there.'),
    ('Карчык алып барып күрсәтә, аяк киемен бик яраталар, хакын да бик яхшы түлиләр.', 'The old woman takes the shoes and shows them; they love them and pay a very good price.'),
]),
('c1-tale', [
    ('Кайтып барышлый бер күл яныннан узганда күрә: күл өстендә үрдәкләр йөзеп йөри.', 'On his way home, passing a lake, he sees ducks swimming on it.'),
    ('Кырык мичкә аракыны кырык мәртәбә тотып эчте, кырык мич ипине кырык кына йотты.', 'He gulped down forty barrels of vodka in forty swigs, and swallowed forty ovenfuls of bread in just forty bites.'),
    ('Мунчаны өч көн, өч төн яктылар, миче генә түгел, стенасы да кып-кызыл ут булды.', 'They heated the bathhouse for three days and three nights until not only the stove but the walls glowed red-hot.'),
    ('Хуҗа иртән торып тышка чыкса - өеп куйган утын әрдәнәләрен төяп алып киткәннәр.', 'When the owner got up in the morning and went outside, the stacks of firewood had been loaded up and carted off.'),
]),
('c1-tale', [
    ('Хан аны күреп алмасын дип, бүре думбрага өрде, думбраны шом тавышлы итеп куйды.', "So that the khan wouldn't see him, the wolf breathed on the dombra and gave it an eerie sound."),
    ('Сарай эчендәге бер бүлмә ишеген ачып, егетне шунда кертеп харап итмәкче була бу.', 'Opening the door of a room inside the palace, he means to lure the young man in there and destroy him.'),
    ('Авылына кайтып, болар ата-аналары белән күрешәләр дә бик яхшы көн итә башлыйлар.', 'Returning to their village, they are reunited with their parents and begin to live very well.'),
    ('Баралар-баралар, бара торгач, барып җитәләр тагын да матуррак бер биек яр буена.', 'On and on they travel, and after a while they reach an even more beautiful high riverbank.'),
]),
('c1-tale', [
    ('Малайга әле унике-унөч яшь кенә, бала акылы әле башыннан чыгып та бетмәгән була.', "The boy is only twelve or thirteen; he still has a child's head on his shoulders."),
    ('Син юкка гына он салдың, минем карын ач, миңа ипи биргән булсаң, яхшы булыр иде.', "You've added flour for nothing; I'm hungry — if you'd given me bread, that would have been good."),
    ('Тегеләй итенә, болай итенә байтал, малайны бәреп төшермәкче була - төшерә алмый.', "The filly tries this way and that to throw the boy off, but she can't."),
    ('Егет, шатланып, моның өстенә менеп утырды да, егетне шул вакыт китереп җиткерде.', 'Delighted, the young man climbed onto it, and it brought him there at once.'),
]),
('c1-tale', [
    ('Патша ауга йөргәндә, ерак болында җен байталларын күргән икән, шуңа кызыга икән.', 'While out hunting, the king had seen the fairy fillies in a distant meadow and coveted them.'),
    ('Балык эләккән көнне тамаклары тук, балык эләкмәгән көнне тамаклары ач була икән.', "On days when they caught fish they were well fed; on days they didn't, they went hungry."),
    ('Ашыйсы килеп, бүлмәләрне карап йөргән чакта, бер кечкенә генә бүлмәгә туры килде.', 'Hungry, he was wandering through the rooms when he came upon a very small room.'),
    ('Данис уйлап та тормый, икенче көнне, көтүен ташлап, ярыш була торган урынга китә.', 'Without a second thought, the next day Danis leaves his herd and goes to where the contest is held.'),
]),
('c1-tale', [
    ('Күрәсез, минем ботларым озын, йөгерә башласам, киекләрне дә, атларны да узам мин.', 'You see, my legs are long; once I start running, I overtake both game and horses.'),
    ('Малай аптырап нишләргә белми торганда, моның янына каяндыр бер бабай килеп чыкты.', 'While the boy stood at a loss, not knowing what to do, an old man appeared from somewhere beside him.'),
    ('Авылның күркәм урынында йорт салып, шунда әле дә булса рәхәт гомер кичерәләр, ди.', 'They built a house in a lovely spot in the village and live a happy life there to this day, they say.'),
    ('Иң әүвәле бу бер мичкә аракыны эчеп бетерде, аннан бер мич икмәкне кабып җибәрде.', 'First of all he drank up the whole barrel of vodka, then swallowed an entire ovenful of bread.'),
]),
('c1-tale', [
    ('Зөлкарнәй алмаз кылычын ала, икенче кулына бер озын тимер тотып бара диюгә каршы.', 'Zulkarnay takes his diamond sword and, holding a long iron bar in his other hand, goes out against the div.'),
    ('Ике көн киткәннән соң һава көймәсен тикшереп карасалар, күрәләр, егет көймәдә юк.', "Two days after setting off, they checked the airship and saw that the young man wasn't in it."),
    ('Кая туры килде, шунда тиз генә киенеп ала да, бабай белән бергәләп китәләр болар.', 'He quickly dresses in whatever comes to hand, and he and the old man set off together.'),
    ('Мин сине хәзер Каф тавының башына илтеп куярмын, аннан ары барырга миңа рөхсәт юк.', "I'll now carry you to the top of Mount Qaf; I'm not allowed to go any further than that."),
]),
('c1-tale', [
    ('Кара әле, мин кызны фәлән җирдә калдырган идем, күгәрченнәр гөрләгәч, исемә төште.', 'Look here, I left the girl in such-and-such a place — I only remembered when the doves cooed.'),
    ('Мин сиңа кирәк булган очракта менә бу кылны яндырсаң, мин шунда ук килеп җитәрмен.', "Whenever you need me, burn this hair and I'll be there at once."),
    ('Патша кызы яхшы атлар җиктереп, үз янына бер-ике иптәш кызын утыртып, урамга чыга.', "The king's daughter has fine horses harnessed, seats one or two girlfriends beside her and drives out into the street."),
    ('Кайтып керсә, моңардан башта атасы да, анасы да курка, бөтенләй нишләргә белмиләр.', "When he comes home, even his father and mother are afraid of him and don't know what to do at all."),
]),
('c1-tale', [
    ('Бакчада сандугачлар сайрый, төрле чәчәкләр, алмагачлар үсеп утыра - бер сахра инде.', 'In the garden nightingales are singing, and all kinds of flowers and apple trees are growing — a paradise.'),
    ('Таз, чишенеп, беренче казанга төшим дигәндә генә, ат пошкырып җибәрә дә, сөт суына.', 'Just as the bald one undresses and is about to step into the first cauldron, the horse snorts and the milk cools.'),
    ('Егет шарны алып чыгыйм дип, барып тотынып караган иде, урыныннан да кузгата алмады.', "The young man tried to lift the ball out, but he couldn't even move it from its place."),
    ('Үзенең чатырын корып, аш хәзерләп, атын үләнгә җибәреп, әлеге Ак бүрене көтеп калды.', 'Pitching his tent, preparing food and letting his horse out to graze, he stayed to wait for the White Wolf.'),
]),
('c1-tale', [
    ('Керсә, ни күрсен, тугыз башын тугыз якка салып, бернәрсә белмичә, җәйрәп йоклап ята.', 'He went in, and what did he see: with his nine heads lying in nine directions, it lay sprawled fast asleep, unaware of anything.'),
    ('Киң балаклы ыштан кигән икән бу карчык, йөгерә торгач, бер-ике җирдә чалынып егылды.', 'The old woman was wearing wide-legged trousers, and as she ran she tripped and fell once or twice.'),
    ('Егет, бу ташларның агасы һәм гаскәрләре икәнен белгәч, күңеле нечкәреп елап җибәрде.', 'When the young man learned that these stones were his brothers and their troops, his heart softened and he burst into tears.'),
    ('Абзалары бөлеп беткән, өйләрен сатып эчеп бетергәннәр, бер мунчада гына торалар, ди.', 'Their brothers have gone bankrupt, sold their house and drunk the money, and live in nothing but a bathhouse, they say.'),
]),
('c1-tale', [
    ('Көннәрнең бер көнендә бу көтүче төш вакытында терлекләрне бер күл янына куып китерә.', 'One day, at noon, this herdsman drives the animals to a lake.'),
    ('Егет, биш алтынны алып, көннәр, атналар үткәч, шул малны ата-анасына кайтарып бирде.', 'The young man took the five gold coins, and days and weeks later returned that wealth to his parents.'),
    ('Әти белән әни дә минем капчыкның болай тиз тулуына гаҗәпләнделәр дә, шатландылар да.', 'Mum and Dad were both amazed and delighted that my sack had filled up so fast.'),
    ('Бер сәгать эчендә пароход дәрьяның икенче ягына чыгып җитә дә яр буена барып туктый.', 'Within an hour the steamer reaches the other side of the river and stops at the bank.'),
]),
('c1-tale', [
    ('Кайтып керүгә, үз патшасы белән күрешеп, бик шатланып үз йортларында тора башладылар.', 'As soon as they got home, they met their own king and, overjoyed, began living in their own house.'),
    ('Бик әйбәт кенә иттереп егетне кунак иттеләр дә кыз белән егетне бик зурлап озаттылар.', 'They entertained the young man splendidly and saw off the girl and the young man with great honour.'),
    ('Мин ни күрсәм дә чыдарга, анамның юлында корбан булырга җиттем, һәммәсенә түзәчәкмен.', 'Whatever I see, I am ready to endure it and to sacrifice myself for my mother; I will bear it all.'),
    ('Адашып йөри торгач, Нәҗип ике авыл арасындагы ярым ташландык каберлеккә килеп чыккан.', 'Wandering lost, Nazhip came out at a half-abandoned cemetery between two villages.'),
]),
('c1-tale', [
    ('Икенче сарайга кереп, бер атның койрыгын тартып җибәргән иде, ат селкенеп кенә куйды.', "Going into the second stable, he pulled a horse's tail, and the horse merely shook itself."),
    ('Кыз атасының сүзләренә ышанмый, бу безне барыбер харап итәр дип, тораташка әйләндерә.', "The girl doesn't believe her father's words; fearing he'll destroy them anyway, she turns him to stone."),
    ('Иртә белән торып, тары белән ярма арасындагы тузанны себерерсең дә эшең беткән булыр.', 'Get up in the morning, sweep the dust between the millet and the groats, and your work will be done.'),
    ('Борын-борын заманда, моннан бик күп еллар элек, җир йөзендә бик матур кешеләр яшәгән.', 'Once upon a time, many, many years ago, very beautiful people lived on the earth.'),
]),
('c1-tale', [
    ('Урманның куе агачлы бер җирендә егетне арлы-бирле агачларга сугып харап итмәкче булды.', 'In a place in the forest where the trees grew thick, it meant to destroy the young man by dashing him against the trees.'),
    ('Икенче көнне бай мунча ишеген ачып җибәрсә, шаккатып ботын чаба: болар барысы да исән!', 'The next day the rich man opened the bathhouse door and slapped his thigh in amazement: they were all alive!'),
    ('Баскычтан төшкәндә аягы таеп егылган да баз эчендәге баткакка башы белән төшеп баткан.', 'Coming down the ladder, he slipped, fell and landed head first in the mud in the cellar.'),
    ('Барып җиткәч, егет бияне агачка илтеп бәйли, үзе коры имән ботаклары хәзерләргә керешә.', 'When he gets there, the young man ties the mare to a tree and sets about gathering dry oak branches.'),
]),
('c1-tale', [
    ('Сыер көтүенә җитә, сарык көтүенә барып чыга, кәҗә көтүенә килә - берсенә дә көтү көтми.', "He comes to the cattle herd, reaches the flock of sheep, comes to the goats — but he won't herd any of them."),
    ('Үзең тирәкнең бер ягына бер баз казып, үзеңне үзең күмәрсең, тик ике күзең генә калсын.', 'Dig a pit on one side of the poplar and bury yourself in it, leaving only your two eyes showing.'),
    ('Чебен очып килә дә табактагы пычак өстеннән кире йөреп чыга һәм көтүченең авызына керә.', "The fly flies over, walks back across the knife on the dish and goes into the shepherd's mouth."),
    ('Ярый, патша шундый бер зур көймә ясатты: утта янмый, суда батмый торган көймә булды бу.', "So the king had a great boat built: a boat that wouldn't burn in fire or sink in water."),
]),
('c1-tale', [
    ('Булган хәтле патронын ала да, яхшылап корып, атасыннан калган мылтыгын алып чыгып китә.', 'He takes as many cartridges as he has, dries them well, takes the gun his father left him and sets off.'),
    ('Бара торгач кич булган, Соры бүре, килененең эзеннән исни-исни барып, тагын куып җиткән.', "As evening came on, the Grey Wolf followed his daughter-in-law's trail, sniffing, and caught up with her again."),
    ('Инде актык соравым булсын: минем тәхетемнән урам бакчасына хәтле балавыз күпере ясыйсың.', 'And let this be my last request: build a wax bridge from my throne to the garden in the street.'),
    ('Авылга барып керсәләр, каралтысыз-коймасыз өй буенда сәләмә генә киенгән бер егет утыра.', 'When they enter the village, a raggedly dressed young man is sitting by a house with no yard or fence.'),
]),
('c1-tale', [
    ('Байтак юллар киткәч, бик калын урманга җитеп, адашып йөри бу, бүреләр сырып алалар моны.', 'After a long way he reaches a very dense forest and wanders lost, and wolves surround him.'),
    ('Алай булгач, мин сиңа урманымда йөрергә, атыңны ашатырга, кошларымны атарга рөхсәт иттем.', 'In that case, I allow you to walk in my forest, to feed your horse and to shoot my birds.'),
    ('Бер дә беркөнне боларның аталары, бик күп сорый торгач, боларга да бер елга рөхсәт бирде.', "One fine day their father, after they had begged and begged, gave them a year's leave too."),
    ('Гыйфрит, егетнең сүзен тыңлап, шәһәрнең читенә илтеп ташлады да үзе шунда ук юк та булды.', "Heeding the young man's words, the ifrit dropped him at the edge of the city and vanished at once."),
]),
('c1-tale', [
    ('Көймә юлбасарларның тора торган урыннарына кайтып җитә, күрәләр, көймә буш, иптәшләре юк.', "The boat reaches the robbers' lair; they look and see the boat is empty, their comrades gone."),
    ('Киңәш итеп, капка төбендә барысын да калдырып, егет үзе генә патшаның сараена кереп китә.', "Taking counsel, they leave everything at the gate, and the young man goes into the king's palace alone."),
    ('Бер дә бер көнне, ястү намазыннан кайтканда, мулла бу кызларның тәрәзәсеннән килеп карый.', "One day, coming home from the night prayer, the mullah comes and looks in at these girls' window."),
    ('Уфа каласында авылдан килгән карт белән карчык Ленин һәйкәленә исләре китеп карап торалар.', 'In the city of Ufa an old man and an old woman from the village stand gazing in astonishment at the Lenin monument.'),
]),
('c1-tale', [
    ('Өч көн, өч төн үткәннән соң, мең мәшәкать белән, болар урманның аргы ягына барып чыктылар.', 'After three days and three nights, with a thousand hardships, they came out on the far side of the forest.'),
    ('Вәзир кушканча, атлар әзерләп, кызның йоклаган җиренә барып, сандыкка салып алып киттеләр.', 'As the vizier ordered, they prepared horses, went to where the girl was sleeping, put her in a chest and carried her off.'),
    ('Юк, ул бик ярлы кеше, ул монда килмәс, аның өс-башы да юк, сез товар биреп кенә җибәрегез.', "No, he's a very poor man; he won't come here, he has no clothes — just give him the goods and send him off."),
    ('Терлекләре су эчеп ял иткәндә, бу көтүче дә зур малае белән утыралар төшке ашларын ашарга.', 'While the animals drink and rest, the herdsman and his eldest son sit down to eat their lunch.'),
]),
('c1-tale', [
    ('Бабайның салган авы бар иде; дию, суларны актарып китереп, балыкны тутырды бабайның авына.', "The old man had cast a net; the div stirred up the waters and filled the old man's net with fish."),
    ('Кызның сөйләп-сөйләп, канлы яшь белән елаганын күргәч, чыдый алмый, бар да елаштылар шунда.', 'Seeing the girl tell her story and weep tears of blood, nobody could bear it, and they all wept together.'),
    ('Таз сөт казаннарына кереп чыккач, башындагы тазлары бетеп, шулкадәр матур егет булып чыкты.', 'When the bald lad came out of the milk cauldrons, his baldness was gone and he turned out to be a very handsome young man.'),
    ('Төн буе аңа атланып йөри, аның алдындагы җимне алып китеп, үзе сөйгән ат алдына илтеп сала.', 'All night he rides it, takes away the feed in front of it and puts it before the horse he loves.'),
]),
('c1-tale', [
    ('Яктыра башлагач, карт сискәнеп уяна да чәчәк эзләп килүе искә төшеп, коймадан бакчага төшә.', 'As it grows light, the old man wakes with a start, remembers he has come looking for the flower and climbs over the wall into the garden.'),
    ('Син танысын дип, мин синең кырыңнан узып китәрмен дә, шунда бер каурыемны калкытып куярмын.', "So that you'll recognise me, I'll pass by you and raise one of my feathers."),
    ('Чишмәнең тирә-ягы яшел үләннәр, матур чәчәкләр белән бизәлгән, агачларда кошлар сайрый икән.', 'Around the spring there were green grasses and beautiful flowers, and birds were singing in the trees.'),
    ('Ялтыраган нәрсәнең янына килеп җитсә, дөнья зурлыгында эшләнгән бер бакыр сарай булып чыкты.', 'When he came up to the shining thing, it turned out to be a copper palace the size of the world.'),
]),
('c1-tale', [
    ('Мулланың йорты янып беткән, күршеләренең бер казыкларына да, бер чыбыкларына да ут капмаган.', "The mullah's house burned to the ground, yet not a single stake or twig of the neighbours' caught fire."),
    ('Егет тә, якты чырай белән каршы алып, әзер булган ашны куеп, чатырга моны да ашарга чакырды.', 'The young man greeted him with a bright face, set out the food that was ready and invited him into the tent to eat.'),
    ('Урып сугалар да, тегермәндә тартып, әйткән вакытка биш потлы күмәчне китереп утырталар моңа.', 'They reap and thresh, grind it at the mill, and at the appointed time set a five-pood loaf before him.'),
    ('Ай киткән, ел киткән, бик озын юллар, кара урманнар, биек таулар үткән, киң диңгезләр кичкән.', 'Months passed, years passed; he crossed very long roads, dark forests and high mountains, and sailed wide seas.'),
]),
('c1-tale', [
    ('Кешеләр фонарьлар, мылтыклар тотып ферма янына килгәндә, бүреләр урман уртасында иделәр инде.', 'By the time people came up to the farm with lanterns and guns, the wolves were already in the middle of the forest.'),
    ('Кырык чакрым биектә бер кош канатын өстенә куеп йоклый икән, шуның бер каурыен урлап төшәләр.', 'Forty versts up, a bird sleeps with its wing over itself, and they steal one of its feathers.'),
    ('Гөлчәчәк бик курыккан, күмәч биреп кенә котылыр иде дә, ул вакытта инде аның күмәче калмаган.', 'Gulchachak was very frightened; she could have escaped by giving it a loaf, but by then she had no bread left.'),
    ('Иң өлкән улына ике ел, уртанчыларына бер ел булган чакта, төпчек улы мәдрәсәдән укудан кайтты.', 'When the eldest son was two and the middle ones one year old, the youngest son came home from his studies at the madrasa.'),
]),
('c1-tale', [
    ('Торса, ни күзе белән күрсен, амбарның эчендә тары белән ярма аерылып куелган энҗе кебек тезеп.', 'He gets up and what does he see: inside the barn the millet and groats have been separated and laid out like pearls.'),
    ('Йорт тотмас күп уйлап тормыйча, өстен-башын чишенеп ташлап, балтаны эзләргә суга кереп киткән.', 'Without thinking long, Yort Totmas threw off his clothes and went into the water to look for the axe.'),
    ('Берзаман патша, хатыны белән икәү, яхшы атлар, яхшы арбалар җигеп, ялан-япан сахрага чыктылар.', 'One day the king and his wife harnessed fine horses to fine carts and drove out into the open steppe.'),
    ('Диюнең ачуы килеп сикереп торып, егетне тотып җиргә күтәреп бәргән иде, бил кадәр җиргә батты.', 'The div leapt up in rage, seized the young man and hurled him at the ground, and he sank in up to his waist.'),
]),
('c1-tale', [
    ('Бабай тиз генә ашап-эчә дә ишегалдына чыгып, кирәк-яракларын хәзерләп, яңадан егет янына керә.', 'The old man quickly eats and drinks, goes out into the yard, gets his things ready and comes back in to the young man.'),
    ('Кече ул агалары кебек казан янында булып, бүрене күргәч, казанының яртысын бүрегә салып бирде.', 'The youngest son, staying by the cauldron like his brothers, gave half the cauldron to the wolf when he saw it.'),
    ('Андый-мондый хәлләр булса, берәр куркынычлык килсә, мине ничек кенә булса да уятырга тырышыгыз.', 'If anything happens, if any danger comes, try by any means to wake me.'),
    ('Азмы-күпме ятканнан соң, бер көтү елкы килеп, бүре әйткәнчә су эчеп үлән ашарга менеп киттеләр.', 'After lying there a while, a herd of horses came, drank as the wolf had said, and went up to graze.'),
]),
('c1-tale', [
    ('Алардан ерак түгел берничә бүренең еш-еш сулаганы, ара-тирә чыбык-чабык сынган тавышлар яңгырый.', 'Not far from them comes the quick panting of several wolves and now and then the sound of snapping twigs.'),
    ('Көймәләре утта янмаслык итеп эшләнгән бит инде боларның, шуңа ышанып, болар һаман алга бардылар.', "Their boats had been made so that they wouldn't burn, so, trusting in that, they kept going forward."),
    ('Инде егет кошны алып, кызны алып, думбраны алып, җиде аргамакны җитәкләп алып, өенә кайтып китте.', 'Then the young man took the bird, the girl and the dombra, led away the seven steeds and went home.'),
    ('Бара торган юллары да ерак була, Вәлинең бер җомгалык азыгын ике кеше өч көндә ашап та бетерәләр.', "The road they travel is long, and two people eat up Vali's food for a week in three days."),
]),
('c1-tale', [
    ('Дүрт ай тулып, бишенче айның беренче көнендә сарай янындагы бик матур бер бакча янына килеп чыга.', 'When four months had passed, on the first day of the fifth month, he comes to a very beautiful garden beside a palace.'),
    ('Пәри егетләре, бер орлыгын да әрәм итмичә, бер саламын да югалтмыйча, таң атканчы, сугып куйдылар.', 'Without wasting a single grain or losing a single straw, the fairy lads threshed it all before dawn.'),
    ('Атлар алтын иярләр белән иярләнгән була, иярләргә алтын кылычлар бәйләп, сугышка хәзерләнгән була.', 'The horses are saddled with golden saddles, golden swords are tied to the saddles, and all is ready for battle.'),
    ('Егет алай сугылды, болай сугылды, бер казанны ачып бераз ашап та карады - кая ул итне ашап бетерү.', 'The young man tried this way and that, opened one cauldron and tasted a little — but there was no way he could finish all that meat.'),
]),
('c1-tale', [
    ('Кичен өйләренә кайткач, атасыннан биш сум акча сорап ала да, малай авылга кызыл әтәч эзләргә чыга.', 'When he gets home in the evening, the boy asks his father for five roubles and goes out into the village to look for a red rooster.'),
    ('Әүвәл заманда бер фәкыйрь урманнан утын күтәреп алып кайтып сата икән дә шуның белән көн итә икән.', "Long ago a poor man used to carry firewood home from the forest and sell it, and that's how he lived."),
    ('Һавага зур-зур ташларны чөеп җибәрә дә, шул ташлар, һавадан аның тезенә төшеп, тузан булып китәләр.', 'He hurls huge stones into the air, and the stones fall from the sky onto his knee and turn to dust.'),
    ('Мин сезнең кебекләрне күп күргән, кызларга тимәгез! - ди дә шул минутта ук ике юлбасарны һәлак итә.', '"I\'ve seen plenty like you — leave the girls alone!" he says, and at that very moment he kills two robbers.'),
]),
('c1-tale', [
    ('Бер озын имәнне бөтен буе белән бер җилкәсенә күтәргән, икенче кулына зур бер тегермән ташын алган.', 'He had lifted a tall oak, whole, onto one shoulder, and in his other hand he held a huge millstone.'),
    ('Ат җигеп китүчеләр күзләрен ачып карасалар, атларын арбага салганнар, үзләре арбаны тартып кайталар.', 'When the carters opened their eyes and looked, their horses were lying in the cart and they themselves were pulling it home.'),
    ('Бер төркем халык җен дип аннан качарга, икенче төркем халык аны тотар өчен артыннан куарга тотынган.', 'One group of people, thinking it a demon, began to run from it; another group chased after it to catch it.'),
    ('Иртә белән Вәли йоклап туйгач, ни күрсен, күз дә ачып булмый: кояш кебек ялтырап тора балавыз күпере.', 'In the morning, when Vali had slept his fill, what did he see? He could hardly open his eyes: the wax bridge was shining like the sun.'),
]),
]
NAMES = {"c1-tale": ("Folk Tales", "Әкиятләр"), "c1-soc": ("Society and History", "Җәмгыять һәм тарих"), "c1-lit": ("Literature and Ideas", "Әдәбият"),
 "c1-prov": ("Sayings", "Мәкальләр"), "c1-life": ("Reflections", "Уйланулар"), "c1-folk": ("Customs and Beliefs", "Йолалар")}
assert len(S) == 100, len(S)
cnt = {}
for i, (top, items) in enumerate(S, 1):
    cnt[top] = cnt.get(top, 0) + 1
    en, tt = NAMES[top]
    L(i, f"{en} {cnt[top]}", f"{tt} {cnt[top]}", items, top)
c.save()
