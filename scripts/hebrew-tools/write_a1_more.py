"""Content source for data/hebrew-src/a1-more.json (A1 lessons 5-20 + reading 101). Run: HE_DICT=<folder with kaikki Hebrew jsonl> python3 write_a1_more.py"""
import os
os.environ.setdefault("HE_DICT", "/private/tmp/claude-501/-Users-omar/3e230d6a-2df5-44ac-a5be-c38644d3169b/scratchpad/he-dict")
from author_he import Course
c = Course("a1", "a1-more", start=5)

c.T("a1-yesh-ein", "There Is and There Isn't: יֵשׁ / אֵין", "יֵשׁ + noun = there is · אֵין + noun = there isn't · יֵשׁ לִי = I have",
 "יֵשׁ means 'there is / there are' and אֵין means 'there isn't / there aren't'. They never change for gender or number. Add לְ + a person to talk about having: יֵשׁ לִי ('I have', literally 'there is to me'), אֵין לָנוּ ('we don't have'). Hebrew has no verb 'to have' at all.",
 "Because יֵשׁ לִי literally means 'there is to me', Hebrew speakers sometimes say 'there is to me a question' when they speak English.",
 [("A", "יֵשׁ לְךָ זְמַן?", "Do you have time?"), ("B", "לֹא, אֵין לִי זְמַן עַכְשָׁו.", "No, I don't have time now.")])
c.L(5, "There Is, There Isn't", "יֵשׁ וְאֵין", [
 ("יֵשׁ חָלָב בַּמְּקָרֵר.", "There is milk in the fridge.", "Yesh chalav ba-mekarer."),
 ("אֵין לֶחֶם בַּבַּיִת.", "There is no bread at home.", "Ein lechem ba-bayit."),
 ("יֵשׁ לִי שְׁאֵלָה.", "I have a question.", "Yesh li she'ela."),
 ("אֵין לִי זְמַן.", "I don't have time.", "Ein li zman."),
 ("יֵשׁ לְךָ אַחִים?", "Do you have brothers?", "Yesh lecha achim?"),
 ("יֵשׁ לָהּ מְכוֹנִית חֲדָשָׁה.", "She has a new car.", "Yesh la mechonit chadasha."),
 ("אֵין לָנוּ כֶּסֶף.", "We don't have money.", "Ein lanu kesef."),
 ("יֵשׁ פֹּה מִסְעָדָה טוֹבָה?", "Is there a good restaurant here?", "Yesh po mis'ada tova?"),
], topic="a1-yesh-ein")

c.T("a1-infinitive", "Want To, Can, Need To", "רוֹצֶה / יָכוֹל / צָרִיךְ + לְ… (infinitive)",
 "After רוֹצֶה (want), יָכוֹל (can) and צָרִיךְ (need, have to), the next verb is in the infinitive, which starts with לְ or לִ: לִלְמֹד (to study), לֶאֱכֹל (to eat), לָלֶכֶת (to go). The first verb agrees with the speaker: a man says אֲנִי רוֹצֶה, a woman says אֲנִי רוֹצָה; plural רוֹצִים / רוֹצוֹת.",
 "אֶפְשָׁר ('it's possible') is the polite all-purpose way to ask for something: אֶפְשָׁר מַיִם? = 'Could I have some water?'",
 [("A", "אַתָּה רוֹצֶה לֶאֱכֹל?", "Do you want to eat?"), ("B", "כֵּן, אֲבָל קֹדֶם אֲנִי צָרִיךְ לַעֲבֹד.", "Yes, but first I need to work.")])
c.L(6, "I Want To, I Can, I Need To", "רוֹצֶה, יָכוֹל, צָרִיךְ", [
 ("אֲנִי רוֹצֶה לִלְמֹד עִבְרִית.", "I want to learn Hebrew. (man)", "Ani rotse lilmod ivrit."),
 ("הִיא רוֹצָה לִשְׁתּוֹת קָפֶה.", "She wants to drink coffee.", "Hi rotsa lishtot kafe."),
 ("אַתָּה יָכוֹל לַעֲזֹר לִי?", "Can you help me? (to a man)", "Ata yachol la'azor li?"),
 ("אֲנִי לֹא יְכוֹלָה לָבוֹא הַיּוֹם.", "I can't come today. (woman)", "Ani lo yechola lavo ha-yom."),
 ("אֲנַחְנוּ צְרִיכִים לָלֶכֶת.", "We need to go.", "Anachnu tsrichim lalechet."),
 ("הוּא צָרִיךְ לַעֲבֹד מָחָר.", "He has to work tomorrow.", "Hu tsarich la'avod machar."),
 ("אֶפְשָׁר לָשֶׁבֶת פֹּה?", "May I sit here?", "Efshar lashevet po?"),
 ("הֵם רוֹצִים לִרְאוֹת סֶרֶט.", "They want to see a film.", "Hem rotsim lir'ot seret."),
], topic="a1-infinitive")

