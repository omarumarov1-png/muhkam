# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("c2", "c2-reading")
R = c.R
R(48, "Abai", "Абай", "The national poet and his Words of Edification.",
  [("Абай Құнанбаев мың сегіз жүз қырық бесінші жылы Семей өңірінде дүниеге келген.", "Abai Kunanbaev was born in 1845 in the Semey region."), ("Ол жас кезінен шығыс ақындарын оқып, кейін орыс және еуропа әдебиетімен танысты.", "From his youth he read the poets of the East, and later became acquainted with Russian and European literature."),
   ("Абай Пушкин мен Крыловтың шығармаларын қазақ тіліне аударды.", "Abai translated the works of Pushkin and Krylov into Kazakh."), ("Оның Қара сөздері халықты еңбекке, білімге және адалдыққа шақырады.", "His Words of Edification call the people to work, learning and honesty."),
   ("Бүгінде Абайдың өлеңдері мен әндерін әрбір қазақ біледі.", "Today every Kazakh knows Abai's poems and songs.")],
  [("Where was Abai born?", ["In Almaty", "In the Semey region", "In Moscow", "In Turkestan"], 1),
   ("Whose works did he translate?", ["Pushkin's and Krylov's", "Tolstoy's", "Shakespeare's", "Goethe's"], 0),
   ("What do his Words of Edification call for?", ["War", "Wealth", "Work, learning and honesty", "Travel"], 2),
   ("Who knows his poems today?", ["Only scholars", "Only children", "Nobody", "Every Kazakh"], 3)])
R(49, "Nauryz", "Наурыз", "The spring festival of renewal.",
  [("Наурыз — көктемнің және жаңа жылдың мерекесі.", "Nauryz is the festival of spring and the new year."), ("Оны жиырма екінші наурызда, күн мен түн теңелген кезде тойлайды.", "It is celebrated on the twenty-second of March, when day and night are equal."),
   ("Бұл күні әр үйде жеті түрлі дәмнен наурыз көже әзірлейді.", "On this day every home prepares nauryz kozhe from seven ingredients."), ("Адамдар бір-біріне жақсы тілек айтып, ескі өкпелерін кешіреді.", "People wish each other well and forgive old grudges."),
   ("Кешке қалалар мен ауылдарда ән, күй және ойындар болады.", "In the evening there are songs, music and games in the towns and villages.")],
  [("What does Nauryz celebrate?", ["Harvest", "Spring and the new year", "Independence", "A wedding"], 1),
   ("When is it celebrated?", ["On the twenty-second of March", "On the first of January", "In autumn", "In June"], 0),
   ("How many ingredients go into nauryz kozhe?", ["Three", "Five", "Seven", "Ten"], 2),
   ("What do people forgive?", ["Debts", "Nothing", "Taxes", "Old grudges"], 3)])
R(50, "The Yurt", "Киіз үй", "The home of the nomads.",
  [("Киіз үй — көшпелі қазақтардың ғасырлар бойы тұрған баспанасы.", "The yurt is the dwelling the nomadic Kazakhs lived in for centuries."), ("Оның ағаш қаңқасы кереге, уық және шаңырақтан тұрады.", "Its wooden frame consists of the lattice walls, the roof poles and the shanyrak."),
   ("Қаңқаның сыртын қалың киізбен жабады, сондықтан ішінде қыста жылы, жазда салқын.", "The frame is covered with thick felt, so inside it is warm in winter and cool in summer."), ("Киіз үйді бір-екі сағатта жинап, түйеге артып, басқа жерге көшіруге болады.", "A yurt can be taken down in an hour or two, loaded onto a camel and moved elsewhere."),
   ("Шаңырақ отбасының бірлігін білдіреді, ол Қазақстанның елтаңбасында да бейнеленген.", "The shanyrak symbolises the unity of the family, and it also appears on the coat of arms of Kazakhstan.")],
  [("Who lived in yurts?", ["City merchants", "Nomadic Kazakhs", "Soldiers only", "Fishermen"], 1),
   ("What covers the frame?", ["Thick felt", "Wooden boards", "Stone", "Cloth only"], 0),
   ("How long does it take to take down a yurt?", ["A week", "A day", "An hour or two", "A month"], 2),
   ("What does the shanyrak symbolise?", ["Wealth", "War", "The sky", "The unity of the family"], 3)])
