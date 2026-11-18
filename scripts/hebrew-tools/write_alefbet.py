"""Content source for data/hebrew-src/alefbet.json (Letters & Vowels). Run: HE_DICT=<folder with kaikki Hebrew jsonl> python3 write_alefbet.py"""
import os
os.environ.setdefault("HE_DICT", "/private/tmp/claude-501/-Users-omar/3e230d6a-2df5-44ac-a5be-c38644d3169b/scratchpad/he-dict")
from author_he import Course
c = Course("alefbet", "alefbet")

# ───────────── Unit 1: the letters (with the "a" vowels only, so every word is readable) ─────────────
c.T("ab-letters-1", "Hebrew Letters Are Consonants", "letter + vowel mark = syllable: בָּ = ba, דָּ = da",
 "Hebrew is read from right to left. Its 22 letters are consonants; vowels are small marks called nikkud (נִקּוּד), written mostly under the letter. In this first unit every word uses only the two 'a' marks: the T-shaped kamatz (ָ) and the flat line patach (ַ), both pronounced 'a' in modern Hebrew. Alef (א) has no sound of its own: אָ is simply 'a'. Bet comes in two forms: with a dot inside (בּ) it is 'b', without the dot (ב) it is 'v'.",
 "The word 'alphabet' comes from the names of the first two Hebrew-Phoenician letters, alef and bet, through Greek alpha and beta.",
 [("A", "מָה זֶה?", "What is this?"), ("B", "זֶה אַבָּא!", "That's dad!")])
c.L(1, "Alef, Bet and Vet", "א · בּ · ב", [
 ("אָ", "a", "a", ["o", "i", "u"]),
 ("בָּ", "ba", "ba", ["va", "ma", "da"]),
 ("בָ", "va", "va", ["ba", "fa", "ka"]),
 ("אַבָּא", "dad", "aba"),
 ("בָּא", "he comes", "ba"),
 ("אָב", "father (formal)", "av"),
], topic="ab-letters-1")

c.L(2, "Gimel, Dalet, He", "ג · ד · ה", [
 ("גָּ", "ga", "ga", ["da", "ha", "ba"]),
 ("דָּ", "da", "da", ["ga", "ra", "ba"]),
 ("הָ", "ha", "ha", ["cha", "a", "ta"]),
 ("גַּג", "roof", "gag"),
 ("דָּג", "fish", "dag"),
 ("בַּד", "cloth, fabric", "bad"),
 ("הַגַּג", "the roof", "ha-gag"),
 ("הַדָּג", "the fish", "ha-dag"),
], topic="ab-letters-1")

c.L(0, "Practice: Alef to He", "חֲזָרָה: א–ה", [
 ("אַ", "a", "", ["e", "o", "u"]),
 ("בַּ", "ba", "", ["va", "da", "ga"]),
 ("בַ", "va", "", ["ba", "fa", "ha"]),
 ("גַּ", "ga", "", ["ka", "da", "ba"]),
 ("דַּ", "da", "", ["ra", "ga", "ta"]),
 ("הַ", "ha", "", ["cha", "a", "ya"]),
 ("א", "alef (silent)", "", ["ayin (silent)", "he (h)", "tav (t)"]),
 ("ג", "gimel (g)", "", ["nun (n)", "zayin (z)", "vav (v)"]),
 ("הַבַּד", "the cloth", "ha-bad"),
 ("אַגָּדָה", "legend", "agada"),
], topic="ab-letters-1")

c.T("ab-letters-2", "The Word 'The': הַ", "הַ + word = 'the' word: דָּג → הַדָּג",
 "Hebrew has no separate word for 'the'. Instead, the letter he with patach (הַ) is attached to the front of the word: דָּג (a fish) → הַדָּג (the fish). The first letter of the word usually gets a dot (dagesh) after הַ, as in הַגַּג. There is no word for 'a' at all: דָּג means 'a fish' or just 'fish'.",
 "Because 'the', 'and', 'in' and 'to' are all single letters attached to the next word, a Hebrew sentence often has fewer, longer-looking words than its English translation.",
 [("A", "הַדָּג גָּדוֹל?", "Is the fish big?"), ("B", "כֵּן, הַדָּג גָּדוֹל.", "Yes, the fish is big.")])
c.L(3, "Vav, Zayin, Chet", "ו · ז · ח", [
 ("וָ", "va", "va", ["ba", "za", "ha"]),
 ("זָ", "za", "za", ["va", "sa", "ga"]),
 ("חָ", "cha", "cha", ["ha", "ka", "za"]),
 ("וָו", "the letter vav; also 'hook'", "vav"),
 ("זָהָב", "gold", "zahav"),
 ("חַג", "holiday", "chag"),
 ("זָז", "moves", "zaz"),
 ("הַחַג", "the holiday", "ha-chag"),
], topic="ab-letters-2")

c.T("ab-kaf", "Kaf and Khaf, and the First Final Letter", "כּ = k · כ = ch · ך = ch at the end of a word",
 "Like bet, kaf has two sounds: with a dot (כּ) it is 'k', without (כ) it is the throaty 'ch', the same sound as chet. At the end of a word kaf changes shape into a long tail, ך (kaf sofit, 'final kaf'). Five Hebrew letters have a special final form: ך ם ן ף ץ. Yod (י) is a small letter written high on the line and sounds like 'y'.",
 "Kaf sofit is the only final letter that often carries a vowel mark inside it: in כָּךְ the kamatz sits inside the tail, and the two dots (shva) show that the word ends there.",
 [("A", "כָּךְ?", "Like this?"), ("B", "כֵּן, כָּכָה.", "Yes, like that.")])
c.L(4, "Tet, Yod, Kaf", "ט · י · כּ · כ · ך", [
 ("טָ", "ta", "ta", ["da", "ka", "cha"]),
 ("יָ", "ya", "ya", ["va", "a", "za"]),
 ("כָּ", "ka", "ka", ["cha", "ga", "ta"]),
 ("כָ", "cha", "cha", ["ka", "ha", "ya"]),
 ("יָד", "hand", "yad"),
 ("כַּד", "jug", "kad"),
 ("כָּךְ", "so, like this", "kach"),
 ("אַךְ", "but, only", "ach"),
 ("טַבָּח", "cook, chef", "tabach"),
], topic="ab-kaf")

c.L(0, "Practice: Vav to Kaf", "חֲזָרָה: ו–ך", [
 ("וַ", "va", "", ["za", "ba", "ya"]),
 ("זַ", "za", "", ["va", "sa", "tsa"]),
 ("חַ", "cha", "", ["ha", "ka", "ta"]),
 ("טַ", "ta", "", ["da", "cha", "ka"]),
 ("יַ", "ya", "", ["va", "a", "la"]),
 ("כַּ", "ka", "", ["cha", "ba", "ga"]),
 ("ט", "tet (t)", "", ["mem (m)", "tav (t)", "kaf (k)"]),
 ("י", "yod (y)", "", ["vav (v, o, u)", "final nun (n)", "zayin (z)"]),
 ("יַחַד", "together", "yachad"),
 ("הַיָּד", "the hand", "ha-yad"),
], topic="ab-kaf")