c.T("a1-et", "The Object Marker אֶת", "verb + אֶת + definite noun: אֲנִי רוֹאֶה אֶת הַיֶּלֶד",
 "When the direct object is definite (it has הַ 'the', or it is a name), Hebrew puts the little word אֶת before it: אֲנִי רוֹאֶה אֶת הַבַּיִת ('I see the house'), אֲנִי אוֹהֵב אֶת דָּנָה ('I love Dana'). With an indefinite object there is no אֶת: אֲנִי רוֹאֶה בַּיִת ('I see a house'). אֶת has no translation; it only marks 'this is the object'.",
 "אֶת can take endings too: אוֹתִי (me), אוֹתְךָ (you), אוֹתוֹ (him), אוֹתָהּ (her).",
 [("A", "אַתָּה רוֹאֶה אֶת הַמּוֹרָה?", "Do you see the teacher?"), ("B", "כֵּן, אֲנִי רוֹאֶה אוֹתָהּ.", "Yes, I see her.")])
c.L(7, "The Word אֶת", "אֶת", [
 ("אֲנִי רוֹאֶה אֶת הַיָּם.", "I see the sea.", "Ani ro'e et ha-yam."),
 ("הִיא קוֹרֵאת אֶת הַסֵּפֶר.", "She is reading the book.", "Hi koret et ha-sefer."),
 ("אֲנַחְנוּ אוֹהֲבִים אֶת הָעִיר.", "We love the city.", "Anachnu ohavim et ha-ir."),
 ("אַתָּה מַכִּיר אֶת דָּנָה?", "Do you know Dana?", "Ata makir et Dana?"),
 ("הוּא שׁוֹתֶה אֶת הַקָּפֶה.", "He is drinking the coffee.", "Hu shote et ha-kafe."),
 ("אֲנִי קוֹנָה לֶחֶם.", "I am buying bread. (woman)", "Ani kona lechem."),
 ("הֵם סוֹגְרִים אֶת הַדֶּלֶת.", "They are closing the door.", "Hem sogrim et ha-delet."),
 ("אֲנִי לֹא מוֹצֵא אֶת הַמַּפְתֵּחַ.", "I can't find the key.", "Ani lo motse et ha-mafte'ach."),
], topic="a1-et")

c.T("a1-def-adj", "The Big House: הַ on the Adjective Too", "הַבַּיִת הַגָּדוֹל = the big house · הַבַּיִת גָּדוֹל = the house is big",
 "The adjective comes after the noun. When the noun has 'the' (הַ), the adjective gets הַ too: הַבַּיִת הַגָּדוֹל ('the big house'). Without the second הַ, it becomes a full sentence: הַבַּיִת גָּדוֹל ('the house is big'). Adjectives also agree in gender and number: יֶלֶד קָטָן, יַלְדָּה קְטַנָּה, יְלָדִים קְטַנִּים.",
 "This tiny הַ is the whole difference between a phrase and a sentence, because Hebrew has no 'is' in the present tense.",
 [("A", "אֵיפֹה הַסֵּפֶר הֶחָדָשׁ?", "Where is the new book?"), ("B", "הַסֵּפֶר הֶחָדָשׁ עַל הַשֻּׁלְחָן.", "The new book is on the table.")])
c.L(8, "The Big House", "הַבַּיִת הַגָּדוֹל", [
 ("הַבַּיִת הַגָּדוֹל שֶׁל סַבָּא.", "The big house is grandpa's.", "Ha-bayit ha-gadol shel saba."),
 ("הַבַּיִת גָּדוֹל.", "The house is big.", "Ha-bayit gadol."),
 ("אֲנִי אוֹהֵב אֶת הַמְּכוֹנִית הָאֲדֻמָּה.", "I love the red car.", "Ani ohev et ha-mechonit ha-aduma."),
 ("הַיַּלְדָּה הַקְּטַנָּה שְׂמֵחָה.", "The little girl is happy.", "Ha-yalda ha-ktana smecha."),
 ("הַסֵּפֶר הֶחָדָשׁ מְעַנְיֵן.", "The new book is interesting.", "Ha-sefer he-chadash me'anyen."),
 ("הַיְּלָדִים הַקְּטַנִּים בַּגַּן.", "The little children are in the kindergarten.", "Ha-yeladim ha-ktanim ba-gan."),
 ("הָעִיר הַזֹּאת יָפָה מְאֹד.", "This city is very beautiful.", "Ha-ir ha-zot yafa me'od."),
 ("הַחֶדֶר הַזֶּה נָקִי.", "This room is clean.", "Ha-cheder ha-ze naki."),
], topic="a1-def-adj")

