# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("b2plus", "b2plus-reading")
R = c.R
R(101, "The Syuyumbike Tower", "Сөембикә манарасы", "A leaning tower and its legend.",
  [("Казан Кремлендә җиде катлы бер манара басып тора, аны Сөембикә манарасы дип йөртәләр.", "In the Kazan Kremlin stands a seven-storey tower known as the Syuyumbike Tower."), ("Сөембикә — Казан ханлыгының соңгы ханбикәләренең берсе.", "Syuyumbike was one of the last queens of the Kazan Khanate."),
   ("Риваять буенча, ул шәһәрне калдырырга теләмичә, манараның иң югары катыннан ташланган.", "According to legend, unwilling to leave the city, she threw herself from the top storey of the tower."), ("Тарихчылар исә ханбикәнең Мәскәүгә алып кителгәнен һәм шунда вафат булганын язалар.", "Historians, however, write that the queen was taken to Moscow and died there."),
   ("Манара бераз авышкан, һәм бүгенге көндә ул Казанның иң танылган символларыннан санала.", "The tower leans slightly, and today it is considered one of Kazan's best-known symbols.")],
  [("How many storeys does the tower have?", ["Five", "Seven", "Nine", "Three"], 1),
   ("Who was Syuyumbike?", ["A queen of the Kazan Khanate", "A poet", "An architect", "A Russian princess"], 0),
   ("What do historians say happened to her?", ["She jumped from the tower", "She became a nun", "She was taken to Moscow and died there", "She ruled for fifty years"], 2),
   ("What is special about the tower today?", ["It is the tallest in Russia", "It is made of wood", "It is closed to everyone", "It leans and is a symbol of Kazan"], 3)])
R(102, "Musa Jalil", "Муса Җәлил", "A poet whose verses survived a prison cell.",
  [("Муса Җәлил — татарның күренекле шагыйре һәм Советлар Союзы Герое.", "Musa Jalil is a prominent Tatar poet and a Hero of the Soviet Union."), ("Бөек Ватан сугышы вакытында ул яраланып, әсирлеккә эләккән.", "During the Second World War he was wounded and taken prisoner."),
   ("Берлиндагы Моабит төрмәсендә ул кечкенә дәфтәрләргә шигырьләр язып калдырган.", "In Moabit prison in Berlin he wrote poems in small notebooks."), ("Шагыйрь мең тугыз йөз кырык дүртенче елда җәзалап үтерелгән, ләкин аның дәфтәрләре туган иленә кайткан.", "The poet was executed in 1944, but his notebooks found their way back to his homeland."),
   ("Моабит дәфтәрләре бүген дә дистәләгән телләрдә укыла.", "The Moabit Notebooks are still read today in dozens of languages.")],
  [("What happened to Jalil during the war?", ["He became a general", "He was wounded and captured", "He emigrated", "He worked in a factory"], 1),
   ("Where did he write his last poems?", ["In Moabit prison in Berlin", "In Kazan", "In a hospital", "At the front"], 0),
   ("What happened to the notebooks?", ["They were burned", "They were lost forever", "They came back to his homeland", "They were sold"], 2),
   ("How are the Moabit Notebooks known today?", ["Only in Tatar", "Only to historians", "They are forbidden", "They are read in dozens of languages"], 3)])
R(103, "Three Alphabets", "Өч әлифба", "How the Tatar script changed in one century.",
  [("Гасырлар буе татарлар гарәп хәрефләре белән язганнар.", "For centuries the Tatars wrote in Arabic letters."), ("Мең тугыз йөз егерме җиденче елда гарәп язуы латин әлифбасы белән алмаштырылган.", "In 1927 the Arabic script was replaced by the Latin alphabet."),
   ("Ун елдан соң исә татар теле кириллицага күчерелгән.", "Ten years later, the Tatar language was moved to Cyrillic."), ("Шуңа күрә бер гаиләдә дә әби, ана һәм балалар төрле язуларда укырга өйрәнгән булырга мөмкин.", "As a result, grandmother, mother and children in the same family may have learned to read in different scripts."),
   ("Бүген дә кайбер галимнәр латин язуына кайту турында бәхәсләшә.", "Even today some scholars debate returning to the Latin script.")],
  [("What script did Tatars use for centuries?", ["Latin", "Arabic", "Cyrillic", "Greek"], 1),
   ("What happened in 1927?", ["Arabic was replaced by Latin", "Cyrillic was introduced", "Tatar was banned", "A dictionary was printed"], 0),
   ("Which script is used now?", ["Arabic", "Latin", "Cyrillic", "Runic"], 2),
   ("What do some scholars still discuss?", ["Banning Tatar", "Inventing a new script", "Returning to Arabic", "Returning to Latin"], 3)])