R(51, "The Dombra and the Kuy", "Домбыра мен күй", "The two-stringed voice of the steppe.",
  [("Домбыра — қазақтың ең танымал екі ішекті музыкалық аспабы.", "The dombra is the best-known two-stringed Kazakh musical instrument."), ("Домбырамен орындалатын аспаптық шығарманы күй деп атайды.", "An instrumental piece played on the dombra is called a kuy."),
   ("Әрбір күйдің артында бір оқиға немесе аңыз жатады.", "Behind every kuy lies a story or a legend."), ("Құрманғазының Сарыарқа күйі даланың кеңдігін бейнелейді.", "Kurmangazy's kuy Saryarka depicts the vastness of the steppe."),
   ("Бүгінде жастар домбыраны рок және поп музыкасында да қолданады.", "Today young people use the dombra in rock and pop music too.")],
  [("How many strings does the dombra have?", ["One", "Two", "Three", "Four"], 1),
   ("What is a kuy?", ["An instrumental piece", "A dance", "A poem", "A drum"], 0),
   ("What lies behind every kuy?", ["A prayer", "A recipe", "A story or legend", "A law"], 2),
   ("What does Saryarka depict?", ["A battle", "A wedding", "A river", "The vastness of the steppe"], 3)])
R(52, "The Aral Sea", "Арал теңізі", "A sea that shrank and is slowly returning.",
  [("Бір кездері Арал теңізі әлемдегі ең үлкен көлдердің бірі болған.", "The Aral Sea was once one of the largest lakes in the world."), ("Өткен ғасырдың алпысыншы жылдарынан бастап өзендердің суы егістікті суаруға жұмсалды.", "From the sixties of the last century, the rivers' water was used to irrigate fields."),
   ("Нәтиже ауыр болды: теңіз тартылып, балықшылар жұмыссыз қалды.", "The result was severe: the sea shrank and the fishermen were left without work."), ("Кейін солтүстік бөлігінде бөгет салынып, су деңгейі қайта көтерілді.", "Later a dam was built in the northern part, and the water level rose again."),
   ("Бүгін ол жерге балық қайтып оралды, бұл үлкен үміт береді.", "Today fish have returned there, which gives great hope.")],
  [("What was the Aral Sea once?", ["A small pond", "One of the largest lakes in the world", "A river", "A desert"], 1),
   ("What was the rivers' water used for?", ["Irrigating fields", "Drinking only", "Factories", "Shipping"], 0),
   ("What happened to the fishermen?", ["They became rich", "They moved to the city to study", "They were left without work", "Nothing"], 2),
   ("What was built in the northern part?", ["A port", "A bridge", "A factory", "A dam"], 3)])
R(53, "Al-Farabi", "Әл-Фараби", "The 'Second Teacher' from Otrar.",
  [("Әбу Насыр әл-Фараби Отырар қаласында туған ұлы ойшыл.", "Abu Nasr al-Farabi was a great thinker born in the city of Otrar."), ("Ол философия, математика, музыка және тіл туралы көптеген еңбек жазған.", "He wrote many works on philosophy, mathematics, music and language."),
   ("Шығыс ғалымдары оны Аристотельден кейінгі екінші ұстаз деп атаған.", "Eastern scholars called him the Second Teacher, after Aristotle."), ("Әл-Фараби бақытқа білім мен ізгілік арқылы жетуге болады деп санаған.", "Al-Farabi believed that happiness can be reached through knowledge and virtue."),
   ("Қазақстанның ең ірі университеттерінің бірі оның есімімен аталады.", "One of the largest universities in Kazakhstan bears his name.")],
  [("Where was al-Farabi born?", ["In Baghdad", "In Otrar", "In Samarkand", "In Almaty"], 1),
   ("What was he called?", ["The Second Teacher", "The Great Khan", "The Poet of the Steppe", "The Father of Medicine"], 0),
   ("How, in his view, can happiness be reached?", ["Through wealth", "Through war", "Through knowledge and virtue", "Through travel"], 2),
   ("What bears his name today?", ["A mountain", "A river", "A city", "A large university"], 3)])
R(54, "Hospitality", "Қонақ күту", "The guest in Kazakh tradition.",
  [("Қазақ халқы ерте заманнан қонақты құрметтеуімен белгілі.", "Since ancient times the Kazakh people have been known for honouring their guests."), ("Қонақ келсе, құт келер, дейді халық.", "When a guest comes, good fortune comes, the people say."),
   ("Қонақты дастарханның төріне отырғызып, ең жақсы тағамды ұсынады.", "The guest is seated at the place of honour at the dastarkhan and offered the best food."), ("Бешбармақ дайындалғанда, қойдың басын ең құрметті қонаққа тартады.", "When beshbarmak is prepared, the sheep's head is served to the most honoured guest."),
   ("Қонақ кетерде үй иелері оған бата беріп, жолына сәттілік тілейді.", "When the guest leaves, the hosts give him a blessing and wish him a good journey.")],
  [("What are Kazakhs known for?", ["Their ships", "Their hospitality", "Their mountains", "Their factories"], 1),
   ("What comes with a guest, according to the saying?", ["Good fortune", "Trouble", "Rain", "Debt"], 0),
   ("Who is served the sheep's head?", ["The youngest child", "The cook", "The most honoured guest", "The host"], 2),
   ("What do the hosts do when the guest leaves?", ["Close the door quickly", "Ask for payment", "Say nothing", "Give a blessing and wish a good journey"], 3)])