c.T("a1-smichut", "Word Pairs: Smichut", "בַּיִת + סֵפֶר → בֵּית סֵפֶר (school, 'house of book')",
 "Hebrew joins two nouns into one idea by putting them side by side: the first noun 'belongs to' the second. בֵּית סֵפֶר ('house of book') is a school, חֲדַר שֵׁנָה ('room of sleep') is a bedroom. The first noun often changes its vowels (בַּיִת → בֵּית, חֶדֶר → חֲדַר), and 'the' goes only on the second: בֵּית הַסֵּפֶר ('the school').",
 "Many everyday words are smichut pairs: בֵּית חוֹלִים (hospital, 'house of the sick'), כַּדּוּרֶגֶל (football, 'ball-foot', written as one word).",
 [("A", "אֵיפֹה בֵּית הַסֵּפֶר?", "Where is the school?"), ("B", "לְיַד בֵּית הַחוֹלִים.", "Next to the hospital.")])
c.L(9, "Word Pairs", "סְמִיכוּת", [
 ("זֶה בֵּית הַסֵּפֶר שֶׁלִּי.", "This is my school.", "Ze beit ha-sefer sheli."),
 ("חֲדַר הַשֵּׁנָה קָטָן.", "The bedroom is small.", "Chadar ha-shena katan."),
 ("אַבָּא שֶׁלִּי בְּבֵית הַחוֹלִים.", "My dad is at the hospital.", "Aba sheli be-veit ha-cholim."),
 ("יֵשׁ לִי עוּגַת שׁוֹקוֹלָד.", "I have a chocolate cake.", "Yesh li ugat shokolad."),
 ("אֲנִי שׁוֹתָה כּוֹס מַיִם.", "I am drinking a glass of water. (woman)", "Ani shota kos mayim."),
 ("יוֹם הַהֻלֶּדֶת שֶׁלִּי בְּמַאי.", "My birthday is in May.", "Yom ha-huledet sheli be-mai."),
 ("אֵיפֹה תַּחֲנַת הָאוֹטוֹבּוּס?", "Where is the bus stop?", "Eifo tachanat ha-otobus?"),
 ("זֶה סֵפֶר לִמּוּד.", "This is a textbook.", "Ze sefer limud."),
], topic="a1-smichut")

c.T("a1-li-iti", "To Me, With Me: Endings on Prepositions", "לִי לְךָ לָךְ לוֹ לָהּ · אִתִּי אִתְּךָ אִתּוֹ",
 "Small words like לְ (to), עִם (with) and שֶׁל (of) take person endings instead of a separate pronoun: לִי (to me), לְךָ (to you, m), לָךְ (to you, f), לוֹ (to him), לָהּ (to her), לָנוּ (to us), לָהֶם (to them). 'With' uses the stem אִת־: אִתִּי (with me), אִתְּךָ (with you), אִתּוֹ (with him), אִתָּנוּ (with us).",
 "The same endings appear on שֶׁל: שֶׁלִּי (mine), שֶׁלְּךָ (yours), שֶׁלּוֹ (his), so once you know one set you know them all.",
 [("A", "אַתָּה בָּא אִתָּנוּ?", "Are you coming with us?"), ("B", "כֵּן, אֲנִי בָּא אִתְּכֶם!", "Yes, I'm coming with you!")])
c.L(10, "To Me, With Me", "לִי וְאִתִּי", [
 ("תֵּן לִי אֶת הַסֵּפֶר, בְּבַקָּשָׁה.", "Give me the book, please.", "Ten li et ha-sefer, bevakasha."),
 ("אֲנִי כּוֹתֵב לָהּ מִכְתָּב.", "I am writing her a letter.", "Ani kotev la michtav."),
 ("זֶה טוֹב לָנוּ.", "That's good for us.", "Ze tov lanu."),
 ("הִיא בָּאָה אִתִּי.", "She is coming with me.", "Hi ba'a iti."),
 ("אֲנִי רוֹצֶה לְדַבֵּר אִתְּךָ.", "I want to talk with you. (to a man)", "Ani rotse ledaber itcha."),
 ("הֵם גָּרִים אִתָּנוּ.", "They live with us.", "Hem garim itanu."),
 ("מָה שָׁלוֹם הַבֵּן שֶׁלָּהּ?", "How is her son?", "Ma shlom ha-ben shela?"),
 ("הַמַּתָּנָה הַזֹּאת בִּשְׁבִילְךָ.", "This present is for you. (to a man)", "Ha-matana ha-zot bishvilcha."),
], topic="a1-li-iti")

c.T("a1-haya", "Was and Had: הָיָה, הָיָה לִי", "הָיִיתִי · הָיִיתָ · הָיָה · הָיְתָה · הָיִינוּ · הָיוּ",
 "The present tense has no 'is', but the past does: הָיָה (he/it was), הָיְתָה (she/it was), הָיִיתִי (I was), הָיִינוּ (we were), הָיוּ (they were). 'I had' is the past of יֵשׁ לִי: הָיָה לִי (with a masculine thing) or הָיְתָה לִי (with a feminine thing).",
 "אֶתְמוֹל means 'yesterday' and שִׁלְשׁוֹם means 'the day before yesterday'.",
 [("A", "אֵיפֹה הָיִיתָ אֶתְמוֹל?", "Where were you yesterday?"), ("B", "הָיִיתִי בַּבַּיִת. הָיָה לִי חֹם.", "I was at home. I had a fever.")])
