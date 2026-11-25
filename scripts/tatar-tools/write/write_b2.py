# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("b2", "b2")
T = c.T
T("b2-prov", "Proverbs and Sayings", "Мәкальләр: …са, …ыр · …ганчы, … · Х — У",
  "Tatar proverbs (мәкальләр) are short, balanced and full of grammar you already know. Two halves often mirror each other: Яхшы сүз җанга рәхәт, яман сүз җанга җәрәхәт — a kind word soothes the soul, a harsh word wounds it. "
  "Conditions use -са with the -ыр future (Көрәшсәң көчлегә чык…), comparisons use -ганчы (rather than): Чит илдә солтан булганчы, үз илеңдә олтан бул. A dash often stands for is: Кара алтын — җир мае.",
  "Many proverbs also work as weather lore: Имәндә чикләвек күп булса, кыш каты килә — lots of acorns means a hard winter.",
  [("A", "Нигә син шулкадәр ашыгасың?", "Why are you in such a hurry?"), ("B", "Эшне бүген бетерәсем килә.", "I want to finish the job today."), ("A", "Ашыккан ашка пешкән, диләр бит.", "Haste scalds itself on the soup, as they say."), ("B", "Ярый, ярый, акрынрак эшлим.", "All right, all right, I'll work more slowly.")])
T("b2-life", "Reflections on Life", "…у · кирәк · …са да · …ган саен",
  "General statements about life lean on verb nouns in -у/-ү as subjects (Ялгышны тану гына аз — admitting a mistake alone isn't enough), on кирәк (one must) and on -ган саен (the more…, the more…): Тау биегрәк булган саен, егылу куркынычы да арта. "
  "Concession is -са да (even if): Кыстасалар да — even if they press you. The generic you is just the second person singular: Үзең сөйли башлаганчы, кеше сүзен тыңлап бетер.",
  "Tatar writers love the pattern Х — ул У дигән сүз (X means Y): Телне югалту ул — гореф-гадәтне югалту дигән сүз.",
  [("A", "Тормышта иң мөһиме нәрсә дип уйлыйсың?", "What do you think matters most in life?"), ("B", "Минемчә, сүзеңдә тору.", "In my view, keeping your word."), ("A", "Ә акча?", "And money?"), ("B", "Акча ул була да бетә торган әйбер.", "Money comes and goes.")])
T("b2-story", "Telling Stories and Tales", "…а икән · …ган, ди · борын-борын заманда · күз ачып йомганчы",
  "Stories often switch to the present tense to make events vivid: Егет авылга килеп керә дә бер кызга очрый — the young man enters the village and meets a girl. "
  "Fairy tales use the -ган past with ди (they say) or икән (it turns out): Яшәгән, ди, булган, ди, бер патша — once there lived, they say, a king. Икән marks a discovery: Капка сакчысы моның үз әтисе икән — the gatekeeper turned out to be his own father.",
  "Tatar tales open with Борын-борын заманда (once upon a time) and often end Әкият шуның белән бетте (and that's the end of the tale).",
  [("A", "Әби, әкият сөйлә әле!", "Grandma, tell me a fairy tale!"), ("B", "Борын-борын заманда бер патша яшәгән, ди.", "Once upon a time there lived a king, they say."), ("A", "Аның кызы булганмы?", "Did he have a daughter?"), ("B", "Булган, ди, бик гүзәл кызы булган.", "He did, they say — a very beautiful daughter.")])
T("b2-opinion", "Views and Arguments", "минемчә · миңа калса · …дыр · …дип уйлыйм · әлбәттә",
  "To give an opinion, start with Минемчә (in my view) or Миңа калса (if you ask me), or close the clause with дип уйлыйм / дип саныйм (I think / I consider). "
  "Soften a claim with -дыр/-дер (probably) or бугай, and strengthen it with әлбәттә (of course) or һичшиксез (without a doubt). To challenge politely: Сезгә … кебек тоелмыймы? — Doesn't it seem to you that…?",
  "In discussions Tatar speakers often begin a counterpoint with Әмма (however) or Икенче яктан (on the other hand).",
  [("A", "Миңа калса, бу проект бик кыйммәт.", "If you ask me, this project is very expensive."), ("B", "Икенче яктан, ул бик файдалы да.", "On the other hand, it's very useful too."), ("A", "Бәлки, син хаклыдыр.", "Maybe you're right.")])
T("b2-cult", "Literature and Culture", "әсәр · иҗат · шигырь · тәрҗемә ителде · …га хас",
  "Writing about books and art uses a recognisable vocabulary: әсәр (work), иҗат (creative output), шигърият (poetry), геройлар (characters), сурәтли (depicts), ачып бирә (reveals). "
  "Passives are frequent: тәрҗемә ителде (was translated), кулланыла (is used). The ending -га хас means typical of: шул чорга хас сүзләр — words typical of that period.",
  "Gabdulla Tukay (1886–1913) is the national poet; his poem И туган тел (O native tongue) is sung at nearly every Tatar gathering.",
  [("A", "Син Тукай шигырьләрен укыдыңмы?", "Have you read Tukay's poems?"), ("B", "Әйе, аеруча И туган тел шигырен яратам.", "Yes, I especially love the poem O Native Tongue."), ("A", "Ул күп телләргә тәрҗемә ителгән.", "It has been translated into many languages.")])
T("b2-soc", "News and Society", "… әйтүенчә · … кысаларында · … буенча · … тарафыннан · көтелә",
  "News Tatar has fixed formulas. Sources: Х әйтүенчә (according to X). Frames: визит кысаларында (as part of a visit). Topics: эш буенча (concerning work). Agents of passives: халык тарафыннан (by the people). Expectations: килүе көтелә (is expected to arrive). "
  "Long noun phrases built from verb nouns are typical: абитуриентлар туплау кыенлашуы — the increasing difficulty of attracting applicants.",
  "Tatarstan's media publish in both Tatar and Russian; the Tatar press uses many Arabic- and Persian-origin words that everyday speech replaces with simpler ones.",
  [("A", "Бүген яңалыкларда нәрсә сөйләделәр?", "What did they say on the news today?"), ("B", "Казанга Австрия Президенты килүе көтелә, диделәр.", "They said the President of Austria is expected in Kazan."), ("A", "Рәсми визит кысаларындамы?", "As part of an official visit?"), ("B", "Әйе, шулай.", "Yes, that's right.")])