R(104, "Shurale", "Шүрәле", "The forest spirit of Tatar folklore.",
  [("Татар халык әкиятләрендә Шүрәле исемле урман иясе бар.", "In Tatar folk tales there is a forest spirit called Shurale."), ("Аның озын бармаклары бар, һәм ул урманга кергән кешеләрне кытыклап үтерә ала, имеш.", "He has long fingers and, they say, can tickle people who enter the forest to death."),
   ("Тукайның шигырендә бер егет Шүрәлене хәйлә белән алдый.", "In Tukay's poem a young man tricks Shurale with cunning."), ("Ул Шүрәленең бармакларын бүрәнә ярыгына кыстыра да качып китә.", "He traps Shurale's fingers in a split log and runs away."),
   ("Бу әкият буенча куелган Шүрәле балеты бүген дә Казан театрында бара.", "The ballet Shurale, based on this tale, is still performed at the Kazan theatre today.")],
  [("Who is Shurale?", ["A king", "A forest spirit", "A river fish", "A hero"], 1),
   ("What is dangerous about him?", ["He tickles people to death", "He steals horses", "He burns houses", "He floods villages"], 0),
   ("How does the young man escape?", ["He fights him", "He runs very fast", "He traps his fingers in a split log", "He gives him gold"], 2),
   ("What was made from the tale?", ["A film", "A novel", "A song", "A ballet"], 3)])
R(105, "Tatars Around the World", "Дөньядагы татарлар", "A people spread across many countries.",
  [("Татарларның яртысыннан азрагы гына Татарстанда яши.", "Fewer than half of all Tatars live in Tatarstan."), ("Калганнары Россиянең башка төбәкләрендә, Казахстанда, Үзбәкстанда, Төркиядә һәм Финляндиядә көн итә.", "The rest live in other regions of Russia, in Kazakhstan, Uzbekistan, Turkey and Finland."),
   ("Финляндия татарлары йөз еллардан артык үз телләрен һәм гореф-гадәтләрен саклап килә.", "The Tatars of Finland have preserved their language and customs for over a hundred years."), ("Биш елга бер тапкыр Казанда Бөтендөнья татар конгрессы җыела.", "Once every five years the World Congress of Tatars meets in Kazan."),
   ("Анда төрле илләрдән килгән делегатлар милли мәдәниятне саклау юлларын тикшерә.", "There, delegates from different countries discuss ways of preserving the national culture.")],
  [("Where do most Tatars live?", ["In Tatarstan", "Outside Tatarstan", "In Finland", "In Turkey"], 1),
   ("What have Finnish Tatars preserved?", ["Their language and customs", "Their ancient script", "Their farms", "Their kings"], 0),
   ("How often does the World Congress of Tatars meet?", ["Every year", "Every ten years", "Once every five years", "Only once"], 2),
   ("What do the delegates discuss?", ["Trade deals", "Sports", "Tourism prices", "Preserving the national culture"], 3)])
R(106, "The Volga", "Идел", "Europe's longest river and its place in Tatar life.",
  [("Идел — Аурупадагы иң озын елга.", "The Volga is the longest river in Europe."), ("Кама елгасы аңа Казаннан көньякта кушыла.", "The Kama River joins it south of Kazan."),
   ("Борынгы заманнардан бирле Идел буе халыклары өчен ул сәүдә юлы булып хезмәт иткән.", "Since ancient times it has served as a trade route for the peoples of the Volga region."), ("Татар җырларында Идел еш кына туган илнең, сагынуның символы булып тора.", "In Tatar songs the Volga is often a symbol of the homeland and of longing."),
   ("Хәзер елгада сусаклагычлар бар, һәм аның экологиясе галимнәрне борчый.", "Today there are reservoirs on the river, and its ecology worries scientists.")],
  [("What is special about the Volga?", ["It is the deepest river", "It is the longest river in Europe", "It flows into the Baltic", "It never freezes"], 1),
   ("Which river joins it near Kazan?", ["The Kama", "The Don", "The Ural", "The Oka"], 0),
   ("What did the Volga serve as in ancient times?", ["A border", "A fortress", "A trade route", "A holy site"], 2),
   ("What worries scientists today?", ["Floods", "Too many tourists", "Its length", "Its ecology"], 3)])