c.L(11, "Was and Had", "הָיָה וְהָיָה לִי", [
 ("אֶתְמוֹל הָיִיתִי בַּיָּם.", "Yesterday I was at the sea.", "Etmol hayiti ba-yam."),
 ("הַסֶּרֶט הָיָה מְצֻיָּן.", "The film was excellent.", "Ha-seret haya metsuyan."),
 ("הִיא הָיְתָה בָּעֲבוֹדָה.", "She was at work.", "Hi hayta ba-avoda."),
 ("הָיִינוּ בִּירוּשָׁלַיִם בַּקַּיִץ.", "We were in Jerusalem in the summer.", "Hayinu bi-Yerushalayim ba-kayits."),
 ("הֵם הָיוּ עֲיֵפִים.", "They were tired.", "Hem hayu ayefim."),
 ("הָיָה לִי כֶּלֶב.", "I had a dog.", "Haya li kelev."),
 ("הָיְתָה לָנוּ דִּירָה קְטַנָּה.", "We had a small apartment.", "Hayta lanu dira ktana."),
 ("לֹא הָיָה לִי זְמַן.", "I didn't have time.", "Lo haya li zman."),
], topic="a1-haya")

c.T("a1-past", "The Past Tense", "כָּתַבְתִּי · כָּתַבְתָּ · כָּתַב · כָּתְבָה · כָּתַבְנוּ · כָּתְבוּ",
 "The past tense is built with endings on the root: -תִּי (I), -תָּ (you, m), -תְּ (you, f), nothing (he), -ָה (she), -נוּ (we), -וּ (they). From כ־ת־ב (write): כָּתַבְתִּי (I wrote), כָּתַב (he wrote), כָּתְבָה (she wrote), כָּתַבְנוּ (we wrote). Because the ending shows the person, the pronoun is often dropped: אָכַלְתִּי = 'I ate'.",
 "In the past tense, 'I' and 'we' endings are the same for men and women: a woman also says כָּתַבְתִּי.",
 [("A", "מָה עָשִׂיתָ אֶתְמוֹל?", "What did you do yesterday?"), ("B", "לָמַדְתִּי וְאַחַר כָּךְ רָאִיתִי סֶרֶט.", "I studied and then I watched a film.")])
c.L(12, "Yesterday I…", "אֶתְמוֹל", [
 ("אֶתְמוֹל כָּתַבְתִּי מִכְתָּב.", "Yesterday I wrote a letter.", "Etmol katavti michtav."),
 ("הוּא אָכַל אֲרוּחַת בֹּקֶר.", "He ate breakfast.", "Hu achal aruchat boker."),
 ("הִיא לָמְדָה כָּל הַלַּיְלָה.", "She studied all night.", "Hi lamda kol ha-laila."),
 ("שָׁמַעְנוּ מוּזִיקָה יָפָה.", "We heard beautiful music.", "Shamanu muzika yafa."),
 ("הֵם גָּמְרוּ אֶת הָעֲבוֹדָה.", "They finished the work.", "Hem gamru et ha-avoda."),
 ("רָאִיתָ אֶת הַסֶּרֶט הֶחָדָשׁ?", "Did you see the new film? (to a man)", "Ra'ita et ha-seret he-chadash?"),
 ("סָגַרְתִּי אֶת הַחַלּוֹן.", "I closed the window.", "Sagarti et ha-chalon."),
 ("מָה עָשִׂית בַּשַּׁבָּת?", "What did you do on Shabbat? (to a woman)", "Ma asit ba-shabat?"),
], topic="a1-past")

c.T("a1-went", "Went and Came", "הָלַכְתִּי (I went) · בָּאתִי (I came) · נָסַעְתִּי (I travelled)",
 "Hebrew distinguishes going on foot from travelling by vehicle: הָלַכְתִּי ('I went, walked') vs נָסַעְתִּי ('I went, drove, travelled'). 'Came' is בָּא: בָּאתִי (I came), הוּא בָּא (he came), הִיא בָּאָה (she came), בָּאנוּ (we came). Notice that בָּא is both 'came' and 'comes': context or a time word decides.",
 "When Israelis say they 'went' to another city, they almost always use נָסַע, since nobody walks from Tel Aviv to Haifa.",
 [("A", "אֵיךְ נְסַעְתֶּם לְאֵילַת?", "How did you get to Eilat?"), ("B", "נָסַעְנוּ בְּאוֹטוֹבּוּס.", "We went by bus.")])