L = c.L
S = [
('b2-life', [
    ('Ике сигез уналты икәнне кем дә белә.', 'Everyone knows that two eights are sixteen.'),
    ('Яшәү төрле булган кебек үлем дә төрле.', 'Just as lives differ, so do deaths.'),
    ('Акча бит ул була да бетә торган әйбер.', 'Money is something that comes and goes.'),
    ('Ни кызганыч, бушка үткән гомерләр дә була.', 'Sadly, some lives are lived in vain.'),
]),
('b2-prov', [
    ('Ана бала өчен төн йокысын өч бүлә.', "A mother breaks her night's sleep three times for her child."),
    ('Бер яхшы эш мең яхшы сүздән артык.', 'One good deed is worth more than a thousand good words.'),
    ('Булса да алтын, һаман да читлек ул.', "Even if it's made of gold, a cage is still a cage."),
    ('Кыңгыр эш кырык елдан соң да беленер.', 'A crooked deed will come to light even after forty years.'),
]),
('b2-cult', [
    ('Аерыласы гына килми бит бу шәп китаптан.', "I just don't want to put this great book down."),
    ('Аеруча ул аның әхлакый ягына киң туктала.', 'He dwells at length on its moral side in particular.'),
    ('Төп герой ролендә үзеңне ничек хис иттең?', 'How did you feel in the lead role?'),
    ('Авыр язмыш моңлы көй булып кына языла ала.', 'A hard fate can only be written as a mournful tune.'),
]),
('b2-story', [
    ('Алайса, сез я бик чибәр, я чын юләр.', "Then you're either very handsome or a real fool."),
    ('Карап торды, болыт һаман төшә дә төшә.', 'He kept watching: the cloud kept coming lower and lower.'),
    ('Алан уртасында зур гына бер төп күренә.', 'A large stump can be seen in the middle of the clearing.'),
    ('Бик кечкенә генә эт ләң-ләң өргән була.', 'A tiny little dog was yapping away.'),
]),
('b2-soc', [
    ('Әлбәттә, һәр халык үз илендә үз телендә сөйләшсен.', 'Of course, let every people speak its own language in its own land.'),
    ('Барлык абитуриентларга да татар телен белү мәҗбүри.', 'Knowledge of Tatar is compulsory for all applicants.'),
    ('Алабугада бер һәм ике бүлмәле фатирларга сорау күп.', "In Yelabuga there's high demand for one- and two-room flats."),
    ('Авыллар зураеп, кешеләрнең бер өлеше бүленеп чыккан.', 'As the villages grew, some of the people split off.'),
]),
('b2-opinion', [
    ('Зинһар, тор да кит, моны үзең өчен эшлә.', 'I beg you, get up and leave, do it for yourself.'),
    ('Алман телендә дүрт килеш, ә идиш телендә — өч.', 'German has four cases and Yiddish has three.'),
    ('Аның Аннага карата дуслык хисләре генә бар иде.', 'He felt nothing more than friendship for Anna.'),
    ('Менә мин сезгә бер тест тапшырырга тәкъдим итәм.', "Here's a test I want you to take."),
]),
('b2-life', [
    ('Сүзендә торган кеше генә ышаныч яулый ала.', 'Only someone who keeps their word can win trust.'),
    ('Булганы җитеп ашса да канәгать була белми.', "Even when he has more than enough, he can't be content."),
    ('Сез бик күп буш сүз сөйлисез, ә эшегез аз.', 'You guys prattle a lot and do little.'),
    ('Элеккеге ирем белән без әле дә яхшы дуслар.', 'My ex-husband and I are still good friends.'),
]),
('b2-prov', [
    ('Ахмак кеше ярдәм итәм дип ярдан этәр.', 'A fool trying to help will push you off the cliff.'),
    ('Акыллы сүзгә кул куй, акылсызга юл куй.', 'Put your name to wise words, and show foolish ones the door.'),
    ('Яхшыга да бер кояш, яманга да бер кояш.', 'The same sun shines on the good and the bad.'),
    ('Яман чир тиз йога, яман гадәт тиз керә.', 'A bad illness is quickly caught, and a bad habit quickly takes hold.'),
]),
('b2-cult', [
    ('Азат бала чактан ук җырлап, гармунда уйнап үсә.', 'From childhood Azat grows up singing and playing the accordion.'),
    ('Сугыш алдыннан авыл тормышы көйләнгән була инде.', 'Before the war, village life had already settled into a steady rhythm.'),
    ('Сугыш һәм солых - төзелеше ягыннан да кызыклы әсәр.', 'War and Peace is also an interesting work in terms of its structure.'),
    ('Авыр темаларны да җиңел һәм аңлаешлы итеп ачып бирә.', 'He presents even difficult topics in an easy, clear way.'),
]),
('b2-story', [
    ('Их, әни, нигә соң син бер дә йөгермисең?', "Oh Mum, why don't you ever run?"),
    ('Сиңа ошасын дип кенә киенә алмыйм ич мин!', "I can't dress just to please you!"),
    ('Аждаһа шул агулы җәрәхәтеннән үзе дә үлгән.', 'The dragon itself died of that poisoned wound.'),
    ('Минемчә, бу велосипед бик үк яңа түгел инде.', "I think this bike isn't exactly new any more."),
]),
('b2-soc', [
    ('Татар телен белгәннәрнең монда гел кирәге чыгып тора.', 'People who know Tatar are always needed here.'),
    ('Реконструкция вакыты күпмегә сузыласы әле билгеле түгел.', 'It is not yet known how long the reconstruction will take.'),
    ('Алабуга да соңгы елларда шактый үзгәрде, шәһәрлеге артты.', 'Yelabuga has also changed a lot in recent years and become more of a city.'),
    ('Бина видеокүзәтү һәм контроль системасы белән җиһазланган.', 'The building is equipped with a video surveillance and access-control system.'),
]),
('b2-opinion', [
    ('Почтага бармас өчен мин яхшы запас маркалар тотам.', 'I keep a good supply of stamps to save trips to the post office.'),
    ('Без бүген дә шул ук нәрсәне кабат эшләргә телибез.', 'We want to do the same thing again today.'),
    ('Җирнең тыңларга әзер кешеләр өчен үз музыкасы бар.', 'The earth has its music for those who will listen.'),
    ('Өч ел элек мин французча чак кына сөйләшә ала идем.', 'I could barely speak French three years ago.'),
]),
('b2-life', [
    ('Сезгә шунда ук әйтергә тиешле бер нәрсә бар.', "There's something I have to let you know right away."),
    ('Адәм баласына тереклек итәр өчен нәрсә кирәк?', 'What does a human being need in order to live?'),
    ('Ялгышны тану гына аз, аны төзәтергә дә кирәк.', "Admitting a mistake isn't enough; you also have to correct it."),
    ('Эшне бер башлап җибәрү генә, аннары үзе китә.', 'You just have to get started; after that the work goes by itself.'),
]),
('b2-prov', [
    ('Ялган уты ел янар, ел янса да җылытмас.', "The fire of a lie may burn for a year, but even then it won't warm you."),
    ('Туган җирдән газиз берни дә юк дөньяда.', 'Nothing in the world is dearer than your native land.'),
    ('Үзең кыек утырсаң да, сүзең туры булсын.', 'Even if you sit crooked, let your words be straight.'),
    ('Март башында тамчы тамса, җәй яхшы килә.', 'If it drips in early March, the summer will be good.'),
]),
('b2-cult', [
    ('Казанда нибары бер татар мәктәбе калган иде ул елларда.', 'In those years only one Tatar school was left in Kazan.'),
    ('Кем генә тирән ихтирам белән телгә алмый икән бу исемне.', "Who doesn't mention this name with deep respect?"),
    ('Авторның иҗатына хас тагын бер үзенчәлекне күрсәтәсе килә.', "I'd like to point out one more feature typical of the author's work."),
    ('Кайберләре, әйтик, кыпчак биләре, хәтта хан дип тә аталган.', 'Some of them, the Kipchak beys for example, were even called khans.'),
]),
('b2-story', [
    ('Тимер юлдан бик зур тизлек белән поезд бара.', 'A train is speeding along the railway.'),
    ('Күз тимәсен, бигрәкләр дә иреңә охшаган икән!', 'Touch wood — he looks so much like your husband!'),
    ('Миләш диеп капкан идем, балан булып чыкты бу.', 'I bit into it thinking it was rowan, but it turned out to be viburnum.'),
    ('Васыять итеп әйтәм - бу бина җимерелергә тиеш.', 'I say this as my last will: this building must be torn down.'),
]),
('b2-soc', [
    ('Элек студентлар экзаменны өчкә, дүрткә яки бишкә бирә иде.', 'Students used to pass their exams with a three, a four or a five.'),
    ('Агымдагы елда бу тармак хезмәткәрләренең эш хакы күтәрелде.', 'This year wages for workers in this sector were raised.'),
    ('Республика халкы тарафыннан да уңай караш булыр, дип уйлыйбыз.', 'We think the people of the republic will view it positively too.'),
    ('Кыскасы, милли үзаң булдыруның һәм үстерүнең төрләре гаять күп.', 'In short, there are very many ways of creating and developing national identity.'),
]),
('b2-opinion', [
    ('Хәл шул дәрәҗәгә җитте ки, без я батабыз, я йөзәбез.', 'The situation has come to the point where we either sink or swim.'),
    ('Марк үзенең кар бабасын эшләпә һәм шарф белән бизәде.', 'Mark dressed his snowman up in a hat and scarf.'),
    ('Тиздән ванна шулкадәр суыныр ки, ул ваннага керә алыр.', 'Soon the bath was cool enough for him to get into.'),
    ('Мин чыннан да бу вакыйганы күрми калырга теләмәс идем.', "I truly wouldn't want to miss this event."),
]),
('b2-life', [
    ('Тыела белмәсәң упкынга тәгәрәве дә озак түгел.', "If you can't hold yourself back, it won't be long before you roll into the abyss."),
    ('Бу бары тик мем гына, җентекләп тикшерү түгел.', "That's just a meme, not a rigorous study."),
    ('Кил монда, балам, миңа сиңа карарга рөхсәт ит.', 'Come here, child, and let me have a look at you.'),
    ('Нәрсә дә булса кирәк булса, миңа хәбәр итегез.', 'Let me know if you need anything.'),
]),
('b2-prov', [
    ('Кеше булган кешенең һәр нәрсәдә эше бар.', 'A real person cares about everything.'),
    ('Түбәң күктә булса да, аягың җирдә булыр.', 'Even if your head touches the sky, keep your feet on the ground.'),
    ('Имәндә чикләвек күп булса, кыш каты килә.', 'If the oaks bear lots of acorns, the winter will be harsh.'),
    ('Кояш баегач, әтәч кычкырса, көн аяз була.', 'If the rooster crows after sunset, the next day will be clear.'),
]),
('b2-cult', [
    ('Алай да моңа кадәр үк Болгарда исламның киң җәелүе билгеле.', 'Even so, it is known that Islam had spread widely in Bolgar before this.'),
    ('Актерлык осталыгы серләренә төшендерүдә Рөстәм үзе катнашачак.', "Rustem himself will take part in teaching the secrets of the actor's craft."),
    ('Миңа калса, гомум әдәбиятта иң мөһим тармак - балалар әдәбияты.', "In my view, the most important branch of literature is children's literature."),
    ('Автор һәм геройлар сөйләмендә шул чорга хас сүзләр еш кулланыла.', 'Words typical of that period are often used in the speech of the author and the characters.'),
]),
('b2-story', [
    ('Кадерлем, безнең өйләнешкәнгә иртәгә ун ел тула.', 'My dear, tomorrow it will be ten years since we got married.'),
    ('Әтисе кызына бу юлы да ярдәм итәргә мәҗбүр булды.', 'Once again her father had to help his daughter.'),
    ('Кояш белән бергә торып, мәктәпкә йөгерәсең дә юк.', "You get up with the sun, and you don't even have to run to school."),
    ('Акча ясаган кешене элек Себергә җибәрәләр иде бит.', 'People who forged money used to be sent to Siberia, you know.'),
]),
('b2-soc', [
    ('Барыбер монда кайткач, үз белгечлекләре буенча эш таба алмыйлар.', "Anyway, when they come back here, they can't find work in their own field."),
    ('Авыл юл һәм газ белән тәэмин ителмичә, үсәчәк дип әйтергә ярамый.', "You can't say a village will grow without being supplied with roads and gas."),
    ('Тик күптән түгел генә архивта кызыклы гына материалларга юлыктык.', 'Only recently did we come across some quite interesting material in the archive.'),
    ('Актерның туганнарының һәм якыннарының тирән кайгысын уртаклашабыз.', "We share the deep grief of the actor's relatives and loved ones."),
]),
('b2-opinion', [
    ('Сез тормыш буйлап тыныч нәфислек белән хәрәкәт итәсез.', 'You move through life with quiet grace.'),
    ('Татар халкының язмышын татарлар үзләре хәл итәргә тиеш.', 'The fate of the Tatar people must be decided by the Tatars themselves.'),
    ('Безгә якын арада нәрсә эшләячәгебезне хәл итәргә кирәк.', "We need to decide what we're going to do soon."),
    ('Минемчә, сиңа Бостонда тагын берничә көн калырга кирәк.', 'I think you should stay in Boston for a few more days.'),
]),
('b2-life', [
    ('Шар ныграк кабарган саен шартлау ихтималы арта.', 'The more a balloon inflates, the more likely it is to burst.'),
    ('Минем аның белән төшке аш ашарга планнарым бар.', 'I have lunch plans with her.'),
    ('Без сиңа моны эшләргә рөхсәт итмәскә тиеш идек.', "We shouldn't have allowed you to do that."),
    ('Сине яратмаганга гына ул кешене дошманга санама.', "Don't consider someone an enemy just because they don't like you."),
]),
('b2-prov', [
    ('Егет булса мут булсын, ике күзе ут булсын.', "If he's a young man, let him be lively, with fire in both eyes."),
    ('Кара алтын — җир мае, аның белән ил байый.', 'Black gold is the oil of the earth; it makes the country rich.'),
    ('Акылсыз башта алтын бүрек тә файда бирмәс.', 'On a foolish head even a golden hat is no use.'),
    ('Эт кебек түзем, ат кебек эшчән булсаң иде.', 'If only you were as patient as a dog and as hard-working as a horse.'),
]),
('b2-cult', [
    ('Җанибәк Кавказдан Сарайга авырып кайта да тиз арада үлеп тә китә.', 'Janibek comes back ill from the Caucasus to Sarai and soon dies.'),
    ('Алай гына да түгел, ул бу җиргә мәхәббәт орлыгы чәчеп калдырачак.', 'Not only that — he will leave seeds of love sown in this land.'),
    ('Сәлимҗан әсәрләре укучыга дөньядагы матурлыкны күрергә ярдәм итә.', "Salimjan's works help the reader see the beauty in the world."),
    ('Авыз ачканнан соң телевизор карау - үзенә күрә бер традиция икән.', 'Watching TV after breaking the fast turns out to be a tradition of its own.'),
]),
('b2-story', [
    ('Вакыты җиткәч, җае табылыр, бабай, бер дә кайгырма.', "When the time comes, a way will be found, grandad — don't worry at all."),
    ('Авызымнан берәр сүз чыгар дип курыккандыр, күрәсең.', "He must have been afraid I'd let something slip."),
    ('Мәсәлән, кофе эчкәч, артыннан чынаягын да ашап куя.', 'For example, after drinking his coffee he eats the cup as well.'),
    ('Шуларны укып танышканнан соң, егет патша янына бара.', 'After reading them through, the young man goes to the king.'),
]),
('b2-soc', [
    ('Телевидение тәнкыйтьчеләре үзләренең күп кенә киңәшләрен дә бирде.', 'The television critics also gave a lot of their own advice.'),
    ('Укытучы Гөлинә Йосыпова мәктәптә кул эшләре түгәрәген алып барган.', 'The teacher Gulina Yusupova ran a handicrafts club at the school.'),
    ('Августта метеорит яңгырын дөньяның төрле почмагыннан күреп булачак.', 'In August the meteor shower will be visible from various corners of the world.'),
    ('Үзгәртеп кору елларында аларның байлыгы таланды, бер кулга тупланды.', 'During the perestroika years their wealth was plundered and concentrated in one pair of hands.'),
]),
('b2-opinion', [
    ('Әгәр мин ир-ат булсам, дин әһеле булыр идем дип уйлыйм.', "If I were a man, I think I'd be a priest."),
    ('Король яңа биналар төзү турында яңа указ чыгарырга тиеш.', 'The king must issue a new decree on the construction of new buildings.'),
    ('Ул вакытта минем үзем белән нибары утыз доллар гына иде.', 'I only had thirty dollars with me at that time.'),
    ('Ул бик игътибар белән тыңлый, ләкин бернәрсә дә аңламый.', 'He listens very attentively, but he doesn’t understand anything.'),
]),
('b2-life', [
    ('Дөнья төрледән төрле – чуар булуы белән күңелле.', "The world is full of variety — it's fun because it's so colourful."),
    ('Мин инде ничә еллар буе шул матур ир-атка гашыйк.', "I've had a big crush on that beautiful man for years now."),
    ('Давид гомере буе шул подвалда калырга җыенмый иде.', 'David was not going to stay in that basement his entire life.'),
    ('Һәр көнне яңа яшелчәләр һәм җимешләр ашарга кирәк.', 'One has to eat fresh vegetables and fruit every day.'),
]),
('b2-prov', [
    ('Ябага тайны хурлама - язга чыкса ат булыр.', "Don't scorn a shaggy foal — by spring it will be a horse."),
    ('Ялган сүздә чама юк, дөрес сүздә чама бар.', 'A lie knows no limits; the truth has its measure.'),
    ('Кеше үзенә баш булса, кешегә дә баш булыр.', 'One who can master himself can lead others.'),
    ('Үзең генә көлеп бетермә, кешегә дә калдыр.', "Don't use up all the laughter yourself — leave some for others."),
]),
('b2-cult', [
    ('Авыруларга ул элеккегә караганда да шәфкатьлерәк, иманлырак булды.', 'She became even more compassionate and devout towards the sick than before.'),
    ('Авторны яңа китабы белән котларга каләмдәшләре, якын дуслары килгән.', 'Fellow writers and close friends came to congratulate the author on his new book.'),
    ('Авторның сандыгында тагын бер томлык запас әкиятләре чират көтеп ята.', "In the author's chest, another volume of fairy tales is waiting its turn."),
    ('Әсәр башыннан ахырына кадәр мәгърифәтчелек идеяләре белән сугарылган.', 'From beginning to end the work is steeped in the ideas of the Enlightenment.'),
]),
('b2-story', [
    ('Акчаны алуга бу шунда ук кабакка барып эчәргә тотына.', 'As soon as he gets the money, he heads straight to the tavern and starts drinking.'),
    ('Авылда әткәйнең әсирлектә булганын беркем дә белмәде.', 'Nobody in the village knew that father had been a prisoner of war.'),
    ('Син бик кыю кеше икәнсең, Әхмәт кебек куркак түгелсең.', 'You turn out to be a very brave person — not a coward like Ahmet.'),
    ('Якынайгач күрде: халык төркеме ишегалдына җыелган икән.', 'When he came closer he saw that a crowd had gathered in the yard.'),
]),
('b2-soc', [
    ('Акция Куйбышев һәм Түбән Кама сусаклагычлары территориясендә узачак.', 'The campaign will take place on the territory of the Kuybyshev and Lower Kama reservoirs.'),
    ('Аларда төп фәннәрдән кала татар, казах, алман телләрен дә өйрәнәләр.', 'Besides the main subjects, they also study Tatar, Kazakh and German there.'),
    ('Авыл җирендә терлек асрамыйча көн күрүне күз алдына китерүе дә кыен.', "It's hard even to imagine making a living in the countryside without keeping livestock."),
    ('Акциянең төп максаты - уңышлы, акчалы кешеләрне хәйрия эшенә җәлеп итү.', 'The main aim of the campaign is to involve successful, wealthy people in charity work.'),
]),
('b2-opinion', [
    ('Зинһар, калган ризыкларны үзегез белән өйгә алып китегез.', 'Please take any leftovers home with you.'),
    ('Аны шөпшә чакты һәм анда аллергик реакция барлыкка килде.', 'A wasp stung him and he had an allergic reaction.'),
    ('Минем ашказаны авыруы яки башка шундый нәрсә булырга тиеш.', 'I must have a stomach bug or something.'),
    ('Әгәр сезнең вакыт машинасы булса, сез кайчан барыр идегез?', 'If you had a time machine, when would you go to?'),
]),
('b2-life', [
    ('Күңелдәге бар ризасызлыкны да тышка чыгарып булмый.', "You can't let out all the discontent in your heart."),
    ('Миллион иен штраф? Минем өчен бу берни дә аңлатмый.', "A one million yen fine? That's nothing to me."),
    ('Ни өчен монда чит ил туристлары саны елдан-ел кими?', "What's the reason why the number of foreign tourists here decreases every year?"),
    ('Яшәү мәгънәсе – көн үткәрү генә түгел икәнен онытма.', "Don't forget that the meaning of life is not just getting through the day."),
]),
('b2-prov', [
    ('Күңел ятмаган эш яратмаган кәләш белән бер.', "Work your heart isn't in is like a bride you don't love."),
    ('Аюны җиңгән ярты ир, ачуын җиңгән бөтен ир.', 'He who defeats a bear is half a man; he who defeats his anger is a whole man.'),
    ('Гыйлем китапның эчендә дә, тышында да була.', 'Knowledge is found both inside books and outside them.'),
    ('Урманда да сукмак бар, агачта да колак бар.', 'The forest has paths, and the trees have ears.'),
]),
('b2-cult', [
    ('Аксак Тимернең явы халык өчен үләт чиреннән яман бер куркыныч булган.', "For the people, Timur's army was a danger worse than the plague."),
    ('Кояш төсле җете сары җирлеккә әфлисун төсендәге көзге яфраклар төшкән.', 'Orange autumn leaves have fallen onto the bright, sun-yellow background.'),
    ('Аларда гаиләләре белән аучылар, балыкчылар һәм иген үстерүчеләр яшәгән.', 'Hunters, fishermen and grain growers lived there with their families.'),
    ('Азат Кадыйр улы әүвәл хәрби гәзитләр өчен мәкаләләр, очерклардан башлый.', 'Azat Kadyrovich started out writing articles and sketches for military newspapers.'),
]),
('b2-story', [
    ('Кара әле, әнә теге кеше шулкадәр Хәсән Туфанга охшаган.', 'Look, that man over there looks so much like Hasan Tufan.'),
    ('Мин аны егермедә очраттым, ә егерме өчтә ташлап киттем.', 'I met him at twenty, and left him at twenty-three.'),
    ('Улым, көн саен дискотекага йөрмә син, саңгырау калырсың!', "Son, don't go to the disco every day — you'll go deaf!"),
    ('Бөтен ил барыбер шуңа күчәчәк, - дип ассызыклады Альберт.', 'The whole country will switch to it anyway, Albert stressed.'),
]),
('b2-soc', [
    ('Дәүләт структураларында, эш кәгазьләрендә телебез гамәлдә түгел диярлек.', 'Our language is hardly used in government bodies and official paperwork.'),
    ('Авылга ярдәм буларак гамәлгә ашырыла торган программаларыбыз бик кирәкле.', 'Our programmes to help the countryside are very much needed.'),
    ('Билбау көрәше безнең тәкъдим белән Универсиада программасына да кертелде.', 'At our suggestion, belt wrestling was also included in the Universiade programme.'),
    ('Бүген бу искиткеч милли бәйрәм чикләрен ачты, ул интернациональгә әйләнде.', 'Today this wonderful national festival has crossed its borders and become international.'),
]),
('b2-opinion', [
    ('Мондагы кешеләрнең барысы да, бездән башка, моны эшләделәр.', 'Everyone here except us has done that.'),
    ('Мин моны үзем генә эшләргә туры килергә мөмкин икәнен беләм.', 'I know that I might have to do that by myself.'),
    ('Бу йортлар әйләнә-тирә пейзажга гармонияле рәвештә туры килә.', 'These houses are in harmony with the surrounding scenery.'),
    ('Мин сезнең моның белән нәрсәгә ирешергә теләвегезне аңламыйм.', "I don't understand what you want to achieve with that."),
]),
('b2-life', [
    ('Мактанганчы эшләп күрсәтсә, күпкә яхшырак булыр иде.', 'It would be much better if he showed what he could do instead of boasting.'),
    ('Мин яхшы тылсымчы булырга теләвемә бик җитди карыйм.', "I'm very serious about wanting to be a good magician."),
    ('Минем әни иртә тол калды, кулында алты баласы калды.', 'My mother was widowed early and left with six children to raise.'),
    ('Мин моның шундый зур әһәмияткә ия икәнен белми идем.', "I didn't know it was a big deal."),
]),
('b2-prov', [
    ('Батыр башлап җибәрә, артыннан мең кул иярә.', 'A hero makes a start, and a thousand hands follow.'),
    ('Хәлеңә карап эш күр, борыныңа карап төчкер!', 'Act according to your means — sneeze according to your nose!'),
    ('Алты көн ач булсаң да, ата гадәтен ташлама.', "Even if you go hungry for six days, don't abandon your father's ways."),
    ('Һәркемнең үз ватаны алтын, йөрәк төбе ялкын.', "Everyone's homeland is golden, a flame deep in the heart."),
]),
('b2-cult', [
    ('Автор аның хатын-кыз итәгенә ябышырга гына торуын бик оста итеп ачып бирә.', "The author shows very skilfully how he only ever clings to a woman's skirt."),
    ('Ак мәчет комплексы Болгар музей-тыюлыгының Көньяк капкасы янында төзелгән.', 'The White Mosque complex was built near the South Gate of the Bolgar museum reserve.'),
    ('Тукайның Казанга килгәч язган иң әүвәлге шигырьләреннән берсе театр турында.', 'One of the first poems Tukay wrote after coming to Kazan is about the theatre.'),
    ('Аларда безнең җәмгыятебезнең чын йөзе, мәдәниятебезнең торышы да ачык күренә.', 'In them the true face of our society and the state of our culture can be clearly seen.'),
]),
('b2-story', [
    ('Нурислам, бер күзен генә ачып, өстәлдәге сәгатенә карады.', 'Nurislam opened just one eye and looked at the clock on the table.'),
    ('Атасы кире борылып, тагын баласының муенына асылынып елый.', "The father turns back and, clinging to his child's neck again, weeps."),
    ('Күз ачып йомганчы егетне патша ишеге алдына китереп куйды.', "In the blink of an eye it set the young man down in the king's courtyard."),
    ('Кадерлем, мине тагын бер үпсәң, гомерлеккә синеке булырмын.', "My dear, if you kiss me once more, I'll be yours forever."),
]),
('b2-soc', [
    ('Киек каз юлы утыз бишкә якын башка галактика белән бер йолдызлык булып тора.', 'The Milky Way is part of a cluster of about thirty-five galaxies.'),
    ('Авыл җирлеге башлыгы Шәүкәт Тимерханов әйтүенчә, элек авылда ике мәчет булган.', 'According to the head of the rural settlement, Shaukat Timerkhanov, there used to be two mosques in the village.'),
    ('Абитуриентлар университетның сайты аша кызыксындырган сорауларына җавап таба ала.', 'Applicants can find answers to their questions on the university website.'),
    ('Премьер-министр Халиков районның элекке җитәкчелеге исеменә рәхмәт сүзләрен җиткерде.', "Prime Minister Khalikov passed on words of thanks to the district's former leadership."),
]),
('b2-opinion', [
    ('Сез соры төстәге ябалакларны башка ябалаклардан аера аласызмы?', 'Can you distinguish between tawny owls and other owls?'),
    ('Сез рәсемнәрегезне сатарга тиеш, чөнки алар чынлап та бик шәп.', "You should sell your drawings because they're really wonderful."),
    ('Без беркайчан да яраткан вакыттагы кебек йомшак була алмыйбыз.', 'We are never as vulnerable as when we love.'),
    ('Һәр сишәмбе көннең икенче яртысында профессорның эш сәгате бар.', 'The professor has office hours every Tuesday afternoon.'),
]),
('b2-life', [
    ('Актив яшәү рәвеше алып бару - ул матурлык һәм яшьлек.', 'Leading an active lifestyle means beauty and youth.'),
    ('Проблеманы бетерү өчен без нинди адымнар ясый алабыз?', 'What steps can we take to fix the problem?'),
    ('Кайчагында үзеңне кирәксез итеп тойган чаклар да була.', 'Sometimes there are moments when you feel unneeded.'),
    ('Сез шуны аңламыйсыз: мине моны эшләргә мәҗбүр иттеләр.', "What you don't realise is that I was coerced into doing it."),
]),
('b2-prov', [
    ('Кәкре үсеп картайган агачны төз итеп булмый.', "A tree that has grown old and crooked can't be made straight."),
    ('Бик шәп аккан чишмәнең башы якын була, имеш.', 'They say a fast-flowing spring has its source close by.'),
    ('Атаң сүзенә колак сал, мәкаль әйтсә язып ал.', "Listen to your father's words, and if he says a proverb, write it down."),
    ('Уңган кеше кулына туфрак учласа да алтын итә.', 'A capable person turns even a handful of soil into gold.'),
]),
('b2-cult', [
    ('Авылдан, чишмә буеннан башланган тормыш юлы аларны төрле биеклекләргә күтәрә.', 'Their path in life, which began in the village by the spring, takes them to various heights.'),
    ('Сезнең өстә - зур җаваплылык, милли театр буларак, милләтне саклау бурычы тора.', 'You bear a great responsibility: as a national theatre, you have the duty of preserving the nation.'),
    ('Автор башта тыныч уеннар уйнаган малайларны бер-берсе белән ярышырга мәҗбүр итә.', 'The author makes boys who were at first playing quiet games compete with one another.'),
    ('Авыл кешеләренең әллә ничә буыныннан бирле килгән легендаларны онытуы ни үкенеч!', 'What a pity that villagers are forgetting legends handed down over so many generations!'),
]),
('b2-story', [
    ('Абыйсы Кәбир төрмәдән кайткач, Фазылны Оренбургка алып китә.', 'When his older brother Kabir comes back from prison, he takes Fazyl to Orenburg.'),
    ('Авыр контузия ала, аңа озак кына лазаретта ятарга туры килә.', 'He suffers a severe concussion and has to spend quite a long time in the field hospital.'),
    ('Абыең дәваханәдә, иртәгә-берсекөнгә чыгарга тиеш, - диде ул.', '"Your brother is in hospital; he should be out tomorrow or the day after," he said.'),
    ('Агаларың шабашкага чыгып киттеләр, алар ике көннән кайтырлар.', "Your brothers have gone off to do odd jobs; they'll be back in two days."),
]),
('b2-soc', [
    ('Авыл үсеп, балалар күбәеп киткән очракта, янкорма күтәрү мөмкинлеге дә исәпкә алынган.', 'In case the village grows and there are more children, building an extension has also been planned for.'),
    ('Алабуга бүгенге көндә Россиядә динамик үсеш кичерүче махсус икътисади зоналарның берсе.', "Today Yelabuga is one of Russia's fast-growing special economic zones."),
    ('Алар һавада утлы шар күрүләрен һәм түбән ешлыклы сузылган тавыш ишетүләрен хәбәр иттеләр.', 'They reported seeing a fireball in the sky and hearing a long, low-frequency sound.'),
    ('Акциягә эре сәүдә челтәрләре, җитештерүчеләр, халыкка хезмәт күрсәтүчеләр дә җәлеп ителде.', 'Large retail chains, producers and service providers were also brought into the campaign.'),
]),
('b2-opinion', [
    ('Бу тартма шулкадәр авыр ки, мин аны ялгызым гына күтәрә алмыйм.', 'This box is too heavy for me alone to lift.'),
    ('Соңгы елларда солдат хезмәтенең абруе эзлекле рәвештә кими бара.', 'In the recent years, the reputation of serving as a soldier has steadily been lowered.'),
    ('Ул якынлыкны аларның мөнәсәбәтләренең мөһим өлеше буларак карый.', 'He views intimacy as an important part of their bond.'),
    ('Безнең компаниянең еллык сату күләме мең миллион иен тәшкил итә.', 'Our company has annual sales of a thousand million yen.'),
]),
('b2-life', [
    ('Керү ишеге янында кемдер бар. Бар, кара әле, кем икән.', "There's somebody at the front door. Go see who it is."),
    ('Авыл кешесенең ничек яшәгәнен, эшчән булуын күреп үстем.', 'I grew up seeing how village people live and how hard they work.'),
    ('Телне югалту ул - гореф-гадәтне, динне югалту дигән сүз.', 'Losing your language means losing your customs and your faith.'),
    ('Бу минем өчен бик кыйммәт. Бәясен бераз төшерә аласызмы?', "That's too expensive for me. Can you lower the price a bit?"),
]),
('b2-prov', [
    ('Имән бик каты агач та, аның да яфрагы саргая.', 'The oak is a very hard tree, yet even its leaves turn yellow.'),
    ('Каршы адәм уен бозар, тинтәк адәм җыен бозар.', 'A contrary person spoils the game; a foolish one spoils the gathering.'),
    ('Балан бал белән тәмле, бал балансыз да тәмле.', 'Viburnum is tasty with honey, but honey is tasty without viburnum.'),
    ('Фәлән җирдә файда бар, үз җиреңдәй кайда бар?', 'There may be profit in a far-off place, but where is there a place like your own land?'),
]),
('b2-cult', [
    ('Шигырь ахырына галим үлеменең зур югалту алып килгәнлеге хакында берничә юл өсти.', "At the end of the poem he adds a few lines about what a great loss the scholar's death was."),
    ('Аерым шигырьләре украин, үзбәк, азәрбайҗан һәм башка милли телләргә тәрҗемә ителде.', 'Some of the poems were translated into Ukrainian, Uzbek, Azerbaijani and other national languages.'),
    ('Акмулла үз шигырьләрен татарча, ләкин шактый дәрәҗәдә казакъ теле йогынтысында яза.', 'Akmulla writes his poems in Tatar, but strongly influenced by Kazakh.'),
    ('Сез кайчан да булса лингвистик чагыштырмалылык концепциясе турында ишеткәнегез бармы?', 'Have you ever heard of the concept of linguistic relativity?'),
]),
('b2-story', [
    ('Гомумән кырысрак булса да, уен-көлке белән сөйләшергә яратты.', 'Although he was rather stern on the whole, he liked to talk with a joke.'),
    ('Агач кәүсәсендә ап-ак эзләр калдырып, Фатыйх кайры кисеп алды.', 'Leaving snow-white marks on the tree trunk, Fatykh cut off some bark.'),
    ('Салих карт шатлыгын биеп шатланмады, кайгысын елап кайгырмады.', "Old Salikh didn't dance with joy or weep with sorrow."),
    ('Егет ныклап караса, шакката: капка сакчысы моның үз әтисе икән.', 'When the young man took a good look, he was stunned: the gatekeeper was his own father.'),
]),
('b2-soc', [
    ('Май азагында Россиягә рәсми визиты кысаларында Казанга Австрия Президентының килүе көтелә.', 'At the end of May the President of Austria is expected in Kazan as part of an official visit to Russia.'),
    ('Радар алдында гына тормозга басарга күнеккән машина йөртүчеләр хәзер штрафтан котыла алмаячак.', 'Drivers used to braking only right in front of a speed camera will no longer escape fines.'),
    ('Аерым алганда, алар ашханәдә булды һәм мәктәп пешекчеләре пешергән ризыкларны татып карадылар.', 'In particular, they visited the canteen and tasted the dishes cooked by the school cooks.'),
    ('Аерым алганда, ул соңгы елларда рус-татар бүлекләренә абитуриентлар туплау кыенлашуына борчыла.', 'In particular, he is worried that in recent years it has become harder to attract applicants to Russian-Tatar departments.'),
]),
('b2-opinion', [
    ('Нәрсә авыррак: бер килограмм алтынмы, әллә бер килограмм көмешме?', 'What weighs more: one kilo of gold or one kilo of silver?'),
    ('Син бит моның ничек булганын беләсең: бер сүз икенчесен китерә....', 'You know how these things go, one word leads to another....'),
    ('Карар кабул иткән саен мин үземә ышанмау йөге басым ясавын тойдым.', 'With every decision, I felt the weight of insecurity pressing down.'),
    ('Мәктәптә иң яраткан фәнегез кайсы иде һәм ул сезгә ни өчен ошый иде?', 'What was your favorite subject in school, and why did you like it?'),
]),
('b2-life', [
    ('Мин елга бер тапкыр күз тикшерүен узарга өстенлек бирәм.', 'I prefer to have a yearly eye exam.'),
    ('Ышаныч ике яклап та булганда гына уңышка исәп тотып була.', 'You can only count on success when there is trust on both sides.'),
    ('Кыстасалар да күңелең тартмаган эшкә алынмавың хәерледер.', "Even if they press you, it's better not to take on work your heart isn't in."),
    ('Күңел кушуы буенча эшләнгән батырлык кына – чын батырлык.', "Only a brave deed done at the heart's bidding is true bravery."),
]),
('b2-prov', [
    ('Яхшы сүз җанга рәхәт, яман сүз җанга җәрәхәт.', 'A kind word soothes the soul; a harsh word wounds it.'),
    ('Ялган сөйләп яшәгәнче, рас сөйләп үлгән яхшы.', 'Better to die telling the truth than to live telling lies.'),
    ('Җиде йортның телен бел, җиде төрле белем бел.', 'Know the language of seven households, and seven kinds of knowledge.'),
    ('Кар яуганда салкын булмый, кар киткәндә суыта.', "It isn't cold while snow is falling; it gets cold when the snow goes."),
]),
('b2-cult', [
    ('Аерым алганда, татарча яхшы китаплар чыгуын, милли традицияләрнең торгызылуын искәртә.', 'In particular, he notes that good books are being published in Tatar and national traditions revived.'),
    ('И туган тел! Һәрвакытта ярдәмең белән синең, кечкенәдән аңлашылган шатлыгым, кайгым минем.', 'Oh native tongue! With your help I have always known my joys and sorrows, understood since I was small.'),
    ('Автор геройларның характерын, психологиясен көтелмәгән сынаулар, дәһшәтле вакыйгалар аша ача.', "The author reveals the characters' personalities and psychology through unexpected trials and terrible events."),
    ('Диңгез көне - июльнең өченче дүшәмбесендә билгеләп үтелә торган Япония милли бәйрәмнәренең берсе.', 'Sea Day is one of the Japanese national holidays celebrated on the third Monday in July.'),
]),
('b2-story', [
    ('Ашыккан акча янчыгын алам дип тәмәке янчыгын алып чыгып киткән.', 'In his hurry he meant to take his purse but went out with his tobacco pouch.'),
    ('Егет шул заманда чокырда көтеп утырганда, машина тавышы ишетелде.', 'While the young man was waiting in the pit, the sound of a car was heard.'),
    ('Әгәр дә студент чакта үзлегемнән стенография өйрәнмәгән булсам...', "If I hadn't taught myself shorthand as a student..."),
    ('Чыгарылыш кичәсенә иске күлмәгемне сүтеп, яңа күлмәк тегеп кидем.', 'For my graduation party I unpicked my old dress, sewed a new one and wore it.'),
]),
('b2-soc', [
    ('Авыл мәктәпләрендә профильле укыту түбән дәрәҗәдә, чөнки аның мөмкинлекләре юк, шартлар тудырылмаган.', "Specialised teaching in village schools is poor, because there are no means for it and the conditions haven't been created."),
    ('Без туфракның уңыш бирүчәнлеген күтәрәбез, без агротехника чараларын үткәрергә кешеләргә ярдәм итәбез.', 'We raise soil fertility and help people carry out agricultural measures.'),
    ('Эре мөгезле терлек үрчетү-фермерның бер шөгыле, һәм терлекләрне алар токымына карап җентекләп сайлап алалар.', "Cattle breeding is one of the farmer's occupations and the animals are carefully selected according to their breed."),
    ('Барлык кешеләр дә азат һәм үз абруйлары һәм хокуклары ягыннан тиң булып туалар. Аларга акыл һәм вөҗдан бирелгән, һәм алар бер-берсенә карата туганнарча мөнәсәбәттә булырга тиешләр.', 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'),
]),
('b2-opinion', [
    ('Авыл халкының әйләнә-тирә мохит турындагы бәхәсе шактый җанлы булды.', 'The discussion the villagers had on the environment was quite lively.'),
    ('Безнең яхшы сыйфатларыбыз, күпчелек очракта, яшерен начарлыклар гына.', 'Our virtues are, most often, only disguised vices.'),
    ('Ул десантчыларның элиталы подразделениесенә керү теләге белән яна иде.', 'He was eager to join the elite unit of paratroopers.'),
    ('Синең өчен шулкадәр борчылдым ки, хәтта төннәрен дә яхшы йоклый алмадым.', "I've been so worried about you that I haven't been sleeping well at night."),
]),
('b2-life', [
    ('Мактауны да, тәнкыйтьне дә тыныч үткәреп җибәрергә өйрән.', 'Learn to take both praise and criticism calmly.'),
    ('Теориядә барысы да бик яхшы, ләкин гамәлдә ул эшләячәкме?', "It's all very well in theory, but will it work in practice?"),
    ('Мин модага хөрмәт белән карыйм, ләкин аның колы түгелмен.', "I appreciate fashion, but I'm not a slave to it."),
    ('Бостонга килү белән, зинһар, минем белән элемтәгә керегез.', 'Please get in touch with me as soon as you arrive in Boston.'),
]),
('b2-prov', [
    ('Акыллы кеше сүз әйткәндә, әйтер сүзен чамалар.', 'A wise person weighs his words before he speaks.'),
    ('Эшле кеше эш арттырыр, эшсез кеше эш калдырыр.', 'A busy person takes on more work; an idle one leaves work undone.'),
    ('Авыздагы сүзгә син ия, авыздан чыккач, сүз ия.', "You own the word in your mouth; once it's out, the word owns you."),
    ('Чит илдә солтан булганчы, үз илеңдә олтан бул.', 'Better to be a shoe sole in your own land than a sultan abroad.'),
]),
('b2-cult', [
    ('Латин теле фильмда фәнни реконструкцияләнгән әйтелешкә туры килми, ә күбрәк итальян теле кебек яңгырый.', "The Latin in the film doesn't follow the scientifically reconstructed pronunciation, but instead sounds rather like Italian."),
    ('Кешеләр бөтен һөнәри юлларын төрки һәм урал телләре арасындагы бәйләнешне табарга тырышуга багышлаганнар.', 'People have spent whole careers trying to find a link between Turkic and Uralic languages.'),
    ('Заманәлиф дип аталган яңа татар язуы сүзләрнең язылышы һәм әйтелеше тулысынча тәңгәл килерлек итеп эшләнгән.', 'The new Tatar script zamanalif is designed so that the spelling and pronunciation of words fully correspond to each other.'),
    ('Татарстан Республикасы флагының яшел төсе – яз һәм яңарыш, агы – ниятләр сафлыгы, кызылы рухи җитлеккәнлек, энергия, яшәү көче дип шәрехләнә.', 'The green of the Tatarstan flag is read as spring and renewal, the white as purity of intention, and the red as spiritual maturity, energy and vitality.'),
]),
('b2-story', [
    ('Ләйләнең моңарчы беркайчан да тәреле муенса тагып йөргәне юк иде.', 'Layla had never, ever worn a cross necklace before.'),
    ('Яшь балалар да, таза, көчле ир-егетләр дә, картлар да җыелган икән.', 'Small children, strong healthy men and old people had all gathered.'),
    ('Әхмәт, бер мең сум бурычын сорар дип куркып, миннән гел качып йөри.', "Afraid I'll ask for the thousand roubles he owes me, Ahmet keeps avoiding me."),
    ('Карчык, яңа гына ишеткән кебек, ул якка борылып азрак тыңлап торды.', 'The old woman, as if she had only just heard, turned that way and listened for a while.'),
]),
('b2-opinion', [
    ('Аның хикәясендәге туры килмәүләр аның белдерүләренең дөреслегенә шик тудыра.', 'The inconsistencies in his story raise doubts about the truthfulness of his statements.'),
    ('Вәзгыять тамырдан үзгәрде, һәм барлык элекке планнардан баш тартырга туры килде.', 'The situation had fundamentally changed, and all prior plans had to be scrapped.'),
    ('Әлеге бүләк тикшеренү һәм фән өлкәсендәге күренекле тормыш казанышлары өчен бирелә.', 'The award recognizes outstanding life accomplishments in research and science.'),
    ('Болытлы һәм беркадәр салкын һава торышы марафонга әзерлек өчен идеаль шартлар тудырды.', 'The cloudy and somewhat cool weather offered perfect conditions to prepare for the marathon.'),
]),
('b2-life', [
    ('Алман һәм француз телләрендә бик күп кызыклы китаплар бар.', 'There are a lot of interesting books in German and French.'),
    ('Битарафлык – үзең теләп тормышта көрәштән читләшү дигән сүз.', "Indifference means stepping out of life's struggle of your own free will."),
    ('Тау биегрәк булган саен аннан егылып төшү куркынычы да арта.', 'The higher the mountain, the greater the danger of falling from it.'),
    ('Тормышта үзеңне генә түгел, эшеңне дә күрсәтә белергә кирәк.', 'In life you need to know how to show not only yourself but also your work.'),
]),
('b2-prov', [
    ('Мыектан олы сакал бар, сүз төбендә мәкаль бар.', "There's a beard bigger than any moustache, and at the root of every speech there's a proverb."),
    ('Ишәккә җәймә түшәк, ишәк түшәк кадерен белмәс.', "Don't spread a featherbed for a donkey: a donkey won't appreciate it."),
    ('Бер агачтан унау үскән, ун агачтан урман үскән.', 'From one tree ten grew, and from ten trees grew a forest.'),
    ('Табаны кызганчы тай узар, табаны кызса ат узар.', "Until their hooves warm up the foal is ahead; once they're warm, the horse overtakes."),
]),
('b2-story', [
    ('Безнең ишегалдында почтальон агач башына менгән дә, этебезне үчекли!', 'In our yard the postman has climbed a tree and is teasing our dog!'),
    ('Ирең Нобель премиясе алырга Стокгольмга киткән икән дип ишеткән идем.', "I'd heard your husband had gone to Stockholm to receive the Nobel Prize."),
    ('Авылга килеп керүгә көянтә белән су алып кайта торган бер кызга очрый.', 'As soon as he enters the village, he meets a girl carrying water on a yoke.'),
    ('Минем моңарчы бер тапкыр да эш хакымны арттыру турында сораганым юк иде.', 'I had never once asked for a pay rise before.'),
]),
('b2-opinion', [
    ('"Мария урыс телен ничек белә?" - "Ул аны урта мәктәптә өченче чит тел буларак өйрәнде."', '"How does Maria know Russian?" "She studied it as a third foreign language in high school."'),
    ('И туган тел, и матур тел, әткәм-әнкәмнең теле! Дөньяда күп нәрсә белдем син туган тел аркылы.', 'Oh native tongue, oh beautiful tongue, the language of my father and mother! Through you, my native tongue, I have come to know so much of the world.'),
    ('Бу гадел сорау. Тик менә тагын бер сорау. Сезгә берьюлы артык күп сораулар бирәсез кебек тоелмыймы?', "Well, that's a fair question. But here's another question. Don't you think that you are asking too many questions at once?"),
    ('Фәлсәфәчеләр ихтыяр көче турында дөньяда иң яхшы танып беленә торган нәрсә сыман фикер йөртергә күнеккәннәр.', 'Philosophers are accustomed to speak of the will as if it were the best-known thing in the world.'),
]),
('b2-life', [
    ('Син инде мөстәкыйль рәвештә аякка басарга җитәрлек олы кеше.', 'You are old enough to stand on your own feet.'),
    ('Дин ул сәламәтлеккә дә, чисталыкка да зур игътибар дигән сүз.', 'Religion also means paying great attention to health and cleanliness.'),
    ('Бу факторлар яңа музыкаль юнәлешләрнең үсешенә этәргеч бирде.', 'These factors encouraged the development of new musical trends.'),
    ('Авыл кешесе эштән башканы белми, эш белән туа, эш белән картая.', 'A villager knows nothing but work: born to work, he grows old working.'),
]),
('b2-prov', [
    ('Юләр белән бал ашаганчы, акыллы белән таш ташы.', 'Better to haul stones with a wise man than eat honey with a fool.'),
    ('Тау түбәсеннән купкан таш төшеп җитми туктамый.', "A stone dislodged from the mountaintop won't stop until it reaches the bottom."),
    ('Үзең сөйли башлаганчы, кеше сүзен тыңлап бетер.', 'Before you start talking, hear the other person out.'),
    ('Елганың башы комлы булса, тамагы да комлы була.', "If a river's source is sandy, its mouth will be sandy too."),
]),
('b2-story', [
    ('Акча түләмәгәч, солдатларны тотып, бик каты итеп кыйнап чыгарып җибәрәләр.', "When they didn't pay, the soldiers were seized, beaten badly and thrown out."),
    ('Ничектер кабельләргә су кергән, һәм алар өзелә башлаган кебек тавыш чыкты.', 'It sounded like water had got onto the cables somehow, and they were breaking.'),
    ('Начар егет түгел шикелле, тора-бара, бәлки, ияләшеп китәрбез, дип уйлады Ләйлә.', "He doesn't seem a bad lad; maybe in time we'll get used to each other, thought Leyla."),
    ('Бу продуктта консервантлар юк. Ачылгач, суыткычта саклагыз һәм тиз арада кулланыгыз.', 'This product contains no preservatives. After opening, refrigerate and consume quickly.'),
]),
('b2-life', [
    ('Нәрсәгәдер ирешкәнмен икән, димәк мин моны ихластан теләгәнмен.', "If I've achieved something, it means I wanted it sincerely."),
    ('Мине спорт көнендә "балалар исеменнән чыгыш ясарга" сайладылар.', 'Me, I was selected to do the "children\'s representative speech" at sports day.'),
    ('Керемнәрне саклау буенча командалар даими рәвештә челтәрдә эшли.', 'Revenue Protection teams are regularly out and about on the network.'),
    ('Койотлар азыкны ничек тоталар, шулай үләксә белән дә тукланалар.', 'Coyotes both catch food and eat carrion.'),
]),
('b2-prov', [
    ('Кеше көлә дип көлә идем, кеше миннән көлә икән.', 'I laughed because people were laughing — turns out they were laughing at me.'),
    ('Алмазны балчык арасына ташласаң да, алмаз булыр.', "Even if you throw a diamond into the mud, it's still a diamond."),
    ('Ярык кайда — җил шунда, ялкау кайда — тел шунда.', "Where there's a crack, there's a draught; where there's a lazy man, there's talk."),
    ('Биш юләргә киңәш иткәнче, бер акыллыга киңәш ит.', 'Rather than consult five fools, consult one wise man.'),
]),
('b2-life', [
    ('Ит ризыкларының тәме аның рецептыннан һәм чимал сыйфатыннан тора.', 'The taste of meat dishes depends on the recipe and the quality of the ingredients.'),
    ('Изге балалар күктән килмиләр, бәлки гаиләләр эчләрендә җитешәләр.', "Good children don't fall from heaven; they are raised within families."),
    ('Яхшы дуслар, яхшы китаплар һәм тыныч вөҗдан – менә идеаль тормыш.', 'Good friends, good books, and a sleepy conscience: this is the ideal life.'),
    ('Ягъни бөтен дөньяга сибелгән татар яшьләрен берләштерүче кеше син.', "In other words, you're the person who unites Tatar young people scattered all over the world."),
]),
('b2-prov', [
    ('Галимнең бер көне, наданның бөтен гомеренә тора.', 'One day of a scholar is worth the whole life of an ignorant man.'),
    ('Һәр нәрсә үз вакытында яхшы икәнне әтәч тә белә.', 'Even the rooster knows that everything is good in its own time.'),
    ('Адәм баласын кыссаң, башлаган эшне дә харап итә.', "If you squeeze a person too hard, he'll ruin even the work he has started."),
    ('Безне адәм иткән — уку, адәмне алга илткән — уку.', 'Learning made us human, and learning moved humanity forward.'),
]),
('b2-life', [
    ('Татарстан милләтара һәм конфессияара татулыкта бай тәҗрибә туплады.', 'Tatarstan has accumulated a rich experience of interethnic and interfaith harmony.'),
    ('Сыйныфташларым мине сүзләрне бозыбрак әйтүем өчен мыскыллыйлар иде.', 'My classmates used to tease me about my accent.'),
    ('Сәясәтчеләрне гадәттә гаугалы яки ярамаган тәртипләре өчен гаеплиләр.', 'Politicians are usually censured for scandalous or inappropriate behavior.'),
    ('Буддизм турындагы мәкалә Көнчыгыш диннәре белән кызыксынуымны яңартты.', 'The article on Buddhism revived my interest in oriental religions.'),
]),
('b2-prov', [
    ('Берәү үзе батыр, берәү качарга курыкканнан батыр.', "One man is brave by nature; another is brave because he's afraid to run."),
    ('Эшләгәнең кеше өчен булса - өйрәнгәнең үзең өчен.', 'What you work at may be for others, but what you learn is for yourself.'),
    ('Син дә мулла, мин дә мулла - атка печән кем сала?', "If you're a mullah and I'm a mullah, who'll give the horse its hay?"),
    ('Кырык эт арасында бер этнең койрыгы бот арасында.', 'Among forty dogs, one always has its tail between its legs.'),
]),
('b2-life', [
    ('Мин монда сине гомереңдәге иң зур хатаны ясаудан туктатыр өчен килдем.', "I'm here to stop you from making the biggest mistake of your life."),
    ('Теләсә кайсы кешенең тормышта үзенә өлге иткән үрнәге булмый калмыйдыр.', 'Surely everyone has someone in life they take as a role model.'),
    ('Берәүләр ни телиләр шуны эшлиләр, икенчеләр исә бар яклап та чикләнгәннәр.', 'Some people do whatever they want, while others are restricted on every side.'),
    ('Белем алу ата-аналар өчен дә, балалар өчен дә авыр йөк булырга тиеш түгел.', 'Education should not be a burden on the parents as well as on the children.'),
]),
('b2-prov', [
    ('Мич башында җиләк пешми, чалкан ятып шалкан үсми.', "Berries don't ripen on top of the stove, and turnips don't grow while you lie on your back."),
    ('Белгәнгә бер сүз җитәр, белмәгәнгә мең сүз дә аз.', "For one who knows, one word is enough; for one who doesn't, a thousand are too few."),
    ('Югарыга карап үрнәк ал, түбәнгә карап гыйбрәт ал.', 'Look up and take an example; look down and learn a lesson.'),
    ('Стенага аткан борчак кире кайтыр да үзеңә бәрелер.', 'A pea thrown at a wall will bounce back and hit you.'),
]),
('b2-life', [
    ('Нәфрәт риторикасы, еш кына, мәхәббәт теле аша бирелгәндә иң нәтиҗәле була.', 'The rhetoric of hate is often most effective when couched in the idiom of love.'),
    ('Бүгенге рәхәтлек иртәгәге михнәткә әверелергә мөмкин икәнен исеңнән чыгарма.', "Don't forget that today's comfort can turn into tomorrow's hardship."),
    ('Сине туган көнең белән котлап, иң изге, якты, матур теләкләребезне юллыйбыз.', 'Congratulating you on your birthday, we send you our kindest, brightest and most beautiful wishes.'),
    ('Тормыш капма-каршылыклары белән генә түгел, охшашлыклары белән дә гыйбрәтле.', 'Life teaches us not only through its contrasts but also through its similarities.'),
]),
('b2-prov', [
    ('Кешегә бик күп акыл өйрәткән кешенең үзенә калмый.', 'The person who teaches others too much sense has none left for himself.'),
    ('Эшне эшләүдә бер хикмәт, яратып эшләүдә ун хикмәт.', "There's one secret in doing work, and ten in doing it with love."),
    ('Көн дә бәйрәм, көн дә туй, көн дә уен, көн дә сый.', 'Every day a holiday, every day a wedding, every day games, every day a feast.'),
    ('Файдасыз гамәлләр гомерне чирдән дә битәр кыскарта.', 'Useless deeds shorten life even more than illness does.'),
]),
('b2-life', [
    ('Авыл китапханәсенә татар телендә нинди генә китап кайтса да, укымыйча калдырмыйм.', 'Whatever Tatar book arrives at the village library, I never leave it unread.'),
    ('Миңа бәдрәфкә барырга кирәк, ләкин синең дусларың коридорны тулысынча тутырдылар.', 'I have to pee, but your friends are completely crowding the hallway.'),
    ('Сезнеңчә, әгәр берәр кеше нидер эшли ала икән, димәк, башкалар да моны эшли аламы?', 'Do you think that if one person can do something, that everyone else can do it too?'),
    ('Минем якты хатирәләрем һәм хисләрем бик күп, Бостон белән бәйле яхшы да, начар да.', 'I have too many intense memories and feelings, both good and bad, associated with Boston.'),
]),
('b2-prov', [
    ('Агач хәтта үзен кисеп торган кешегә дә күләгә бирә.', 'A tree gives shade even to the person cutting it down.'),
    ('Ачулы кешегә песи койрыгын күтәреп йөрсә дә ярамый.', 'To an angry man, even a cat walking with its tail up is annoying.'),
    ('Боздан чыксаң, алдан чык, судан чыксаң, арттан чык.', 'When crossing ice, go first; when crossing water, go last.'),
    ('Авызың тулы кара кан булса да, кеше алдында төкермә!', "Even if your mouth is full of blood, don't spit in front of people."),
]),
('b2-life', [
    ('Мин белергә теләр идем, ни өчен беркем дә бу тәкъдим өчен җаваплылыкны үз өстенә алмады.', "I'd like to know why no one has taken ownership of that sentence yet."),
    ('Мин дәүләт идарәсе сыйныфында иң либераль студентларның берсе, һәм миңа яхшы дебатлар ошый.', "I'm one of the more liberal students in my government class, and I like a good debate."),
    ('Мин чыннан да күнегүләр ясарга яратмыйм, ләкин табиб миңа күнегүләр ясарга кирәклеген әйтте.', "I don't really like exercising, but my doctor tells me I need to."),
    ('Бөдрә коңгырт чәчле, шаян коңгырт күзле, мыскыллы елмаюлы авызлы озын буйлы бер малай иде ул.', 'He was a tall boy, with curly brown hair, roguish hazel eyes, and a mouth twisted into a teasing smile.'),
]),
('b2-prov', [
    ('Агач тамырдан, кеше дуслык-туганлыктан көч алып яши.', 'A tree draws strength from its roots, a person from friendship and kinship.'),
    ('Эшкә булса — уф табаным, ашка булса — китер табагым.', "When it's time to work — oh, my poor feet!; when it's time to eat — bring me my plate!"),
    ('Ат күрдем дип аксап барма, су күрдем дип сусап барма.', "Don't start limping just because you've seen a horse, or get thirsty just because you've seen water."),
    ('Кояш тигез җылыткандай кешеләргә тигез карарга өйрән.', 'Learn to treat people equally, just as the sun warms everyone equally.'),
]),
('b2-life', [
    ('Бик татлы булма кабып йотарлар, бик ачы булма — төкереп ташларлар.', "Don't be too sweet or they'll swallow you; don't be too bitter or they'll spit you out."),
    ('Барлы булсаң - гөл сибәрләр йөзеңә; ярлы булсаң - көл сибәрләр күзеңә.', "If you're rich, they scatter flowers before you; if you're poor, they throw ash in your eyes."),
    ('Болай тукталышта такси көтүдән мәгънә юклыгын аңлагач, без атлый-чаба порт ягына юнәлдек.', 'Realising there was no point waiting for a taxi at the stop, we hurried off towards the port.'),
    ('Һәркемнең дә акылсыз фикерләре була, ләкин акыллы кешеләр аларны үз эчләрендә генә калдыралар.', 'Everyone has dumb ideas, but smart people keep them to themselves.'),
]),
('b2-prov', [
    ('Юнен тапкан айга очар, юньсез тигез җирдә абынып үләр.', 'A resourceful man will fly to the moon; a hopeless one trips and falls on level ground.'),
    ('Көрәшсәң көчлегә чык, егылсаң да һөнәрен отып калырсың.', "If you wrestle, take on someone stronger: even if you fall, you'll learn his skill."),
    ('Яңа чагында киемеңне сакла, яшь чагында исемеңне сакла.', "Look after your clothes while they're new, and your good name while you're young."),
    ('Көнен үз ихтыярына буйсындыра алмаган кеше төнлә эшләр.', "A person who can't make his day obey his will ends up working at night."),
]),
('b2-life', [
    ('Көз көне төштән соңгы яктылык табигатьне сары, әфлисун, кызыл, алтын һәм коңгырт төсләргә кертә.', 'The light of autumn afternoons colours the landscape in hues of yellow, orange, red, gold and brown.'),
    ('Әгәр сез өйдә тынычланырга һәм ял итәргә телисез икән, башта сезгә эш мәсьәләләре турында уйламаска кирәк.', 'If you want to set your mind at rest and relax at home, first you have to not think about work matters.'),
    ('Ләкин аның кече кызы шулкадәр гүзәл булган: хәтта кояш та, аның йөзе балкыганда, таң кала торган булган, ди.', 'But his youngest daughter was so beautiful the sun itself was astonished whenever it shone on her face.'),
    ('Ирләр хатын-кызларны ярата, хатын-кызлар балаларны ярата, балалар әрләннәрне ярата, ә әрләннәр беркемне дә яратмый.', "Men love women, women love kids, kids love hamsters, and hamsters don't love anyone."),
]),
('b2-prov', [
    ('Ата йөрәге — таудан өлкән, ана йөрәге — диңгездән тирән.', "A father's heart is greater than a mountain; a mother's heart is deeper than the sea."),
    ('Песи мич башына менеп ятса, суык; идәнгә ятса, җылы була.', "If the cat climbs up onto the stove, it'll be cold; if it lies on the floor, it'll be warm."),
    ('Вөҗдансыз кеше үзәксез агач кебек, үзлегеннән аварга тора.', 'A man without conscience is like a tree without a core: ready to fall by itself.'),
    ('Сагызны чәйни белмәсәң, эрер, сүзне сөйли белмәсәң, черер.', "If you can't chew gum it melts; if you can't speak well, your words rot."),
]),
('b2-life', [
    ('Гадәти, табигый үлемдә, үзен тормышка ашырган һәм үз гомерен үткәргән кешенең үлемендә бернинди дә куркыныч нәрсә юк.', 'There is nothing frightening about a normal, natural death, the death of a man who has fulfilled himself and lived out his life.'),
    ('Борын-борын заманда, хыяллар әле тормышка ашканда, яшәгән, ди, булган, ди, бер патша. Аның кызлары барысы да бик гүзәл булган, ди.', 'Once upon a time, when wishes still came true, there lived a king. His daughters were all very beautiful, they say.'),
    ('Аның минем белән сөйләшүе, ни генә әйтергә җыенса да, күңелемә хуш килә; аның миңа нәрсә булса да әйтергә теләве генә дә миңа бик ошый.', 'I like when he speaks to me, regardless of what he tries to say; I like the simple fact that he wants to talk to me about something.'),
    ('Вилһелм Фридрих Радлов — танылган алман галиме, төрки халыкларның тарихын һәм авыз иҗатын өйрәнгән һәм татар халык дастаннарының беренче тупланмасын әзерләгән кеше.', 'Wilhelm Friedrich Radloff is the famous German scientist who studied the history and folklore of Turkic peoples and compiled the first collection of Tatar folk dastans.'),
]),
('b2-prov', [
    ('Кешенең кемлеген төсеннән белеп булмый, эшеннән белеп була.', "You can't tell who a person is from their looks, only from their deeds."),
    ('Бии белгәнгә бер такта җитә, бии белмәгәнгә йөз такта да аз.', "For someone who can dance one plank is enough; for someone who can't, a hundred planks are too few."),
    ('Аңлаган бер кылдан да аңлар, аңламаган бүрәнәдән дә аңламас.', "One who understands will understand from a single hair; one who doesn't won't understand even from a log."),
    ('Кайчагында тәгәрмәчкә сыланган балчык та арбаны туктата ала.', 'Sometimes even the mud stuck to a wheel can stop a cart.'),
]),
('b2-prov', [
    ('Әгәр беренче мартта тәрәзәләргә боз катса, бу елны кыяр уңар.', 'If ice forms on the windows on the first of March, cucumbers will do well that year.'),
    ('Кошның матурлыгы төсенә карап, кешенең матурлыгы эшенә карап.', "A bird's beauty is in its colours, a person's beauty in their deeds."),
    ('Дару белән өч шешә, шешә бавын теш чишә, шешә чишсәң теш шешә.', "Three bottles of medicine; teeth untie the bottle's string; untie a bottle and your tooth will swell. (a tongue twister)"),
    ('Галимнең сүзе гомерең үткәнче, наданның сүзе ишектән чыкканчы.', "A scholar's words last until your life is over; a fool's words last until you're out the door."),
]),
('b2-prov', [
    ('Май ае салкын булса, игенгә туклык булыр, чебешкә юклык булыр.', "If May is cold, there'll be plenty of grain but few chicks."),
    ('Ата-анасына игелек күрсәтмәгән, олыгайгач үзе дә игелек күрмәс.', "He who isn't kind to his parents will see no kindness himself in old age."),
    ('Белемле үлсә, кәгазьдә хаты калыр, оста үлсә, эшләгән заты калыр.', 'When a learned man dies, his writing remains on paper; when a craftsman dies, the things he made remain.'),
    ('Ачма серең дустыңа, дустыңның да дусты бар, ул да сөйләр дустына.', "Don't tell your secret to your friend: your friend has a friend, and he'll tell his friend too."),
]),
]
NAMES = {"b2-prov": ("Proverbs", "Мәкальләр"), "b2-life": ("Life", "Тормыш турында"), "b2-story": ("Stories", "Хикәяләр"),
 "b2-opinion": ("Views", "Фикерләр"), "b2-cult": ("Culture", "Мәдәният"), "b2-soc": ("Society", "Җәмгыять")}
assert len(S) == 100, len(S)
cnt = {}
for i, (top, items) in enumerate(S, 1):
    cnt[top] = cnt.get(top, 0) + 1
    en, tt = NAMES[top]
    L(i, f"{en} {cnt[top]}", f"{tt} {cnt[top]}", items, top)
c.save()
