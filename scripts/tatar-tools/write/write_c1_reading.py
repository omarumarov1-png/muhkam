# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("c1", "c1-reading")
R = c.R
R(101, "The Fall of Kazan", "Казанның алынуы", "The siege of 1552 and its place in memory.",
  [("Мең биш йөз илле икенче елның көзендә Иван Грозный гаскәрләре Казанны камап алган.", "In the autumn of 1552 the troops of Ivan the Terrible laid siege to Kazan."), ("Шәһәр берничә атна буе каршылык күрсәткән, ләкин ахыр чиктә стеналар астына куелган дары шартлаган.", "The city resisted for several weeks, but in the end gunpowder placed under the walls exploded."),
   ("Шәһәрне яклаучыларның күбесе һәлак булган, ә Кол Шәриф мәдрәсәсенең шәкертләре соңгы сулышка кадәр сугышкан.", "Most of the city's defenders were killed, and the students of the Qol Sharif madrasa fought to their last breath."), ("Казан ханлыгының бетүе Идел буе тарихында яңа чор башлаган.", "The end of the Kazan Khanate began a new era in the history of the Volga region."),
   ("Бүген бу вакыйга татар халкының хәтерендә фаҗига һәм батырлык символы буларак саклана.", "Today this event lives on in the memory of the Tatar people as a symbol of tragedy and heroism.")],
  [("When was Kazan besieged?", ["In 1452", "In the autumn of 1552", "In the spring of 1612", "In 1812"], 1),
   ("What finally broke the defence?", ["Gunpowder exploded under the walls", "Hunger", "A traitor opened the gates", "A flood"], 0),
   ("Who fought to the last breath?", ["The khan's guards", "Foreign soldiers", "The students of the Qol Sharif madrasa", "The merchants"], 2),
   ("How is the event remembered today?", ["As a celebration", "It is forgotten", "As a trade agreement", "As a symbol of tragedy and heroism"], 3)])
R(102, "Kayum Nasyri", "Каюм Насыйри", "A scholar who wrote for ordinary people.",
  [("Каюм Насыйри — унтугызынчы гасырда яшәгән татар галиме, мәгърифәтчесе һәм язучысы.", "Kayum Nasyri was a nineteenth-century Tatar scholar, enlightener and writer."), ("Ул беренчеләрдән булып фәнни китапларны гади халык аңлаешлы телдә язарга омтылган.", "He was one of the first to try to write scientific books in language ordinary people could understand."),
   ("Аның календарьлары, сүзлекләре һәм дәреслекләре татар авылларында киң таралган.", "His calendars, dictionaries and textbooks spread widely in Tatar villages."), ("Насыйри халык авыз иҗатын да җыйган, мәкальләрне һәм әкиятләрне язып алган.", "Nasyri also collected folklore, writing down proverbs and fairy tales."),
   ("Аны хаклы рәвештә хәзерге татар әдәби теленә нигез салучыларның берсе дип саныйлар.", "He is rightly considered one of the founders of the modern Tatar literary language.")],
  [("When did Kayum Nasyri live?", ["In the eighteenth century", "In the nineteenth century", "In the twentieth century", "In the sixteenth century"], 1),
   ("What did he try to do?", ["Write science for ordinary people", "Translate the Quran", "Write only poetry", "Found a political party"], 0),
   ("What else did he collect?", ["Coins", "Paintings", "Proverbs and fairy tales", "Old weapons"], 2),
   ("How is he regarded today?", ["As a forgotten writer", "As a foreign scholar", "As a politician", "As a founder of the modern literary language"], 3)])
