import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import Course
c = Course("a1", "a1")
c.T("a1-greetings", "Greetings and Politeness", "Сәлам! · Хәерле иртә! · Рәхмәт! · Сау бул! / Сау булыгыз!",
    "Tatar greetings are short and warm. Сәлам (hello) works almost everywhere; Хәерле иртә / көн / кич wish someone a good morning, day or evening. "
    "Many polite words have two forms: a plain one for one friend (Сау бул!, Рәхим ит!) and one with -ыгыз/-егез for several people or anyone you address politely (Сау булыгыз!, Гафу итегез).",
    "Tatar is a Turkic language spoken by several million people. It is an official language of the Republic of Tatarstan alongside Russian, and its closest relative is Bashkir.",
    [("A", "Сәлам!", "Hello!"), ("B", "Сәлам! Хәлләр ничек?", "Hello! How are you?"), ("A", "Яхшы, рәхмәт.", "Fine, thank you."), ("B", "Сау бул!", "Bye!")])
c.T("a1-pronouns", "I, You, He: Personal Pronouns", "мин · син · ул · без · сез · алар",
    "The pronouns are мин (I), син (you, one friend), ул (he, she or it — Tatar has no gender), без (we), сез (you, several people or polite) and алар (they). "
    "In everyday speech the word for am/is/are is simply left out: Мин студент — I (am a) student. Ул татар — He (is a) Tatar.",
    "Because ул means both he and she, Tatar sentences never tell you a person's gender through the pronoun — context does that job.",
    [("A", "Сез кем?", "Who are you?"), ("B", "Мин студент. Ә сез?", "I'm a student. And you?"), ("A", "Мин табиб.", "I'm a doctor.")])
c.T("a1-possessive", "My Mother, Your Father: Possessive Endings", "минем әни-ем · синең әти-ең · аның кыз-ы · безнең әти",
    "Possession is marked twice: by a pronoun (минем my, синең your, аның his/her, безнең our) and by an ending on the noun: -ым/-ем for my, -ың/-ең for your, -ы/-е for his/her. "
    "The pronoun can be dropped because the ending already says it all: Әнием белми — my mum doesn't know.",
    "Tatar words have vowel harmony: words with back vowels (а, о, у, ы) take back-vowel endings like -ым, and words with front vowels (ә, ө, ү, е, и) take front ones like -ем.",
    [("A", "Бу кем?", "Who is this?"), ("B", "Бу минем әнием.", "This is my mother."), ("A", "Ә бу кем?", "And who is this?"), ("B", "Бу минем әтием.", "This is my father.")])
c.T("a1-this", "This Is…: Бу and Questions with -мы", "Бу нәрсә? · Бу — китап. · Бу мәче-ме?",
    "Бу means this and ул means that. To say what something is, just put the two words side by side: Бу китап — this (is a) book. "
    "To turn a statement into a yes/no question, add -мы or -ме to the word you ask about: Бу мәче — this is a cat; Бу мәчеме? — is this a cat?",
    "The dash in Бу — китап is only punctuation. It marks the missing is and is often left out in writing.",
    [("A", "Бу нәрсә?", "What is this?"), ("B", "Бу — китап.", "This is a book."), ("A", "Бу мәчеме?", "Is this a cat?"), ("B", "Әйе.", "Yes.")])
c.T("a1-locative", "Where Things Are: -да/-дә, -та/-тә", "өй-дә · Казан-да · кесә-мдә · өй артында",
    "The ending -да/-дә (after voiceless consonants -та/-тә) means in, at or on: өйдә — at home, Казанда — in Kazan, паркта — in the park. "
    "Words like артында (behind) and астында (under) follow the noun: өй артында — behind the house, урындык астында — under the chair.",
    "Кайда means where (at what place) and кая means where to — but in everyday speech кая is also often used for where.",
    [("A", "Әтиең кайда?", "Where's your dad?"), ("B", "Ул өйдә юк.", "He's not at home."), ("A", "Ә әниең?", "And your mum?"), ("B", "Ул Казанда.", "She's in Kazan.")])
c.T("a1-present", "I Read, You Write: The Present Tense", "яз-а-м · укы-йм · яз-а-сың · сөйләш-ә-сез · яз-мый-м",
    "The present tense adds -а/-ә (or -ый/-и after vowels) to the verb and then a personal ending: -м (I), -сың/-сең (you), nothing (he/she), -быз/-без (we), -сыз/-сез (you all), -лар/-ләр (they). "
    "Язам — I write, язасыз — you (all) write, яза — he writes. The negative uses -мый/-ми: язмыйм — I don't write.",
    "This one tense covers both I write and I am writing: Мин язам can mean either, and context decides.",
    [("A", "Татарча сөйләшәсезме?", "Do you speak Tatar?"), ("B", "Әйе, мин татар телен өйрәнәм.", "Yes, I'm learning Tatar."), ("A", "Сез кофе эчәсезме?", "Do you drink coffee?"), ("B", "Юк, мин чәй яратам.", "No, I like tea.")])
