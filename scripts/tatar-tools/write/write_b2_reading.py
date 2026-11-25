# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("b2", "b2-reading")
R = c.R
R(101, "Gabdulla Tukay", "Габдулла Тукай", "The life of the Tatar national poet.",
  [("Габдулла Тукай мең сигез йөз сиксән алтынчы елда Казан губернасында туган.", "Gabdulla Tukay was born in 1886 in Kazan Governorate."), ("Ул бик иртә ятим калган, һәм аның бала чагы төрле гаиләләрдә узган.", "He was orphaned very early, and his childhood was spent with various families."),
   ("Яшь чагында ул Җаекта укыган һәм шунда беренче шигырьләрен язган.", "As a young man he studied in Uralsk (Jayıq), where he wrote his first poems."), ("Тукай нибары егерме җиде ел яшәгән, ләкин татар әдәбиятына бик зур өлеш керткән.", "Tukay lived only twenty-seven years, but made an enormous contribution to Tatar literature."),
   ("Бүгенге көндә аның туган көне, егерме алтынчы апрель, Туган тел көне буларак билгеләп үтелә.", "Today his birthday, 26 April, is celebrated as Native Language Day.")],
  [("What happened to Tukay early in life?", ["He moved abroad", "He was orphaned", "He became rich", "He went to war"], 1),
   ("Where did he write his first poems?", ["In Uralsk", "In Kazan", "In Moscow", "In his village"], 0),
   ("How long did Tukay live?", ["Seventy years", "Fifty years", "Twenty-seven years", "Forty years"], 2),
   ("What is celebrated on his birthday?", ["Sabantuy", "Teachers' Day", "Republic Day", "Native Language Day"], 3)])
R(102, "The Story of Sabantuy", "Сабантуй тарихы", "How an old farming festival went global.",
  [("Сабантуй — татар халкының иң борынгы бәйрәмнәренең берсе.", "Sabantuy is one of the oldest festivals of the Tatar people."), ("Элек ул язгы чәчү эшләре тәмамлангач үткәрелгән.", "In the past it was held once the spring sowing was over."),
   ("Бәйрәмнең төп ярышы — көрәш, һәм җиңүчегә тәкә бүләк ителә.", "The main contest of the festival is wrestling, and the winner receives a ram."), ("Шулай ук йөгерү, капчык киеп сикерү, чүлмәк вату кебек күңелле уеннар бар.", "There are also fun games such as racing, sack-jumping and pot-breaking."),
   ("Хәзер Сабантуй дөньяның күп шәһәрләрендә үткәрелә.", "Today Sabantuy is held in many cities around the world.")],
  [("When was Sabantuy held in the past?", ["In winter", "After the spring sowing", "At harvest time", "On New Year's Day"], 1),
   ("What is the main contest?", ["Wrestling", "Horse racing", "Singing", "Pot-breaking"], 0),
   ("What does the winner receive?", ["A horse", "Money", "A ram", "A cup"], 2),
   ("Where is Sabantuy held today?", ["Only in villages", "Only in Kazan", "Only in Tatarstan", "In many cities around the world"], 3)])
R(103, "Town and Country", "Шәһәр һәм авыл", "Why people move — and why some move back.",
  [("Соңгы елларда күп яшьләр авылдан шәһәргә күчеп китә.", "In recent years many young people have been moving from villages to towns."), ("Шәһәрдә эш табу җиңелрәк, хезмәт хакы да югарырак.", "In town it's easier to find work, and the pay is higher."),
   ("Ләкин авылда һава саф, тормыш тынычрак, кешеләр бер-берсен яхшы белә.", "But in the village the air is clean, life is calmer, and people know each other well."), ("Кайбер гаиләләр, киресенчә, шәһәрдән авылга кайтып, үз хуҗалыкларын булдыралар.", "Some families, on the contrary, move back from town to the village and set up their own farms."),
   ("Һәр кеше үзенә нәрсә кадерлерәк икәнен үзе хәл итә.", "Each person decides for themselves what is dearer to them.")],
  [("Who is moving to the towns?", ["Old people", "Many young people", "Farmers", "Teachers"], 1),
   ("What is an advantage of town life?", ["Clean air", "Calm life", "Higher pay", "Knowing everyone"], 2),
   ("What do some families do?", ["Move back to the village", "Move abroad", "Sell their farms", "Stay in hotels"], 0),
   ("What is the text's conclusion?", ["Town is always better", "Village is always better", "Nobody should move", "Each person decides for themselves"], 3)])