c.T("ab-mem", "Lamed, Mem and Final Mem", "ל = l · מ = m · ם = m at the end",
 "Lamed (ל) is the only letter that rises above the line, like a flag. Mem has a normal form (מ) and a closed, square final form (ם) used only as the last letter of a word: מָה (what) starts with מ, יָם (sea) ends with ם. The dot in לָמָּה and חַלָּה doubles the letter in classical Hebrew; today it is pronounced as a single letter.",
 "The common question לָמָּה ('why?') is literally 'for what': לְ (for) + מָה (what).",
 [("A", "לָמָּה?", "Why?"), ("B", "כִּי יֵשׁ חַג!", "Because it's a holiday!")])
c.L(5, "Lamed and Mem", "ל · מ · ם", [
 ("לָ", "la", "la", ["ma", "na", "ra"]),
 ("מָ", "ma", "ma", ["na", "la", "ba"]),
 ("מָה", "what", "ma"),
 ("לָמָּה", "why", "lama"),
 ("יָם", "sea", "yam"),
 ("חַלָּה", "challah (Shabbat bread)", "chala"),
 ("כַּלָּה", "bride", "kala"),
 ("מַזָּל", "luck", "mazal"),
 ("אָדָם", "person, human being", "adam"),
], topic="ab-mem")

c.T("ab-nun", "Nun, Samech, Ayin", "נ = n · ן = n at the end · ס = s · ע = silent",
 "Nun is a small bent letter (נ) with a long straight final form (ן): גַּן (garden). Samech (ס) is a closed circle and sounds 's'. Ayin (ע) looks like a y with a slanted tail; in modern Israeli speech it is silent, just like alef, so עָנָן is pronounced 'anan'.",
 "In some Middle Eastern Jewish communities ayin is still pronounced as a deep throat sound, as in Arabic, while most Israelis pronounce it like alef.",
 [("A", "אֵיפֹה סַבָּא?", "Where is grandpa?"), ("B", "סַבָּא בַּגַּן.", "Grandpa is in the garden.")])
c.L(6, "Nun, Samech, Ayin", "נ · ן · ס · ע", [
 ("נָ", "na", "na", ["ma", "la", "ta"]),
 ("סָ", "sa", "sa", ["za", "sha", "ta"]),
 ("עָ", "a", "a", ["ha", "na", "ya"]),
 ("גַּן", "garden, park", "gan"),
 ("סַבָּא", "grandpa", "saba"),
 ("עָנָן", "cloud", "anan"),
 ("נַעַל", "shoe", "na'al"),
 ("בָּנָנָה", "banana", "banana"),
 ("עַם", "people, nation", "am"),
], topic="ab-nun")

c.L(0, "Practice: Lamed to Ayin", "חֲזָרָה: ל–ע", [
 ("לַ", "la", "", ["na", "ra", "ma"]),
 ("מַ", "ma", "", ["na", "ba", "la"]),
 ("נַ", "na", "", ["ma", "la", "ga"]),
 ("סַ", "sa", "", ["sha", "za", "tsa"]),
 ("עַ", "a", "", ["ha", "ya", "na"]),
 ("ל", "lamed (l)", "", ["final kaf (ch)", "nun (n)", "resh (r)"]),
 ("נ", "nun (n)", "", ["gimel (g)", "kaf (k)", "bet (b)"]),
 ("ע", "ayin (silent)", "", ["tsadi (ts)", "shin (sh)", "alef (silent)"]),
 ("סַל", "basket", "sal"),
 ("עַל", "on", "al"),
 ("נָמָל", "port, harbour", "namal"),
], topic="ab-nun")

c.T("ab-pe", "Pe and Fe, Tsadi", "פּ = p · פ = f · ף = f at the end · צ = ts · ץ = ts at the end",
 "Pe is the third letter that changes with a dot: פּ is 'p', פ (no dot) is 'f', and at the end of a word it becomes ף: כַּף (spoon), אַף (nose). Tsadi (צ) sounds 'ts' as in 'cats', with the final form ץ. So there are three dot pairs to remember: בּ/ב (b/v), כּ/כ (k/ch), פּ/פ (p/f).",
 "A handy rule: at the very start of a word, ב כ פ almost always have the dot, so a word begins with 'b', 'k' or 'p', never 'v', 'ch' or 'f'.",
 [("A", "אֵיפֹה הַכַּף?", "Where is the spoon?"), ("B", "הַכַּף בַּצַּד.", "The spoon is on the side.")])
c.L(7, "Pe, Fe, Tsadi", "פּ · פ · ף · צ · ץ", [
 ("פָּ", "pa", "pa", ["fa", "ba", "ta"]),
 ("פָ", "fa", "fa", ["pa", "va", "ha"]),
 ("צָ", "tsa", "tsa", ["sa", "za", "ta"]),
 ("פַּח", "trash can", "pach"),
 ("כַּף", "spoon", "kaf"),
 ("אַף", "nose", "af"),
 ("צַד", "side", "tsad"),
 ("צָב", "turtle", "tsav"),
 ("פַּעַם", "once; one time", "pa'am"),
], topic="ab-pe")

c.T("ab-qof", "Qof and Resh", "ק = k · ר = r",
 "Qof (ק) sounds exactly like kaf with a dot (כּ) in modern Hebrew; the difference is only in spelling. Its leg goes below the line. Resh (ר) is a rounded corner, pronounced as a French or German throaty 'r'. Don't confuse ר with dalet (ד), which has a small corner sticking out at the top right.",
 "Many Hebrew words come in sets built from a root of three letters: from ק־ר־א come קָרָא (he read), קוֹרֵא (reading) and מִקְרָא (Scripture).",
 [("A", "קַר הַיּוֹם?", "Is it cold today?"), ("B", "כֵּן, קַר מְאֹד.", "Yes, very cold.")])
c.L(8, "Qof and Resh", "ק · ר", [
 ("קָ", "ka", "ka", ["ra", "ga", "cha"]),
 ("רָ", "ra", "ra", ["da", "ka", "la"]),
 ("קַר", "cold", "kar"),
 ("רַק", "only", "rak"),
 ("בָּקָר", "cattle", "bakar"),
 ("קָרָא", "he read", "kara"),
 ("נָהָר", "river", "nahar"),
], topic="ab-qof")

c.T("ab-shin", "Shin, Sin and Tav", "שׁ (dot on the right) = sh · שׂ (dot on the left) = s · ת = t",
 "One letter, two sounds: with a dot on its right shoulder (שׁ) it is 'sh', with a dot on its left shoulder (שׂ) it is 's' and is called sin. Tav (ת) is the last letter of the alphabet and sounds 't'. Sin sounds the same as samech; the spelling depends on the word.",
 "Shin is the letter that stands for God's name שַׁדַּי on a mezuzah, the small case on Jewish doorposts.",
 [("A", "שַׁבָּת שָׁלוֹם!", "Shabbat shalom!"), ("B", "שַׁבָּת שָׁלוֹם, סַבָּא!", "Shabbat shalom, grandpa!")])