R(103, "The New Method", "Яңа ысул", "The Jadid movement and the reform of schooling.",
  [("Унтугызынчы гасыр ахырында татар мәдрәсәләрендә укыту иске ысул белән барган.", "At the end of the nineteenth century teaching in Tatar madrasas was carried out by the old method."), ("Шәкертләр гарәп текстларын еллар буе яттан өйрәнгәннәр, ләкин мәгънәсен аңламаганнар.", "Students learned Arabic texts by heart for years without understanding their meaning."),
   ("Җәдитчеләр исә авазлы ысулны кертеп, балаларны тиз генә укырга һәм язарга өйрәтә башлаганнар.", "The Jadids introduced the phonetic method and began teaching children to read and write quickly."), ("Яңа мәктәпләрдә дини фәннәр белән бергә география, тарих, математика да укытылган.", "In the new schools geography, history and mathematics were taught alongside religious subjects."),
   ("Бу хәрәкәт бөтен төрки дөньяга йогынты ясаган һәм яңа зыялылар буынын тәрбияләгән.", "This movement influenced the whole Turkic world and raised a new generation of intellectuals.")],
  [("What was the problem with the old method?", ["It was too expensive", "Students memorised texts without understanding them", "There were no teachers", "It was only for girls"], 1),
   ("What did the Jadids introduce?", ["The phonetic method", "Military training", "Latin lessons", "Boarding schools"], 0),
   ("What was taught in the new schools?", ["Only religion", "Only languages", "Religion plus geography, history and maths", "Only crafts"], 2),
   ("What was the wider effect?", ["Schools closed", "It stayed in Kazan only", "Nothing changed", "It influenced the whole Turkic world"], 3)])
R(104, "Five Notes", "Биш аваз", "Why Tatar melodies sound the way they do.",
  [("Татар халык көйләре биш авазлы гаммага нигезләнгән.", "Tatar folk melodies are based on a five-note (pentatonic) scale."), ("Шуңа күрә алар Европа музыкасына күнеккән колакка моңлы һәм бераз сәер булып ишетелә.", "That's why they sound melancholy and a little strange to an ear used to European music."),
   ("Татарлар бу хисне моң сүзе белән атыйлар, һәм аны башка телгә тәрҗемә итү бик кыен.", "Tatars call this feeling moñ, and it is very hard to translate into another language."), ("Борынгы озын көйләрне башкару өчен җырчыдан аеруча киң тын һәм зур осталык таләп ителә.", "Performing the old 'long songs' demands especially deep breath and great skill from the singer."),
   ("Салих Сәйдәшев кебек композиторлар халык көйләрен классик музыка белән берләштергән.", "Composers such as Salikh Saydashev combined folk melodies with classical music.")],
  [("What are Tatar folk melodies based on?", ["A seven-note scale", "A five-note scale", "Church music", "Jazz"], 1),
   ("How do they sound to a European ear?", ["Melancholy and a little strange", "Fast and cheerful", "Exactly like European music", "Very loud"], 0),
   ("What is moñ?", ["A musical instrument", "A dance", "A feeling expressed in the melodies", "A composer"], 2),
   ("What did Saydashev do?", ["Banned folk songs", "Wrote only operas in Italian", "Collected fairy tales", "Combined folk melodies with classical music"], 3)])
R(105, "The Tale of Yusuf", "Йосыф кыйссасы", "A medieval poem and its long life.",
  [("Кол Гали унөченче гасырда Йосыф кыйссасы поэмасын язган.", "In the thirteenth century Qol Ghali wrote the poem The Tale of Yusuf."), ("Поэманың сюжеты Коръәндәге Йосыф пәйгамбәр турындагы хикәягә нигезләнгән.", "The plot of the poem is based on the Quranic story of the prophet Yusuf."),
   ("Анда абыйлары тарафыннан коега ташланган егетнең Мисырда хөкемдар булуы сурәтләнә.", "It describes how a young man thrown into a well by his brothers becomes a ruler in Egypt."), ("Гасырлар буе бу әсәр татар гаиләләрендә кычкырып укылган һәм кулдан күчереп язылган.", "For centuries this work was read aloud in Tatar families and copied out by hand."),
   ("Галимнәр аны Идел буе төркиләренең иң борынгы әдәби истәлекләреннән берсе дип саный.", "Scholars consider it one of the oldest literary monuments of the Volga Turks.")],
  [("When was the poem written?", ["In the nineteenth century", "In the thirteenth century", "In the tenth century", "In the twentieth century"], 1),
   ("What is the plot based on?", ["The Quranic story of Yusuf", "A Russian legend", "A Greek myth", "The author's own life"], 0),
   ("What happens to the young man?", ["He becomes a poet", "He dies in the well", "He becomes a ruler in Egypt", "He returns to his village"], 2),
   ("How was the poem preserved?", ["Only in a museum", "On stone tablets", "In a single printed copy", "Read aloud and copied by hand in families"], 3)])
