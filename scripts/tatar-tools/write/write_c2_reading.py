# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("c2", "c2-reading")
R = c.R
R(101, "The Golden Horde", "Алтын Урда", "An empire on the lower Volga and its legacy.",
  [("Алтын Урда унөченче гасырда Бату хан тарафыннан нигезләнгән һәм тиз арада Евразиянең иң куәтле дәүләтләренең берсенә әверелгән.", "The Golden Horde was founded by Batu Khan in the thirteenth century and soon became one of the most powerful states in Eurasia."), ("Аның башкаласы Сарай шәһәре Иделнең түбән агымында урнашкан булган һәм Көнчыгыш белән Көнбатыш арасындагы сәүдә юлларын тоташтырган.", "Its capital, Sarai, lay on the lower Volga and linked the trade routes between East and West."),
   ("Үзбәк хан идарә иткән чорда ислам дәүләт дине итеп игълан ителгән, бу исә мәдәният һәм язма әдәбият үсешенә этәргеч биргән.", "Under Uzbek Khan, Islam was proclaimed the state religion, which gave a push to the development of culture and written literature."), ("Унбишенче гасырда эчке низаглар нәтиҗәсендә дәүләт таркалып, аның урынында Казан, Кырым, Әстерхан кебек ханлыклар барлыкка килгән.", "In the fifteenth century the state broke apart as a result of internal strife, and khanates such as Kazan, Crimea and Astrakhan arose in its place."),
   ("Бүгенге татар тарихчылары Алтын Урданы халкыбызның дәүләтчелек тәҗрибәсендә мөһим баскыч дип саный.", "Today's Tatar historians regard the Golden Horde as an important stage in our people's experience of statehood.")],
  [("Who founded the Golden Horde?", ["Uzbek Khan", "Batu Khan", "Ivan the Terrible", "Edigu"], 1),
   ("Where was Sarai?", ["On the lower Volga", "In Crimea", "On the Kama", "In Siberia"], 0),
   ("What happened under Uzbek Khan?", ["The capital moved to Kazan", "The state collapsed", "Islam became the state religion", "Trade routes closed"], 2),
   ("What arose after the Horde broke apart?", ["A single kingdom", "A republic", "Nothing", "Khanates such as Kazan, Crimea and Astrakhan"], 3)])
R(102, "The Script Debate", "Язу турындагы бәхәс", "Why Tatarstan's switch to Latin letters was halted.",
  [("Мең тугыз йөз туксан тугызынчы елда Татарстан Дәүләт Советы татар телен латин графикасына күчерү турында закон кабул иткән.", "In 1999 the State Council of Tatarstan passed a law moving the Tatar language to the Latin script."), ("Яклаучылар латин хәрефләренең татар авазларын төгәлрәк бирүен һәм төрки дөнья белән элемтәне ныгытуын әйткәннәр.", "Supporters argued that Latin letters render Tatar sounds more accurately and strengthen ties with the Turkic world."),
   ("Әмма ике мең икенче елда федераль закон Россиядәге барлык дәүләт телләре өчен кириллицаны мәҗбүри итеп куйган.", "But in 2002 a federal law made Cyrillic compulsory for all the state languages of Russia."), ("Татарстанның моңа каршы шикаяте Конституция мәхкәмәсендә каралган, ләкин аны кире каккан.", "Tatarstan's challenge to this was heard in the Constitutional Court, but rejected."),
   ("Шул вакыттан бирле латин язуы рәсми булмаса да, кайбер сайтларда һәм шәхси хат алышуда кулланыла.", "Since then the Latin script, though not official, has been used on some websites and in private correspondence.")],
  [("What did the 1999 law decide?", ["To ban Tatar", "To move Tatar to the Latin script", "To return to Arabic", "To make Russian the only language"], 1),
   ("What did supporters argue?", ["Latin renders Tatar sounds more accurately", "Latin is cheaper", "Cyrillic is too old", "Nobody reads Cyrillic"], 0),
   ("What did the 2002 federal law require?", ["Latin for all languages", "Arabic for religious texts", "Cyrillic for all state languages", "Two alphabets in schools"], 2),
   ("Where is the Latin script used today?", ["In all schools", "In official documents", "On banknotes", "On some websites and in private letters"], 3)])