c.L(9, "Shin, Sin and Tav", "שׁ · שׂ · ת", [
 ("שָׁ", "sha", "sha", ["sa", "ta", "tsa"]),
 ("שָׂ", "sa", "sa", ["sha", "za", "tsa"]),
 ("תָּ", "ta", "ta", ["da", "cha", "sa"]),
 ("שַׁבָּת", "Shabbat, Saturday", "shabat"),
 ("בַּת", "daughter", "bat"),
 ("אַתָּה", "you (to a man)", "ata"),
 ("שָׁנָה", "year", "shana"),
 ("שַׂר", "minister", "sar"),
], topic="ab-shin")

c.L(0, "Practice: Pe to Tav", "חֲזָרָה: פ–ת", [
 ("פַּ", "pa", "", ["fa", "ba", "ta"]),
 ("פַ", "fa", "", ["pa", "va", "ha"]),
 ("צַ", "tsa", "", ["sa", "za", "ta"]),
 ("קַ", "ka", "", ["ra", "ga", "cha"]),
 ("רַ", "ra", "", ["da", "ka", "la"]),
 ("שַׁ", "sha", "", ["sa", "tsa", "cha"]),
 ("שַׂ", "sa", "", ["sha", "za", "tsa"]),
 ("תַ", "ta", "", ["da", "cha", "sa"]),
 ("פ", "pe / fe (p, f)", "", ["kaf (k)", "bet (b)", "tsadi (ts)"]),
 ("ק", "qof (k)", "", ["he (h)", "final kaf (ch)", "resh (r)"]),
 ("שָׁר", "sings", "shar"),
 ("תָּמָר", "date (fruit)", "tamar"),
], topic="ab-shin")

c.T("ab-final", "The Five Final Letters", "כ → ך · מ → ם · נ → ן · פ → ף · צ → ץ",
 "Five letters change shape at the end of a word. Kaf, nun, pe and tsadi grow a long tail down below the line (ך ן ף ץ), while mem closes into a square (ם). They sound the same as the normal forms. A memory phrase Hebrew children use: כַּמְנַפֵּץ ('like a smasher'), built from the five letters in order.",
 "The finals make Hebrew easier to read without spaces: in ancient scrolls they showed where one word ended and the next began.",
 [("A", "אֵיפֹה הַיָּם?", "Where is the sea?"), ("B", "הַיָּם שָׁם.", "The sea is there.")])
c.L(10, "Final Letters", "אוֹתִיּוֹת סוֹפִיּוֹת", [
 ("ך", "final kaf (ch)", "kaf sofit", ["final nun (n)", "resh (r)", "dalet (d)"]),
 ("ם", "final mem (m)", "mem sofit", ["samech (s)", "final tsadi (ts)", "tet (t)"]),
 ("ן", "final nun (n)", "nun sofit", ["vav (v)", "zayin (z)", "final kaf (ch)"]),
 ("ף", "final pe (f)", "pe sofit", ["final tsadi (ts)", "final kaf (ch)", "qof (k)"]),
 ("ץ", "final tsadi (ts)", "tsadi sofit", ["final pe (f)", "ayin (silent)", "final mem (m)"]),
 ("חָם", "hot", "cham"),
 ("לָבָן", "white", "lavan"),
 ("קַיִץ", "summer", "kayits"),
], topic="ab-final")

c.T("ab-lookalike", "Letters That Look Alike", "ב/כ · ד/ר · ה/ח/ת · ו/ז/ן · ס/ם",
 "Some letters differ by one small detail. ב has a little foot at the bottom right; כ is round with no foot. ד has a corner sticking out; ר is smoothly rounded. ה has a gap at the top left; ח is closed; ת has a little foot on the left. ו is a plain line, ז has a small cap, and ן goes below the line. ס is round; ם is square.",
 "Print and handwriting differ a lot in Hebrew: handwritten (cursive) letters have quite different shapes, so many learners learn print first, as in this unit.",
 [("A", "זֶה דָּלֶת?", "Is that a dalet?"), ("B", "לֹא, זֹאת אוֹת אַחֶרֶת.", "No, it's a different letter.")])
c.L(11, "Letters That Look Alike", "אוֹתִיּוֹת דּוֹמוֹת", [
 ("ב", "bet / vet (b, v)", "bet", ["kaf / khaf (k, ch)", "nun (n)", "gimel (g)"]),
 ("כ", "kaf / khaf (k, ch)", "kaf", ["bet / vet (b, v)", "pe / fe (p, f)", "nun (n)"]),
 ("ד", "dalet (d)", "dalet", ["resh (r)", "final kaf (ch)", "vav (v)"]),
 ("ר", "resh (r)", "resh", ["dalet (d)", "final kaf (ch)", "vav (v)"]),
 ("ה", "he (h)", "he", ["chet (ch)", "tav (t)", "qof (k)"]),
 ("ח", "chet (ch)", "chet", ["he (h)", "tav (t)", "qof (k)"]),
 ("ת", "tav (t)", "tav", ["chet (ch)", "he (h)", "final mem (m)"]),
 ("ו", "vav (v, o, u)", "vav", ["zayin (z)", "final nun (n)", "yod (y)"]),
 ("ז", "zayin (z)", "zayin", ["vav (v, o, u)", "final nun (n)", "gimel (g)"]),
 ("ס", "samech (s)", "samech", ["final mem (m)", "tet (t)", "ayin (silent)"]),
], topic="ab-lookalike")

# ───────────── Unit 2: the vowel marks (nikkud) ─────────────
c.T("ab-review", "The Whole Alphabet", "א ב ג ד ה ו ז ח ט י כ ל מ נ ס ע פ צ ק ר ש ת",
 "These are the 22 letters in order, right to left: alef, bet, gimel, dalet, he, vav, zayin, chet, tet, yod, kaf, lamed, mem, nun, samech, ayin, pe, tsadi, qof, resh, shin, tav. Plus the five final forms ך ם ן ף ץ. Knowing the names helps when people spell a word aloud, which Israelis often do on the phone.",
 "Hebrew letters also count as numbers: א = 1, ב = 2, י = 10, ק = 100. Years in the Jewish calendar and the chapters of many books are still numbered with letters.",
 [("A", "אֵיךְ כּוֹתְבִים אֶת זֶה?", "How do you spell that?"), ("B", "ד, ג. דָּג.", "Dalet, gimel. Dag.")])