c.L(13, "Went and Came", "הָלַכְתִּי וּבָאתִי", [
 ("הָלַכְתִּי לַשּׁוּק בַּבֹּקֶר.", "I went to the market in the morning.", "Halachti la-shuk ba-boker."),
 ("נָסַעְנוּ לְחֵיפָה בְּרַכֶּבֶת.", "We went to Haifa by train.", "Nasanu le-Cheifa be-rakevet."),
 ("הִיא בָּאָה מְאֻחָר.", "She came late.", "Hi ba'a me'uchar."),
 ("מָתַי בָּאתָ הַבַּיְתָה?", "When did you come home? (to a man)", "Matai bata ha-bayta?"),
 ("הֵם הָלְכוּ לַיָּם.", "They went to the beach.", "Hem halchu la-yam."),
 ("בָּאנוּ לְיִשְׂרָאֵל לִפְנֵי שָׁנָה.", "We came to Israel a year ago.", "Banu le-Yisra'el lifnei shana."),
 ("הוּא נָסַע לָעֲבוֹדָה בְּאוֹפַנַּיִם.", "He went to work by bike.", "Hu nasa la-avoda be-ofanayim."),
 ("הָלַכְתְּ לַסֶּרֶט אֶתְמוֹל?", "Did you go to the film yesterday? (to a woman)", "Halacht la-seret etmol?"),
], topic="a1-went")

c.T("a1-going-to", "I'm Going To…", "הוֹלֵךְ / הוֹלֶכֶת + infinitive = going to",
 "Just like English, Hebrew can talk about plans with 'going to': אֲנִי הוֹלֵךְ לִקְנוֹת ('I'm going to buy'), הִיא הוֹלֶכֶת לִלְמֹד ('she's going to study'). Use the present tense of הוֹלֵךְ (agreeing with the speaker) + an infinitive. Time words: מָחָר (tomorrow), בַּשָּׁבוּעַ הַבָּא (next week), אַחַר כָּךְ (later).",
 "Hebrew also has a real future tense (אֶקְנֶה = 'I will buy'), which you'll meet at the next level; 'going to' is the easy way in.",
 [("A", "מָה אַתָּה הוֹלֵךְ לַעֲשׂוֹת מָחָר?", "What are you going to do tomorrow?"), ("B", "אֲנִי הוֹלֵךְ לָנוּחַ!", "I'm going to rest!")])
c.L(14, "Plans: Going To", "מָה עוֹשִׂים מָחָר?", [
 ("מָחָר אֲנִי הוֹלֵךְ לִקְנוֹת אוֹפַנַּיִם.", "Tomorrow I'm going to buy a bike.", "Machar ani holech liknot ofanayim."),
 ("הִיא הוֹלֶכֶת לִלְמֹד בָּאוּנִיבֶרְסִיטָה.", "She is going to study at the university.", "Hi holechet lilmod ba-universita."),
 ("אֲנַחְנוּ הוֹלְכִים לֶאֱכֹל בְּמִסְעָדָה.", "We are going to eat at a restaurant.", "Anachnu holchim le'echol be-mis'ada."),
 ("מָה אַתְּ הוֹלֶכֶת לַעֲשׂוֹת?", "What are you going to do? (to a woman)", "Ma at holechet la'asot?"),
 ("הֵם הוֹלְכִים לִרְאוֹת אֶת סָבְתָא.", "They are going to see grandma.", "Hem holchim lir'ot et savta."),
 ("בַּשָּׁבוּעַ הַבָּא אֲנִי הוֹלֵךְ לַעֲבֹד.", "Next week I'm going to work.", "Ba-shavua ha-ba ani holech la'avod."),
 ("אֲנִי הוֹלֶכֶת לְבַשֵּׁל אֲרוּחַת עֶרֶב.", "I'm going to cook dinner. (woman)", "Ani holechet levashel aruchat erev."),
 ("אַחַר כָּךְ אֲנַחְנוּ הוֹלְכִים לָנוּחַ.", "Afterwards we are going to rest.", "Achar kach anachnu holchim lanu'ach."),
], topic="a1-going-to")

c.T("a1-numbers", "Numbers to 100 and Prices", "עֶשְׂרִים · שְׁלוֹשִׁים · אַרְבָּעִים · חֲמִשִּׁים … מֵאָה",
 "Tens end in -ִים: עֶשְׂרִים (20), שְׁלוֹשִׁים (30), אַרְבָּעִים (40), חֲמִשִּׁים (50), שִׁשִּׁים (60), שִׁבְעִים (70), שְׁמוֹנִים (80), תִּשְׁעִים (90), מֵאָה (100). Join units with וְ: עֶשְׂרִים וְאַחַת (21). Prices are counted in shekels (שֶׁקֶל, plural שְׁקָלִים), and people use the feminine number forms: חֲמִשָּׁה שְׁקָלִים but עֶשְׂרִים שֶׁקֶל in speech. Ask כַּמָּה זֶה עוֹלֶה? ('how much does it cost?').",
 "The Israeli shekel is often written ₪, and since 1985 it has been the 'new shekel', שֶׁקֶל חָדָשׁ.",
 [("A", "כַּמָּה זֶה עוֹלֶה?", "How much does it cost?"), ("B", "שְׁלוֹשִׁים שֶׁקֶל.", "Thirty shekels.")])
