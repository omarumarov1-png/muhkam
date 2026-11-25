# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("c2", "c2")
T = c.T
T("c2-gov", "Official and Ceremonial Language", "… теләктәшлегендә · … кысаларында · … тарафыннан · тәбрик итәм · … телим",
  "Government reports and public speeches form their own register. Titles are given in full (Татарстан Республикасы Президенты), events are framed with postpositions (Президент теләктәшлегендә — with the support of the President; программа кысаларында — within the programme), and the passive dominates (уздырыла, тапшырылды, расланган). "
  "Ceremonial greetings follow fixed patterns: Сезне … белән чын күңелдән тәбрик итәм, and wishes in -сын (булсын, сөендерсен) or with телим.",
  "Official Tatar coins many terms by translating Russian ones (күрсәткеч — indicator, хакимият — administration), so knowing both languages helps with news Tatar.",
  [("A", "Утырышны кем алып барды?", "Who chaired the meeting?"), ("B", "Татарстан Республикасы Премьер-министры.", "The Prime Minister of the Republic of Tatarstan."), ("A", "Нинди карар кабул ителде?", "What decision was adopted?"), ("B", "Программа бертавыштан хупланды.", "The programme was approved unanimously.")])
T("c2-faith", "Faith, Ethics and Tradition", "Аллаһы Тәгалә · гамәл · нигъмәт · игелек · фарыз",
  "Religious and ethical texts use a rich Arabic-origin vocabulary: гамәл (deed), нигъмәт (blessing), игелек (good deed), фарыз (obligatory), гыйлем (knowledge), мәрхәмәт (mercy). "
  "Exhortations use the first person plural optative (күркәм гамәлләр кылыйк — let us do fine deeds) and blessings use -сын. Abstract nouns in -лык/-лек carry moral ideas: гаделлек, җаваплылык, шәфкатьлелек.",
  "Many Tatar ethical terms are shared with Turkish, Persian and Arabic, which makes this register the most international part of the vocabulary.",
  [("A", "Бу айда нәрсәгә игътибар итәргә кирәк?", "What should we pay attention to this month?"), ("B", "Игелекле гамәлләр кылырга, бер-беребезгә шәфкать күрсәтергә.", "To do good deeds and show mercy to one another."), ("A", "Аллаһ кабул итсен.", "May God accept it.")])
T("c2-lit", "Literary Criticism and Scholarship", "иҗади мирас · … өлкәсенә карый · сурәтләнә · тәгаенләнә · гротеск",
  "Writing about literature at this level piles up participles, verb nouns and abstract terms: Габдулла Гомәрнең иҗади мирасы башлыча әдәби тәрҗемә өлкәсенә карый — Gabdulla Gumar's creative legacy lies mainly in literary translation. "
  "Critics hedge and evaluate with фикеремчә, … дигән тәэсир кала (one is left with the impression that…), and describe technique with verbs like тәгаенләнә (becomes definite), гәүдәләнә (is embodied) and күпертелә (is exaggerated).",
  "Tatar literary scholarship is centred at the Galimjan Ibragimov Institute of Language, Literature and Art in Kazan.",
  [("A", "Бу романның төп кимчелеге нәрсәдә, синеңчә?", "What do you think is this novel's main weakness?"), ("B", "Геройлар тамашачының симпатиясен казана алмый.", "The characters can't win the reader's sympathy."), ("A", "Ә теле?", "And its language?"), ("B", "Теле бай, ләкин бераз күпертелгән дигән тәэсир кала.", "The language is rich, but one is left with the impression it's a little overblown.")])
T("c2-soc", "Social Commentary", "кызганыч ки · мисал китерәм · … дәрәҗәсендә · кагыйдә буларак",
  "Opinion journalism mixes formal structures with emotional comment: Кызганыч ки… (sadly…), Тагын бер мисал гына китерәм (I'll give just one more example), … юк дәрәҗәсендә (almost non-existent). "
  "Rhetorical questions are a favourite device: Кайчан безнең Сабантуй шундый үрнәк булып торганы бар?! — When has our Sabantuy ever been such an example?!",
  "Tatar commentators often frame social problems in terms of the nation's survival: language, birth rate, and the village.",
  [("A", "Мәдәнияткә мөнәсәбәт үзгәрдеме?", "Has the attitude to culture changed?"), ("B", "Кызганыч ки, күпләр аңа примитив нәрсә итеп карый.", "Sadly, many treat it as something primitive."), ("A", "Моның сәбәбе нәрсәдә?", "What's the reason?"), ("B", "Бәлки, мәгариф системасындадыр.", "Perhaps the education system.")])
T("c2-hist", "History and Memory", "… гасырда · … нәтиҗәсендә · бәйнә-бәйнә · инкыйраз",
  "Historical writing alternates between the narrative present (Хан Болгар капкасыннан чыгып кача) and the -ган past for reported facts (Кыпчаклар шул дәүләтнең көнбатыш тармагын тәшкил иткәннәр). "
  "Look out for formal vocabulary: инкыйраз (decline), бәйнә-бәйнә (in detail), сынаулар (trials), мирас (heritage), and the construction … өчен бурычлы (owing it to…).",
  "The Tatar national narrative links the Volga Bulgars, the Golden Horde and the Kazan Khanate as successive stages of one history.",
  [("A", "Тарихны ничек дөрес язарга?", "How should history be written truthfully?"), ("B", "Бөтен вакыйгаларны бер китапта бәйнә-бәйнә ачып булмый.", "You can't reveal every event in detail in one book."), ("A", "Димәк, күп китап кирәк.", "So many books are needed."), ("B", "Әйе, һәм күп буын галимнәр.", "Yes, and many generations of scholars.")])
T("c2-tale", "Epic and Tale Style", "… алып · … белән · ни күзе белән күрсен · кырык · җиде",
  "Epic narratives (дастаннар) such as Alpamysh use heightened, formulaic language: numbers like forty and seven, chains of converbs (алып, төяп, саубуллашып), and dramatic hyperbole: алтмыш колачлы алтын тирәк — a golden poplar sixty fathoms high. "
  "Direct speech is ceremonious and often rhythmic: Малыңа тимим, шәһәреңне ватмыйм, гаскәреңне кырмыйм, миңа кызыңны гына бир.",
  "The epic Alpamysh is shared by many Turkic peoples; the Tatar and Bashkir versions are close relatives of the Uzbek and Kazakh ones.",
  [("A", "Алпамша кайтканын халык ничек белә?", "How do the people know Alpamysh has returned?"), ("B", "Ул мылтыгын күтәреп ата.", "He raises his gun and fires."), ("A", "Аннары нәрсә була?", "And then what happens?"), ("B", "Дошманнары куркып кача.", "His enemies flee in fear.")])
T("c2-life", "Reflection and Nuance", "… дигән тәэсир · кайвакыт · … белән бергә · бәлки",
  "At C2 you meet the full range of nuance: concession (Теләк булу беләнмени… — as if wanting were enough…), irony (Менә үзен мактаган чагында мактанырга яратмавы хакында да әйтмәсә), and compressed metaphor (Еллар бер-беренә ялганып гомер боҗрасын тәшкил итәләр). "
  "Read for the speaker's attitude as much as for the literal meaning.",
  "Tatar essayists love images from nature — rivers, trees, birds — to talk about time and human life.",
  [("A", "Гомер нәрсә ул, синеңчә?", "What is a lifetime, in your view?"), ("B", "Еллар бер-беренә ялганып ясаган боҗра.", "A ring made of years joined to one another."), ("A", "Матур әйттең.", "Beautifully put."), ("B", "Шагыйрьләрдән өйрәндем.", "I learned it from the poets.")])