R(104, "Migrating Birds", "Күчмә кошлар", "Long journeys and an old piece of folk wisdom.",
  [("Көз җиткәч, күп кошлар җылы якларга очып китә.", "When autumn comes, many birds fly off to warmer lands."), ("Алар меңнәрчә чакрым юл үтәләр һәм юлны кояш һәм йолдызлар буенча табалар.", "They travel thousands of kilometres and find their way by the sun and the stars."),
   ("Кыр казлары очканда күктә матур почмак ясыйлар.", "When wild geese fly, they form a beautiful wedge in the sky."), ("Язын алар туган җирләренә кайталар һәм оя кора башлыйлар.", "In spring they return to their homelands and begin building nests."),
   ("Халыкта, кошлар иртә кайтса, яз да иртә килә, дип сөйлиләр.", "People say that if the birds come back early, spring will come early too.")],
  [("When do the birds fly away?", ["In spring", "In summer", "When autumn comes", "In winter"], 2),
   ("How do they find their way?", ["By the sun and the stars", "By rivers", "By following people", "By smell"], 0),
   ("What do wild geese form in the sky?", ["A circle", "A wedge", "A line", "A cloud"], 1),
   ("What does folk wisdom say?", ["Birds bring rain", "Late birds mean a hot summer", "Birds never return", "Early birds mean an early spring"], 3)])
R(105, "Learning Languages", "Телләр өйрәнү", "What science says about speaking more than one language.",
  [("Галимнәр фикеренчә, ике тел белгән балалар мәсьәләләрне тизрәк чишә.", "According to scientists, children who know two languages solve problems faster."), ("Яңа тел өйрәнү хәтерне ныгыта һәм кешене картлыкта да актив итә.", "Learning a new language strengthens memory and keeps people active even in old age."),
   ("Иң мөһиме — көн саен азрак булса да шөгыльләнү.", "The most important thing is to practise every day, even if only a little."), ("Тел өйрәнгәндә хаталардан курыкмаска кирәк, чөнки алар безне өйрәтә.", "When learning a language you shouldn't fear mistakes, because they teach us."),
   ("Кем татар телен белә, ул башка төрки телләрне дә җиңел аңлый.", "Whoever knows Tatar easily understands other Turkic languages too.")],
  [("What do bilingual children do faster?", ["Read", "Solve problems", "Run", "Sleep"], 1),
   ("What does learning a language strengthen?", ["Memory", "Muscles", "Eyesight", "Hearing"], 0),
   ("What is most important?", ["Expensive courses", "Travelling abroad", "Practising every day", "Learning grammar first"], 2),
   ("Why shouldn't you fear mistakes?", ["Nobody notices them", "They are rare", "Teachers ignore them", "They teach us"], 3)])
R(106, "Bolgar", "Болгар", "An ancient city on the Volga.",
  [("Болгар шәһәре Идел буенда, Казаннан көньякка таба урнашкан.", "The town of Bolgar lies on the Volga, to the south of Kazan."), ("Унынчы гасырда биредә Идел Болгарстаны дәүләте ислам динен кабул иткән.", "In the tenth century the state of Volga Bulgaria adopted Islam here."),
   ("Борынгы шәһәрнең таш биналары һәм манаралары әле дә сакланган.", "The ancient city's stone buildings and minarets survive to this day."), ("Ике мең уникенче елда Болгар ЮНЕСКОның Бөтендөнья мирасы исемлегенә кертелгән.", "In 2012 Bolgar was added to UNESCO's World Heritage list."),
   ("Ел саен анда меңләгән туристлар һәм зиярәтчеләр килә.", "Every year thousands of tourists and pilgrims come there.")],
  [("Where is Bolgar?", ["North of Kazan", "On the Volga, south of Kazan", "In the mountains", "On the Kama, east of Kazan"], 1),
   ("What happened there in the tenth century?", ["Islam was adopted", "The city was destroyed", "A university opened", "Kazan was founded"], 0),
   ("What has survived?", ["Wooden houses", "Nothing", "Stone buildings and minarets", "Only coins"], 2),
   ("What happened in 2012?", ["A new mosque was built", "A festival began", "Tourists stopped coming", "It joined UNESCO's World Heritage list"], 3)])
R(107, "Tea Culture", "Чәй мәдәнияте", "Tea as a sign of hospitality.",
  [("Татарлар өчен чәй — гади эчемлек кенә түгел, ә кунакчыллык билгесе.", "For Tatars tea is not just a drink but a sign of hospitality."), ("Кунак килсә, өстәлгә шунда ук самавыр, бал, чәкчәк һәм бавырсак куела.", "When a guest arrives, the samovar, honey, chak-chak and baursak go on the table at once."),
   ("Чәйне гадәттә сөт белән эчәләр.", "Tea is usually drunk with milk."), ("Хуҗабикә кунакның чынаягын беркайчан да буш калдырмый.", "The hostess never leaves a guest's cup empty."),
   ("Кунак җитәрлек эчкәч, чынаягын каплап куя яки рәхмәт әйтә.", "When the guest has had enough, he covers his cup or says thank you.")],
  [("What is tea for Tatars?", ["Medicine", "A sign of hospitality", "Only a breakfast drink", "A drink for children"], 1),
   ("How is tea usually drunk?", ["With milk", "With lemon", "Cold", "Without anything"], 0),
   ("What does the hostess never do?", ["Serve honey", "Sit down", "Leave a guest's cup empty", "Use a samovar"], 2),
   ("How does a guest show he has had enough?", ["He leaves", "He stands up", "He asks for coffee", "He covers his cup or says thank you"], 3)])