c.L(0, "More Look-Alike Letters", "עוֹד אוֹתִיּוֹת דּוֹמוֹת", [
 ("ע", "ayin (silent)", "", ["tsadi (ts)", "tet (t)", "shin (sh)"]),
 ("צ", "tsadi (ts)", "", ["ayin (silent)", "tet (t)", "shin (sh)"]),
 ("ג", "gimel (g)", "", ["nun (n)", "zayin (z)", "vav (v)"]),
 ("נ", "nun (n)", "", ["gimel (g)", "kaf (k)", "bet (b)"]),
 ("ט", "tet (t)", "", ["mem (m)", "tsadi (ts)", "shin (sh)"]),
 ("מ", "mem (m)", "", ["tet (t)", "samech (s)", "final mem (m)"]),
 ("ם", "final mem (m)", "", ["samech (s)", "tet (t)", "mem (m)"]),
 ("ן", "final nun (n)", "", ["vav (v, o, u)", "zayin (z)", "final kaf (ch)"]),
 ("ף", "final pe (f)", "", ["final kaf (ch)", "final tsadi (ts)", "resh (r)"]),
], topic="ab-lookalike")
c.L(0, "The Whole Alphabet", "כָּל הָאוֹתִיּוֹת", [
 ("א", "alef", "", ["ayin", "he", "tet"]),
 ("ג", "gimel", "", ["nun", "zayin", "lamed"]),
 ("י", "yod", "", ["vav", "zayin", "nun"]),
 ("ל", "lamed", "", ["kaf", "resh", "nun"]),
 ("מ", "mem", "", ["tet", "samech", "tav"]),
 ("פ", "pe", "", ["kaf", "bet", "tsadi"]),
 ("צ", "tsadi", "", ["ayin", "tet", "shin"]),
 ("ק", "qof", "", ["he", "resh", "chet"]),
 ("ש", "shin", "", ["tsadi", "ayin", "tet"]),
 ("ת", "tav", "", ["chet", "he", "dalet"]),
], topic="ab-review")

c.T("ab-a", "Kamatz and Patach: 'a'", "בָּ = ba · בַּ = ba",
 "Kamatz (ָ, a small T) and patach (ַ, a flat line) both sound 'a' in modern Hebrew. You have already read many words with them. Notice where the mark sits: always under the letter it follows in sound, so בָּ is 'b' + 'a'.",
 "Kamatz and patach once sounded different, and some communities still distinguish them in prayer, but in everyday Israeli Hebrew they are identical.",
 [("A", "יֵשׁ לְךָ מַפָּה?", "Do you have a map?"), ("B", "כֵּן, הִנֵּה הַמַּפָּה.", "Yes, here's the map.")])
c.L(12, "Kamatz and Patach", "קָמָץ וּפַתָּח", [
 ("מַ", "ma", "ma", ["mi", "mu", "me"]),
 ("תַּ", "ta", "ta", ["ti", "to", "tu"]),
 ("מַפָּה", "map; tablecloth", "mapa"),
 ("שָׂפָה", "language", "safa"),
 ("חָלָב", "milk", "chalav"),
 ("גָּמָל", "camel", "gamal"),
 ("דַּף", "page", "daf"),
 ("שָׁמַיִם", "sky", "shamayim"),
], topic="ab-a")

c.L(0, "Practice: the 'a' Sound", "חֲזָרָה: קָמָץ וּפַתָּח", [
 ("גָּ", "ga", "", ["gi", "go", "gu"]),
 ("זַ", "za", "", ["zi", "zo", "ze"]),
 ("חָ", "cha", "", ["chi", "cho", "chu"]),
 ("כַּ", "ka", "", ["ki", "ko", "ke"]),
 ("לָ", "la", "", ["li", "lo", "lu"]),
 ("צַ", "tsa", "", ["tsi", "tso", "tsu"]),
 ("רָ", "ra", "", ["ri", "ro", "ru"]),
 ("שַׁ", "sha", "", ["shi", "sho", "shu"]),
 ("קָטָן", "small", "katan"),
 ("חָתָן", "groom", "chatan"),
], topic="ab-a")

c.T("ab-i", "Chirik: 'i'", "בִּ = bi · בִּי = bi (with yod)",
 "Chirik is a single dot under the letter (ִ) and sounds 'ee' as in 'see'. It is often followed by a yod that is not pronounced separately: מִי (who), שִׁיר (song). This 'helper' yod is called chirik male ('full chirik').",
 "Hebrew uses four letters, א ה ו י, as helpers that show vowels. That is why words are still readable when the nikkud is left out.",
 [("A", "מִי זֶה?", "Who is that?"), ("B", "זֹאת אִמָּא שֶׁלִּי.", "That's my mom.")])
c.L(13, "Chirik", "חִירִיק", [
 ("בִּ", "bi", "bi", ["ba", "bu", "be"]),
 ("מִי", "who", "mi"),
 ("אִמָּא", "mom", "ima"),
 ("שִׁיר", "song", "shir"),
 ("עִיר", "city", "ir"),
 ("גִּיל", "age", "gil"),
 ("תִּיק", "bag", "tik"),
 ("דִּירָה", "apartment", "dira"),
], topic="ab-i")

c.L(0, "Practice: the 'i' Sound", "חֲזָרָה: חִירִיק", [
 ("גִּ", "gi", "", ["ga", "go", "gu"]),
 ("דִּ", "di", "", ["da", "do", "de"]),
 ("לִ", "li", "", ["la", "lo", "lu"]),
 ("מִ", "mi", "", ["ma", "mo", "me"]),
 ("נִ", "ni", "", ["na", "no", "nu"]),
 ("שִׁ", "shi", "", ["sha", "sho", "she"]),
 ("תִּ", "ti", "", ["ta", "to", "tu"]),
 ("רִ", "ri", "", ["ra", "ro", "re"]),
 ("לִי", "to me, for me", "li"),
 ("כִּי", "because", "ki"),
 ("מִיץ", "juice", "mits"),
 ("גִּיר", "chalk", "gir"),
], topic="ab-i")

c.T("ab-e", "Tsere and Segol: 'e'", "בֵּ = be · בֶּ = be",
 "Two marks sound 'e' as in 'bed': tsere, two dots side by side (ֵ), and segol, three dots in a triangle (ֶ). Tsere is often followed by a silent yod (בֵּי). Many common nouns follow the 'segolate' pattern with two segols: סֵפֶר (book), כֶּלֶב (dog), יֶלֶד (boy), stressed on the first syllable.",
 "Segol takes its name from the Aramaic for 'cluster of grapes', after its three dots.",
 [("A", "יֵשׁ לְךָ כֶּלֶב?", "Do you have a dog?"), ("B", "כֵּן, וְגַם חָתוּל.", "Yes, and a cat too.")])
c.L(14, "Tsere and Segol", "צֵירֵי וּסֶגוֹל", [
 ("בֵּ", "be", "be", ["bi", "ba", "bo"]),
 ("מֶ", "me", "me", ["mu", "mi", "ma"]),
 ("סֵפֶר", "book", "sefer"),
 ("עֵץ", "tree", "ets"),
 ("כֶּלֶב", "dog", "kelev"),
 ("שֵׁם", "name", "shem"),
 ("יֶלֶד", "boy, child", "yeled"),
 ("בֵּיצָה", "egg", "beitsa"),
 ("אֶרֶץ", "land, country", "erets"),
], topic="ab-e")