R(55, "Shokan Ualikhanov", "Шоқан Уәлиханов", "A scholar who lived only thirty years.",
  [("Шоқан Уәлиханов — қазақтың алғашқы ғалымы және саяхатшысы.", "Shokan Ualikhanov was the first Kazakh scholar and traveller."), ("Ол Омбыдағы кадет корпусында оқып, бірнеше тілді меңгерді.", "He studied at the cadet corps in Omsk and mastered several languages."),
   ("Жас кезінде ол жасырын түрде Шығыс Түркістанға барып, оның тарихын зерттеді.", "As a young man he travelled in secret to East Turkestan (Kashgar) and studied its history."), ("Шоқан Манас жырының бір бөлігін алғаш рет қағазға түсірді.", "Shokan was the first to write down part of the Manas epic."),
   ("Ол небәрі отыз жыл өмір сүрсе де, ғылымда терең із қалдырды.", "Although he lived only thirty years, he left a deep mark on scholarship.")],
  [("Who was Shokan Ualikhanov?", ["A khan", "The first Kazakh scholar and traveller", "A poet", "A general"], 1),
   ("Where did he study?", ["At the cadet corps in Omsk", "In Paris", "In Bukhara", "At home"], 0),
   ("Where did he travel in secret?", ["Moscow", "Tashkent", "East Turkestan", "Istanbul"], 2),
   ("What did he write down for the first time?", ["The Quran", "A dictionary", "A law code", "Part of the Manas epic"], 3)])
R(56, "Baikonur", "Байқоңыр", "The steppe that launched the first man into space.",
  [("Байқоңыр — Қазақстанның даласында орналасқан әлемдегі ең алғашқы ғарыш айлағы.", "Baikonur, located on the steppe of Kazakhstan, is the world's first spaceport."), ("Мың тоғыз жүз алпыс бірінші жылы осы жерден Юрий Гагарин ғарышқа ұшты.", "In 1961 Yuri Gagarin flew into space from here."),
   ("Қазақтың тұңғыш ғарышкері Тоқтар Әубәкіров те Байқоңырдан ұшқан.", "The first Kazakh cosmonaut, Toktar Aubakirov, also flew from Baikonur."), ("Бүгінде мұнда ғарыш кемелері мен жүк зымырандары жиі ұшырылады.", "Today spacecraft and cargo rockets are often launched from here."),
   ("Ғарыш айлағының маңындағы қалада мұражай бар, оған туристер көп келеді.", "The town near the spaceport has a museum that many tourists visit.")],
  [("What is Baikonur?", ["A lake", "The world's first spaceport", "A mountain", "A university"], 1),
   ("Who flew into space from Baikonur in 1961?", ["Yuri Gagarin", "Neil Armstrong", "Abai", "Al-Farabi"], 0),
   ("Who was the first Kazakh cosmonaut?", ["Shokan Ualikhanov", "Kurmangazy", "Toktar Aubakirov", "Abai Kunanbaev"], 2),
   ("What is near the spaceport?", ["A sea", "A desert palace", "A forest", "A town with a museum"], 3)])
R(57, "The Blessing", "Бата", "Words that send a person on their way.",
  [("Бата — қазақтың ежелгі дәстүрлерінің бірі.", "The bata, or blessing, is one of the ancient Kazakh traditions."), ("Үлкендер жастарға жолға шығарда, үйленгенде немесе дастарқан басында бата береді.", "Elders give the young a blessing when they set off on a journey, when they marry, or at the table."),
   ("Батада денсаулық, бақыт, ұзақ өмір және ел тыныштығы тіленеді.", "A blessing asks for health, happiness, long life and peace for the people."), ("Халық ақ батаны ең қымбат сыйлықтан да жоғары бағалаған.", "The people valued a sincere blessing above even the most precious gift."),
   ("Бата алған адам үлкендердің сеніміне ие болды деп саналады.", "A person who has received a blessing is considered to have earned the elders' trust.")],
  [("What is a bata?", ["A song", "A blessing", "A dish", "A game"], 1),
   ("Who gives the blessing?", ["Elders", "Children", "Strangers", "Teachers only"], 0),
   ("What does a blessing ask for?", ["Victory in war", "Money", "Health, happiness, long life and peace", "Rain"], 2),
   ("How did the people value a sincere blessing?", ["Less than money", "As unimportant", "As a formality", "Above the most precious gift"], 3)])
c.save()