R(103, "The First Tatar Theatre", "Беренче татар театры", "How a professional stage was born in 1906.",
  [("Беренче рәсми татар спектакле мең тугыз йөз алтынчы елның декабрендә Казанда куелган.", "The first official Tatar play was staged in Kazan in December 1906."), ("Ул вакытта күп кенә руханилар театрны гөнаһлы шөгыль дип санаган, шуңа күрә артистларга җәмгыять каршылыгын җиңәргә туры килгән.", "At that time many clergy considered theatre a sinful pastime, so the actors had to overcome society's opposition."),
   ("Хатын-кыз рольләрен башта ирләр башкарган, чөнки хатын-кызның сәхнәгә чыгуы оят дип исәпләнгән.", "At first men played the women's roles, because it was considered shameful for a woman to appear on stage."), ("Галиәсгар Камал кебек драматурглар татар тормышын үткен юмор һәм тирән кызгану белән сурәтләгәннәр.", "Playwrights such as Galiaskar Kamal portrayed Tatar life with sharp humour and deep compassion."),
   ("Бүген Камал исемендәге академия театры татар сәхнә сәнгатенең үзәге булып тора.", "Today the Kamal Academic Theatre is the centre of Tatar stage art.")],
  [("When was the first official Tatar play staged?", ["In 1856", "In December 1906", "In 1917", "In 1926"], 1),
   ("Why did actors face opposition?", ["Many clergy considered theatre sinful", "Tickets were too expensive", "There were no buildings", "The government banned it"], 0),
   ("Who played women's roles at first?", ["Children", "Russian actresses", "Men", "Nobody — there were no female roles"], 2),
   ("How did Galiaskar Kamal portray Tatar life?", ["Only tragically", "As a fairy tale", "Without humour", "With sharp humour and deep compassion"], 3)])
R(104, "Shihabuddin Marjani", "Шиһабетдин Мәрҗани", "A theologian who rewrote Tatar history.",
  [("Шиһабетдин Мәрҗани — унтугызынчы гасырның иң күренекле татар галиме, тарихчысы һәм дин белгече.", "Shihabuddin Marjani was the most prominent Tatar scholar, historian and theologian of the nineteenth century."), ("Ул Бохарада һәм Сәмәркандта озак еллар укыган, ләкин анда өйрәтелгән коры схоластиканы тәнкыйтьләгән.", "He studied for many years in Bukhara and Samarkand, but criticised the dry scholasticism taught there."),
   ("Мәрҗани мөселманнарны Коръәнне һәм хәдисләрне үз акылы белән аңларга, сукыр ияреп барудан баш тартырга чакырган.", "Marjani called on Muslims to understand the Quran and hadith with their own reason and to reject blind imitation."), ("Тарихи хезмәтләрендә ул казан татарларының Идел буе болгарларыннан килүен исбатларга омтылган.", "In his historical works he sought to prove that the Kazan Tatars descend from the Volga Bulgars."),
   ("Аның карашлары соңрак җәдитчелек хәрәкәтенә нигез булып хезмәт иткән.", "His views later served as a foundation for the Jadid movement.")],
  [("What was Marjani?", ["A poet and singer", "A scholar, historian and theologian", "A khan", "A merchant"], 1),
   ("What did he criticise?", ["Dry scholasticism", "Theatre", "Russian schools", "Trade"], 0),
   ("What did he call on Muslims to do?", ["Stop reading", "Leave Russia", "Understand scripture with their own reason", "Study only Arabic"], 2),
   ("What did his views later inspire?", ["The Golden Horde", "The Soviet state", "The script reform", "The Jadid movement"], 3)])
R(105, "The Epic of Edigu", "Идегәй дастаны", "A hero shared by many Turkic peoples.",
  [("Идегәй — Алтын Урдада ундүртенче гасыр ахырында яшәгән тарихи шәхес, көчле әмир.", "Edigu was a historical figure, a powerful emir, who lived in the Golden Horde at the end of the fourteenth century."),
   ("Аның турында дастан татарлар, башкортлар, казахлар һәм нугайлар арасында гасырлар буе телдән-телгә күчеп сакланган.", "The epic about him has been preserved for centuries, passed from mouth to mouth among Tatars, Bashkirs, Kazakhs and Nogais."),
   ("Дастанда Идегәй Туктамыш ханның золымына каршы чыккан гаделлек өчен көрәшүче итеп сурәтләнә.", "In the epic, Edigu is depicted as a fighter for justice who rose up against Tokhtamysh Khan's tyranny."), ("Әсәрдә шигъри өлешләр чәчмә аралаш килә, һәм аны махсус җырчылар башкарган.", "In the work, verse passages alternate with prose, and it was performed by special singers."),
   ("Совет чорында дастан берникадәр вакыт тыелган, ләкин хәзер ул татар әдәбиятының алтын фондына кертелгән.", "In the Soviet period the epic was banned for a while, but it is now part of the golden treasury of Tatar literature.")],
  [("Who was Edigu?", ["A poet", "A powerful emir of the Golden Horde", "A Russian prince", "A merchant"], 1),
   ("How was the epic preserved?", ["Passed on orally for centuries", "In a single manuscript", "Carved in stone", "In Russian chronicles"], 0),
   ("Whom did Edigu oppose in the epic?", ["Batu Khan", "Ivan the Terrible", "Tokhtamysh Khan", "Timur"], 2),
   ("What happened to the epic in Soviet times?", ["It became a film", "It was translated widely", "It was taught in schools", "It was banned for a while"], 3)])