R(106, "Two Languages", "Ике тел", "Bilingualism in Tatarstan today.",
  [("Татарстанда ике дәүләт теле бар: татар һәм рус телләре.", "Tatarstan has two state languages: Tatar and Russian."), ("Шәһәрләрдә күпчелек кеше көндәлек тормышта русча сөйләшә, ә авылларда татар теле ешрак яңгырый.", "In the towns most people speak Russian in daily life, while in villages Tatar is heard more often."),
   ("Соңгы елларда мәктәпләрдә татар телен укыту сәгатьләре кыскартылды, һәм бу җәмгыятьтә бәхәсләр тудырды.", "In recent years the hours for teaching Tatar in schools were cut, and this sparked debate in society."), ("Шул ук вакытта интернетта татарча сайтлар һәм мобиль кушымталар саны арта.", "At the same time the number of Tatar websites and mobile apps on the internet is growing."),
   ("Күп белгечләр телнең киләчәге гаиләдә сөйләшүгә бәйле дип саный.", "Many specialists believe the language's future depends on it being spoken in the family.")],
  [("How many state languages does Tatarstan have?", ["One", "Two", "Three", "Four"], 1),
   ("Where is Tatar heard more often?", ["In villages", "In towns", "In offices", "On television"], 0),
   ("What caused debate?", ["New Tatar websites", "A new alphabet", "Cuts to Tatar lessons in schools", "Tourism"], 2),
   ("What do specialists see as key to the language's future?", ["Laws", "Television", "Schools only", "Speaking it in the family"], 3)])
R(107, "Wedding Customs", "Туй йолалары", "How a traditional Tatar wedding unfolded.",
  [("Элек татар туе берничә көн дәвам иткән һәм үзенең катлаулы йолалары белән аерылып торган.", "In the past a Tatar wedding lasted several days and was distinguished by its elaborate customs."), ("Иң элек кияү ягыннан яучылар килеп, кызның әти-әнисе белән сөйләшкән.", "First, matchmakers came from the groom's side to talk with the girl's parents."),
   ("Килешкәннән соң кияү кәләш өчен калым түләгән, ә кыз ягы бирнә әзерләгән.", "Once they had agreed, the groom paid a bride price, and the girl's side prepared a dowry."), ("Никах укылганнан соң яшьләр берничә ай аерым яшәгән, кияү кәләшкә кунакка гына йөргән.", "After the nikah was read, the young couple lived apart for several months, the groom only visiting the bride."),
   ("Хәзер туйлар кыскарак, ләкин никах уку һәм чәкчәк кебек гадәтләр һаман саклана.", "Today weddings are shorter, but customs such as reading the nikah and chak-chak are still kept.")],
  [("How long did a traditional wedding last?", ["One evening", "Several days", "A month", "A whole year"], 1),
   ("Who came first to the girl's parents?", ["Matchmakers from the groom's side", "The mullah", "The groom alone", "The bride's friends"], 0),
   ("What did the girl's side prepare?", ["A bride price", "A house", "A dowry", "A horse"], 2),
   ("What is still kept today?", ["Living apart for months", "The bride price", "Week-long feasts", "The nikah and chak-chak"], 3)])