R(108, "The Hardest Years", "Иң авыр еллар", "A family's memories of the war.",
  [("Бабам сугыш башланганда унсигез яшьлек егет булган.", "When the war began, my grandfather was an eighteen-year-old lad."), ("Ул фронтка киткән, ә авылда хатын-кызлар һәм балалар гына калган.", "He went to the front, and only women and children were left in the village."),
   ("Әбием сөйләвенчә, алар көне-төне кырда эшләгәннәр.", "According to my grandmother, they worked in the fields day and night."), ("Ипи җитмәгән, шуңа күрә бәрәңге һәм үлән белән тукланганнар.", "There wasn't enough bread, so they lived on potatoes and wild herbs."),
   ("Бабам мең тугыз йөз кырык бишенче елда, яраланып булса да, исән кайткан.", "My grandfather came home alive in 1945, though wounded.")],
  [("How old was the grandfather when the war began?", ["Sixteen", "Eighteen", "Twenty", "Twenty-five"], 1),
   ("Who stayed in the village?", ["Women and children", "Only old men", "Soldiers", "Nobody"], 0),
   ("What did people eat?", ["Meat and fish", "Bread and honey", "Potatoes and wild herbs", "Only porridge"], 2),
   ("What happened to the grandfather?", ["He never came back", "He stayed in the army", "He moved to Moscow", "He came back alive though wounded"], 3)])
R(109, "Ecology in the City", "Шәһәрдә экология", "Cars, pollution and what people are doing about it.",
  [("Безнең шәһәрдә соңгы елларда машиналар саны бик артты.", "In our city the number of cars has grown a lot in recent years."), ("Шуның аркасында һава пычрана, кешеләр ешрак авырый башлады.", "Because of this the air is getting dirtier, and people have started falling ill more often."),
   ("Шәһәр хакимияте яңа велосипед юллары төзергә карар кылды.", "The city authorities decided to build new cycle lanes."), ("Мәктәп укучылары да чүп җыю һәм агач утырту акцияләрендә катнаша.", "School pupils also take part in litter-picking and tree-planting campaigns."),
   ("Табигатьне саклау — һәрберебезнең бурычы.", "Protecting nature is the duty of each of us.")],
  [("What has increased in the city?", ["The number of trees", "The number of cars", "The number of parks", "The number of schools"], 1),
   ("What is the result?", ["Polluted air and more illness", "Cleaner streets", "Cheaper petrol", "Fewer accidents"], 0),
   ("What did the authorities decide to build?", ["New roads", "A new airport", "Cycle lanes", "Car parks"], 2),
   ("What do pupils do?", ["Wash cars", "Build roads", "Sell bicycles", "Pick litter and plant trees"], 3)])
R(110, "A Letter to a Friend", "Дуска хат", "News from home for a friend far away.",
  [("Кадерле дустым Әлфия!", "My dear friend Alfiya!"), ("Синең хатыңны алып бик шатландым, мин аны озак көттем.", "I was so glad to get your letter; I'd been waiting for it for a long time."),
   ("Бездә барысы да әйбәт: мин яңа эшкә урнаштым, ә энем университетка керде.", "All is well here: I've started a new job, and my younger brother has got into university."), ("Җәен Казанга кайтсаң, мин сине Иске татар бистәсенә алып барырмын.", "If you come back to Kazan in summer, I'll take you to the Old Tatar Quarter."),
   ("Сине бик сагындым, хатыңны түземсезлек белән көтәм.", "I miss you very much and can't wait for your next letter.")],
  [("How did the writer feel about Alfiya's letter?", ["Surprised", "Very glad", "Worried", "Indifferent"], 1),
   ("What news is there about the younger brother?", ["He got into university", "He got married", "He found a job", "He moved abroad"], 0),
   ("Where will the writer take Alfiya?", ["To the Kremlin", "To a village", "To the Old Tatar Quarter", "To the theatre"], 2),
   ("How does the letter end?", ["With a complaint", "With an invitation to a wedding", "With a request for money", "Saying the writer misses her"], 3)])
c.save()