c.L(0, "Practice: the 'e' Sound", "חֲזָרָה: צֵירֵי וּסֶגוֹל", [
 ("דֵּ", "de", "", ["da", "di", "do"]),
 ("לֶ", "le", "", ["la", "li", "lu"]),
 ("נֶ", "ne", "", ["na", "ni", "no"]),
 ("סֵ", "se", "", ["sa", "si", "so"]),
 ("רֶ", "re", "", ["ra", "ri", "ru"]),
 ("שֶׁ", "she", "", ["sha", "shi", "shu"]),
 ("תֵּ", "te", "", ["ta", "ti", "to"]),
 ("לֶחֶם", "bread", "lechem"),
 ("מֶלֶךְ", "king", "melech"),
 ("שֶׁלֶג", "snow", "sheleg"),
 ("רֶגֶל", "leg, foot", "regel"),
], topic="ab-e")

c.T("ab-o", "Cholam: 'o'", "בֹּ = bo · בּוֹ = bo (with vav)",
 "Cholam is a dot above the letter, at its top left (ֹ), and sounds 'o'. Very often it sits on top of a vav: וֹ is simply 'o', as in שָׁלוֹם and טוֹב. Then the vav is not a 'v' at all; it only carries the vowel.",
 "שָׁלוֹם means 'peace' as well as 'hello' and 'goodbye', so one word covers greeting and parting.",
 [("A", "שָׁלוֹם! מָה שְׁלוֹמְךָ?", "Hello! How are you?"), ("B", "טוֹב, תּוֹדָה!", "Good, thanks!")])
c.L(15, "Cholam", "חוֹלָם", [
 ("בֹּ", "bo", "bo", ["bu", "ba", "bi"]),
 ("לוֹ", "lo", "lo", ["lu", "le", "la"]),
 ("טוֹב", "good", "tov"),
 ("יוֹם", "day", "yom"),
 ("אוֹר", "light", "or"),
 ("לֹא", "no, not", "lo"),
 ("סוֹף", "end", "sof"),
 ("שָׁלוֹם", "hello; peace", "shalom"),
], topic="ab-o")

c.L(0, "Practice: the 'o' Sound", "חֲזָרָה: חוֹלָם", [
 ("גּוֹ", "go", "", ["gu", "ga", "gi"]),
 ("דּוֹ", "do", "", ["du", "da", "de"]),
 ("מוֹ", "mo", "", ["mu", "ma", "mi"]),
 ("נוֹ", "no", "", ["nu", "na", "ne"]),
 ("רוֹ", "ro", "", ["ru", "ra", "ri"]),
 ("תּוֹ", "to", "", ["tu", "ta", "ti"]),
 ("חוֹ", "cho", "", ["chu", "cha", "chi"]),
 ("חוֹל", "sand", "chol"),
 ("קוֹל", "voice", "kol"),
 ("דּוֹד", "uncle", "dod"),
 ("רֹאשׁ", "head", "rosh"),
], topic="ab-o")

c.T("ab-u", "Kubutz and Shuruk: 'u'", "בֻּ = bu · בּוּ = bu",
 "'U' as in 'rule' has two spellings: kubutz, three slanted dots under the letter (ֻ), and shuruk, a vav with a dot in its middle (וּ). Both sound the same. Careful: וּ (shuruk) is 'u', but וֹ (cholam) is 'o'; the position of the dot decides.",
 "The little word וּ ('and') before a word starting with ב מ פ is pronounced 'u': וּבַיִת means 'and a house'.",
 [("A", "הוּא בַּשּׁוּק?", "Is he at the market?"), ("B", "כֵּן, הוּא קוֹנֶה תּוּת.", "Yes, he's buying strawberries.")])
c.L(16, "Kubutz and Shuruk", "קֻבּוּץ וְשׁוּרוּק", [
 ("בֻּ", "bu", "bu", ["bo", "bi", "ba"]),
 ("סוּ", "su", "su", ["so", "se", "sa"]),
 ("הוּא", "he", "hu"),
 ("סוּס", "horse", "sus"),
 ("שׁוּק", "market", "shuk"),
 ("תּוּת", "strawberry", "tut"),
 ("שֻׁלְחָן", "table", "shulchan"),
 ("דֻּבִּי", "teddy bear", "dubi"),
], topic="ab-u")

c.L(0, "Practice: the 'u' Sound", "חֲזָרָה: קֻבּוּץ וְשׁוּרוּק", [
 ("גּוּ", "gu", "", ["go", "ga", "gi"]),
 ("דּוּ", "du", "", ["do", "da", "de"]),
 ("לוּ", "lu", "", ["lo", "la", "li"]),
 ("מוּ", "mu", "", ["mo", "ma", "mi"]),
 ("רוּ", "ru", "", ["ro", "ra", "ri"]),
 ("תֻּ", "tu", "", ["to", "ta", "te"]),
 ("צוּ", "tsu", "", ["tso", "tsa", "tsi"]),
 ("סֻכָּה", "sukkah, hut", "suka"),
 ("כֻּלָּם", "everyone", "kulam"),
 ("גּוּף", "body", "guf"),
 ("צוּר", "rock", "tsur"),
], topic="ab-u")
c.T("ab-allvowels", "One Letter, Every Vowel", "לָ · לִ · לֵ · לוֹ · לוּ",
 "Read across: the same consonant with each vowel mark in turn. לָ la, לִ li, לֵ le, לוֹ lo, לוּ lu. Then the same with shin: שָׁ sha, שִׁ shi, שֵׁ she, שׁוֹ sho, שׁוּ shu. This is how Israeli children practise in first grade, and it is the fastest way to make the marks automatic.",
 "Israeli first-graders traditionally finish learning all the letters and vowels by Hanukkah or soon after, and celebrate with a 'siddur party' where they receive their first prayer book.",
 [("A", "מָה כָּתוּב פֹּה?", "What does it say here?"), ("B", "כָּתוּב שָׁלוֹם.", "It says shalom.")])