R(107, "Chak-Chak", "Чәкчәк", "A sweet that belongs at every celebration.",
  [("Чәкчәк — татар табынының иң танылган тәм-томы.", "Chak-chak is the best-known sweet on a Tatar table."), ("Аны камырдан ясалган кечкенә кисәкләрне майда кыздырып, аннары бал белән бутап әзерлиләр.", "It is made by frying small pieces of dough in oil and then mixing them with honey."),
   ("Борынгы гадәт буенча, кәләш кияү йортына чәкчәк алып килергә тиеш булган.", "By old custom, a bride was expected to bring chak-chak to the groom's house."), ("Чәкчәкнең тәме хуҗабикәнең осталыгын күрсәткән.", "The taste of the chak-chak showed the skill of the housewife."),
   ("Хәзер аны кибетләрдә дә сатып алып була, ләкин өйдә пешергәне тәмлерәк, диләр.", "Now you can buy it in shops too, but people say homemade is tastier.")],
  [("What is chak-chak?", ["A soup", "A sweet", "A drink", "A bread"], 1),
   ("How is it made?", ["Fried dough mixed with honey", "Baked meat pie", "Boiled rice with sugar", "Frozen milk"], 0),
   ("Who traditionally brought chak-chak to the groom's house?", ["The groom's mother", "The guests", "The bride", "The mullah"], 2),
   ("What do people say about homemade chak-chak?", ["It is too sweet", "It is cheaper", "It is hard to make", "It is tastier"], 3)])
R(108, "Kazan University", "Казан университеты", "One of Russia's oldest universities.",
  [("Казан университеты мең сигез йөз дүртенче елда ачылган.", "Kazan University was founded in 1804."), ("Ул Россиянең иң борынгы университетларының берсе санала.", "It is considered one of the oldest universities in Russia."),
   ("Монда атаклы математик Лобачевский укыган һәм озак еллар ректор булып эшләгән.", "The famous mathematician Lobachevsky studied here and served as rector for many years."), ("Университетта шулай ук Лев Толстой һәм Владимир Ульянов белем алган.", "Leo Tolstoy and Vladimir Ulyanov also studied at the university."),
   ("Бүгенге көндә анда илледән артык илдән килгән студентлар укый.", "Today students from more than fifty countries study there.")],
  [("When was the university founded?", ["In 1904", "In 1804", "In 1704", "In 1854"], 1),
   ("Who was rector for many years?", ["Lobachevsky", "Tolstoy", "Tukay", "Ulyanov"], 0),
   ("Which writer studied there?", ["Pushkin", "Gogol", "Leo Tolstoy", "Chekhov"], 2),
   ("Who studies there today?", ["Only Tatars", "Only Russians", "Only men", "Students from over fifty countries"], 3)])
R(109, "Tatar Names", "Татар исемнәре", "What names tell us about a family.",
  [("Татар исемнәренең күбесе гарәп, фарсы һәм төрки чыгышлы.", "Most Tatar names are of Arabic, Persian or Turkic origin."), ("Мәсәлән, Айгөл исеме ай һәм гөл сүзләреннән торган.", "For example, the name Aygul is made up of the words moon and flower."),
   ("Элек балага исемне мулла кушкан, һәм бу йола исем туе дип аталган.", "In the past the mullah named the child, and this ceremony was called the naming feast."), ("Совет елларында күп гаиләләр балаларына рус исемнәре биргән.", "In Soviet years many families gave their children Russian names."),
   ("Соңгы вакытта исә борынгы татар исемнәре яңадан популярлашты.", "Recently, however, old Tatar names have become popular again.")],
  [("What origin are most Tatar names?", ["Greek and Latin", "Arabic, Persian or Turkic", "Russian", "Mongolian"], 1),
   ("What does the name Aygul consist of?", ["Moon and flower", "Sun and sky", "Snow and rose", "Star and river"], 0),
   ("Who named the child in the past?", ["The grandmother", "The father", "The mullah", "The teacher"], 2),
   ("What is happening with old Tatar names now?", ["They are banned", "They are forgotten", "They are changed to Russian", "They are popular again"], 3)])
R(110, "A Village Spring", "Авыл чишмәсе", "Springs as the heart of village life.",
  [("Һәр татар авылында диярлек чишмә бар.", "Almost every Tatar village has a spring."), ("Элек хатын-кызлар чишмәгә көянтә белән су алырга төшкән.", "In the past women went down to the spring with a yoke to fetch water."),
   ("Анда яшьләр очрашкан, яңалыклар белән уртаклашкан.", "Young people met there and shared news."), ("Халыкта, чишмәне пычраткан кешегә бәхет булмый, дигән ышаныч бар.", "There is a folk belief that a person who pollutes a spring will have no luck."),
   ("Бүгенге көндә авыл халкы чишмәләрне чистарта, аларны бизәп куя.", "Today villagers clean their springs and decorate them.")],
  [("What does almost every village have?", ["A castle", "A spring", "A school", "A theatre"], 1),
   ("How did women carry water?", ["With a yoke", "In a cart", "In a car", "On horseback"], 0),
   ("What did young people do at the spring?", ["Washed clothes", "Studied", "Met and shared news", "Fished"], 2),
   ("What do villagers do today?", ["Fill in the springs", "Sell the water", "Build factories near them", "Clean and decorate them"], 3)])
c.save()