c.T("a1-numbers", "Numbers, Age and Time", "бер · ике · өч · дүрт · биш · алты · җиде · сигез · тугыз · ун",
    "The numbers one to ten are бер, ике, өч, дүрт, биш, алты, җиде, сигез, тугыз, ун; eleven is ун бер (written унбер), eighteen is унсигез. "
    "After a number the noun stays singular: ике мәче — two cats. Age uses the dative: Миңа ун яшь — I am ten (lit. to me ten years). The time is сәгать: Сәгать ничә? — What time is it?",
    "Tatar counts like the other Turkic languages: ун бер is literally ten one, and егерме бер is twenty one.",
    [("A", "Сәгать ничә?", "What time is it?"), ("B", "Сәгать алты инде.", "It's six o'clock already."), ("A", "Сиңа ничә яшь?", "How old are you?"), ("B", "Миңа ун яшь.", "I'm ten.")])
c.T("a1-have", "Having: бар and юк", "минем мәчем бар · аның эте бар · акчам юк · …бармы?",
    "Tatar has no verb to have. Instead it says my cat exists: Минем мәчем бар — I have a cat (lit. my cat there is). "
    "Юк means there isn't: Акчам юк — I have no money. Ask with бармы: Ручкагыз бармы? — Do you have a pen?",
    "The same бар/юк pair also means there is / there isn't on its own: Монда балалар бар — There are children here.",
    [("A", "Синең этең бармы?", "Do you have a dog?"), ("B", "Юк, минем мәчем бар.", "No, I have a cat."), ("A", "Мәчең нинди?", "What is your cat like?"), ("B", "Мәче ак төстә.", "The cat is white.")])
c.T("a1-negation", "Saying No: түгел, юк, -ма", "Мин табиб түгел · Ул өйдә юк · Елама! · Аңламыйм",
    "Tatar has several ways to say no. Түгел negates a description: Мин табиб түгел — I'm not a doctor. Юк says something isn't there. "
    "Verbs take -ма/-мә in commands (Елама! — Don't cry!) and -мый/-ми in the present tense (Аңламыйм — I don't understand).",
    "Начар түгел (lit. not bad) is a common modest way to say something is good.",
    [("A", "Син ачмы?", "Are you hungry?"), ("B", "Юк, мин ач түгел.", "No, I'm not hungry."), ("A", "Ашыкма!", "Don't rush!"), ("B", "Ярый.", "Okay.")])
c.T("a1-questions", "Asking Questions", "кем · нәрсә · кайда · кая · ничек · ничә · кайчан · нигә · …мы/-ме",
    "Question words stay where the answer would be: Ул кем? — Who is he? Сез кайда яшисез? — Where do you live? "
    "For yes/no questions add -мы/-ме to the key word: Сез ялгызмы? — Are you alone? The word order doesn't change.",
    "Нәрсә (what) is often shortened to ни in set phrases, as in Ни хәлләр? — How are things?",
    [("A", "Бу кем?", "Who is this?"), ("B", "Бу минем дустым.", "This is my friend."), ("A", "Ул кайда яши?", "Where does he live?"), ("B", "Казанда.", "In Kazan.")])
c.T("a1-imperative", "Asking and Telling: the Imperative", "кил · килегез · бир · бирегез · әйдә · әйдәгез",
    "The bare verb is a command to one friend: Кил! — Come! Бир! — Give! Adding -ыгыз/-егез makes it plural or polite: Килегез! Керегез! "
    "Әйдә / әйдәгез means come on, let's go. Add зинһар to make any request softer: Зинһар, гафу ит!",
    "Әле after a command softens it, like just: Газета бир әле — Just give me the paper.",
    [("A", "Керегез!", "Come in!"), ("B", "Рәхмәт!", "Thank you!"), ("A", "Утырыгыз, зинһар.", "Please sit down."), ("B", "Рәхмәт! Өегез бик матур.", "Thank you! Your home is very beautiful.")])
c.T("a1-dative", "Going Places: -га/-гә, -ка/-кә", "шәһәр-гә · эш-кә · мәктәп-кә · хастаханә-гә",
    "The ending -га/-гә (after voiceless consonants -ка/-кә) shows where you are going or who receives something: шәһәргә — to town, эшкә — to work, мәктәпкә — to school, Әниемә хат язам — I'm writing a letter to my mum. "
    "Кая барасыз? — Where are you going?",
    "Personal pronouns change in the dative: мин → миңа, син → сиңа, ул → аңа.",
    [("A", "Кая барасыз?", "Where are you going?"), ("B", "Шәһәргә барам.", "I'm going to town."), ("A", "Мин эшкә барам.", "I'm going to work.")])