c.L(15, "Numbers and Prices", "מִסְפָּרִים וּמְחִירִים", [
 ("כַּמָּה זֶה עוֹלֶה?", "How much does this cost?", "Kama ze ole?"),
 ("זֶה עוֹלֶה עֶשְׂרִים שֶׁקֶל.", "It costs twenty shekels.", "Ze ole esrim shekel."),
 ("בַּכִּתָּה יֵשׁ שְׁלוֹשִׁים תַּלְמִידִים.", "There are thirty students in the class.", "Ba-kita yesh shloshim talmidim."),
 ("סַבָּא שֶׁלִּי בֶּן שְׁמוֹנִים.", "My grandpa is eighty.", "Saba sheli ben shmonim."),
 ("הַסֵּפֶר עוֹלֶה חֲמִשִּׁים שֶׁקֶל.", "The book costs fifty shekels.", "Ha-sefer ole chamishim shekel."),
 ("זֶה יָקָר מִדַּי!", "That's too expensive!", "Ze yakar midai!"),
 ("יֵשׁ מֵאָה עַמּוּדִים בַּסֵּפֶר.", "There are a hundred pages in the book.", "Yesh me'a amudim ba-sefer."),
 ("אֶפְשָׁר לְשַׁלֵּם בְּכַרְטִיס?", "Can I pay by card?", "Efshar leshalem be-chartis?"),
], topic="a1-numbers")

c.T("a1-time", "Telling the Time", "מָה הַשָּׁעָה? · הַשָּׁעָה שָׁלוֹשׁ · בְּשָׁעָה שֶׁבַע",
 "Ask מָה הַשָּׁעָה? ('what's the time?'). Hours use the feminine numbers: הַשָּׁעָה אַחַת (one o'clock), הַשָּׁעָה שָׁלוֹשׁ (three o'clock). 'At' a time is בְּשָׁעָה: בְּשָׁעָה שֶׁבַע ('at seven'). Half past is וְחֵצִי: שְׁתַּיִם וְחֵצִי (half past two), and a quarter past is וְרֶבַע.",
 "In Israel the working week runs Sunday to Thursday; Friday is a short day and Saturday (Shabbat) is the weekend.",
 [("A", "מָה הַשָּׁעָה?", "What time is it?"), ("B", "הַשָּׁעָה שְׁמוֹנֶה וְחֵצִי.", "It's half past eight.")])
c.L(16, "What Time Is It?", "מָה הַשָּׁעָה?", [
 ("מָה הַשָּׁעָה עַכְשָׁו?", "What time is it now?", "Ma ha-sha'a achshav?"),
 ("הַשָּׁעָה שָׁלוֹשׁ.", "It's three o'clock.", "Ha-sha'a shalosh."),
 ("הַשִּׁעוּר מַתְחִיל בְּשָׁעָה תֵּשַׁע.", "The lesson starts at nine.", "Ha-shi'ur matchil be-sha'a tesha."),
 ("אֲנִי קָם בְּשָׁעָה שֶׁבַע.", "I get up at seven.", "Ani kam be-sha'a sheva."),
 ("הָאוֹטוֹבּוּס יוֹצֵא בְּשָׁעָה שְׁתַּיִם וְחֵצִי.", "The bus leaves at half past two.", "Ha-otobus yotse be-sha'a shtayim va-chetsi."),
 ("הַחֲנוּת סְגוּרָה עַד עֶשֶׂר.", "The shop is closed until ten.", "Ha-chanut sgura ad eser."),
 ("כְּבָר מְאֻחָר.", "It's already late.", "Kvar me'uchar."),
 ("נִפָּגֵשׁ בְּשָׁעָה חָמֵשׁ?", "Shall we meet at five?", "Nipagesh be-sha'a chamesh?"),
], topic="a1-time")

c.T("a1-cafe", "At the Café", "אֶפְשָׁר …? · אֲנִי רוֹצֶה … · הַחֶשְׁבּוֹן, בְּבַקָּשָׁה",
 "Ordering is easy with אֶפְשָׁר ('is it possible'): אֶפְשָׁר קָפֶה? ('Can I have a coffee?'). Or say אֲנִי רוֹצֶה / רוֹצָה + the item. The bill is הַחֶשְׁבּוֹן. A very Israeli coffee order is הָפוּךְ ('upside down'), a milky coffee like a latte.",
 "Israeli breakfast in a café usually comes with eggs, a chopped salad, bread, cheeses and dips, and many cafés serve it all day.",
 [("A", "מָה תִּרְצֶה?", "What would you like?"), ("B", "הָפוּךְ גָּדוֹל וּמַיִם, בְּבַקָּשָׁה.", "A large latte and water, please.")])