c.L(0, "One Letter, Every Vowel", "אוֹת אַחַת, כָּל הַתְּנוּעוֹת", [
 ("לָ", "la", "", ["li", "le", "lo"]),
 ("לִ", "li", "", ["la", "le", "lu"]),
 ("לֵ", "le", "", ["li", "la", "lo"]),
 ("לוֹ", "lo", "", ["lu", "la", "le"]),
 ("לוּ", "lu", "", ["lo", "li", "la"]),
 ("שָׁ", "sha", "", ["shi", "she", "sho"]),
 ("שִׁ", "shi", "", ["sha", "she", "shu"]),
 ("שֵׁ", "she", "", ["shi", "sha", "sho"]),
 ("שׁוֹ", "sho", "", ["shu", "sha", "she"]),
 ("שׁוּ", "shu", "", ["sho", "shi", "sha"]),
], topic="ab-allvowels")
c.T("ab-namevowel", "Name That Vowel", "ָ ַ kamatz, patach · ִ chirik · ֵ ֶ tsere, segol · ֹ cholam · ֻ וּ kubutz, shuruk · ְ shva",
 "Now go the other way: look at the mark and name it. Under the letter: a T is kamatz, a line is patach (both 'a'); one dot is chirik ('i'); two dots side by side are tsere and three in a triangle are segol (both 'e'); three slanted dots are kubutz ('u'); two dots stacked vertically are shva. Above the letter, top left, the single dot is cholam ('o'). In a vav, a middle dot is shuruk ('u').",
 "The names describe the marks: kamatz means 'closing' (the mouth), patach 'opening', chirik 'gnashing', and cholam 'strong' or 'full'.",
 [("A", "אֵיזֶה סִימָן זֶה?", "Which mark is this?"), ("B", "זֶה חִירִיק.", "That's a chirik.")])
c.L(0, "Name That Vowel", "אֵיזֶה נִקּוּד?", [
 ("דָּ", "kamatz (a)", "", ["chirik (i)", "segol (e)", "shuruk (u)"]),
 ("תַּ", "patach (a)", "", ["tsere (e)", "cholam (o)", "shva (none)"]),
 ("בִּ", "chirik (i)", "", ["kamatz (a)", "segol (e)", "cholam (o)"]),
 ("גֵּ", "tsere (e)", "", ["segol (e)", "chirik (i)", "kubutz (u)"]),
 ("דֶּ", "segol (e)", "", ["tsere (e)", "kamatz (a)", "shva (none)"]),
 ("מֹ", "cholam (o)", "", ["shuruk (u)", "chirik (i)", "patach (a)"]),
 ("לֻ", "kubutz (u)", "", ["segol (e)", "shuruk (u)", "tsere (e)"]),
 ("נוּ", "shuruk (u)", "", ["cholam (o)", "kubutz (u)", "chirik (i)"]),
 ("סְ", "shva (none)", "", ["tsere (e)", "chirik (i)", "patach (a)"]),
], topic="ab-namevowel")

c.T("ab-shva", "Shva: No Vowel, or a Quick 'e'", "בְּ = b' · סָבְתָא = sav-ta · יְלָדִים = ye-la-dim",
 "Shva is two dots stacked vertically under a letter (ְ). Usually it means 'no vowel here': in סָבְתָא the ב is closed off, 'sav-ta'. At the start of a word it is often a very short 'e' or just a quick release: יְלָדִים is 'yeladim', תְּמוּנָה is 'tmuna'. The prefixes בְּ (in), לְ (to) and כְּ (like) all carry shva.",
 "Israeli speakers often drop the 'e' of shva completely, so בְּבַקָּשָׁה ('please') is commonly pronounced 'bevakasha' but also 'bvakasha'.",
 [("A", "אֶפְשָׁר מַיִם, בְּבַקָּשָׁה?", "Could I have some water, please?"), ("B", "בְּבַקָּשָׁה!", "Here you go!")])
c.L(17, "Shva", "שְׁוָא", [
 ("בְּ", "b'", "b'", ["ba", "bo", "bi"]),
 ("יְלָדִים", "children", "yeladim"),
 ("סָבְתָא", "grandma", "savta"),
 ("תְּמוּנָה", "picture", "tmuna"),
 ("מַלְכָּה", "queen", "malka"),
 ("שְׁמוֹנֶה", "eight", "shmone"),
 ("לְאַט", "slowly", "le'at"),
 ("בְּבַקָּשָׁה", "please; you're welcome", "bevakasha"),
], topic="ab-shva")

c.L(0, "Practice: Shva", "חֲזָרָה: שְׁוָא", [
 ("שְׁלוֹשָׁה", "three", "shlosha"),
 ("סְפָרִים", "books", "sfarim"),
 ("מִשְׁפָּחָה", "family", "mishpacha"),
 ("יַלְדָּה", "girl", "yalda"),
 ("כְּבָר", "already", "kvar"),
 ("שְׁאֵלָה", "question", "she'ela"),
 ("מַחְבֶּרֶת", "notebook", "machberet"),
 ("תְּשׁוּבָה", "answer", "tshuva"),
], topic="ab-shva")

c.T("ab-hataf", "Hataf Vowels under Throat Letters", "אֲ = a · אֱ = e · אֳ = o",
 "The throat letters א ה ח ע can't take a plain shva, so they use a 'hataf' (hurried) vowel instead: shva + patach (ֲ) sounds 'a', shva + segol (ֱ) sounds 'e', shva + kamatz (ֳ) sounds 'o'. In speech they are just ordinary short vowels: אֲנִי = 'ani' (I), אֱמֶת = 'emet' (truth).",
 "אֱמֶת ('truth') is spelled with the first, middle and last letters of the alphabet (א מ ת), which rabbis read as a hint that truth covers everything.",
 [("A", "אֲנִי לוֹמֵד עִבְרִית.", "I'm learning Hebrew."), ("B", "בֶּאֱמֶת? יֹפִי!", "Really? Great!")])
c.L(18, "Hataf Vowels", "חֲטָפִים", [
 ("אֲ", "a", "a", ["e", "o", "i"]),
 ("אֱ", "e", "e", ["a", "o", "u"]),
 ("אֲנִי", "I", "ani"),
 ("אֱמֶת", "truth", "emet"),
 ("עֲבוֹדָה", "work, job", "avoda"),
 ("חֲבֵרָה", "friend (female)", "chavera"),
 ("אֳנִיָּה", "ship", "oniya"),
 ("חֳדָשִׁים", "months", "chodashim"),
], topic="ab-hataf")

c.T("ab-dagesh", "Dagesh: the Dot Inside", "כּוֹ = ko · כוֹ = cho · פִּ = pi · פִ = fi",
 "A dot inside a letter is called dagesh. In three letters it changes the sound: בּ b / ב v, כּ k / כ ch, פּ p / פ f. In all other letters it doesn't change the sound in modern Hebrew (it once doubled the letter, as in אִמָּא and סַבָּא). Watch the middle of words: in סֵפֶר the פ has no dot, so it is 'sefer', not 'seper'.",
 "Inside a vav, a dot is not a dagesh but shuruk, the vowel 'u': וּ.",
 [("A", "אֶפְשָׁר כּוֹס מַיִם?", "Can I have a glass of water?"), ("B", "כֵּן, הִנֵּה.", "Yes, here you are.")])
c.L(19, "Dagesh", "דָּגֵשׁ", [
 ("כּוֹ", "ko", "ko", ["cho", "bo", "po"]),
 ("כוֹ", "cho", "cho", ["ko", "ho", "vo"]),
 ("פִּ", "pi", "pi", ["fi", "bi", "vi"]),
 ("פִ", "fi", "fi", ["pi", "vi", "hi"]),
 ("פֶּה", "mouth", "pe"),
 ("כּוֹס", "glass, cup", "kos"),
 ("עִפָּרוֹן", "pencil", "iparon"),
 ("מִכְתָּב", "letter (mail)", "michtav"),
], topic="ab-dagesh")