L = c.L
S = [
('c2-gov', [
    ('Әмма бүгенгә кадәр суд карарлары гамәлгә ашырылмаган.', 'But to this day the court rulings have not been carried out.'),
    ('Без шундый талантлы яшьләребез булу белән горурланабыз.', 'We are proud to have such talented young people.'),
    ('Ихластан татарстанлыларны Корбан гаете белән тәбрик итәм.', 'I sincerely congratulate the people of Tatarstan on Eid al-Adha.'),
    ('Без милләтебезнең киләчәгенә якты өметләр белән карыйбыз.', 'We look to the future of our nation with bright hopes.'),
]),
('c2-faith', [
    ('Галәмнәрнең Бөек Серләре ачкычы Коръән Хәкимдә саклана.', 'The key to the Great Secrets of the worlds is kept in the Wise Quran.'),
    ('Шулай да әбекәй диннән аерылмаган, намазларын калдырмаган.', 'Even so, the old woman did not abandon her faith and did not miss her prayers.'),
    ('Коръәнне укырга өйрәтә торган китап озакламый дөнья күрәчәк.', 'A book that teaches how to read the Quran will soon be published.'),
    ('Әгәр кеше кушылган көннәрдә корбан чалып өлгермәсә нишләргә?', "What should a person do if he doesn't manage to make the sacrifice on the prescribed days?"),
]),
('c2-lit', [
    ('Китапның әлеге гаиләгә ничек килеп эләккәне билгесез.', 'How the book came into this family is unknown.'),
    ('Татар халкының инкыйраз юлына атлаганын шагыйрь күрде.', 'The poet saw that the Tatar people had set foot on the road to decline.'),
    ('Мөхәммәдъяр дәрвиш кыяфәтендә ерак сәфәргә чыгып китә.', 'Muhammadyar sets off on a long journey disguised as a dervish.'),
    ('Нәбирә ханым халык тарихының тирән катламнарына төшми.', "Mrs Nabira doesn't go down into the deep layers of the people's history."),
]),
('c2-soc', [
    ('Сессияләр арасында өстәмә белем аларга мөмкинлек бирә.', 'Additional education between sessions gives them the opportunity.'),
    ('Аеруча аны Бердәм дәүләт имтиханнары мәсьәләсе борчый.', 'He is especially worried about the Unified State Exams.'),
    ('Проблемалар күп, аларны чишәргә теләүчеләр генә күренми.', "There are many problems; it's just that nobody seems to want to solve them."),
    ('Культурага примитив карашның тагын бер мисалын гына китерәм.', "I'll give just one more example of a primitive attitude to culture."),
]),
('c2-hist', [
    ('Әмма крепость капкасын өч-дүрт көнгә кадәр ачмадылар.', "But they didn't open the fortress gate for three or four days."),
    ('Тартып алынган хокуклар урынына бурычлар өеп бирелгән.', 'In place of the rights taken away, duties were piled on.'),
    ('Ә җәй айларында хатын-кызлар кырда чөгендер утаганнар.', 'And in the summer months the women weeded beetroot in the fields.'),
    ('Бу табылдык турында моңарчы беркайда да искәртелмәгән.', 'This find has never been mentioned anywhere before.'),
]),
('c2-tale', [
    ('Суны эчеп бетергәч, ерткыч хайваннар картка ташланалар.', "When they've finished drinking the water, the wild beasts throw themselves at the old man."),
    ('Минем чәч алучыларым сакалымны кырганда бик рәнҗетәләр.', 'My barbers hurt me badly when they shave my beard.'),
    ('Менә берзаман каенаталары белән хатыны килеп кергәннәр.', 'Then one day his father-in-law and his wife came in.'),
    ('Мин барында син курыкма, әҗәлгә кермәссең, коткарырмын.', "While I'm here, don't be afraid; you won't meet your death — I'll save you."),
]),
('c2-life', [
    ('Шыгырдавыклы агач озак чыдар, шыгырдамаган тиз сынар.', 'A creaking tree lasts long; one that never creaks snaps fast.'),
    ('Дөньяны яуларга омтылма, аның гыйлемен яуларга омтыл.', "Don't strive to conquer the world; strive to conquer its knowledge."),
    ('Дан-шөһрәт диңгезендә йөзеп тончыгып үлүчеләр дә бар.', 'Some swim in the sea of fame and glory and drown.'),
    ('Оятларына көч килә, хурлыгын ничек күтәрергә белмиләр.', "Their shame overwhelms them; they don't know how to bear the disgrace."),
]),
('c2-gov', [
    ('Барлык мөрәҗәгатьләр буенча тиз арада тикшерү уздырылачак.', 'An inspection will be carried out promptly on all the complaints.'),
    ('Шулай итеп, кешеләр арасында социаль тигезлек урнаштырыла.', 'In this way, social equality is established among people.'),
    ('Киләчәктә аны даими рәвештә тулыландырып торырга ниятлиләр.', 'They intend to keep adding to it on a regular basis in future.'),
    ('Системаларның хәзерге торышында программага туры килмәүләр бар.', 'In the current state of the systems there are discrepancies with the programme.'),
]),
('c2-faith', [
    ('Мәчет эченә сыймаган мөселманнар урамда торып гыйбадәт кылды.', "The Muslims who couldn't fit inside the mosque prayed standing in the street."),
    ('Төн уртасында хатыны чыгып сызгыра, пәриләр җыелышып киләләр.', 'At midnight his wife goes out and whistles, and the fairies gather and come.'),
    ('Гарасат мәйданында аяклар сызламасын өчен нәрсә эшләргә кирәк?', "What must one do so that one's feet don't ache on the field of the Last Judgement?"),
    ('Әлеге көн мөселманнарны изге, игелекле гамәлләр кылырга чакыра.', 'This day calls Muslims to do holy and charitable deeds.'),
]),
('c2-lit', [
    ('Аксакал галим язган фәнни хезмәтләрнең исәбе-хисабы юк.', 'The scholarly works written by the venerable scholar are beyond counting.'),
    ('Спектакльнең премьерасында Идея ролен Такташ үзе башкара.', 'At the premiere of the play, Takhtash himself plays the role of Idea.'),
    ('Фатыйма бикә Мәрьямне гимназиягә бирергә иҗтиһат кылган иде.', 'Fatima bike had taken great pains to send Maryam to the gymnasium.'),
    ('Кулын иягенә куеп, уйланып утыра; күңелендәге уйларын актара.', 'With his hand on his chin he sits thinking, sorting through the thoughts in his heart.'),
]),
('c2-soc', [
    ('Чираттагы Сабантуй иҗтимагый-сәяси хәрәкәттә нинди урын алды?', "What place did this year's Sabantuy take in social and political life?"),
    ('Мондый төрлелек республикабызга кабатланмас милли төсмер өсти.', 'Such diversity gives our republic a unique national colour.'),
    ('Укытучы баланың дәрестә булмавына аерым игътибар бирергә тиеш.', "A teacher must pay special attention to a child's absence from class."),
    ('Без шәһәребезгә карата мөнәсәбәтне үзгәртәбез, үзебез үзгәрәбез.', 'We are changing our attitude to our city, and we ourselves are changing.'),
]),
('c2-hist', [
    ('Ак мәчет төзелешендә күп төрле материаллар кулланылган.', 'Many different materials were used in building the White Mosque.'),
    ('Милләт мәҗлесенә, мәгариф нәзарәтенә әгъза итеп сайлана.', 'He is elected a member of the National Assembly and the education directorate.'),
    ('Кыпчаклар шул дәүләтнең көнбатыш тармагын тәшкил иткәннәр.', 'The Kipchaks made up the western branch of that state.'),
    ('Татарның кайда, ничек яшәгәнен бәйнә-бәйнә сөйләргә мөмкин.', 'One can tell in detail where and how the Tatars lived.'),
]),
('c2-tale', [
    ('Патша хәзрәтләренә хезмәткә син калырсың, үзең карарсың.', "You will stay in the service of His Majesty the king; you'll see for yourself."),
    ('Егет, теләсә-теләмәсә дә, балыкны патшага китереп биргән.', 'Willing or not, the young man brought the fish to the king.'),
    ('Егетне кырык казан урнаштырылган бер сарайга бикләп куйдылар.', 'They locked the young man in a palace in which forty cauldrons had been set up.'),
    ('Үтерергә теләсә дә, егеттән куркып, хатынын үтерергә кыймады.', "Although he wanted to kill her, he didn't dare kill his wife for fear of the young man."),
]),
('c2-life', [
    ('Карамалының кара малаена чана карамаларга биргән идем.', "I lent a sled to Karamaly's dark-haired boy to look after. (a tongue twister)"),
    ('Еллар бер-беренә ялганып гомер боҗрасын тәшкил итәләр.', 'The years join one another to form the ring of a lifetime.'),
    ('Талантның бер өлеше тумыштан, тугыз өлеше тырышлыктан.', 'Talent is one part birth and nine parts hard work.'),
    ('Тешләнәсең килмәсә, ярсыган эт яныннан узмавың хәерле.', "If you don't want to be bitten, better not walk past a mad dog."),
]),
('c2-gov', [
    ('Барыгызга да саулык-сәламәтлек, җан тынычлыгы һәм муллык телим.', 'I wish you all good health, peace of mind and abundance.'),
    ('Инде килеп үзебезнең туган республикабыздагы хәлләргә күз салыйк.', 'Now let us take a look at the situation in our own native republic.'),
    ('Хөрмәтле ветераннар, сезгә ихлас күңелдән хәерле озын гомер телим!', 'Dear veterans, I sincerely wish you a long and blessed life!'),
    ('Ирешелгән уңышларга таянып, без киләчәк үсеш бурычларын билгелибез.', 'Building on the successes achieved, we set the tasks for future development.'),
]),
('c2-faith', [
    ('Коръәни-Кәримдә әлеге изге айның фазыйләтләренә зур урын бирелә.', 'In the Holy Quran a great place is given to the virtues of this holy month.'),
    ('Бәйге хаҗда булып кайткан мөселман кардәшләребез өчен оештырыла.', 'The contest is organised for our Muslim brothers and sisters who have returned from the Hajj.'),
    ('Мөселманнар булуыбыз берләшүгә, килешеп эшләүгә нигез булып тора.', 'Being Muslims is a basis for uniting and working together in harmony.'),
    ('Безнең халык хәтерендә янмый торган Гайшә риваяте сакланып калган.', "The legend of Gaysha, which never fades, has been preserved in our people's memory."),
]),
('c2-lit', [
    ('Азат әсәрләренең геройларын укучылар тиз арада яратып өлгерә.', "Readers quickly come to love the heroes of Azat's works."),
    ('Мондый җәза кылычы Карадуган өстендә дә ялтырап-ялтырап алган.', 'Such a sword of punishment also flashed over Karadugan.'),
    ('Самат - җаваплылыкны башкаларга җиңел аударучы өстенлекле зат.', 'Samat is a domineering character who easily shifts responsibility onto others.'),
    ('Язучы буларак Рәхимулла әдәбиятның төрле жанрларында иҗат итә.', 'As a writer, Rakhimulla works in various literary genres.'),
]),
('c2-soc', [
    ('Бүгенге яшәешебезне мәгълүмат алмашудан башка күзаллап та булмый.', "It's impossible even to imagine our life today without the exchange of information."),
    ('Шулай ук җәмгыять ялгыз һәм көчсез пенсионерлар турында кайгырта.', 'The society also looks after lonely and frail pensioners.'),
    ('Программа һәрбер теләгән кешегә татар телен өйрәнергә ярдәм итәчәк.', 'The programme will help anyone who wishes to learn the Tatar language.'),
    ('Кайбер җырчылар акча эшләү максатыннан туйларда чыгышлар ясап йөри.', 'Some singers go round performing at weddings to make money.'),
]),
('c2-hist', [
    ('Хәзер хатирәләребезне яңартыйк, тарих битләренә күз салыйк.', 'Now let us refresh our memories and look at the pages of history.'),
    ('Бу хакта Дунай буе болгарларында бер легенда-риваять калган.', 'A legend about this has survived among the Danube Bulgars.'),
    ('Шуларның яртысы диярлек сугыш кырларында мәңгегә ятып калды.', 'Almost half of them remained forever on the battlefields.'),
    ('Автономия булдырып, нугайлар бу җирләрне саклап калырга тели.', 'By creating an autonomy, the Nogais want to preserve these lands.'),
]),
('c2-tale', [
    ('Балалары белән елаша-елаша чокыр казып, елан патшаны күмәләр.', 'Weeping with the children, they dig a pit and bury the Snake King.'),
    ('Кыз биегән саен, аннан чылтыр-чылтыр алтын-көмеш коела башлый.', 'Every time the girl dances, gold and silver come tinkling off her.'),
    ('Тукта, монда тагын безнең кардәшләребез бар, аларны коткарыйк.', "Wait — there are more of our kinsmen here; let's save them."),
    ('Бүре аргамакларга карады, өрде, аргамаклар ямьсез атларга әйләнде.', 'The wolf looked at the steeds and breathed on them, and the steeds turned into ugly nags.'),
]),
('c2-life', [
    ('Бу мәсьәләдә уйланырлык, борчылырлык нәрсәләр юк түгел.', "In this matter there's no shortage of things to think about and worry over."),
    ('Бу вәзгыять ниләргә китерәчәге турында уйлану урынлырак.', "It's more appropriate to think about what this situation will lead to."),
    ('Алдындагы чүлмәккә карап, аяк астындагы түмгәккә абынма.', "Don't trip over the tussock at your feet while staring at the pot in front of you."),
    ('Проблеманы тудырганчы аны булдырмау өстендә эшләү зарур.', "It's essential to work on preventing a problem before it arises."),
]),
('c2-gov', [
    ('Тиражларыгыз зур, укучыларыгыз, тыңлаучыларыгыз күп һәм актив булсын.', 'May your print runs be large, and your readers and listeners many and active.'),
    ('Моратов үз докладында вәкиллекләрне үстерү курсы хакында чыгыш ясады.', 'In his report Moratov spoke about the course for developing the representative offices.'),
    ('Прокуратура органнары гаризаларның законга туры килүен тикшерергә тиеш.', "The prosecutor's office must check that the applications comply with the law."),
    ('Алабуга хакимияте бу тәкъдим буенча тиешле ведомстволарга хат әзерләгән.', 'The Yelabuga administration has prepared a letter on this proposal to the relevant authorities.'),
]),
('c2-faith', [
    ('Монда берәр нинди чикләүләр, халык белеп бетермәгән гамәлләр бармы?', "Are there any restrictions here, any practices the people don't fully know about?"),
    ('Хөкемдарларның, ягъни ил башлыкларының, патшаларның гаделлеген алам.', 'I take the justice of rulers, that is, of heads of state and kings.'),
    ('Әлеге олуг бәйрәмне барча мөселманнар түземсезлек белән көтеп алалар.', 'All Muslims await this great festival with impatience.'),
    ('Пәйгамбәребезнең хәдисенә нигезләнеп, гыйлемнең ике төрле булуын беләбез.', "On the basis of our Prophet's hadith, we know that there are two kinds of knowledge."),
]),
('c2-lit', [
    ('Яшүсмер, рәссам булып, дөньяга үзеннән матурлык өстәргә омтыла.', 'Becoming an artist, the teenager strives to add his own beauty to the world.'),
    ('Рушан Хафизов әлеге спектакльдә сәүдәгәр Рәмиев ролен башкарды.', 'Rushan Khafizov played the merchant Ramiev in this production.'),
    ('Нәтиҗә итеп әйткәндә, яңа концерт сезонына тырышып әзерләнәбез.', 'In conclusion, we are diligently preparing for the new concert season.'),
    ('Бу мәкаләдә мин шундый дәресләрдән берсенең эчтәлегенә тукталам.', 'In this article I focus on the content of one such lesson.'),
]),
('c2-soc', [
    ('Безгә, татарларга, Көнбатыш кешесендә булган кайбер сыйфатлар җитми.', 'We Tatars lack certain qualities that Western people have.'),
    ('Кайчан безнең Сабантуйның шундый азгынлык үрнәге булып торганы бар?!', 'When has our Sabantuy ever been such an example of depravity?!'),
    ('Дарулар, медицина хезмәте кыйммәт, бушлай булуы кәгазьдә генә калды.', 'Medicines and medical services are expensive; their being free has remained only on paper.'),
    ('Менә шушы ташу вакытларына, пычрак көннәргә туры китерергә тырышалар.', 'They try to time it for exactly these flood seasons, the muddy days.'),
]),
('c2-hist', [
    ('Алардан матур бәйрәмнәр, төрле ырымнар, ышанулар, мифлар калды.', 'They left behind beautiful festivals, all kinds of rituals, beliefs and myths.'),
    ('Хөсәеновлар гаиләсенә туган якларын яңадан күрергә насыйп булмый.', 'The Khuseynov family was not destined to see its native land again.'),
    ('Болгар йортында Кытайдан, Һиндстаннан килгән кешеләр күп булгандыр.', 'There must have been many people from China and India in the land of Bolgar.'),
    ('Матбугат эше киң колач алды, мәдәни-агарту оешмалары күпләп ачылды.', 'Printing expanded widely, and cultural and educational organisations opened in large numbers.'),
]),
('c2-tale', [
    ('Син үзеңнең егетлегең аркасында әллә нинди куркынычлардан котылдың.', 'Thanks to your courage you escaped all kinds of dangers.'),
    ('Көн сугыштылар, төн сугыштылар, кич сугыштылар, бик озак сугыштылар.', 'They fought by day, they fought by night, they fought in the evening — they fought for a very long time.'),
    ('Чәй кайнатып, бергә ашыйлар-эчәләр, монда кунарга туры килә боларга.', 'They boil tea, eat and drink together, and they have to spend the night here.'),
    ('Ничәмә-ничә еллык азык төяп, көймәне юлга чыгарга хәзерләп куйдылар.', 'They loaded the boat with provisions for many, many years and made it ready to set off.'),
]),
('c2-life', [
    ('Минминлекле кеше үзеннән уздырганнарны дошман итеп күрә.', 'An egotist sees enemies in those who surpass him.'),
    ('Ләкин кешеләр вакытны дөрес файдаланырга өйрәнмәделәр әле.', 'But people have not yet learned to use their time properly.'),
    ('Һава торышы: җылы-суык, җил-давыл, явым-төшем һәм башкалар.', 'Weather: warmth and cold, wind and storm, precipitation and so on.'),
    ('Сагынып көтәр кешең булганда гына кайтырга омтылып торасың.', "You only long to go home when there's someone there missing you and waiting."),
]),
('c2-gov', [
    ('Әһәмиятле сорауларда бабаларыбыз тәҗрибәсенә, тарихи мираска таяначакбыз.', 'On important questions we will rely on the experience of our forefathers and on our historical heritage.'),
    ('Традиция буенча яңа билгеләнгән министрга портфель һәм значок тапшырылды.', 'By tradition, the newly appointed minister was presented with a portfolio and a badge.'),
    ('Президент форумда катнашучы яшьләрнең теләк-тәкъдимнәрен дә тыңларга әзер.', 'The President is ready to listen to the wishes and proposals of the young people taking part in the forum.'),
    ('Рәсәй Федерациясе Мәдәният министрлыгы гауга тынганчы читтә калырга булды.', 'The Ministry of Culture of the Russian Federation decided to stay out of it until the scandal died down.'),
]),
('c2-faith', [
    ('Иртәгесен табак коп-коры булып, ашның барлыгын бичура ашаган, ялаган була.', 'The next morning the dish is bone dry: the bichura has eaten and licked up all the food.'),
    ('Аллаһы Тәгалә ризалыгы өчен күркәм гамәлләр кылыйк, динебезгә хезмәт итик.', 'Let us do fine deeds for the pleasure of God Almighty and serve our faith.'),
    ('Шул гыйлем белән гамәл кылырга, аңа нигезләнеп яшәргә кирәклеген онытмагыз.', 'Do not forget that you must act on that knowledge and live by it.'),
    ('Үлем юк, ахирәткә китүчеләр безнең яратуыбызны һәм догаларыбызны тоеп тора.', 'There is no death: those who have gone to the hereafter feel our love and our prayers.'),
]),
('c2-lit', [
    ('Конкурс өч номинациядә үтә: шигърият, чәчмә әсәрләр, драматургия.', 'The competition has three categories: poetry, prose and drama.'),
    ('Тантананың яңа унъеллыгы башлану яңа идеяләр тууга этәргеч булды.', "The beginning of the festival's new decade gave rise to new ideas."),
    ('Әдип Сөембикә нәселенең Идегәй әмиргә барып тоташканлыгын күрсәтә.', "The writer shows that Syuyumbike's lineage went back to Emir Edigu."),
    ('Монументның авторы - Россиянең атказанган рәссамы Салават Щербаков.', 'The author of the monument is Salavat Shcherbakov, Honoured Artist of Russia.'),
]),
('c2-soc', [
    ('Бу көннәрдә күп кенә илләрдә, төбәкләрдә юбилей тантаналары уздырыла.', 'These days anniversary celebrations are being held in many countries and regions.'),
    ('Республикада милли мәктәпкәчә балалар учреждениеләре челтәре үсә бара.', 'The network of national preschool institutions in the republic is growing.'),
    ('Авылларда, әйтик, ятим калган сабыйларны туганнары яки күршеләре алган.', 'In the villages, say, orphaned infants were taken in by relatives or neighbours.'),
    ('Мәктәптә табигать фәннәре Чарльз Дарвинның эволюция теориясенә корылган.', "At school the natural sciences are built on Charles Darwin's theory of evolution."),
]),
('c2-hist', [
    ('Сугышта күрсәткән батырлыклары өчен орден-медальләр белән бүләкләнә.', 'He is awarded orders and medals for the bravery he showed in the war.'),
    ('Авыл башта хәзерге урманның көньяк-көнчыгыш өлешенә урнашкан булган.', 'At first the village was located in the south-eastern part of the present forest.'),
    ('Яуга каршы көрәшне оештыру бурычы үзеннән-үзе Сөембикә җилкәсенә төшә.', "The task of organising the fight against the invaders falls by itself onto Syuyumbike's shoulders."),
    ('Ниһаять, үзебездә дә тарихыбыз битләрен актарып карау мөмкинлеге ачылды.', 'At last we too have the opportunity to leaf through the pages of our history.'),
]),
('c2-tale', [
    ('Ут тавына якынлаша башлау белән, тотындылар тегеннән ут яудырырга...', 'As soon as they began to approach the Fire Mountain, it started to rain fire down on them...'),
    ('Гөлчәчәкнең абыйсы капка төбенә чыккан икән, чәч бөртекләрен күргән.', "Gulchachak's brother had gone out to the gate, it turned out, and saw the strands of hair."),
    ('Ярый, мин синең сүзеңне тыңлап, аларны әүвәлге кыяфәтләренә кайтарам.', "Very well, I'll heed your words and return them to their former shape."),
    ('Алпамша мылтыгын күтәреп аткач, халык инде Алпамшаның кайтуына ышана.', 'When Alpamysh raises his gun and fires, the people now believe Alpamysh has returned.'),
]),
('c2-life', [
    ('Үткәннәр бүгенгә, бүгенге киләчәккә тоташып гомер хасил итә.', 'The past joins the present, and the present the future, and together they make a life.'),
    ('Изге сөйләсәң, изге ишетерсең, яман сөйләсәң, яман ишетерсең.', "Speak good and you'll hear good; speak ill and you'll hear ill."),
    ('Теләк булу беләнмени, аны тормышка ашырырга шартлар булмагач.', "Wanting it isn't enough when there are no conditions for making it happen."),
    ('Тулаем алганда, беренче омтылышыбыз мактауга лаек, дип уйлыйм.', 'On the whole, I think our first attempt deserves praise.'),
]),
('c2-gov', [
    ('Болар инде дәүләт җитәкчеләренең лексиконында булырга тиешле сүзләр түгел.', 'These are not words that should be in the vocabulary of heads of state.'),
    ('Чит ил һәм Россия университетлары белән фәнни-эзләнү элемтәсе булдырылган.', 'Scientific research links have been established with foreign and Russian universities.'),
    ('Төп законыбыз Татарстан халыкларының милли үсешенә тигез мөмкинлекләр ача.', 'Our Basic Law opens equal opportunities for the national development of the peoples of Tatarstan.'),
    ('Сезне Татарстан Республикасы Матбугат көне белән чын күңелдән тәбрик итәм.', 'I sincerely congratulate you on Press Day of the Republic of Tatarstan.'),
]),
('c2-faith', [
    ('Гөнаһларның гафу ителүе, дога кылучыларның догалары кабул ителәчәге аңлашыла.', 'It is understood that sins are forgiven and the prayers of those who pray will be accepted.'),
    ('Сөйләнәсе вәгазьләр контрольгә алынды, ләкин нәрсәдер үзгәрде дип әйтеп булмый.', "The sermons to be given were brought under control, but one can't say that anything has changed."),
    ('Ислам Россия халыкларының рухи тормышында күп гасырлар буена мөһим роль уйнады.', 'Islam has played an important role in the spiritual life of the peoples of Russia for many centuries.'),
    ('Мигъраҗ вакытында пәйгамбәребезгә Аллаһ шулай ук җәннәтне һәм җәһәннәмне күрсәтә.', "During the Mi'raj God also shows our Prophet paradise and hell."),
]),
('c2-lit', [
    ('Туксанынчы елларда әдипнең иҗади кызыксынулары төрле юнәлештә бара.', "In the nineties the writer's creative interests went in various directions."),
    ('Чын сәнгатьне, чын шигъриятне тудырган затлар бервакытта да үлмиләр.', 'Those who create true art and true poetry never die.'),
    ('Автор алдан һәр китапның киңәйтелгән планын төзи, исемнәрен билгели.', 'The author first draws up a detailed plan of each book and decides on the titles.'),
    ('Габдулла Гомәрнең иҗади мирасы башлыча әдәби тәрҗемә өлкәсенә карый.', "Gabdulla Gumar's creative legacy lies mainly in the field of literary translation."),
]),
('c2-soc', [
    ('Русия гражданнарының өчтән бере азык-төлекне кирәгеннән артык сатып ала.', 'A third of Russian citizens buy more food than they need.'),
    ('Сабан туенда без беренче чиратта авыл хуҗалыгы алдынгыларын хөрмәтлибез.', 'At Sabantuy we honour first of all the best agricultural workers.'),
    ('Татарстан ветераннарының инде күбесе яңа фатирларга күченеп яши башлады.', "Most of Tatarstan's veterans have already moved into new flats."),
    ('Бөтен коллективлар да милли киемнәрен киеп, стадион кырына тезелеп бастылар.', 'All the groups put on their national costumes and lined up along the edge of the stadium.'),
]),
('c2-hist', [
    ('Бер китапта бөтен тарихи вакыйгаларны бәйнә-бәйнә ачып бирү мөмкин түгел.', "It's impossible to reveal every historical event in detail in a single book."),
    ('Милләтнең кайсы юлдан китәргә, кемнәрдән үрнәк алырга белми аптыраган чагы.', 'It is a time when the nation is at a loss as to which path to take and whom to follow.'),
    ('Төп транспорт чарасы ат булган чорда зооветеринария буенча белгечләр җитешми.', "At a time when the horse was the main means of transport, there weren't enough veterinary specialists."),
    ('Тарих тагын да хаклы рәвештә яктыртылсын өчен, без халыкларыбыз алдында бурычлы.', 'We owe it to our peoples to make sure history is portrayed even more truthfully.'),
]),
('c2-tale', [
    ('Инеш буйларында, су тегермәне тирәләрендә тулганып йөреп вакыт уздырды.', 'He passed the time wandering along the stream banks and around the watermill.'),
    ('Өстәл өчпочмак, бәлеш, чәк-чәк, пәрәмәч кебек ризыклардан сыгылып торды.', 'The table was groaning with dishes such as öçpoçmaq, pies, chak-chak and peremech.'),
    ('Син, балам, күз нурым, карлыгач бул, җитезлегең белән адәмнәрне сокландыр.', 'You, my child, the light of my eyes, be a swallow and delight people with your nimbleness.'),
    ('Курыкмас җиреңнән куркырсың: тегеләр капкан саен бер көлтәне йота бирәләр.', "You'll be scared where you'd never expect: every time they open their mouths, they swallow a whole sheaf."),
]),
('c2-life', [
    ('Кеше хайванга караганда күпкә мәкерлерәк булуы белән куркыныч.', 'Man is dangerous in being far more cunning than an animal.'),
    ('Нишләптер безнең күршеләрнең, өч көн инде, кычкырышканнары юк.', "For some reason our neighbours haven't shouted at each other for three days now."),
    ('Бүгенге сабакны белмәсәң, иртәгәге сабакны бигрәк тә белмәссең.', "If you don't know today's lesson, you'll know tomorrow's even less."),
    ('Галимнәргә иярсәң, күзең ачылыр, наданнарга иярсәң күзең чыгар.', "Follow scholars and your eyes will open; follow the ignorant and you'll lose your eyes."),
]),
('c2-gov', [
    ('Утырышны Татарстан Республикасы Премьер-министры Рөстәм Миңнеханов үткәрде.', 'The meeting was chaired by the Prime Minister of the Republic of Tatarstan, Rustam Minnikhanov.'),
    ('Ураза бәйрәме күңелләребезгә иман нуры иңдерсен, киләчәккә ышаныч китерсен.', 'May Eid al-Fitr bring the light of faith into our hearts and confidence in the future.'),
    ('Бу барыбызга да телебезне һәм мәдәниятебезне үстерүдә зур җаваплылык йөкли.', 'This places a great responsibility on all of us to develop our language and culture.'),
    ('Шуңа күрә комитет утырышында законны урыннарда куллану турында сүз барачак.', 'That is why the committee meeting will discuss how the law is applied locally.'),
]),
('c2-faith', [
    ('Без дә үзебезгә бирелгән нигъмәтләрнең ләззәтен алардан тыелмыйча торып белмибез.', 'We too can only know the delight of the blessings given to us by restraining ourselves from them.'),
    ('Бүгенге көндә барлык районнарда да диярлек Коръән укучылар конкурслары булып үтте.', 'Quran recitation contests have now been held in almost every district.'),
    ('Бер атадан һәм анадан булуларына карамастан, Аллаһы Тәгалә аларны төрле-төрле итте.', 'Although they came from one father and one mother, God Almighty made them all different.'),
    ('Имештер, бик борынгы заманнарда усак яфраклары тирәк яфраклары төсле озынча булганнар.', 'It is said that in very ancient times aspen leaves were long, like poplar leaves.'),
]),
('c2-lit', [
    ('Әсәрдә Мөхәммәдъяр образы күренекле акыл иясе, философ итеп бирелгән.', 'In the work, the image of Muhammadyar is presented as a distinguished thinker and philosopher.'),
    ('Алайса, шигырьләр яза торган Габдулла Тукаевны яхшы белә торгансыздыр.', 'In that case you must know Gabdulla Tukayev, who writes poems, well.'),
    ('Казан дәүләт университетының татар теле һәм әдәбияты бүлеген тәмамлый.', 'He graduates from the Tatar language and literature department of Kazan State University.'),
    ('Фәнни хезмәтләре татар алфавиты һәм орфографиясен өйрәнүгә багышланган.', 'His scholarly works are devoted to the study of the Tatar alphabet and orthography.'),
]),
('c2-soc', [
    ('Авыр хәлдәге бер балага махсуслаштырылган үзәктә оператив дәвалау таләп ителә.', 'A seriously ill child requires urgent treatment at a specialised centre.'),
    ('Без хәзер культурага бер примитив нәрсәгә караган кебек кенә карарга керештек.', 'We have now begun to regard culture as if it were something primitive.'),
    ('Авылда туган, шәһәрнең зыялы гаиләләрендә тәрбияләнгәннәр арасында алар байтак.', 'Among them there are many who were born in the village and brought up in educated city families.'),
    ('Тарихи-мәдәни мирас елы җәмгыятьнең үткән заманга игътибары артуына ярдәм итте.', "The Year of Historical and Cultural Heritage helped increase society's attention to the past."),
]),
('c2-hist', [
    ('Болгарда шәһәрләр төзү һәм, гомумән, шәһәр мәдәнияте шактый югары дәрәҗәдә торган.', 'City building and urban culture in general were at quite a high level in Bolgar.'),
    ('Аларда төрки халыклар язмышы, төрки халыклар төзегән дәүләтләр турында бәян ителә.', 'They set out the fate of the Turkic peoples and the states the Turkic peoples founded.'),
    ('Сафа Гәрәй хан хатыннарын, балаларын, якыннарын алып Болгар капкасыннан чыгып кача.', 'Khan Safa Giray flees through the Bolgar Gate, taking his wives, children and relatives.'),
    ('Әлеге истәлекле көннәрдән соң узган гасырлар тарихка зур сынаулар белән кереп калды.', 'After these memorable days, the centuries that followed entered history with great trials.'),
]),
('c2-tale', [
    ('Лапас артыннан әйләнеп үткәч, кинәт бик искитмәле күренеш алдына чыктылар.', 'After going round behind the shed, they suddenly came upon an astonishing sight.'),
    ('Малыңа тимим, шәһәреңне ватмыйм, гаскәреңне кырмыйм, миңа кызыңны гына бир.', "I won't touch your wealth, I won't destroy your city, I won't slaughter your army — just give me your daughter."),
    ('Икенче күтәрүдә башына җиткерде, өченче күтәрүдә һавага кул сузымы күтәрде.', "With the second lift he raised it to his head; with the third he raised it an arm's length into the air."),
    ('Шуның аркасында кайнанам белән кайнатам арасында гомерлеккә ризасызлык кала.', 'Because of this, a lifelong resentment remains between my mother-in-law and father-in-law.'),
]),
('c2-life', [
    ('Капчыклап сораганда учлап, учлап сораганда бөртекләп кенә бирә.', 'When you ask by the sackful he gives by the handful; when you ask by the handful he gives by the grain.'),
    ('Билетларны таратып бетергәннән соң укытучы бүлмәдән чыгып китте.', 'After handing out the tickets, the teacher left the room.'),
    ('Сез акчаны куркып сорамагыз, хезмәт хакын икеләтә-өчләтә сорагыз.', "Don't be afraid to ask for money: ask for double or triple the wage."),
    ('Өеңдәге хәбәрне күршедән, күршеңдәге хәбәрне күрше авылдан сораш.', 'Ask the neighbour for news of your own house, and the next village for news of your neighbour.'),
]),
('c2-gov', [
    ('Укучыларыгыз сезне белемле, тәрбияле һәм итагатьле булулары белән сөендерсен.', 'May your pupils delight you by being knowledgeable, well brought up and courteous.'),
    ('Сезгә чын күңелдән бәхет, тынычлык, бәрәкәт, иминлек һәм исәнлек-саулык телим!', 'I sincerely wish you happiness, peace, abundance, well-being and good health!'),
    ('Әлеге карарны Россия Федерациясе Федераль Собраниесе Дәүләт Думасына җибәрергә.', 'This decision is to be sent to the State Duma of the Federal Assembly of the Russian Federation.'),
    ('Рөстәм Миңнеханов барлык хәйриячеләргә игелекле гамәлләре өчен рәхмәт белдерде.', 'Rustam Minnikhanov thanked all the benefactors for their charitable deeds.'),
]),
('c2-faith', [
    ('Аллаһы Тәгалә безне төрле халыклар, кабиләләр кылды, бер-беребезне тану, ярдәмләшү өчен.', 'God Almighty made us different peoples and tribes so that we might know and help one another.'),
    ('Чөнки тормышыбызның әхлакый чисталыгына бары тик игелекле гамәлләр аша гына ирешеп була.', 'Because moral purity in our lives can only be achieved through good deeds.'),
    ('Шул вакытта гөнаһ шомлыгына каршы бер эт килеп бусага өстендәге икмәкне алып китмәсенме?', "Just then, as ill luck would have it, didn't a dog come and take the bread off the threshold?"),
    ('Коръән Кәримдәге миһербанлык һәм шәфкать турындагы гыйбарәләрнең мәгънәсе тагын да көчәя.', 'The meaning of the passages about mercy and compassion in the Holy Quran becomes even stronger.'),
]),
('c2-lit', [
    ('Монда эпитетлар дин тойгыларын үстерүгә хезмәт иттерелеп китерелгәннәр.', 'Here the epithets are deployed to serve the development of religious feeling.'),
    ('Шуңа күрә әлеге факт гротеск дәрәҗәсендә күпертелгән дигән тәэсир кала.', 'One is left with the impression that this fact has been exaggerated to the point of the grotesque.'),
    ('Академик дәрәҗәдәге мондый форумда җитмештән артык доклад тәкъдим ителә.', 'At a forum of this academic level more than seventy papers are presented.'),
    ('Бу нисбәттән Хәсән Туфанның биш томлыгын чыгаруны билгеләп үтәргә кирәк.', "In this connection, the publication of Hasan Tufan's five-volume collected works should be noted."),
]),
('c2-soc', [
    ('Саба тәҗрибәсен Германия, Швеция, Финляндия кебек илләрдән дә килеп өйрәнделәр.', 'Countries such as Germany, Sweden and Finland came to study the Saba experience.'),
    ('Кызганыч ки, татар халкының әле мондый продукциясе җитәрлек күләмдә түгел икән.', "Sadly, it seems the Tatar people don't yet have enough products like this."),
    ('Яңа үзәкнең максаты - белем бирү процессында дистанцион технологияләрне куллану.', 'The aim of the new centre is to use distance-learning technologies in the educational process.'),
    ('Исемнәрне ничек язуны мәҗбүри өйрәтергә кирәк түгел, әмма тәкъдим итәргә мөмкин.', 'There is no need to make people learn how to write names, but it can be recommended.'),
]),
('c2-hist', [
    ('Көнбатыштан һөҗүмнәр ешаю аркасында Идел һәм Кама буйлары куркыныч урыннарга әйләнгән.', 'As attacks from the west became more frequent, the banks of the Volga and Kama turned into dangerous places.'),
    ('Айсылу хатирәләреннән бу атаклы лицейда байтак татар кызының белем алганлыгы аңлашыла.', "From Aysylu's memoirs it is clear that quite a few Tatar girls were educated at this famous lyceum."),
    ('Авылның атамасы аның кайда урнашуына, ягъни географик үзенчәлегенә бәйле булырга мөмкин.', "A village's name may depend on its location, that is, on its geographical features."),
    ('Ленинград блокадасындагы һәм фашист концлагерьларындагы вәхшәт халык күңеленә тирән яра салды.', "The savagery of the Leningrad blockade and the fascist concentration camps left a deep wound in the people's soul."),
]),
('c2-tale', [
    ('Алтын сарайларның, бакчаларның беленмәслек булып кайбер урыннары гына калды.', 'Of the golden palaces and gardens only a few barely recognisable places were left.'),
    ('Тора-бара таныш түгел кызның Тәнзиләгә бөтенләй дә охшамаганлыгын да аңлады.', "Gradually he also realised that the unfamiliar girl didn't look like Tanzila at all."),
    ('Шәһәргә кайтып кергәнче, керфеген какмый, күзен йоммый, текәлеп карап торды.', 'Until he got back to the city, he stared intently without blinking or closing his eyes.'),
    ('Элек мин йоклармын, син каравылларсың, аннан син каравылларсың, мин йоклармын.', "First I'll sleep and you'll keep watch, then you'll sleep and I'll keep watch."),
]),
('c2-life', [
    ('Юкка өметләнгәнче булганын тартып-сузып булса да җиткерү мәслихәт.', "Rather than hope in vain, it's wiser to make do with what there is, even if you have to stretch it."),
    ('Менә үзен мактаган чагында мактанырга яратмавы хакында да әйтмәсә.', "If only he didn't also mention, while praising himself, how much he dislikes boasting."),
    ('Үзеңне биеклектә тоярга яратасың икән, канатлы булып туарга кирәк.', 'If you like to feel yourself up high, you need to be born with wings.'),
    ('Әмма пединститутка аяк тартмады, борылып, театр училищесына киттек.', 'But I had no wish to go to the teacher training institute; I turned round and went to the theatre college.'),
]),
('c2-gov', [
    ('Судья әфәнде, гаепләнүченең балачагы бик авыр узганны исәптән чыгармасагыз иде.', 'Your Honour, I wish you would take into account that the defendant had a very hard childhood.'),
    ('Яңа закондагы нормалар буенча, баланы караган өчен чыгымнар өч төркемгә бүленә.', 'Under the provisions of the new law, childcare expenses are divided into three groups.'),
    ('Сезне туган көнегез белән котлап, иң изге, якты, матур теләкләребезне юллыйбыз.', 'Congratulating you on your birthday, we send you our kindest, brightest and most beautiful wishes.'),
    ('Премьер-министр министрлыкның элеккеге җитәкчесе эшен дә игътибарсыз калдырмады.', "The Prime Minister did not overlook the work of the ministry's former head either."),
]),
('c2-faith', [
    ('Хәзер мираска таянган һәм бүгенге заманга туры килгән интеллектуаль ислам булдыру сорала.', 'What is now needed is an intellectual Islam that rests on heritage and suits the present day.'),
    ('Ә башка берәүләр исә бу гамәлнең дөресме-түгелме икәнен тикшереп, моңа каршы дәлилләр эзли.', 'Others, however, examine whether this deed is right or not and look for arguments against it.'),
    ('Без аны мескеннәргә, ятимнәргә, гарип-горабаларга, тол хатыннарга, мохтаҗларга бирергә тиеш.', 'We must give it to the poor, orphans, the disabled, widows and those in need.'),
    ('Ислам һәрвакыт гаделлеккә, җаваплылыкка, әхлаклы, зирәк, шәфкатьле-мәрхәмәтле булырга өйрәтте.', 'Islam has always taught justice, responsibility, and being moral, wise, compassionate and merciful.'),
]),
('c2-lit', [
    ('Авылларда, шәһәр мәдрәсәләрендә Тукайны күмгән көнне дәресләр уздырылмый.', 'On the day Tukay was buried, no lessons were held in the villages or in the town madrasas.'),
    ('Бер шигырьдә ачык итеп әйтеп бетерелмәгән уй икенчесендә тәгаенләнә төшә.', 'A thought not fully expressed in one poem becomes more definite in another.'),
    ('Кешелек сыйфатлары белән ул бик булдыксыз, буынсыз, ихтыярсыз булып чыга.', 'As a human being he turns out to be very incompetent, spineless and weak-willed.'),
    ('Инде ничәнче мәртәбә куелуына карамастан, ул үзенең популярлыгын югалтмый.', "Despite being staged who knows how many times, it hasn't lost its popularity."),
]),
('c2-soc', [
    ('Кагыйдә буларак, болай эшләү югалу, артта калу кебек күренешләрне шактый киметә.', 'As a rule, doing things this way considerably reduces things like losses and falling behind.'),
    ('Авыл кешеләренең аңлыраклары хуҗалык калдыкларын элек тирән чокырга ташлыйлар иде.', 'The more conscious villagers used to throw household waste into a deep pit.'),
    ('Казанлылар өчен генә түгел, республика башкаласына турист буларак килгәннәр өчен дә.', 'Not only for the people of Kazan, but also for those who come to the capital of the republic as tourists.'),
    ('Әмма уңай тәэсирләр алып килүче мәгълүмат белән бергә, негатив хәбәрләр дә таратыла.', 'But along with information that has a positive effect, negative news is spread too.'),
]),
('c2-tale', [
    ('Авызы колагына җиткән, сөенеченнән балкып торган Ринат Гөлия белән сөйләшә иде.', 'Grinning from ear to ear and beaming with joy, Rinat was talking with Gulia.'),
    ('Болытларның берсе гадәти болыт түгел, аннан яңгыр тамчылары урынына сүзләр ява.', 'One of the clouds is no ordinary cloud: instead of raindrops, words fall from it.'),
    ('Шул вакытта инде болар Алпамшаның исән икәнлеген, аның нәрсә сораганын беләләр.', 'By then they knew that Alpamysh was alive and what he was asking for.'),
    ('Болар, узышканда, икенче шәһәргә җитеп, шунда печать бастырып кайтырга булдылар.', 'Racing each other, they decided to reach the other city, have the seal stamped there and come back.'),
]),
('c2-life', [
    ('Ашлыклар эшен бетергәч, бакчага чыгып, бәрәңге казырга вакыт җитте.', "Once the grain work is finished, it's time to go out to the garden and dig potatoes."),
    ('Киләчәкне тиз генә таралмый торган билгесезлек томаны уратып алган.', "The future is shrouded in a fog of uncertainty that won't lift quickly."),
    ('Үз-үзен яратуы шундый көчле, шуңа башкаларны онытып торырга мәҗбүр.', 'His self-love is so strong that he is forced to forget about others.'),
    ('Авыл башындагы зират та җилне исәр юлыннан тоткарлап тынычландырадыр.', 'The cemetery at the end of the village, too, perhaps checks the wind in its path and calms it.'),
]),
('c2-gov', [
    ('Татарстан Республикасы Президенты Рөстәм Миңнеханов шул хактагы Указны имзалады.', 'The President of the Republic of Tatarstan, Rustam Minnikhanov, signed a decree to that effect.'),
    ('Мәгариф һәм сәламәтлек саклау өлкәләрен модернизацияләү эзлекле башкарылып килә.', 'The modernisation of education and healthcare is being carried out consistently.'),
    ('Барлык премияләр дә конкурсның генераль һәм рәсми спонсорлары тарафыннан бирелә.', "All prizes are awarded by the competition's general and official sponsors."),
    ('Бу турыда Татарстан Сәламәтлек саклау министрлыгының матбугат хезмәте хәбәр итә.', 'This was reported by the press service of the Ministry of Health of Tatarstan.'),
]),
('c2-faith', [
    ('Бу айда без барча уй-ниятләребезне бер-беребезгә рәхим-шәфкать күрсәтүгә һәм игелек кылуга юнәлттек.', 'This month we have directed all our thoughts and intentions towards showing mercy to one another and doing good.'),
    ('Бу көннәрдә мөселманнар фарыз намазларын укыганнан соң, Аллаһы Тәгаләне мактап махсус сүзләр әйтәләр.', 'On these days, after performing the obligatory prayers, Muslims say special words praising God Almighty.'),
    ('Әлеге бәйрәм көннәрендә Аллаһы Тәгаләнең бөеклегенә, Исламның хак дин булуына тагын бер кат инанабыз.', 'On these festive days we are convinced once again of the greatness of God Almighty and the truth of Islam.'),
    ('Шул ук вакытта яшьләрнең күпчелегенең ислам һәм башка диннәр кыйммәтләре буенча белеме юк дәрәҗәсендә.', 'At the same time, most young people have almost no knowledge of the values of Islam and other religions.'),
]),
('c2-lit', [
    ('Ләкин болар гәзиттә басарлык булып бетмәгәннәр әле дип, кире кайтарганнар.', "But they sent them back, saying they weren't yet fit to print in the newspaper."),
    ('Әсәрдә күрсәтелгәнчә, Зыяның тормышы, эшләре бу сорауга җавап бирә алалар.', "As the work shows, Ziya's life and deeds can answer this question."),
    ('Авыл мөгаллимнәре Венера һәм Гомәр Ялаловлар аның беренче ярдәмчеләре була.', 'The village teachers Venera and Gumar Yalalov become his first helpers.'),
    ('Адлер абый, Сез физика-математика факультетын тәмамлап, әдәбиятка килгән кеше.', 'Adler abi, you came to literature after graduating from the faculty of physics and mathematics.'),
]),
('c2-soc', [
    ('Акциянең максаты - кулланучылар арасында Интернетта татарча аралашуны популярлаштыру.', 'The aim of the campaign is to popularise communication in Tatar among internet users.'),
    ('Май ае исә волонтерлар, табиблар, хокук саклау органнары, артистлар өчен билгеләнгән.', 'May is dedicated to volunteers, doctors, law-enforcement officers and performers.'),
    ('Аккредитацияне безгә күптән түгел - Универсиада башланырга берничә көн кала бирделәр.', 'We were given our accreditation only recently, a few days before the Universiade began.'),
    ('Бу көнне укучылар чит телләр, география, химия яки тарих фәннәреннән имтихан тапшыра.', 'On this day pupils take exams in foreign languages, geography, chemistry or history.'),
]),
('c2-tale', [
    ('Сезгә рәхмәт тыңлаган өчен, миңа рәхмәт сөйләгән өчен, йокларга вакыт, йоклагыз!', "Thank you for listening, and thanks to me for telling — it's time to sleep, so sleep!"),
    ('Бераз көннәр яланда очып килгәннәр иде, агасының калган чокырына килеп җиттеләр.', 'After flying over the steppe for some days, they reached the pit where his brother had been left.'),
    ('Бик каты сугышканнан соң, Сандугач, авыр яраланып, атасының йортына кайтып китә.', "After a very fierce fight, Sanduğaç, badly wounded, goes back to her father's house."),
    ('Шуннан мулла көннән-көн байый башлаган: акчасы да арткан, терлекләре дә күбәйгән.', 'From then on the mullah began to grow richer day by day: his money increased and his livestock multiplied.'),
]),
('c2-life', [
    ('Мәктәптә үткәрелгән төрле конкурсларда җиңүче булып калганым да булды.', 'I also happened to win various competitions held at school.'),
    ('Үлә-бетә тырышасың, тырмашасың – дөньяга кирәкне һаман җиткереп булмый.', "You try yourself to death, you strain every nerve — and still you can't provide all that's needed in the world."),
    ('Алабута оныннан пешерелгән кабартманың теш үтмәс катылыгы әле дә исемдә.', 'I still remember how impossibly hard the flatbread baked from goosefoot flour was.'),
    ('Без аларның көндәлек гади эшкә бирелгән вакытларындагы тормышын күрмибез.', "We don't see their lives at the times when they are given over to ordinary daily work."),
]),
('c2-gov', [
    ('Югары, урта һөнәри, мәктәпкәчә һәм өстәмә белем бирүдә уңай үзгәрешләр күзәтелә.', 'Positive changes are being seen in higher, secondary vocational, preschool and supplementary education.'),
    ('Бүген Татарстан бай икътисади потенциалга, нык үскән социаль инфраструктурага ия.', 'Today Tatarstan has rich economic potential and a well-developed social infrastructure.'),
    ('Агымдагы елның беренче яртысы йомгаклары гомуми икътисади хәлнең яхшыруын раслый.', 'The results of the first half of this year confirm an improvement in the general economic situation.'),
    ('Хөрмәтле ветераннар, безне сөендереп, арабызда мөмкин кадәр озаграк яшәсәгез иде!', 'Dear veterans, we wish you would stay among us as long as possible and keep bringing us joy!'),
]),
('c2-lit', [
    ('Башта үз авылларындагы мәдрәсәдә укый, аннары күрше авылындагы мәдрәсәгә күчә.', 'At first he studies at the madrasa in his own village, then moves to the madrasa in a neighbouring village.'),
    ('Ник дигәндә, китаптагы һәр мәзәктә, һәр вакыйгада конкрет шәхесләр тасвирлана.', 'Because every anecdote and every event in the book describes real people.'),
    ('Моңа, һичшиксез, Нәҗип Җиһановның һәм аның фикердәшләренең олы хезмәте кергән.', 'Nazhip Zhiganov and his like-minded colleagues undoubtedly made a great contribution to this.'),
    ('Җиңүче авторлар акчалата беренче, икенче һәм өченче премияләр белән бүләкләнә.', 'The winning authors are awarded first, second and third cash prizes.'),
]),
('c2-soc', [
    ('Тормыш йөген тартырдай, кулыннан эш килә торган сәламәт ир-егетләр турында сөйләнәбез.', "We are talking about healthy men who are capable of carrying life's burden and who know how to work."),
    ('Эчтәлеккә килгәндә, тарих, математика һәм информатикадан тестларга үзгәрешләр кертелгән.', 'As for the content, changes have been made to the tests in history, mathematics and computer science.'),
    ('Журналистика эшчәнлеге - хәзерге җәмгыять үсешендә аеруча мөһим этәргеч көчләрнең берсе.', 'Journalism is one of the especially important driving forces in the development of modern society.'),
    ('Сабантуйда борынгы гореф-гадәтләр, җыр-биюләр, йолалар һәм уеннар бер-берсенә үрелеп бара.', 'At Sabantuy, ancient customs, songs, dances, rituals and games are interwoven.'),
]),
('c2-tale', [
    ('Егет, бик күңелсезләнеп өенә кайтып, әтисенең язып калдырган дәфтәрен укып карый.', 'Very downcast, the young man goes home and reads the notebook his father had left behind.'),
    ('Үзе, патша хәзрәтләре, зур бәйрәмнәрдә Ак байталны мәйданга чыгарып күрсәтә икән.', 'His Majesty the king himself brings the White Filly out into the square and shows her at great festivals.'),
    ('Шунда пәриләр боларның артларыннан куып киләләр, тик артыннан куып җитә алмыйлар.', "Then the fairies come chasing after them, but they can't catch up."),
    ('Елгада басманың булмавы, су алуның читенлеге, ярның текәлеге яшь киленгә ошамаган.', "The young bride didn't like that there was no footbridge on the river, that fetching water was hard and that the bank was steep."),
]),
('c2-life', [
    ('Хәлемне аңлап, кызганмый-нитми, күләмле акча күчерүчеләр дә шактый булды.', 'Understanding my situation, quite a few people transferred considerable sums without hesitation.'),
    ('Безнең бер милләт булып тора алуыбыз телебезне саклый алуыбызга бәйледер.', 'Our ability to remain one nation probably depends on our ability to preserve our language.'),
    ('Тирәнрәк уйлап карасак, әйткәнемчә, сөйләшер сүзләр, уйланырлык уйлар бар.', 'If we think more deeply, as I said, there are words to discuss and thoughts worth pondering.'),
    ('Бала дөньяга килә, беренче тапкыр туган нигезендә үзенең тавышын яңгырата.', 'A child comes into the world and for the first time makes its voice heard in its family home.'),
]),
('c2-gov', [
    ('Күп эшләр башкарылган, әмма Тәтеш районы күрсәткечләре буенча урталыкта да түгел.', "A great deal of work has been done, but by its indicators Tetyushi district isn't even in the middle."),
    ('Бу форумда да мөселманнар һәм татар милләте алдында торган проблемалар өйрәнелер.', 'At this forum, too, the problems facing Muslims and the Tatar nation will be examined.'),
    ('Квестның төп максаты - республиканың икетеллелек канунын куллануны контрольдә тоту.', "The main aim of the quest is to monitor the application of the republic's law on bilingualism."),
    ('Җәмгыять тормышында актив катнашыгыз, остазларыгыздан килгән традицияләрне саклагыз.', 'Take an active part in the life of society and preserve the traditions handed down by your mentors.'),
]),
('c2-lit', [
    ('Адаптация - ул алган тирән белемнәрне Россия шартларына яраклаштыру дигән сүз.', 'Adaptation means fitting the deep knowledge one has gained to Russian conditions.'),
    ('Әдәбият фәне методологиясен камилләштерү турында мәкаләләр белән чыгышлар ясый.', 'He gives talks and publishes articles on improving the methodology of literary studies.'),
    ('Авазлар тамактан гына түгел, карыннан ук агылганда төрлесе була торгандыр инде.', 'I suppose sounds come out differently when they flow not just from the throat but from the very belly.'),
    ('Авыл халкы исә, председатель белән Хәлимәне жәлләп, тавышсыз гына эчтән үкседе.', 'The villagers, pitying the chairman and Khalima, sobbed silently inside.'),
]),
('c2-soc', [
    ('Дөньяда, илебездә һәм республикада булган вакыйгалар турында турыдан-туры мәгълүмат алабыз.', 'We receive first-hand information about events in the world, in our country and in the republic.'),
    ('Сабантуйларга барганда һәрвакыт шул төбәктә яшәгән милләттәшләребезгә бүләкләр алып баралар.', 'When going to Sabantuys, they always take presents to our fellow Tatars living in that region.'),
    ('Студентларга Төркия Республикасының дәүләт стипендиясе түләнә һәм тулай торакта урын бирелә.', 'Students are paid a state scholarship of the Republic of Turkey and given a place in a hall of residence.'),
    ('Кызганыч, бүген күп ирләр хатын-кызларның зифа сыннарыннан, озын чәчләреннән башкасын күрмиләр.', 'Sadly, many men today see nothing in women but their slender figures and long hair.'),
]),
('c2-tale', [
    ('Кайткач, елашып күрешәләр, әтисенә-әнисенә гомерлек байлык бирә, балаларын күрсәтә.', 'When they come home they embrace in tears, he gives his father and mother wealth for life and shows them their grandchildren.'),
    ('Әтиләре намазга киткәч, бу кызлар кычкырышып, шау-гөр килеп уйнаганнар да уйнаганнар.', 'When their father went to prayers, these girls played on and on, shouting and making a racket.'),
    ('Аргамаклар алда ни көткәнен сизенәләр бугай, борын тишекләре дөянеке сыман киерелгән.', "The steeds seem to sense what lies ahead; their nostrils are flared like a camel's."),
    ('Ни күзе белән күрсен, сандык эче туп-тулы алтын-көмеш, энҗе-мәрҗән, кыйммәтле ташлар.', 'And what does he see — the chest is full to the brim of gold and silver, pearls and coral and precious stones.'),
]),
('c2-life', [
    ('Кое төбеннән караучыга күк бәләкәй, энә тишегеннән караучыга дөнья бәләкәй.', 'To one looking up from the bottom of a well the sky is small; to one looking through the eye of a needle the world is small.'),
    ('Шул вакытта телевидениедә үзем теләгәнне эшләп, бәйсез журналистка әйләндем.', 'At that time I did what I wanted on television and became an independent journalist.'),
    ('Хәйрия белән шөгыльләнергә күбрәк вакыты калсын өчен махсус шулай эшләгән ул.', 'He did it on purpose so as to have more time left for charity work.'),
    ('Атлана алмасаң, ялына ябышырга, ялына ябыша алмасаң, койрыгына ябышырга тырыш.', "If you can't mount the horse, try to grab its mane; if you can't grab its mane, grab its tail."),
]),
('c2-gov', [
    ('Икенче төркемдәге муниципалитетларда ул республика буенча уртача күрсәткечтән түбән.', "In the municipalities of the second group it is below the republic's average."),
    ('Проект Татарстан Республикасы Мәгариф һәм фән министрлыгы белән бергә гамәлгә ашырыла.', 'The project is being carried out together with the Ministry of Education and Science of the Republic of Tatarstan.'),
    ('Адвокатның сүзләренә караганда, Марат бөтен гөнаһларны үз өстенә алыр дәрәҗәгә җиткән.', 'According to his lawyer, Marat had reached the point of taking all the blame upon himself.'),
    ('Халкыбыз, илебез һәм Татарстаныбыз хакына кылган батырлыкларыгыз өчен чиксез зур рәхмәт!', 'Boundless thanks for the heroic deeds you performed for the sake of our people, our country and our Tatarstan!'),
]),
('c2-lit', [
    ('Шагыйрьнең күп кенә лирик шигырьләре композиторлар тарафыннан музыкага салынган.', "Many of the poet's lyric poems have been set to music by composers."),
    ('Китап халкыбызның мәдәни мирасы, фольклоры белән кызыксынучыларга тәкъдим ителә.', "The book is recommended to those interested in our people's cultural heritage and folklore."),
    ('Алайса, сез сүзнең урынлы кулланылышы, гомумән, сүз кадеренә игътибар итәсездер.', 'So you must pay attention to the apt use of words and, in general, to the value of the word.'),
    ('Шушы нигездә татар әдәбияты классигы, Әмирхан хәзрәтнең оныгы Фатих Әмирхан туа.', 'It was on this basis that the classic of Tatar literature Fatikh Amirkhan, grandson of Amirkhan hazrat, was born.'),
]),
('c2-soc', [
    ('Кызганыч, авыл җирендә сәнгать мәктәпләре булмау никадәрле талантларны дөньяга чыгармый калдыра.', 'Sadly, the lack of art schools in the countryside leaves so many talents undiscovered.'),
    ('Программа кысаларында бизнес-планның методлары, аны чынга ашыру этаплары белән тәфсилләп танышырсыз.', 'As part of the programme you will become familiar in detail with business-plan methods and the stages of putting one into practice.'),
    ('Чөнки кешедәге культура дәрәҗәсе бездә шундый түбән, без инде хәзер күп нәрсәләрне аңламый башладык.', "Because the level of culture in people here is so low, we've already begun to fail to understand many things."),
    ('Кинога, фотога төшердек, альбомнар ясадык, аның сугышчысы исәпләнгән якташларыбыз исемлеген барладык.', 'We filmed and photographed, made albums and compiled a list of our fellow countrymen counted among his soldiers.'),
]),
('c2-tale', [
    ('Әмма ышансагыз ышаныгыз, ышанмасагыз юк, якын тирәдә мондый атны алырдай кеше чыкмый.', "But believe it or not, there's nobody around here who could buy such a horse."),
    ('Анда калган җиде аргамакны, кошны, думбраны һәм кызны алып, өйләренә кайтып киттеләр.', 'Taking the seven steeds left there, the bird, the dombra and the girl, they went home.'),
    ('Башына өрпәк салып йөри, бәрәңге базларында, идән асларында, ташландык мунчаларда тора.', 'He goes about with a cloth over his head and lives in potato cellars, under floors and in abandoned bathhouses.'),
    ('Вәзирләрне чакыртып алып, егетне азаплаулары өчен, аларга берәм-берәм җәзаларын бирделәр.', 'They summoned the viziers and punished them one by one for tormenting the young man.'),
]),
('c2-life', [
    ('Авырту, сызлану кебек яман хисләрне татып карагач даруханәгә, табибка чабабыз.', "Once we've tasted bad feelings like aches and pains, we run to the chemist's and the doctor."),
    ('Шул вакыттан башлап, без бер-беребезгә йөрешмәскә, күрешмәскә сүз куешкан идек.', 'From that time on we had agreed not to visit or see one another.'),
    ('Илнур үзенә кунакка килгән берәүгә өр-яңа, галәмәт зур коттеджын күрсәтеп йөри.', 'Ilnur shows a guest around his brand-new, enormous cottage.'),
    ('Рус мохитендә үскәнгәме, беренче сыйныфта укыганда рус җырлары гына җырлый идем.', 'Perhaps because I grew up among Russians, in the first class I sang only Russian songs.'),
]),
('c2-gov', [
    ('Яшьләргә дәүләт ярдәмен камилләштерү бик мөһим, чөнки Татарстанның киләчәге алар кулында.', "Improving state support for young people is very important, because Tatarstan's future is in their hands."),
    ('Күргәзмәләр үзәге территориясендә Татарстан тауар җитештерүчеләренең даими күргәзмәсе эшли.', 'A permanent exhibition of Tatarstan manufacturers operates on the grounds of the exhibition centre.'),
    ('Хәзерге вакытта бу вакыйганың барлык нечкәлекләрен ачыклауга юнәлдерелгән чаралар үткәрелә.', 'Measures are now being taken to clarify every detail of this incident.'),
    ('Аерым алганда, сәнәгатьтә, сәүдәдә, авыл хуҗалыгында производство күләменең кимүе күзәтелә.', 'In particular, a fall in production is being observed in industry, trade and agriculture.'),
]),
('c2-lit', [
    ('Чит илләрдә йөрү башка халыкларның тормышын сурәтләгән әсәрләр тууга сәбәп була.', 'Travelling abroad gives rise to works depicting the lives of other peoples.'),
    ('Рәссамнар тудырган матурлыктан хәерчелектә, ялгызлыкта үлгән кешеләргә ни мәгънә?', 'What does the beauty created by artists mean to people who died in poverty and loneliness?'),
    ('Тинчурин үзенең әсәрләре белән масса арасында яхшы танылган драматурглардан санала.', 'Tinchurin is considered one of the playwrights who became well known to the masses through his works.'),
    ('Чын халыкчан иҗаты аның табигый моңына һәм үзенчәлекле тембрлы тавышына нигезләнде.', 'His truly popular art was founded on his natural soulful melody and his distinctive timbre.'),
]),
('c2-tale', [
    ('Спорт күнегүләренең берсендә турниктан егылып, имгәнеп, гомерлеккә йөри алмас хәлдә кала.', 'In one of his training sessions he fell from the horizontal bar, was injured, and was left unable to walk for life.'),
    ('Үзенең бәхетсезлегенә кызның җаны әрнегән, ләкин бәхетсезлеге өчен берәүне дә гаепләмәгән.', "The girl's soul grieved at her misfortune, but she blamed no one for it."),
    ('Шул заманда, бик каты ышкуга чыдый алмыйча, алтмыш колачлы алтын тирәк шартлап төбеннән сынды.', 'At that moment, unable to bear the hard rubbing, the golden poplar sixty fathoms tall cracked and broke off at the root.'),
    ('Шуннан киңәшәләр дә, егет үзе өйдә калып, ата-аналарын, туганнарын кырык пар атка утыртып җибәрә.', 'Then they take counsel, and the young man stays at home and sends his parents and relatives off in forty pairs of horses.'),
]),
('c2-life', [
    ('Ишәк аңгыра һәм күндәм булганга әзмәвердәй адәмнәрне үз сыртына атландырып йөртә.', 'Because the donkey is foolish and docile, it carries hulking men on its back.'),
    ('Чөнки миллионлаган кеше дөреслек һәм гаделлек яклы, аларны куркытырга мөмкин түгел.', 'Because millions of people are on the side of truth and justice, and they cannot be intimidated.'),
    ('Беләсеңме, әни, мин беркайчан да йоклаганда гырлый торган кешегә кияүгә чыкмаячакмын.', "You know, Mum, I'll never marry a man who snores in his sleep."),
    ('Алардан котылуның башка, үзе өчен, беренче карашка, чагыштырмача зарарсызрак юлын тапты.', 'He found another way out of them that was, for him, at first sight comparatively less harmful.'),
]),
('c2-gov', [
    ('Күңелләрегез һәрчак саф, изге, җаныгыз-тәнегез сау-сәламәт, кул-аякларыгыз сызлаусыз булсын.', 'May your hearts always be pure and holy, your souls and bodies healthy, and your arms and legs free of pain.'),
    ('Кадерле татарстанлылар, сезнең һәммәгезгә бәхет, исәнлек-саулык, тынычлык һәм иминлек телим.', 'Dear people of Tatarstan, I wish you all happiness, good health, peace and well-being.'),
    ('Барлык татарстанлыларга мөрәҗәгать итеп, халык санын алуда һәркемне актив катнашырга чакырам.', 'Addressing all the people of Tatarstan, I call on everyone to take an active part in the census.'),
    ('Аерым игътибарны шәһәр башлыгы дәүләт имтиханнары вакытында кагыйдә бозуларны булдырмауга юнәлтә.', 'The mayor pays special attention to preventing rule-breaking during state exams.'),
]),
('c2-lit', [
    ('Училищены тәмамлап кайткач, аны Минзәлә дәүләт драма театрына актер итеп җибәрәләр.', 'After finishing college, he is sent to the Menzelinsk State Drama Theatre as an actor.'),
    ('Романның яртыдан артыгы Зыяның солдатка китү, Мәрьямнән аерылу вакыйгаларына бирелә.', "More than half of the novel is devoted to Ziya's going off to be a soldier and his parting from Maryam."),
    ('Авылдагы әткәй-әнкәсе, дуслары, алма бакчалары, чишмә буйлары сагындырып үзәген өзә.', 'His parents in the village, his friends, the apple orchards and the banks of the spring make him ache with longing.'),
    ('Автор-башкаручы буларак танылган бу татар кызы рус, татар, инглиз телләрендә җырлый.', 'This Tatar girl, known as a singer-songwriter, sings in Russian, Tatar and English.'),
]),
('c2-tale', [
    ('Моңа тегүчеләрдәге унбиш потлы гер ташын китерделәр, анда аның үзенең дә, улының да исеме язылган.', "They brought him the fifteen-pood weight from the tailors', which had both his name and his son's written on it."),
    ('Сәлам биреп, исәнлек-саулык сорашып, үзенең хәлен сөйли башлый, кырыгына кырык кыз кирәклекне әйтә.', 'He greets them, asks after their health and begins to explain his situation: he needs forty girls for his forty sons.'),
    ('Әлеге юл чатындагы язулы баганага барып җитсә, абыйлары кайтып җитмәгәнен белде, аларны эзләргә китте.', "When he reached the signpost at this crossroads, he learned that his brothers hadn't come back and went to look for them."),
    ('Болар тагын бер хәйлә корып, бу егетне бер пәри патшасына алтын канатлы кош алырга җибәрергә булдылар.', 'Hatching another plot, they decided to send this young man to a fairy king for a bird with golden wings.'),
]),
('c2-life', [
    ('Бүген без хыялыбызда үсмер чакка әйләнеп кайттык, сыйныфташлар, укытучылар белән очраштык.', 'Today in our dreams we went back to our teenage years and met our classmates and teachers.'),
    ('Әлеге сыйфатлар кешенең иҗтимагый һәм социаль җитлегүенең бер дәлиле буларак, аеруча әһәмиятле.', "These qualities are especially important as evidence of a person's civic and social maturity."),
    ('Менә бит, тырышсам, чыннан да, булдырам, башкаларныкыннан аерылып торырлык рәсемнәр ясыйм, дим.', "There you go — if I try, I really can do it; I can paint pictures that stand out from everyone else's, I tell myself."),
    ('Бу дөньяда нинди генә биеклекләргә ирешсәк тә, уңышларыбызның башында укытучы торганын һәркем таный.', 'Whatever heights we reach in this world, everyone acknowledges that a teacher stands at the root of our success.'),
]),
('c2-gov', [
    ('Актлар матди дәлилләрне барлаганда, документларны, матди кыйммәтләрне кулланудан чыгарганда языла.', 'Reports are drawn up when material evidence is inventoried and when documents and valuables are withdrawn from use.'),
    ('Татарстан белән Башкортстан рәсми шәхесләре, гадәттәгечә, үзләре әзерләгән бүләкләрне дә тапшырды.', 'The officials of Tatarstan and Bashkortostan, as usual, also exchanged gifts they had prepared themselves.'),
    ('Авыл хезмәтчәннәренә, бүгенге уңышларның нигезен салган тармак ветераннарына аерым рәхмәт белдерде.', "He expressed special thanks to rural workers and to the veterans of the sector who laid the foundations of today's successes."),
    ('Бу этапта билгеле сәбәпләр аркасында төп дулкында катнаша алмаучы чыгарылыш укучылары имтихан бирә.', 'At this stage, exams are taken by school leavers who for certain reasons could not take part in the main wave.'),
]),
('c2-lit', [
    ('Әлеге әсәрләр дә, күләменә-ниенә карамастан, уй-газапларсыз, интегүсез дөньяга килми.', 'These works too, whatever their size, do not come into the world without anguish of thought and suffering.'),
    ('Татарстан Республикасы Фәннәр академиясенең мөхбир әгъзасы, атказанган фән эшлеклесе.', 'He is a corresponding member of the Academy of Sciences of the Republic of Tatarstan and an honoured scientist.'),
    ('Нәсел сыйфатлары, милли сыйфатлар күзәтелеп, алар идеал дәрәҗәсенә күтәреп сурәтләнә.', 'Hereditary and national qualities are observed and portrayed raised to the level of an ideal.'),
    ('Авыруына карамастан, ул соңгы көнгә кадәр фәнни, җәмәгатьчелек эше белән шөгыльләнде.', 'Despite his illness, he continued his scholarly and public work until his last day.'),
]),
('c2-life', [
    ('Әмма бу күптөрлелек аларга беркайчан да үзләрен бердәм татар халкы итеп тоярга комачауламаган.', 'But this diversity never prevented them from feeling themselves to be one Tatar people.'),
    ('Әмма большевистик режим вакытында безнең әдәбиятта ханбикә турында бер генә әсәр дә дөнья күрмәде.', 'But under the Bolshevik regime not a single work about the queen was published in our literature.'),
    ('Туган тел халыкның тарихын, рухын, ерак гасырлардан буыннан-буынга килүче гореф-гадәтләрне чагылдыра.', "A native language reflects a people's history, its spirit and the customs passed down the generations from distant centuries."),
    ('Әлеге система Россиядә бик таралыш тапмаган, әмма Европаның әйдәп баручы университетлары аны куллана.', "This system isn't very widespread in Russia, but Europe's leading universities use it."),
]),
('c2-gov', [
    ('Депутатларны Программа белән Татарстан Республикасы Икътисад министры Мидхәт Шаһиәхмәтов таныштырды.', 'The Programme was presented to the deputies by the Minister of Economy of the Republic of Tatarstan, Midkhat Shagiakhmetov.'),
    ('Менә шушыларны кеше үти алмаган вакытта, шуны үтәргә кешенең сәләте җитмәгән вакытта законнар языла.', 'Laws are written for the times when people cannot fulfil these things, when they lack the capacity to do so.'),
    ('Без суднолар төзелешендә, автомобиль сәнәгатендә һәм нефть химиясендә алдынгы технологияләр кертәбез.', 'We are introducing advanced technologies in shipbuilding, the car industry and petrochemicals.'),
    ('Фестиваль Татарстан Республикасы Президенты һәм Татарстан Республикасы Хөкүмәте теләктәшлегендә уздырыла.', 'The festival is held with the support of the President and the Government of the Republic of Tatarstan.'),
]),
('c2-lit', [
    ('Такталачык урта мәктәбендә белем алганда, Ленар каләм тибрәтә башлый, иҗатка тартыла.', 'While studying at Taktalachyk secondary school, Lenar begins to write and is drawn to creative work.'),
    ('Чөнки әкиятне балалар укый, алар үскәннән соң үз балаларына шул әкиятләрне сөйләячәк.', "Because children read fairy tales, and when they grow up they'll tell those tales to their own children."),
    ('Газета-журнал редакцияләрендә озак эшләү әдипнең журналистлык талантын да ачып җибәрә.', "Long years of work in newspaper and magazine offices also revealed the writer's talent as a journalist."),
    ('Геройлар тамашачының симпатиясен казана алмый икән, әсәрдә нинди драматизм була алсын?', "If the characters can't win the audience's sympathy, what drama can there be in the work?"),
]),
('c2-lit', [
    ('Инде, мөгаен, үзем хәтерләмәсәм дә, шигырь-такмак чыгаруым күрше-тирәгә дә сизелгәндер.', "I suppose, though I don't remember it myself, my making up verses and ditties must have been noticed by the neighbours."),
    ('Картинада фашистлар тарафыннан җәзалап үтерелгән каһарман шагыйрь Муса Җәлил сурәтләнә.', 'The painting depicts the heroic poet Musa Jalil, executed by the fascists.'),
    ('Гарәп графикасы нигезендәге литерлар өчен рәсемнәр татар дин әһелләре тарафыннан ясала.', 'The designs for the letters based on Arabic script are made by Tatar religious scholars.'),
    ('Җидееллык белемне туган авылында ала, сигезенче классны Баулы урта мәктәбендә тәмамлый.', 'He receives his seven-year schooling in his native village and finishes the eighth class at Bavly secondary school.'),
]),
('c2-lit', [
    ('Халык мәкаленә нигезләнгән бу җыр җиңел яшәргә күнеккәннәрнең яшәү фәлсәфәсен чагылдыра.', 'This song, based on a folk proverb, reflects the life philosophy of those used to an easy life.'),
    ('Хатын-кызның гүзәллегенә, зиһененә, талантына, сөйкемлелегенә меңнәрчә гасыр дан җырлана.', "For thousands of centuries songs have praised woman's beauty, intelligence, talent and charm."),
    ('Панаевлар нәселеннән байтак күренекле кешеләр - язучылар, шагыйрьләр, музыкантлар чыккан.', 'Quite a number of prominent people — writers, poets and musicians — came from the Panaev family.'),
    ('Акмулла укулары чараларының Башкортстан дәүләт педагогия университетында башлануы табигый.', 'It is natural that the Akmulla Readings began at the Bashkir State Pedagogical University.'),
]),
('c2-lit', [
    ('Акча артыннан куган, бер-берсен ашарга торган, наркоманнар, эчкечеләр турында язып булмый.', "You can't write about people who chase money, are ready to devour one another, or about drug addicts and drunkards."),
    ('Егет белән кыз мәхәббәт ялкыннарына бирелеп, аерылып яшәү заманнарының зарларын сөйләшәләр.', 'Given over to the flames of love, the young man and the girl lament the times they had to live apart.'),
    ('Шунлыктан кеше күзенә күренерлек булган һәрнәрсәсендә бер буяу, бер куык, бер күтәрелү була.', 'Hence everything visible to the human eye has a coat of paint, a bubble, an exaltation.'),
    ('Шуңа күрә дә күп кенә композиторлар, аның иҗатына мөрәҗәгать итеп, шигырьләрен көйгә салалар.', 'That is why many composers turn to his work and set his poems to music.'),
]),
('c2-lit', [
    ('Җентекләп карагач, реставрация ясаган кешенең язулары камиллек ягыннан бераз калышканы сизелә.', "On close inspection one can sense that the restorer's inscriptions lag somewhat behind in perfection."),
    ('Шушы вакыт эчендә ул империя төрмәләрен дә, ятимлек ачысын, акчасызлык газабын да татып өлгерә.', "In this time he manages to taste the empire's prisons, the bitterness of being an orphan and the agony of poverty."),
    ('Мәктәп елларыннан ук район гәзит битләрендә мәкаләләрем, хикәяләрем, шигырьләрем дөнья күрделәр.', 'From my school years my articles, stories and poems appeared in the pages of the district newspaper.'),
    ('Минем дәреслектә булмаган, үзем танышкан шигырьләре хакындагы фикерләрем белән уртаклашасым килде.', "I wanted to share my thoughts about his poems that weren't in the textbook, ones I'd come across myself."),
]),
]
NAMES = {"c2-gov": ("Official Language", "Рәсми тел"), "c2-faith": ("Faith and Ethics", "Иман һәм әхлак"), "c2-lit": ("Criticism", "Әдәби тәнкыйть"),
 "c2-soc": ("Commentary", "Публицистика"), "c2-hist": ("History", "Тарих"), "c2-tale": ("Epic Style", "Дастаннар"), "c2-life": ("Nuance", "Нечкәлекләр")}
assert len(S) == 100, len(S)
cnt = {}
for i, (top, items) in enumerate(S, 1):
    cnt[top] = cnt.get(top, 0) + 1
    en, tt = NAMES[top]
    L(i, f"{en} {cnt[top]}", f"{tt} {cnt[top]}", items, top)
c.save()