c.L(17, "At the Café", "בְּבֵית קָפֶה", [
 ("אֶפְשָׁר תַּפְרִיט, בְּבַקָּשָׁה?", "Could I have the menu, please?", "Efshar tafrit, bevakasha?"),
 ("אֲנִי רוֹצָה הָפוּךְ גָּדוֹל.", "I'd like a large latte. (woman)", "Ani rotsa hafuch gadol."),
 ("יֵשׁ לָכֶם תֵּה?", "Do you have tea?", "Yesh lachem te?"),
 ("אֶפְשָׁר סָלָט בְּלִי בָּצָל?", "Can I have a salad without onion?", "Efshar salat bli batsal?"),
 ("הָאֹכֶל טָעִים מְאֹד!", "The food is very tasty!", "Ha-ochel ta'im me'od!"),
 ("עוֹד כּוֹס מַיִם, בְּבַקָּשָׁה.", "Another glass of water, please.", "Od kos mayim, bevakasha."),
 ("הַחֶשְׁבּוֹן, בְּבַקָּשָׁה.", "The bill, please.", "Ha-cheshbon, bevakasha."),
 ("תּוֹדָה, הָיָה מְצֻיָּן!", "Thanks, it was excellent!", "Toda, haya metsuyan!"),
], topic="a1-cafe")

c.T("a1-transport", "Getting Around", "בְּאוֹטוֹבּוּס · בְּרַכֶּבֶת · בְּמוֹנִית · בָּרֶגֶל",
 "'By' a means of transport is בְּ: בְּאוֹטוֹבּוּס (by bus), בְּרַכֶּבֶת (by train), בְּמוֹנִית (by taxi), בִּמְכוֹנִית (by car). 'On foot' is בָּרֶגֶל. Ask the way with אֵיךְ מַגִּיעִים לְ…? ('how do you get to…?').",
 "On Shabbat most Israeli buses and trains don't run, from Friday afternoon until Saturday evening.",
 [("A", "אֵיךְ מַגִּיעִים לַתַּחֲנָה הַמֶּרְכָּזִית?", "How do you get to the central bus station?"), ("B", "בְּאוֹטוֹבּוּס מִסְפָּר חָמֵשׁ.", "By bus number five.")])
c.L(18, "Getting Around", "תַּחְבּוּרָה", [
 ("אֲנִי נוֹסֵעַ לָעֲבוֹדָה בְּאוֹטוֹבּוּס.", "I go to work by bus.", "Ani nose'a la-avoda be-otobus."),
 ("הָרַכֶּבֶת לִירוּשָׁלַיִם מְהִירָה.", "The train to Jerusalem is fast.", "Ha-rakevet li-Yerushalayim mehira."),
 ("אֲנַחְנוּ צְרִיכִים מוֹנִית.", "We need a taxi.", "Anachnu tsrichim monit."),
 ("אֵיךְ מַגִּיעִים לַיָּם?", "How do you get to the beach?", "Eich magi'im la-yam?"),
 ("זֶה קָרוֹב, אֶפְשָׁר לָלֶכֶת בָּרֶגֶל.", "It's close, you can walk.", "Ze karov, efshar lalechet ba-regel."),
 ("אֵיפֹה עוֹצֵר הָאוֹטוֹבּוּס?", "Where does the bus stop?", "Eifo otser ha-otobus?"),
 ("כַּמָּה עוֹלֶה כַּרְטִיס?", "How much is a ticket?", "Kama ole kartis?"),
 ("הַשְּׂדֵה תְּעוּפָה רָחוֹק מֵהָעִיר.", "The airport is far from the city.", "Ha-sde te'ufa rachok me-ha-ir."),
], topic="a1-transport")

c.T("a1-jobs", "Jobs", "רוֹפֵא / רוֹפְאָה · מוֹרֶה / מוֹרָה · מְהַנְדֵּס / מְהַנְדֶּסֶת",
 "Job words have a masculine and a feminine form: רוֹפֵא / רוֹפְאָה (doctor), מוֹרֶה / מוֹרָה (teacher), מְהַנְדֵּס / מְהַנְדֶּסֶת (engineer), אָחוֹת (nurse). Say what someone does with no 'is': הִיא רוֹפְאָה ('she is a doctor'). Ask בְּמָה אַתָּה עוֹבֵד? ('what do you work in?').",
 "Many Israelis serve in the army after school (usually 2–3 years) and only then go to university, so students are often older than in other countries.",
 [("A", "בְּמָה אַתָּה עוֹבֵד?", "What do you do for work?"), ("B", "אֲנִי מוֹרֶה. וְאַתְּ?", "I'm a teacher. And you?"), ("A", "אֲנִי אָחוֹת.", "I'm a nurse.")])