R(106, "The Birth of the Tatar Press", "Татар матбугатының тууы", "The newspapers that followed 1905.",
  [("Мең тугыз йөз бишенче елгы революциядән соң татарларга үз телләрендә газета-журналлар чыгарырга рөхсәт ителгән.", "After the revolution of 1905, Tatars were permitted to publish newspapers and magazines in their own language."), ("Берничә ел эчендә Казанда, Оренбургта, Уфада һәм Петербургта дистәләгән басмалар дөнья күргән.", "Within a few years dozens of publications appeared in Kazan, Orenburg, Ufa and St Petersburg."),
   ("Аларның битләрендә мәгариф, хатын-кыз хокуклары, дин һәм сәясәт турында кызу бәхәсләр барган.", "Their pages hosted heated debates about education, women's rights, religion and politics."), ("Ризаэддин Фәхретдин мөхәррирлегендә Оренбургта чыккан Шура журналы аеруча зур абруй казанган.", "The journal Shura, published in Orenburg under the editorship of Rizaeddin Fakhreddin, earned particularly great prestige."),
   ("Тукай да үзенең шигырьләрен һәм публицистик мәкаләләрен нәкъ менә шул чор матбугатында бастырган.", "Tukay too published his poems and essays in exactly this period's press.")],
  [("What changed after 1905?", ["Tatar was banned", "Tatars could publish in their own language", "Kazan became a capital", "Schools closed"], 1),
   ("Where did publications appear?", ["In Kazan, Orenburg, Ufa and St Petersburg", "Only in Moscow", "Only abroad", "Only in villages"], 0),
   ("Who edited Shura?", ["Tukay", "Marjani", "Rizaeddin Fakhreddin", "Kayum Nasyri"], 2),
   ("What did Tukay publish in this press?", ["Only translations", "Novels", "Plays", "Poems and essays"], 3)])
R(107, "Mukhlisa Bubi", "Мөхлисә Буби", "A woman judge in 1917.",
  [("Мөхлисә Буби — татар мәгърифәтчесе, хатын-кызлар өчен мәктәпләр ачкан педагог.", "Mukhlisa Bubi was a Tatar enlightener and educator who opened schools for women."), ("Ул Иж-Буби авылында туган, анда абыйлары белән бергә мәшһүр мәдрәсәдә укыткан.", "She was born in the village of Izh-Bobya, where she taught with her brothers at a famous madrasa."),
   ("Мең тугыз йөз унҗиденче елда ул Уфадагы Диния нәзарәтенә казый итеп сайланган.", "In 1917 she was elected a qadi, a judge, of the Spiritual Administration in Ufa."), ("Бу вакыйга ул заманда мөселман дөньясында хатын-кызның шундый вазифа биләве өчен бик сирәк очрак булган.", "At that time this was a very rare case in the Muslim world of a woman holding such a post."),
   ("Совет хакимияте чорында ул репрессиягә эләккән, һәм аның исеме озак еллар онытылып торган.", "Under Soviet rule she fell victim to repression, and her name was forgotten for many years.")],
  [("What did Mukhlisa Bubi do as an educator?", ["She wrote novels", "She opened schools for women", "She ran a newspaper", "She founded a theatre"], 1),
   ("Where did she teach with her brothers?", ["At the madrasa in Izh-Bobya", "In Moscow", "In Bukhara", "At Kazan University"], 0),
   ("What position was she elected to in 1917?", ["Mayor", "Mufti", "Qadi (judge)", "Member of parliament"], 2),
   ("What happened to her under Soviet rule?", ["She became a minister", "She emigrated to Turkey", "She was given awards", "She was repressed and forgotten"], 3)])