c.L(0, "Practice: Dagesh", "חֲזָרָה: דָּגֵשׁ", [
 ("בִ", "vi", "", ["bi", "fi", "mi"]),
 ("פֻּ", "pu", "", ["fu", "bu", "vu"]),
 ("כּוֹכָב", "star", "kochav"),
 ("כִּתָּה", "class, classroom", "kita"),
 ("פִּיל", "elephant", "pil"),
 ("כֶּסֶף", "money; silver", "kesef"),
 ("לֵב", "heart", "lev"),
 ("חָבֵר", "friend (male)", "chaver"),
 ("סַפָּר", "barber", "sapar"),
], topic="ab-dagesh")

c.T("ab-furtive", "Shin or Sin, and the 'Stolen' Patach", "שׁוֹ = sho · שׂוֹ = so · רוּחַ = ru-ach",
 "Always check which side the dot of ש is on: שֶׁמֶשׁ (sun, 'sh') vs עֶשֶׂר (ten, 's'). A second trap: when a word ends in ח or ע with a patach under it, the 'a' is said BEFORE the consonant. This 'stolen' (furtive) patach turns רוּחַ into 'ruach', not 'rucha', and תַּפּוּחַ into 'tapuach'.",
 "Furtive patach exists because a throat sound at the very end of a word is hard to say right after 'u', 'i' or 'e', so a little 'a' slips in before it.",
 [("A", "אַתָּה שָׂמֵחַ?", "Are you happy?"), ("B", "כֵּן, מְאֹד שָׂמֵחַ!", "Yes, very happy!")])
c.L(20, "Shin, Sin and Furtive Patach", "שׁ · שׂ · רוּחַ", [
 ("שׁוֹ", "sho", "sho", ["so", "cho", "to"]),
 ("שׂוֹ", "so", "so", ["sho", "tso", "zo"]),
 ("שֶׁמֶשׁ", "sun", "shemesh"),
 ("עֶשֶׂר", "ten", "eser"),
 ("שָׂדֶה", "field", "sade"),
 ("רוּחַ", "wind; spirit", "ruach"),
 ("יָרֵחַ", "moon", "yare'ach"),
 ("תַּפּוּחַ", "apple", "tapuach"),
 ("שָׂמֵחַ", "happy", "same'ach"),
], topic="ab-furtive")

c.L(0, "Practice: Shin and Sin", "חֲזָרָה: שׁ · שׂ", [
 ("שִׁ", "shi", "", ["si", "chi", "tsi"]),
 ("שִׂ", "si", "", ["shi", "zi", "tsi"]),
 ("שֵׁ", "she", "", ["se", "che", "tse"]),
 ("שֵׂ", "se", "", ["she", "ze", "tse"]),
 ("שָׁלוֹשׁ", "three (feminine)", "shalosh"),
 ("שִׂמְלָה", "dress", "simla"),
 ("שָׁעוֹן", "clock, watch", "sha'on"),
 ("עָשִׁיר", "rich", "ashir"),
 ("שֵׂעָר", "hair", "se'ar"),
], topic="ab-furtive")

c.T("ab-nonikkud", "Reading Without Nikkud", "שָׁלוֹם → שלום · יֶלֶד → ילד",
 "Everyday Hebrew (signs, newspapers, phones) is written without nikkud. Readers rely on the helper letters ו and י, which often show 'o', 'u' or 'i', and on knowing the word. Compare: שָׁלוֹם → שלום, תּוֹדָה → תודה, אִמָּא → אמא. Learn words with nikkud first, then practise recognising them bare.",
 "Children's books, poetry, prayer books and texts for new immigrants are still printed with full nikkud.",
 [("A", "אַתָּה קוֹרֵא בְּלִי נִקּוּד?", "Can you read without nikkud?"), ("B", "עוֹד לֹא, אֲבָל אֲנִי לוֹמֵד.", "Not yet, but I'm learning.")])
c.L(21, "Reading Without Nikkud", "בְּלִי נִקּוּד", [
 ("שלום", "hello (shalom), written without nikkud", "shalom"),
 ("תודה", "thank you (toda)", "toda"),
 ("ילד", "boy (yeled)", "yeled"),
 ("ספר", "book (sefer)", "sefer"),
 ("בית", "house (bayit)", "bayit"),
 ("אמא", "mom (ima)", "ima"),
 ("מים", "water (mayim)", "mayim"),
 ("כלב", "dog (kelev)", "kelev"),
], topic="ab-nonikkud")

# ───────────── Unit 3: reading practice ─────────────
c.L(0, "Without Nikkud: More Words", "עוֹד מִלִּים בְּלִי נִקּוּד", [
 ("תפוח", "apple (tapuach)", "tapuach"),
 ("שולחן", "table (shulchan)", "shulchan"),
 ("ירושלים", "Jerusalem (Yerushalayim)", "Yerushalayim"),
 ("חבר", "friend (chaver)", "chaver"),
 ("עבודה", "work (avoda)", "avoda"),
 ("שמש", "sun (shemesh)", "shemesh"),
 ("לחם", "bread (lechem)", "lechem"),
 ("משפחה", "family (mishpacha)", "mishpacha"),
], topic="ab-nonikkud")

c.T("ab-reading", "Putting It Together", "read syllable by syllable, right to left",
 "Read a new word one syllable at a time: find the letter, then its vowel mark, then move left. בֹּ + קֶר → בֹּקֶר ('boker', morning). Two-word phrases are read the same way. Hebrew stress usually falls on the last syllable, except segolate words like בֹּקֶר and סֵפֶר.",
 "Most Hebrew greetings wish for something: לַיְלָה טוֹב is 'good night', and בֹּקֶר אוֹר ('morning of light') is the standard reply to 'good morning'.",
 [("A", "בֹּקֶר טוֹב!", "Good morning!"), ("B", "בֹּקֶר אוֹר!", "Good morning! (reply)")])
c.L(22, "Reading Phrases", "קוֹרְאִים מִשְׁפָּטִים קְצָרִים", [
 ("בֹּקֶר טוֹב", "good morning", "boker tov"),
 ("לַיְלָה טוֹב", "good night", "laila tov"),
 ("תּוֹדָה רַבָּה", "thank you very much", "toda raba"),
 ("מָה שְׁלוֹמְךָ?", "how are you? (to a man)", "ma shlomcha?"),
 ("יוֹם הֻלֶּדֶת שָׂמֵחַ", "happy birthday", "yom huledet same'ach"),
 ("סְלִיחָה", "sorry; excuse me", "slicha"),
 ("לְהִתְרָאוֹת", "see you", "lehitra'ot"),
 ("שַׁבָּת שָׁלוֹם", "Shabbat shalom", "shabat shalom"),
], topic="ab-reading")