c.L(19, "Jobs", "מִקְצוֹעוֹת", [
 ("אִמָּא שֶׁלִּי רוֹפְאָה.", "My mom is a doctor.", "Ima sheli rof'a."),
 ("אֲנִי מוֹרֶה לְאַנְגְּלִית.", "I am an English teacher.", "Ani more le-anglit."),
 ("הוּא מְהַנְדֵּס בְּחֶבְרָה גְּדוֹלָה.", "He is an engineer at a big company.", "Hu mehandes be-chevra gdola."),
 ("הִיא עוֹבֶדֶת בְּבַנְק.", "She works at a bank.", "Hi ovedet be-bank."),
 ("בְּמָה אַתָּה עוֹבֵד?", "What do you do for work? (to a man)", "Be-ma ata oved?"),
 ("הָאָחוֹת עוֹזֶרֶת לַחוֹלִים.", "The nurse helps the patients.", "Ha-achot ozeret la-cholim."),
 ("אֲנִי סְטוּדֶנְטִית.", "I am a student. (woman)", "Ani studentit."),
 ("הַנַּהָג נוֹסֵעַ לְאַט.", "The driver is driving slowly.", "Ha-nahag nose'a le'at."),
], topic="a1-jobs")

c.T("a1-compare", "Bigger Than: יוֹתֵר … מִ", "יוֹתֵר גָּדוֹל מִ… (bigger than) · הֲכִי גָּדוֹל (the biggest)",
 "To compare, put יוֹתֵר ('more') before the adjective and מִ ('from') before the thing compared: תֵּל אָבִיב יוֹתֵר גְּדוֹלָה מֵחֵיפָה ('Tel Aviv is bigger than Haifa'). 'Less' is פָּחוֹת. 'The most' is הֲכִי: הֲכִי טוֹב ('the best'). Before ה, ח, ע, ר the prefix מִ becomes מֵ.",
 "הֲכִי טוֹב ('the best') is also an everyday reply meaning 'great, perfect'.",
 [("A", "מָה יוֹתֵר טָעִים, פִּיצָה אוֹ פָלָאפֶל?", "What's tastier, pizza or falafel?"), ("B", "פָלָאפֶל, בָּרוּר!", "Falafel, obviously!")])
c.L(20, "Bigger Than", "יוֹתֵר וּפָחוֹת", [
 ("הָאָח שֶׁלִּי יוֹתֵר גָּבֹהַּ מִמֶּנִּי.", "My brother is taller than me.", "Ha-ach sheli yoter gavo'ah mimeni."),
 ("הַקַּיִץ יוֹתֵר חַם מֵהַחֹרֶף.", "Summer is hotter than winter.", "Ha-kayits yoter cham me-ha-choref."),
 ("הַסֵּפֶר הַזֶּה פָּחוֹת מְעַנְיֵן.", "This book is less interesting.", "Ha-sefer ha-ze pachot me'anyen."),
 ("זֶה הַבַּיִת הֲכִי יָפֶה בָּרְחוֹב.", "This is the most beautiful house on the street.", "Ze ha-bayit hachi yafe ba-rechov."),
 ("הָרַכֶּבֶת יוֹתֵר מְהִירָה מֵהָאוֹטוֹבּוּס.", "The train is faster than the bus.", "Ha-rakevet yoter mehira me-ha-otobus."),
 ("הִיא הַתַּלְמִידָה הֲכִי טוֹבָה בַּכִּתָּה.", "She is the best student in the class.", "Hi ha-talmida hachi tova ba-kita."),
 ("הַיּוֹם יוֹתֵר קַר מֵאֶתְמוֹל.", "Today is colder than yesterday.", "Ha-yom yoter kar me-etmol."),
 ("מָה יוֹתֵר טָעִים?", "What's tastier?", "Ma yoter ta'im?"),
], topic="a1-compare")

c.R(101, "Reading: A Day in Tel Aviv", "יוֹם בְּתֵל אָבִיב", "Yoni describes a Friday in Tel Aviv.", [
 ("בְּיוֹם שִׁשִּׁי נָסַעְתִּי לְתֵל אָבִיב בְּרַכֶּבֶת.", "On Friday I went to Tel Aviv by train."),
 ("בַּבֹּקֶר הָלַכְתִּי לַשּׁוּק וְקָנִיתִי פֵּרוֹת.", "In the morning I went to the market and bought fruit."),
 ("אַחַר כָּךְ יָשַׁבְתִּי בְּבֵית קָפֶה וְשָׁתִיתִי הָפוּךְ.", "Then I sat in a café and drank a latte."),
 ("בַּצׇּהֳרַיִם הָלַכְתִּי לַיָּם עִם חָבֵר.", "At noon I went to the beach with a friend."),
 ("הַמַּיִם הָיוּ חַמִּים וְהָיָה הַרְבֵּה אֲנָשִׁים.", "The water was warm and there were a lot of people."),
 ("בָּעֶרֶב חָזַרְתִּי הַבַּיְתָה עָיֵף אֲבָל שָׂמֵחַ.", "In the evening I came home tired but happy."),
], [
 ("How did Yoni get to Tel Aviv?", ["By train", "By bus", "By car", "On foot"], 0),
 ("What did he buy at the market?", ["Fruit", "Bread", "A book", "Clothes"], 0),
 ("What did he drink at the café?", ["A latte", "Tea", "Juice", "Water"], 0),
 ("How did he feel in the evening?", ["Tired but happy", "Sad", "Hungry", "Angry"], 0),
])
c.save()