R(108, "Language and Identity", "Тел һәм үзаң", "An essay on what a language carries.",
  [("Тел — аралашу коралы гына түгел, ул халыкның дөньяга карашын, хәтерен һәм хисләрен үзендә саклый.", "Language is not just a means of communication; it holds a people's worldview, memory and feelings."), ("Мәсәлән, татарча моң яки сагыш сүзләрен башка телгә төгәл тәрҗемә итү мөмкин түгел диярлек.", "For example, it is almost impossible to translate Tatar words like moñ or sağış exactly into another language."),
   ("Телне югалткан халык, тышкы яктан исән калса да, үзенең эчке йөзен акрынлап онытырга мөмкин.", "A people that loses its language, even if it survives outwardly, may gradually forget its inner face."), ("Шуңа күрә күп кенә галимнәр тел саклауны кешелекнең уртак бурычы дип саный.", "That is why many scholars consider preserving languages a shared duty of humanity."),
   ("Әмма бу бурычны канун гына түгел, ә һәр гаиләдәге көндәлек сөйләм генә үти ала.", "But this duty can be fulfilled not by law alone, but only by everyday speech in every family.")],
  [("What, according to the essay, does a language hold?", ["Only grammar", "A people's worldview, memory and feelings", "Only words", "Laws"], 1),
   ("What example of untranslatable words is given?", ["Moñ and sağış", "Bread and salt", "Mother and father", "Sun and moon"], 0),
   ("What may happen to a people that loses its language?", ["It becomes richer", "Nothing", "It may forget its inner face", "It gets a new homeland"], 2),
   ("What can truly fulfil the duty of preserving a language?", ["Laws alone", "Scholars", "Television", "Everyday speech in every family"], 3)])
R(109, "The Village and the City", "Авыл һәм шәһәр", "A reflection on a disappearing way of life.",
  [("Егерменче гасыр башында татарларның күпчелеге авылларда яшәгән, бүген исә хәл киресенчә.", "At the start of the twentieth century most Tatars lived in villages; today it's the other way round."), ("Авыл гасырлар буе телнең, йолаларның һәм халык иҗатының табигый сакчысы булып торган.", "For centuries the village was the natural guardian of the language, customs and folk art."),
   ("Шәһәрдә исә кеше күбрәк мөмкинлекләр ала, ләкин еш кына тамырларыннан аерыла.", "In the city a person gains more opportunities, but is often cut off from his roots."), ("Кайбер язучылар бу күчешне фаҗига итеп сурәтли, икенчеләр аны котылгысыз үсеш дип кабул итә.", "Some writers portray this shift as a tragedy, while others accept it as inevitable progress."),
   ("Мөгаен, хакыйкать урталыкта: шәһәрдә дә авыл рухын саклап калырга мөмкин.", "Perhaps the truth lies in between: one can keep the spirit of the village even in the city.")],
  [("Where did most Tatars live in the early twentieth century?", ["In cities", "In villages", "Abroad", "In Kazan"], 1),
   ("What role did the village play?", ["Guardian of language, customs and folk art", "Centre of industry", "Seat of government", "Place of exile"], 0),
   ("What is the downside of city life, according to the text?", ["Fewer opportunities", "Bad weather", "Being cut off from one's roots", "High prices"], 2),
   ("What conclusion does the text suggest?", ["Everyone should return to villages", "Villages are useless", "Cities are a tragedy", "The village spirit can be kept even in the city"], 3)])
R(110, "Heritage", "Мирас", "What one generation owes the next.",
  [("Һәр буын үзеннән соң нәрсәдер калдыра: йортлар, китаплар, җырлар, гореф-гадәтләр.", "Every generation leaves something behind: houses, books, songs, customs."), ("Ләкин иң кыйммәтле мирас — ул күзгә күренми торган әйберләр: тел, хәтер, намус төшенчәләре.", "But the most precious heritage is invisible: language, memory, notions of honour."),
   ("Бабаларыбыз авыр сынауларны үткәндә дә балаларына белем бирергә, аларны кеше итәргә тырышканнар.", "Even while going through severe trials, our ancestors strove to educate their children and raise them as decent people."), ("Безнең бурыч — алардан калганны саклау гына түгел, ә аны баету һәм киләсе буынга тапшыру.", "Our duty is not only to preserve what they left, but to enrich it and hand it on to the next generation."),
   ("Халык мәкале әйтмешли, агачны үстерергә илле ел, кисәргә биш минут кирәк.", "As the folk proverb says, it takes fifty years to grow a tree and five minutes to cut it down.")],
  [("What does every generation leave behind?", ["Only money", "Houses, books, songs and customs", "Nothing", "Only debts"], 1),
   ("What is the most precious heritage?", ["Invisible things like language and memory", "Gold", "Land", "Buildings"], 0),
   ("What did the ancestors strive to do?", ["Become rich", "Leave the country", "Educate their children and raise them well", "Build palaces"], 2),
   ("What is our duty, according to the text?", ["To forget the past", "To sell the heritage", "Only to preserve it", "To preserve, enrich and pass it on"], 3)])
c.save()