c.L(23, "Reading Sentences", "קוֹרְאִים מִשְׁפָּטִים", [
 ("אַבָּא בַּבַּיִת.", "Dad is at home.", "Aba ba-bayit."),
 ("הַיֶּלֶד אוֹכֵל תַּפּוּחַ.", "The boy is eating an apple.", "Ha-yeled ochel tapuach."),
 ("אִמָּא קוֹרֵאת סֵפֶר.", "Mom is reading a book.", "Ima koret sefer."),
 ("הַכֶּלֶב גָּדוֹל.", "The dog is big.", "Ha-kelev gadol."),
 ("הַשֶּׁמֶשׁ חַמָּה.", "The sun is hot.", "Ha-shemesh chama."),
 ("יֵשׁ לִי חָתוּל.", "I have a cat.", "Yesh li chatul."),
 ("הַבַּיִת שֶׁלָּנוּ קָטָן.", "Our house is small.", "Ha-bayit shelanu katan."),
 ("אֲנִי לוֹמֵד עִבְרִית.", "I am learning Hebrew.", "Ani lomed ivrit."),
], topic="ab-reading")

c.L(24, "Names and Places", "שֵׁמוֹת וּמְקוֹמוֹת", [
 ("יְרוּשָׁלַיִם", "Jerusalem", "Yerushalayim"),
 ("תֵּל אָבִיב", "Tel Aviv", "Tel Aviv"),
 ("חֵיפָה", "Haifa", "Cheifa"),
 ("יִשְׂרָאֵל", "Israel", "Yisra'el"),
 ("דָּוִד", "David", "David"),
 ("שָׂרָה", "Sarah", "Sara"),
 ("מֹשֶׁה", "Moses (Moshe)", "Moshe"),
 ("רִבְקָה", "Rebecca (Rivka)", "Rivka"),
], topic="ab-reading")

c.L(0, "Reading: My Family", "קוֹרְאִים: הַמִּשְׁפָּחָה שֶׁלִּי", [
 ("יֵשׁ לִי אָח וְאָחוֹת.", "I have a brother and a sister.", "Yesh li ach ve-achot."),
 ("סָבְתָא אוֹפָה עוּגָה.", "Grandma is baking a cake.", "Savta ofa uga."),
 ("אַבָּא וְאִמָּא בַּמִּטְבָּח.", "Dad and mom are in the kitchen.", "Aba ve-ima ba-mitbach."),
 ("הַיְּלָדִים מְשַׂחֲקִים בַּחוּץ.", "The children are playing outside.", "Ha-yeladim mesachakim ba-chuts."),
 ("אֲנִי אוֹהֵב אֶת הַמִּשְׁפָּחָה שֶׁלִּי.", "I love my family.", "Ani ohev et ha-mishpacha sheli."),
 ("יֵשׁ לָנוּ כֶּלֶב וְחָתוּל.", "We have a dog and a cat.", "Yesh lanu kelev ve-chatul."),
 ("הַבַּת שֶׁלִּי בַּכִּתָּה.", "My daughter is in class.", "Ha-bat sheli ba-kita."),
 ("סַבָּא קוֹרֵא עִתּוֹן.", "Grandpa is reading a newspaper.", "Saba kore iton."),
], topic="ab-reading")
c.L(0, "Reading: Food", "קוֹרְאִים: אֹכֶל", [
 ("אֲנִי שׁוֹתֶה מַיִם.", "I am drinking water.", "Ani shote mayim."),
 ("הַלֶּחֶם טָרִי.", "The bread is fresh.", "Ha-lechem tari."),
 ("אִמָּא קוֹנָה חָלָב בַּשּׁוּק.", "Mom buys milk at the market.", "Ima kona chalav ba-shuk."),
 ("הַקָּפֶה חַם מְאֹד.", "The coffee is very hot.", "Ha-kafe cham me'od."),
 ("אֲנִי רוֹצֶה עוֹד פְּרִי.", "I want more fruit.", "Ani rotse od pri."),
 ("הַגְּלִידָה טְעִימָה.", "The ice cream is tasty.", "Ha-glida te'ima."),
 ("אֲנַחְנוּ אוֹכְלִים יַחַד.", "We eat together.", "Anachnu ochlim yachad."),
 ("סָלָט, בְּבַקָּשָׁה.", "A salad, please.", "Salat, bevakasha."),
], topic="ab-reading")

c.R(101, "Reading: Dani and the Dog", "דָּנִי וְהַכֶּלֶב", "A first story with full nikkud.", [
 ("דָּנִי יֶלֶד קָטָן.", "Dani is a little boy."),
 ("יֵשׁ לוֹ כֶּלֶב גָּדוֹל.", "He has a big dog."),
 ("הַכֶּלֶב שֶׁל דָּנִי לָבָן.", "Dani's dog is white."),
 ("בַּבֹּקֶר דָּנִי וְהַכֶּלֶב הוֹלְכִים לַגַּן.", "In the morning Dani and the dog go to the park."),
 ("בַּגַּן יֵשׁ עֵצִים וּפְרָחִים.", "In the park there are trees and flowers."),
 ("דָּנִי שָׂמֵחַ, וְגַם הַכֶּלֶב שָׂמֵחַ.", "Dani is happy, and the dog is happy too."),
], [
 ("Who is Dani?", ["A little boy", "A big dog", "A teacher", "A grandfather"], 0),
 ("What colour is the dog?", ["White", "Black", "Brown", "Red"], 0),
 ("Where do they go in the morning?", ["To the park", "To school", "To the sea", "To the market"], 0),
 ("What is in the park?", ["Trees and flowers", "Cars and buses", "Fish", "Books"], 0),
])
c.R(102, "Reading: Noa at the Market", "נֹעָה בַּשּׁוּק", "A Friday trip to the market, with full nikkud.", [
 ("הַיּוֹם יוֹם שִׁשִּׁי.", "Today is Friday."),
 ("נֹעָה הוֹלֶכֶת לַשּׁוּק עִם אִמָּא.", "Noa goes to the market with mom."),
 ("בַּשּׁוּק יֵשׁ פֵּרוֹת וִירָקוֹת.", "At the market there are fruits and vegetables."),
 ("אִמָּא קוֹנָה תַּפּוּחִים וְחַלָּה לְשַׁבָּת.", "Mom buys apples and challah for Shabbat."),
 ("נֹעָה רוֹצָה תּוּת.", "Noa wants strawberries."),
 ("בָּעֶרֶב כָּל הַמִּשְׁפָּחָה אוֹכֶלֶת יַחַד.", "In the evening the whole family eats together."),
], [
 ("What day is it?", ["Friday", "Saturday", "Sunday", "Monday"], 0),
 ("Who goes to the market with Noa?", ["Her mom", "Her grandpa", "Her brother", "Her friend"], 0),
 ("What does mom buy for Shabbat?", ["Apples and challah", "Milk and bread", "Fish", "Ice cream"], 0),
 ("What does Noa want?", ["Strawberries", "Bananas", "Juice", "A book"], 0),
])
c.save()