L = c.L
L(1, "Greetings 1", "Сәламләшү 1", [("Сәлам.", "Hello."), ("Хәерле иртә!", "Good morning!"), ("Хәерле көн!", "Good afternoon!"), ("Хәерле кич!", "Good evening!")], "a1-greetings")
L(2, "Greetings 2", "Сәламләшү 2", [("Рәхмәт!", "Thank you!"), ("Мең рәхмәт!", "Thank you very much!"), ("Юк, рәхмәт.", "No, thank you."), ("Зинһар.", "Please.")], "a1-greetings")
L(3, "Greetings 3", "Сәламләшү 3", [("Сау бул!", "Bye!"), ("Хушыгыз!", "Goodbye!"), ("Тыныч йокы!", "Good night!"), ("Әлегә!", "Bye for now!")], "a1-greetings")
L(4, "Greetings 4", "Сәламләшү 4", [("Рәхим ит!", "Welcome!"), ("Гафу итегез.", "Excuse me."), ("Хәлләр ничек?", "How are you?"), ("Су, зинһар.", "Water, please.")], "a1-greetings")
L(5, "About Me 1", "Минем турында 1", [("Мин студент.", "I'm a student."), ("Мин табиб.", "I am a doctor."), ("Мин турист.", "I'm a tourist."), ("Мин яхшы.", "I'm fine.")], "a1-pronouns")
L(6, "About Me 2", "Минем турында 2", [("Мин ач.", "I am hungry."), ("Мин шат!", "I'm glad!"), ("Мин әзер.", "I am ready."), ("Мин ялгызак.", "I'm lonely.")], "a1-pronouns")
L(7, "About Me 3", "Минем турында 3", [("Сез кайдан?", "Where are you from?"), ("Мин мисырлы.", "I am Egyptian."), ("Мин япон.", "I'm Japanese."), ("Ул татар.", "He's a Tatar.")], "a1-pronouns")
L(8, "About Me 4", "Минем турында 4", [("Минем исемем Алсу.", "My name is Alsu."), ("Мин Казанда яшим.", "I live in Kazan."), ("Миңа утыз яшь.", "I am thirty years old."), ("Мин ашамыйм.", "I am not eating.")], "a1-pronouns")
L(9, "Family 1", "Гаилә 1", [("Ул минем әнием.", "She's my mother."), ("Ул безнең әти.", "He's our father."), ("Бу минем кызым.", "This is my daughter."), ("Минем әтием табиб.", "My father is a doctor.")], "a1-possessive")
L(10, "Family 2", "Гаилә 2", [("Ике апам бар.", "I have two older sisters."), ("Ике улым бар.", "I have two sons."), ("Улыгыз бармы?", "Do you have a son?"), ("Алар балалар.", "They're children.")], "a1-possessive")
L(11, "Family 3", "Гаилә 3", [("Әтиең кайда?", "Where's your dad?"), ("Әни белми.", "Mum doesn't know."), ("Сәлам, бабай.", "Hello, Grandad."), ("Ул безнең анабыз.", "She's our mother.")], "a1-possessive")
L(12, "Family 4", "Гаилә 4", [("Хатынымны яратам.", "I love my wife."), ("Әниегезне яратасызмы?", "Do you love your mother?"), ("Әтиең белән кил.", "Come with your father."), ("Әниемә хат язам.", "I am writing a letter to my mum.")], "a1-possessive")
L(13, "What Is This? 1", "Бу нәрсә? 1", [("Бу нәрсә?", "What is this?"), ("Бу — китап.", "This is a book."), ("Бу — эт.", "This is a dog."), ("Бу мәктәп.", "This is a school.")], "a1-this")
L(14, "What Is This? 2", "Бу нәрсә? 2", [("Бу карандаш.", "This is a pencil."), ("Бу — харита.", "This is a map."), ("Бу курчак.", "This is a doll."), ("Бу боҗра.", "This is a ring.")], "a1-this")
L(15, "What Is This? 3", "Бу нәрсә? 3", [("Бу мәчеме?", "Is that a cat?"), ("Бу үгезме?", "Is that a bull?"), ("Бу пошимы?", "Is that a moose?"), ("Бу балык түгел.", "This isn't a fish.")], "a1-this")
L(16, "What Is This? 4", "Бу нәрсә? 4", [("Бу яхшы.", "That's good."), ("Бу сәер.", "This is strange."), ("Дөрес!", "That's right!"), ("Бу — хәреф.", "This is a letter of the alphabet.")], "a1-this")
L(17, "At Home 1", "Өйдә 1", [("Өем бар.", "I have a house."), ("Бу минем өем.", "This is my home."), ("Бу зур йорт.", "It's a big house."), ("Өй иске.", "The house is old.")], "a1-locative")
L(18, "At Home 2", "Өйдә 2", [("Өең кайда?", "Where is your house?"), ("Өегез бармы?", "Do you have a house?"), ("Ул өйдә юк.", "He's not at home."), ("Бакча өй артында.", "The garden is behind the house.")], "a1-locative")
L(19, "At Home 3", "Өйдә 3", [("Минем фатирым яхшы.", "I have a nice apartment."), ("Бу синең фатирыңмы?", "Is this your apartment?"), ("Песи урындык астында.", "The cat is under the chair."), ("Янчыгым кесәмдә.", "My wallet is in my pocket.")], "a1-locative")
L(20, "At Home 4", "Өйдә 4", [("Тәрәзәне яп!", "Close the window!"), ("Урыныңны җәй.", "Make your bed."), ("Аны өстәлгә куегыз.", "Put it on the table."), ("Өстәлдә алма бар.", "There is an apple on the table.")], "a1-locative")
L(21, "Food and Drink 1", "Ашау-эчү 1", [("Су эчегез.", "Drink water."), ("Ачмы?", "Hungry?"), ("Мин ач түгел.", "I'm not hungry."), ("Син бик ачмы?", "Are you very hungry?")], "a1-present")
L(22, "Food and Drink 2", "Ашау-эчү 2", [("Бу алма татлы.", "This apple is sweet."), ("Бу алмалар зур.", "These apples are big."), ("Ничә алма?", "How many apples?"), ("Бәлеш тәмле.", "The pie is tasty.")], "a1-present")
L(23, "Food and Drink 3", "Ашау-эчү 3", [("Кофе эчәсезме?", "Do you drink coffee?"), ("Мин ит ашамыйм.", "I don't eat meat."), ("Ул бүтән эчми.", "He doesn't drink anymore."), ("Минем балам ач.", "My child is hungry.")], "a1-present")
L(24, "Food and Drink 4", "Ашау-эчү 4", [("Аша да эч.", "Eat and drink."), ("Су ага.", "Water flows."), ("Мин алма яратмыйм.", "I don't like apples."), ("Сез алма яратасызмы?", "Do you like apples?")], "a1-present")
L(25, "Numbers 1", "Саннар 1", [("Өч, ике, бер.", "Three, two, one."), ("Әйе, ике.", "Yes, two."), ("Хәзер унбер.", "It's eleven now."), ("Җидеме?", "Seven?")], "a1-numbers")
L(26, "Numbers 2", "Саннар 2", [("Ике мәчем бар.", "I have two cats."), ("Ике китабың бар.", "You have two books."), ("Аның өч кызы бар.", "He has three daughters."), ("Аның өч баласы бар.", "He has three children.")], "a1-numbers")
L(27, "Numbers 3", "Саннар 3", [("Сиңа ун яшьме?", "Are you ten years old?"), ("Сезгә ничә яшь?", "How old are you?"), ("Миңа унсигез яшь.", "I am eighteen years old."), ("Ике бишең - ун.", "Two times five is ten.")], "a1-numbers")
L(28, "Numbers 4", "Саннар 4", [("Сәгать алты инде.", "It's six o'clock already."), ("Сәгать ничә?", "What time is it?"), ("Тагын бер кат әйт.", "Say it one more time."), ("Бу номерга шалтырат.", "Call this number.")], "a1-numbers")
L(29, "Time 1", "Вакыт 1", [("Бүген шимбә.", "Today is Saturday."), ("Иртәгә дүшәмбе.", "Tomorrow is Monday."), ("Бүген пәнҗешәмбе.", "Today is Thursday."), ("Бүген салкын.", "It's cold today.")], "a1-numbers")
L(30, "Time 2", "Вакыт 2", [("Хәзер вакыт.", "Now is the time."), ("Соңга калма.", "Don't be late."), ("Бүген китәбез.", "We're leaving today."), ("Кайчан очрашабыз?", "When are we meeting?")], "a1-numbers")
L(31, "Time 3", "Вакыт 3", [("Яңа ел белән!", "Happy New Year!"), ("Туган көнең белән!", "Happy birthday!"), ("Тизрәк савыгыгыз!", "Get well soon!"), ("Күңелле төшләр!", "Sweet dreams!")], "a1-numbers")
L(32, "Time 4", "Вакыт 4", [("Иртәгә укымыйбыз.", "We don't have school tomorrow."), ("Сез кайчан эшкә барасыз?", "What time do you go to work?"), ("Рейсыгыз кайчан?", "When is your flight?"), ("Уңайсызрак вакытмы?", "Is this a bad time?")], "a1-numbers")
L(33, "Weather 1", "Һава торышы 1", [("Яңгыр явамы?", "Is it raining?"), ("Яңгыр һаман явамы?", "Is it still raining?"), ("Бераз җилле.", "It's slightly windy."), ("Бүген көн әйбәт.", "The weather is nice today.")], "a1-present")
L(34, "Weather 2", "Һава торышы 2", [("Мин язны яратам.", "I like spring."), ("Мин язны яратмыйм.", "I don't like spring."), ("Кара, ничек салкын!", "Wow, it's so cold!"), ("Ни өчен шулкадәр эссе?", "Why is it so hot?")], "a1-present")
L(35, "Weather 3", "Һава торышы 3", [("Кояш кайда?", "Where is the sun?"), ("Кош күктә.", "The bird is in the sky."), ("Кояш Җирдән бик ерак.", "The Sun is very far from the Earth."), ("Әбиләр чуагы.", "Indian summer.")], "a1-present")
L(36, "Weather 4", "Һава торышы 4", [("Кышын салкын.", "It's cold in winter."), ("Җәен эссе.", "It's hot in summer."), ("Бүген кар ява.", "It's snowing today."), ("Мин кышны яратам.", "I like winter.")], "a1-present")
L(37, "Nature 1", "Табигать 1", [("Елга ага.", "The river flows."), ("Бу елгамы?", "Is it a river?"), ("Күл бик тирән.", "The lake is very deep."), ("Бу күл тирәнме?", "Is this lake deep?")], "a1-locative")
L(38, "Nature 2", "Табигать 2", [("Мин диңгезне яратам.", "I like the sea."), ("Диңгездә утраулар бар.", "There are islands in the sea."), ("Сез чәчәкне күрәсез.", "You see a flower."), ("Бу чәчәкләр чынмы?", "Are these flowers real?")], "a1-locative")
L(39, "Nature 3", "Табигать 3", [("Бу чәчәк шәмәхә төстә.", "This flower is purple."), ("Һава судан җиңелрәк.", "Air is lighter than water."), ("Салават күпере җиде төстә.", "The rainbow has seven colours."), ("Олы корабка — зур диңгез.", "A big ship needs a big sea.")], "a1-locative")
L(40, "Nature 4", "Табигать 4", [("Урманда агачлар күп.", "There are many trees in the forest."), ("Тау бик биек.", "The mountain is very high."), ("Бу агач бик зур.", "This tree is very big."), ("Кырда чәчәкләр бар.", "There are flowers in the field.")], "a1-locative")
L(41, "Animals 1", "Хайваннар 1", [("Песи ак.", "The cat is white."), ("Мәче кара төстә.", "The cat is black."), ("Мәчем бар.", "I have a cat."), ("Аның эте бар.", "She has a dog.")], "a1-have")
L(42, "Animals 2", "Хайваннар 2", [("Этең кайда?", "Where's your dog?"), ("Синең этең бармы?", "Do you have a dog?"), ("Эт синеке.", "The dog is yours."), ("Бу аларның этеме?", "Is it their dog?")], "a1-have")
L(43, "Animals 3", "Хайваннар 3", [("Эт йокламый.", "The dog isn't sleeping."), ("Мәче мияулый.", "The cat says \"meow\"."), ("Бу минем атым.", "It's my horse."), ("Атлар – дус хайваннар.", "Horses are friendly animals.")], "a1-have")
L(44, "Animals 4", "Хайваннар 4", [("Тычкан!", "A mouse!"), ("Каргалар кара.", "Crows are black."), ("Каз - су кошы.", "A goose is a water bird."), ("Миңа эт кирәк.", "I need a dog.")], "a1-have")
L(45, "Colours and Things 1", "Төсләр 1", [("Бу китап кызыл.", "The book is red."), ("Бу алма кып-кызыл.", "This apple is very red."), ("Машина зур.", "The car is big."), ("Бу - яшел куен дәфтәре.", "This is a green notebook.")], "a1-this")
L(46, "Colours and Things 2", "Төсләр 2", [("Син матур.", "You are beautiful."), ("Күзләрең матур.", "Your eyes are beautiful."), ("Дөнья гүзәл!", "The world is beautiful!"), ("Минем сеңлем чибәр.", "My little sister is pretty.")], "a1-this")
L(47, "Colours and Things 3", "Төсләр 3", [("Бу иске яңалыклар.", "This is old news."), ("Яңалыклар бармы?", "Is there any news?"), ("Газетагыз кая?", "Where is your newspaper?"), ("Газеталарым кая?", "Where are my newspapers?")], "a1-this")
L(48, "Colours and Things 4", "Төсләр 4", [("Ул аннан олырак.", "She is older than him."), ("Миңа да унҗиде яшь.", "I'm seventeen too."), ("Ул бик чибәр.", "She is very pretty."), ("Бу коточкыч китап.", "That's a terrible book.")], "a1-this")
L(49, "In the City 1", "Шәһәрдә 1", [("Казанда метро бар.", "There is a metro in Kazan."), ("Казан — Татарстанның башкаласы.", "Kazan is the capital of Tatarstan."), ("Паркта кеше күп.", "There are many people in the park."), ("Кечкенә генә шәһәр.", "It's a small city.")], "a1-dative")
L(50, "In the City 2", "Шәһәрдә 2", [("Бүген шәһәргә барасызмы?", "Are you going to town today?"), ("Мин эшкә барам.", "I go to work."), ("Безне хастаханәгә илтегез.", "Take us to the hospital."), ("Ул шәһәрдә түгел.", "He is not in the city.")], "a1-dative")
L(51, "In the City 3", "Шәһәрдә 3", [("Бу — музей түгел.", "That isn't a museum."), ("Бу шәһәр Франциядә.", "This city is in France."), ("Рум - борынгы шәһәр.", "Rome is an ancient city."), ("Бу сезнең машинагызмы?", "Is this your car?")], "a1-dative")
L(52, "In the City 4", "Шәһәрдә 4", [("Машинам начар хәлдә.", "My car is in bad shape."), ("Китап кибете ачык.", "The bookshop is open."), ("Бәдрәф кайда?", "Where's the toilet?"), ("Лифт кайда?", "Where is the lift?")], "a1-dative")
L(53, "School 1", "Мәктәп 1", [("Мин язам.", "I write."), ("Мин өйрәнәм.", "I am learning."), ("Сез язасызмы?", "Do you write?"), ("Укы!", "Study!")], "a1-present")
L(54, "School 2", "Мәктәп 2", [("Син студентмы?", "Are you a student?"), ("Ул студент.", "He's a student."), ("Мәктәбең кайда?", "Where's your school?"), ("Ручкагыз бармы?", "Do you have a pen?")], "a1-present")
L(55, "School 3", "Мәктәп 3", [("Китапларыгызны ачыгыз.", "Open your books."), ("Минем китапларым күп.", "I have many books."), ("Аңа китапларны бир.", "Give him the books."), ("Иртәгә алар укымый.", "They don't have school tomorrow.")], "a1-present")
L(56, "School 4", "Мәктәп 4", [("Төрек телен өйрәнәм.", "I'm learning Turkish."), ("Инглиз телен өйрәнәм.", "I'm learning English."), ("Ул укый-яза белми.", "She can't read or write."), ("Сиңа иртәгә мәктәпкә.", "You have school tomorrow.")], "a1-present")
L(57, "Languages 1", "Телләр 1", [("Татарча сөйләшәсезме?", "Do you speak Tatar?"), ("Инглизчә сөйләшәсезме?", "Do you speak English?"), ("Алманча сөйләшәсезме?", "Do you speak German?"), ("Мин инглизчә сөйләшәм.", "I speak English.")], "a1-present")
L(58, "Languages 2", "Телләр 2", [("Ул русмы?", "Is he Russian?"), ("Мин корейча сөйләшәм.", "I speak Korean."), ("Мин сине аңламыйм.", "I don't understand you."), ("Аңламыйм.", "I don't get it.")], "a1-present")
L(59, "Languages 3", "Телләр 3", [("Бу кызыклы тел.", "It's an interesting language."), ("Бу тел аңлашылмый.", "This language is hard to understand."), ("Татар телен өйрәнегез.", "Learn the Tatar language."), ("Татарча җавап бир!", "Answer in Tatar!")], "a1-present")
L(60, "Languages 4", "Телләр 4", [("Интернетта татарча сайтлар аз.", "There are few Tatar websites on the Internet."), ("Исемлектә минем телем юк!", "My language isn't on the list!"), ("Бу — фин-угыр теле.", "It's a Finno-Ugric language."), ("Сүз бирәм сиңа.", "I give you my word.")], "a1-present")
L(61, "Work 1", "Эш 1", [("Ул табиб.", "He is a doctor."), ("Алар докторлар.", "They are doctors."), ("Мин табиб түгел.", "I'm not a doctor."), ("Минем хатыным - табиб.", "My wife is a doctor.")], "a1-negation")
L(62, "Work 2", "Эш 2", [("Эшлисезме?", "Are you working?"), ("Ул мәшгуль.", "He's busy."), ("Нәрсә пешерәсез?", "What are you cooking?"), ("Сез яхшы әзерлисез.", "You're a good cook.")], "a1-negation")
L(63, "Work 3", "Эш 3", [("Офис уң якта.", "The office is on the right."), ("Офиста караңгы.", "It's dark in the office."), ("Мин эштә иң яше.", "I'm the youngest at work."), ("Аның эше бертөрле.", "Her work is repetitive.")], "a1-negation")
L(64, "Work 4", "Эш 4", [("Аның акчасы күп.", "He has a lot of money."), ("Бүген минем акчам юк.", "I have no money today."), ("Синең акчаң күп түгел.", "You don't have a lot of money."), ("Ул башка эшләми.", "It doesn't work anymore.")], "a1-negation")
L(65, "Likes 1", "Яратам 1", [("Мин сине яратам.", "I love you."), ("Мин футбол яратам.", "I like football."), ("Мин борчак яратам.", "I like peas."), ("Мин гөмбә яратмыйм.", "I don't like mushrooms.")], "a1-present")
L(66, "Likes 2", "Яратам 2", [("Син алма яратмыйсыңмы?", "Don't you like apples?"), ("Кем аны яратмый?", "Who doesn't love her?"), ("Нәрсәне күбрәк ошатасыз?", "What do you prefer?"), ("Крендель телисезме?", "Would you like a pretzel?")], "a1-present")
L(67, "Likes 3", "Яратам 3", [("Безгә лидер кирәк.", "We need a leader."), ("Миңа җилләткеч кирәк.", "I need the fan."), ("Безнең белән барасызмы?", "Will you come with us?"), ("Мәхәббәт - нәрсә ул?", "Love — what is it?")], "a1-present")
L(68, "Likes 4", "Яратам 4", [("Мин чәй яратам.", "I like tea."), ("Ул кофе яратмый.", "She doesn't like coffee."), ("Без музыка тыңлыйбыз.", "We listen to music."), ("Сез нәрсә яратасыз?", "What do you like?")], "a1-present")
L(69, "Feelings 1", "Хисләр 1", [("Ул бәхетле.", "He is happy."), ("Сез бәхетлеме?", "Are you happy?"), ("Ул авырый.", "He is ill."), ("Миңа күңелсез.", "I'm bored.")], "a1-negation")
L(70, "Feelings 2", "Хисләр 2", [("Ачуланма миңа.", "Don't be angry with me."), ("Мин ачуланмыйм инде.", "I'm not angry anymore."), ("Ул инде ачуланмый.", "He isn't angry anymore."), ("Барысы да яхшы.", "Everything is fine.")], "a1-negation")
L(71, "Feelings 3", "Хисләр 3", [("Сез нәрсәдән куркасыз?", "What are you afraid of?"), ("Мин сугыштан куркам.", "I'm afraid of war."), ("Балачак - бәхетле чак.", "Childhood is a happy time."), ("Зыяны юк.", "There's no harm in it.")], "a1-negation")
L(72, "Feelings 4", "Хисләр 4", [("Начар түгел.", "Not bad."), ("Хафаланмагыз.", "Don't worry."), ("Ашыкма.", "Don't rush."), ("Елама!", "Don't cry!")], "a1-negation")
L(73, "Having 1", "Бар һәм юк 1", [("Минем филем бар.", "I have an elephant."), ("Миндә алар юк.", "I don't have any."), ("Тылмачыгыз бармы?", "Do you have an interpreter?"), ("Билетлар сездәме?", "Do you have the tickets?")], "a1-have")
L(74, "Having 2", "Бар һәм юк 2", [("Монда балалар бар.", "There are children here."), ("Вакытыбыз бик аз.", "We have very little time."), ("Буш вакытыгыз күпме?", "How much free time do you have?"), ("Вакыт җәдвәлең бармы?", "Do you have a timetable?")], "a1-have")
L(75, "Having 3", "Бар һәм юк 3", [("Һавасыз тормыш юк.", "There is no life without air."), ("Аның тәҗрибәсе зур.", "He has a lot of experience."), ("Аның нияте яхшы.", "She has good intentions."), ("Анда желатин бармы?", "Does it have gelatine in it?")], "a1-have")
L(76, "Having 4", "Бар һәм юк 4", [("Аның акчасы юк.", "She has no money."), ("Ике тубың бар.", "You have two balls."), ("Өстәлдә бер алма бар.", "There is one apple on the table."), ("Декабрьдә утыз бер көн.", "December has thirty-one days.")], "a1-have")
L(77, "Saying No 1", "Түгел 1", [("Юк.", "No."), ("Шаулама.", "Don't make noise."), ("Кагылма!", "Don't touch it!"), ("Сикермә!", "Don't jump!")], "a1-negation")
L(78, "Saying No 2", "Түгел 2", [("Бәхәсләшмә.", "Don't argue."), ("Онытмагыз.", "Don't forget."), ("Мине онытма.", "Don't forget me."), ("Безне онытма!", "Don't forget us!")], "a1-negation")
L(79, "Saying No 3", "Түгел 3", [("Мин монда калмыйм.", "I won't stay here."), ("Мин телевизор карамыйм.", "I don't watch television."), ("Ут белән уйнама!", "Don't play with fire!"), ("Әйтәсеңме-юкмы?", "Will you tell me or not?")], "a1-negation")
L(80, "Saying No 4", "Түгел 4", [("Тинтәк булма.", "Don't be silly."), ("Хәзер, хәзер!", "Just a moment!"), ("Һичшиксез.", "Without a doubt."), ("Эт йокламый, ул уйный.", "The dog isn't sleeping, it's playing.")], "a1-negation")
L(81, "Where? 1", "Кайда? 1", [("Сез кайда?", "Where are you?"), ("Ул кая?", "Where is he?"), ("Малайлар кайда?", "Where are the boys?"), ("Сәгатем кайда?", "Where's my watch?")], "a1-locative")
L(82, "Where? 2", "Кайда? 2", [("Кая барабыз?", "Where are we going?"), ("Кая барасыз?", "Where are you going?"), ("Кайда очрашабыз?", "Where shall we meet?"), ("Сез кайда яшисез?", "Where do you live?")], "a1-locative")
L(83, "Where? 3", "Кайда? 3", [("Тышка кара.", "Look outside."), ("Нигә ул монда?", "Why is he here?"), ("Монда шактый матур.", "It's quite nice here."), ("Мин монда еш булам.", "I'm here often.")], "a1-locative")
L(84, "Where? 4", "Кайда? 4", [("Кайда минем гаиләм?", "Where's my family?"), ("Кайда таба?", "Where's the frying pan?"), ("Моның сәбәбе бар.", "There's a reason for that."), ("Башка аңлатма юк.", "There's no other explanation.")], "a1-locative")
L(85, "Questions 1", "Сораулар 1", [("Кем ул?", "Who is he?"), ("Син кем?", "Who are you?"), ("Бу кем?", "Who's this?"), ("Кем мин?", "Who am I?")], "a1-questions")
L(86, "Questions 2", "Сораулар 2", [("Нәрсә?", "What?"), ("Нигә?", "Why?"), ("Күпме?", "How much?"), ("Шулаймы?", "Is that so?")], "a1-questions")
L(87, "Questions 3", "Сораулар 3", [("Дөресме?", "Is that right?"), ("Чыннан да?", "Really?"), ("Сез ялгызмы?", "Are you alone?"), ("Кем каршы?", "Who is against it?")], "a1-questions")
L(88, "Questions 4", "Сораулар 4", [("Хәлләрең ничегрәк?", "How have you been?"), ("Сез уйгурмы?", "Are you Uyghur?"), ("Яхшымы?", "Okay?"), ("Алар кемнәр?", "Who are they?")], "a1-questions")
L(89, "Requests 1", "Үтенечләр 1", [("Кер!", "Come in!"), ("Керегез!", "Come in, all of you!"), ("Ал.", "Take it."), ("Карагыз!", "Look!")], "a1-imperative")
L(90, "Requests 2", "Үтенечләр 2", [("Бир аны миңа.", "Give it to me."), ("Газета бир әле.", "Give me the paper."), ("Кулыңны бир әле!", "Give me your hand!"), ("Дөресен әйт.", "Tell the truth.")], "a1-imperative")
L(91, "Requests 3", "Үтенечләр 3", [("Кунакка килегез!", "Come and visit!"), ("Миңа кунакка кил.", "Come and visit me."), ("Әйдәгез безнең белән.", "Come with us."), ("Әйдәгез!", "Let's go!")], "a1-imperative")
L(92, "Requests 4", "Үтенечләр 4", [("Зинһар, гафу ит!", "Please forgive me!"), ("Еламасана, зинһар.", "Please don't cry."), ("Күземә кара.", "Look into my eyes."), ("Ачыгыз күзләрегезне.", "Open your eyes."), ("Бар, апаңа ярдәм ит.", "Go and help your sister.")], "a1-imperative")
L(93, "People 1", "Кешеләр 1", [("Ул минем дустым.", "He is my friend."), ("Син минем дустым.", "You are my friend."), ("Ул яхшы кеше.", "He's a good person."), ("Ул яхшы кеше түгел.", "He's not a good person.")], "a1-pronouns")
L(94, "People 2", "Кешеләр 2", [("Бу кеше кем?", "Who is that person?"), ("Кем ул егет?", "Who is that guy?"), ("Бу ир бала кем?", "Who is that boy?"), ("Син малаймы?", "Are you a boy?")], "a1-pronouns")
L(95, "People 3", "Кешеләр 3", [("Ул ышанычлы кеше.", "She is a reliable person."), ("Мәрьям - сизгер кыз.", "Maryam is a sensitive girl."), ("Ул бик матур хатын.", "She is a very beautiful woman."), ("Идеаль кеше түгелмен.", "I'm not a perfect person.")], "a1-pronouns")
L(96, "People 4", "Кешеләр 4", [("Рәхмәт, егеткәем!", "Thank you, young man!"), ("Кешенең ике аягы бар.", "A person has two legs."), ("Бу ир-ат табиб.", "This man is a doctor."), ("Бу дус өчен.", "It's for a friend.")], "a1-pronouns")
L(97, "My Day 1", "Минем көнем 1", [("Мин тиз барам.", "I walk fast."), ("Ул һәркөн кырына.", "He shaves every day."), ("Син һәрвакыт ач!", "You're always hungry!"), ("Ул һәрвакыт берүзе.", "He's always by himself.")], "a1-present")
L(98, "My Day 2", "Минем көнем 2", [("Һәрвакыт ачык.", "Always open."), ("Алайса, тыңла.", "Then listen."), ("Бәла ялгыз йөрми.", "Misfortunes never come alone."), ("Сандугач читлектә сайрамый.", "A nightingale won't sing in a cage.")], "a1-present")
L(99, "Review 1", "Кабатлау 1", [("Ул тарихчы.", "He's a historian."), ("Мин географ.", "I'm a geographer."), ("Ул сакаллы.", "He has a beard."), ("Бу да алма.", "This is an apple too.")], "a1-questions")
L(100, "Review 2", "Кабатлау 2", [("Ни хәлләр бар?", "What's new?"), ("Мин монда калам.", "I'm staying here."), ("Бу китап минеке.", "This book is mine."), ("Иртәгә очрашабыз.", "We'll meet tomorrow.")], "a1-questions")
c.save()