R(108, "Nardugan", "Нардуган", "A winter festival rediscovered.",
  [("Нардуган — кыш уртасында, көннәр озая башлагач үткәрелә торган борынгы бәйрәм.", "Nardugan is an ancient festival held in midwinter, when the days begin to lengthen."), ("Бу көннәрдә яшьләр битлек киеп, өйдән-өйгә йөргән һәм җырлап, бииләр булган.", "On these days young people put on masks, went from house to house, sang and danced."),
   ("Хуҗалар аларны тәмле ризыклар белән сыйлаган, чөнки кунакны кире кагу бәхетсезлеккә дип саналган.", "The hosts treated them to tasty food, because turning guests away was thought to bring bad luck."), ("Кызлар киләчәк кияүләрен белер өчен төрле юраулар ясаганнар.", "Girls practised various kinds of fortune-telling to learn who their future husbands would be."),
   ("Совет чорында онытылган бу бәйрәмне соңгы елларда кайбер авылларда яңадан торгыза башладылар.", "Forgotten in the Soviet period, the festival has in recent years begun to be revived in some villages.")],
  [("When is Nardugan held?", ["In early spring", "In midwinter", "At harvest", "In midsummer"], 1),
   ("What did young people do?", ["Went from house to house in masks, singing and dancing", "Went to the mosque", "Worked in the fields", "Stayed at home"], 0),
   ("Why did hosts treat the visitors?", ["They were paid", "It was the law", "Turning guests away brought bad luck", "The guests were relatives"], 2),
   ("What is happening to the festival now?", ["It is banned", "It became a state holiday", "It moved to Moscow", "It is being revived in some villages"], 3)])
R(109, "The Qol Sharif Mosque", "Кол Шәриф мәчете", "A mosque rebuilt after four and a half centuries.",
  [("Казан Кремлендә урнашкан Кол Шәриф мәчете ике мең бишенче елда ачылган.", "The Qol Sharif Mosque in the Kazan Kremlin opened in 2005."), ("Ул мең биш йөз илле икенче елда җимерелгән борынгы мәчетнең истәлегенә төзелгән.", "It was built in memory of the ancient mosque destroyed in 1552."),
   ("Мәчеткә шәһәрне яклап һәлак булган имам Кол Шәриф исеме бирелгән.", "The mosque was named after Imam Qol Sharif, who died defending the city."), ("Аны төзү өчен бөтен республикадан һәм чит илләрдән кешеләр иганә җыйган.", "People from all over the republic and from abroad collected donations to build it."),
   ("Хәзер ул гыйбадәт кылу урыны гына түгел, ә музей һәм шәһәрнең иң танылган биналарының берсе.", "Today it is not only a place of worship but also a museum and one of the city's best-known buildings.")],
  [("When did the mosque open?", ["In 1995", "In 2005", "In 2015", "In 1552"], 1),
   ("What does it commemorate?", ["The ancient mosque destroyed in 1552", "A royal wedding", "The founding of Kazan", "A victory in battle"], 0),
   ("Who was Qol Sharif?", ["An architect", "A khan", "An imam who died defending the city", "A merchant"], 2),
   ("How was its construction funded?", ["By a single rich man", "By a bank loan", "By ticket sales", "By donations from many people"], 3)])
R(110, "Language in the Digital Age", "Санлы заманда тел", "Can a minority language thrive online?",
  [("Бүгенге яшьләр көненең зур өлешен телефон экраны каршында үткәрә.", "Young people today spend a large part of their day in front of a phone screen."), ("Әгәр анда туган телдә кызыклы эчтәлек булмаса, алар аны башка телдә эзлиләр.", "If there's no interesting content in their native language there, they look for it in another language."),
   ("Шуңа күрә соңгы елларда татарча блоглар, видеоуеннар һәм тавыш ярдәмчеләре барлыкка килә башлады.", "That's why Tatar blogs, video games and voice assistants have begun to appear in recent years."), ("Кайбер галимнәр, ясалма интеллект кечкенә телләрне саклап калырга ярдәм итәр, дип өметләнә.", "Some scholars hope artificial intelligence will help preserve small languages."),
   ("Әмма теләсә нинди технология дә кешеләрнең үз телләрендә сөйләшү теләген алыштыра алмый.", "But no technology can replace people's own desire to speak their language.")],
  [("Where do young people spend much of their day?", ["In libraries", "In front of a phone screen", "In sports clubs", "Outdoors"], 1),
   ("What happens if there's no native-language content?", ["They look for it in another language", "They stop using phones", "They create it themselves", "They complain to the government"], 0),
   ("What has appeared recently?", ["New schools", "A new alphabet", "Tatar blogs, games and voice assistants", "Tatar television channels"], 2),
   ("What can't technology replace?", ["Teachers", "Books", "Dictionaries", "People's desire to speak their language"], 3)])
c.save()
