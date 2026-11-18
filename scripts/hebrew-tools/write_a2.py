"""Content source for data/hebrew-src/a2.json. Run: HE_DICT=<folder with kaikki Hebrew jsonl> python3 write_a2.py"""
import os
os.environ.setdefault("HE_DICT", "/private/tmp/claude-501/-Users-omar/3e230d6a-2df5-44ac-a5be-c38644d3169b/scratchpad/he-dict")
from author_he import Course
c = Course("a2", "a2", start=1)

c.T("a2-future", "The Future Tense", "אֶלְמַד · תִּלְמַד · יִלְמַד · תִּלְמַד · נִלְמַד · יִלְמְדוּ",
 "The future tense is built with prefixes: אֶ־ (I), תִּ־ (you, m; she), יִ־ (he), נִ־ (we), and יִ…וּ (they). From ל־מ־ד: אֶלְמַד (I will study), תִּלְמַד (you will study / she will study), יִלְמַד (he will study), נִלְמַד (we will study), יִלְמְדוּ (they will study). 'You' to a woman adds ־ִי: תִּלְמְדִי.",
 "In everyday speech the future is also used for polite requests: תִּסְגֹּר אֶת הַדֶּלֶת = 'close the door, would you'.",
 [("A", "מָתַי תִּגְמֹר?", "When will you finish?"), ("B", "אֶגְמֹר בְּעוֹד שָׁעָה.", "I'll finish in an hour.")])
c.L(1, "I Will…", "עָתִיד", [
 ("מָחָר אֶלְמַד בַּסִּפְרִיָּה.", "Tomorrow I will study in the library.", "Machar elmad ba-sifriya."),
 ("הוּא יִכְתֹּב לָנוּ מִכְתָּב.", "He will write us a letter.", "Hu yichtov lanu michtav."),
 ("הִיא תִּגְמֹר אֶת הָעֲבוֹדָה בְּעֶרֶב.", "She will finish the work in the evening.", "Hi tigmor et ha-avoda be-erev."),
 ("נִשְׁמַע מוּזִיקָה בַּמְּכוֹנִית.", "We will listen to music in the car.", "Nishma muzika ba-mechonit."),
 ("הֵם יִלְמְדוּ בָּאוּנִיבֶרְסִיטָה.", "They will study at the university.", "Hem yilmedu ba-universita."),
 ("מָתַי תִּסְגֹּר אֶת הַחֲנוּת?", "When will you close the shop? (to a man)", "Matai tisgor et ha-chanut?"),
 ("אֶשְׁמֹר לְךָ מָקוֹם.", "I'll save you a seat.", "Eshmor lecha makom."),
 ("בַּשָּׁנָה הַבָּאָה נִגְמֹר אֶת הַלִּמּוּדִים.", "Next year we will finish our studies.", "Ba-shana ha-ba'a nigmor et ha-limudim."),
], topic="a2-future")

c.T("a2-future-irr", "Will Go, Will Come, Will Be", "אֵלֵךְ · אָבוֹא · אֶהְיֶה · אֶעֱשֶׂה · אֹכַל",
 "The most common verbs have short future forms that are worth memorising: אֵלֵךְ (I'll go), תֵּלֵךְ, יֵלֵךְ, נֵלֵךְ; אָבוֹא (I'll come), יָבוֹא, נָבוֹא; אֶהְיֶה (I'll be), יִהְיֶה (he/it will be), תִּהְיֶה (she will be), נִהְיֶה; אֶעֱשֶׂה (I'll do), נַעֲשֶׂה (we'll do).",
 "יִהְיֶה בְּסֵדֶר ('it will be fine') is probably the most Israeli sentence there is.",
 [("A", "אַתָּה תָּבוֹא לַמְּסִבָּה?", "Will you come to the party?"), ("B", "כֵּן, אָבוֹא אַחֲרֵי הָעֲבוֹדָה.", "Yes, I'll come after work.")])
c.L(2, "Will Go, Will Come, Will Be", "אֵלֵךְ, אָבוֹא, אֶהְיֶה", [
 ("מָחָר אֵלֵךְ לָרוֹפֵא.", "Tomorrow I'll go to the doctor.", "Machar elech la-rofe."),
 ("הִיא תָּבוֹא בְּשָׁעָה שְׁמוֹנֶה.", "She will come at eight.", "Hi tavo be-sha'a shmone."),
 ("יִהְיֶה בְּסֵדֶר.", "It will be fine.", "Yihye be-seder."),
 ("מָה נַעֲשֶׂה בַּשַּׁבָּת?", "What will we do on Shabbat?", "Ma na'ase ba-shabat?"),
 ("אֲנִי אֶהְיֶה בַּבַּיִת כָּל הַיּוֹם.", "I will be at home all day.", "Ani ehye ba-bayit kol ha-yom."),
 ("הֵם יֵלְכוּ לַיָּם בַּבֹּקֶר.", "They will go to the beach in the morning.", "Hem yelchu la-yam ba-boker."),
 ("מָחָר יִהְיֶה חַם.", "Tomorrow it will be hot.", "Machar yihye cham."),
 ("נָבוֹא אֲלֵיכֶם בְּעֶרֶב.", "We'll come to you in the evening.", "Navo aleichem be-erev."),
], topic="a2-future-irr")

c.T("a2-imperative", "Come Here! Commands and Requests", "בּוֹא · בּוֹאִי · שֵׁב · תֵּן לִי · אַל + future = don't",
 "Short commands: בּוֹא / בּוֹאִי / בּוֹאוּ (come, to m / f / pl), שֵׁב / שְׁבִי (sit), תֵּן / תְּנִי (give), תַּגִּיד (tell, said politely with the future). 'Don't' is אַל + the future: אַל תִּדְאַג ('don't worry'), אַל תְּדַבֵּר ('don't talk'). Add בְּבַקָּשָׁה and it's polite.",
 "The future used as a command (תַּגִּיד, תָּבוֹא) sounds softer than the real imperative, so it is what most Israelis actually say.",
 [("A", "בּוֹא, שֵׁב אִתָּנוּ!", "Come, sit with us!"), ("B", "תּוֹדָה, אֲבָל אַל תְּחַכּוּ לִי.", "Thanks, but don't wait for me.")])
c.L(3, "Come Here! Commands", "צִוּוּי", [
 ("בּוֹא הֵנָּה, בְּבַקָּשָׁה.", "Come here, please. (to a man)", "Bo hena, bevakasha."),
 ("בּוֹאִי נֵלֵךְ.", "Come on, let's go. (to a woman)", "Bo'i nelech."),
 ("שֵׁב, בְּבַקָּשָׁה.", "Sit down, please. (to a man)", "Shev, bevakasha."),
 ("תֵּן לִי אֶת הַמַּפְתֵּחַ.", "Give me the key. (to a man)", "Ten li et ha-mafte'ach."),
 ("אַל תִּדְאַג.", "Don't worry. (to a man)", "Al tid'ag."),
 ("אַל תִּשְׁכְּחִי אֶת הַטֵּלֵפוֹן.", "Don't forget the phone. (to a woman)", "Al tishkechi et ha-telefon."),
 ("תַּגִּיד לִי מָתַי.", "Tell me when. (to a man)", "Tagid li matai."),
 ("בּוֹאוּ לֶאֱכֹל!", "Come and eat! (to everyone)", "Bo'u le'echol!"),
], topic="a2-imperative")

c.T("a2-conj", "Because, When, If", "כִּי (because) · כְּשֶׁ… (when) · אִם (if) · אֲבָל (but)",
 "Join two ideas with: כִּי ('because'), כְּשֶׁ ('when', written joined to the next word: כְּשֶׁאֲנִי), אִם ('if'), אֲבָל ('but'), אָז ('so, then'). With אִם and כְּשֶׁ about the future, Hebrew uses the future tense in both parts: אִם יִהְיֶה חַם, נֵלֵךְ לַיָּם ('if it's hot, we'll go to the sea').",
 "Hebrew has no separate subjunctive: אִם + future does all the work of English 'if… will'.",
 [("A", "לָמָּה אַתָּה לֹא בָּא?", "Why aren't you coming?"), ("B", "כִּי אֲנִי עָיֵף.", "Because I'm tired.")])
c.L(4, "Because, When, If", "כִּי, כְּשֶׁ, אִם", [
 ("אֲנִי לֹא בָּא כִּי אֲנִי חוֹלֶה.", "I'm not coming because I'm sick.", "Ani lo ba ki ani chole."),
 ("כְּשֶׁאֲנִי עָיֵף, אֲנִי שׁוֹתֶה קָפֶה.", "When I'm tired, I drink coffee.", "Ksheani ayef, ani shote kafe."),
 ("אִם יִהְיֶה חַם, נֵלֵךְ לַיָּם.", "If it's hot, we'll go to the beach.", "Im yihye cham, nelech la-yam."),
 ("רָצִיתִי לָבוֹא, אֲבָל לֹא הָיָה לִי זְמַן.", "I wanted to come, but I didn't have time.", "Ratsiti lavo, aval lo haya li zman."),
 ("יָרַד גֶּשֶׁם, אָז נִשְׁאַרְנוּ בַּבַּיִת.", "It rained, so we stayed home.", "Yarad geshem, az nisharnu ba-bayit."),
 ("אִם תִּרְצֶה, אֶפְשָׁר לְהִפָּגֵשׁ מָחָר.", "If you want, we can meet tomorrow.", "Im tirtse, efshar lehipagesh machar."),
 ("כְּשֶׁהָיִיתִי יֶלֶד, גַּרְנוּ בְּחֵיפָה.", "When I was a child, we lived in Haifa.", "Kshehayiti yeled, garnu be-Cheifa."),
 ("הִיא שְׂמֵחָה כִּי הִיא קִבְּלָה מַתָּנָה.", "She is happy because she got a present.", "Hi smecha ki hi kibla matana."),
], topic="a2-conj")

c.T("a2-she", "The Book That I Bought: שֶׁ", "הַסֵּפֶר שֶׁקָּנִיתִי · הָאִישׁ שֶׁגָּר פֹּה",
 "'That / who / which' is the prefix שֶׁ, joined to the next word: הַסֵּפֶר שֶׁקָּנִיתִי ('the book that I bought'), הָאִישׁ שֶׁגָּר פֹּה ('the man who lives here'). It also introduces what someone says or thinks: הוּא אוֹמֵר שֶׁהוּא עָיֵף ('he says that he is tired').",
 "In formal writing you'll also see אֲשֶׁר instead of שֶׁ; it means exactly the same.",
 [("A", "מִי הָאִשָּׁה שֶׁעוֹמֶדֶת שָׁם?", "Who is the woman standing there?"), ("B", "זֹאת הַמּוֹרָה שֶׁלִּי.", "That's my teacher.")])
c.L(5, "The One That…", "שֶׁ", [
 ("זֶה הַסֵּפֶר שֶׁקָּנִיתִי אֶתְמוֹל.", "This is the book I bought yesterday.", "Ze ha-sefer shekaniti etmol."),
 ("הָאִישׁ שֶׁגָּר פֹּה הוּא רוֹפֵא.", "The man who lives here is a doctor.", "Ha-ish shegar po hu rofe."),
 ("אֲנִי חוֹשֵׁב שֶׁהוּא צוֹדֵק.", "I think that he is right.", "Ani choshev shehu tsodek."),
 ("הִיא אָמְרָה שֶׁהִיא תָּבוֹא.", "She said that she would come.", "Hi amra shehi tavo."),
 ("אֵיפֹה הַמְּכוֹנִית שֶׁקָּנִיתָ?", "Where is the car you bought? (to a man)", "Eifo ha-mechonit shekanita?"),
 ("יֵשׁ לִי חָבֵר שֶׁמְּדַבֵּר רוּסִית.", "I have a friend who speaks Russian.", "Yesh li chaver shemedaber rusit."),
 ("הָעִיר שֶׁנּוֹלַדְתִּי בָּהּ קְטַנָּה.", "The town where I was born is small.", "Ha-ir shenoladti ba ktana."),
 ("אֲנִי יוֹדַעַת שֶׁזֶּה קָשֶׁה.", "I know that it's hard. (woman)", "Ani yoda'at sheze kashe."),
], topic="a2-she")

c.T("a2-piel", "Piel Verbs: מְדַבֵּר, דִּבַּרְתִּי", "present מְדַבֵּר · past דִּבַּרְתִּי · infinitive לְדַבֵּר",
 "Verbs in the pattern called piel have a doubled middle letter and an 'i–e' past: דִּבֵּר (he spoke), בִּקֵּר (he visited), חִפֵּשׂ (he looked for), שִׁלֵּם (he paid). The present starts with מְ: מְדַבֵּר, מְבַקֵּר, מְחַפֵּשׂ. The infinitive starts with לְ: לְדַבֵּר, לְבַקֵּר, לְשַׁלֵּם.",
 "Once you hear the מְ…ֵ sound in the present (מְדַבֵּר, מְסַפֵּר, מְנַקֶּה) you can recognise piel verbs anywhere.",
 [("A", "מָה אַתָּה מְחַפֵּשׂ?", "What are you looking for?"), ("B", "אֲנִי מְחַפֵּשׂ אֶת הַמַּפְתְּחוֹת.", "I'm looking for the keys.")])
c.L(6, "Speak, Visit, Look For", "בִּנְיַן פִּעֵל", [
 ("אֶתְמוֹל דִּבַּרְתִּי עִם אִמָּא.", "Yesterday I talked with mom.", "Etmol dibarti im ima."),
 ("בַּשַּׁבָּת בִּקַּרְנוּ אֶת סָבְתָא.", "On Shabbat we visited grandma.", "Ba-shabat bikarnu et savta."),
 ("הוּא מְחַפֵּשׂ עֲבוֹדָה חֲדָשָׁה.", "He is looking for a new job.", "Hu mechapes avoda chadasha."),
 ("מִי שִׁלֵּם עַל הָאֹכֶל?", "Who paid for the food?", "Mi shilem al ha-ochel?"),
 ("הִיא מְסַפֶּרֶת סִפּוּר לַיְּלָדִים.", "She is telling the children a story.", "Hi mesaperet sipur la-yeladim."),
 ("אֲנִי רוֹצֶה לְבַקֵּר בִּירוּשָׁלַיִם.", "I want to visit Jerusalem.", "Ani rotse levaker bi-Yerushalayim."),
 ("צָרִיךְ לְנַקּוֹת אֶת הַבַּיִת.", "The house needs cleaning.", "Tsarich lenakot et ha-bayit."),
 ("הַמּוֹרֶה מְלַמֵּד עִבְרִית.", "The teacher teaches Hebrew.", "Ha-more melamed ivrit."),
], topic="a2-piel")

c.T("a2-hitpael", "Hitpael: Doing It to Yourself", "מִתְלַבֵּשׁ · הִתְלַבַּשְׁתִּי · לְהִתְלַבֵּשׁ",
 "The pattern hitpael often means doing something to yourself or with each other. It starts with מִתְ in the present, הִתְ in the past and lehit- in the infinitive: מִתְלַבֵּשׁ (gets dressed), הִתְרַחַצְתִּי (I washed), לְהִתְקַשֵּׁר (to call), הִתְחַתְּנוּ (they got married).",
 "לְהִתְקַשֵּׁר ('to call') literally means 'to connect yourself': you 'connect yourself to' someone, אֲנִי מִתְקַשֵּׁר אֵלֶיךָ.",
 [("A", "תִּתְקַשֵּׁר אֵלַי מָחָר?", "Will you call me tomorrow?"), ("B", "בֶּטַח, אֶתְקַשֵּׁר בַּבֹּקֶר.", "Sure, I'll call in the morning.")])
c.L(7, "Getting Dressed, Calling", "בִּנְיַן הִתְפַּעֵל", [
 ("אֲנִי מִתְלַבֵּשׁ מַהֵר בַּבֹּקֶר.", "I get dressed quickly in the morning.", "Ani mitlabesh maher ba-boker."),
 ("הִיא הִתְקַשְּׁרָה אֵלַי אֶתְמוֹל.", "She called me yesterday.", "Hi hitkashra elai etmol."),
 ("הֵם הִתְחַתְּנוּ בַּקַּיִץ.", "They got married in the summer.", "Hem hitchatnu ba-kayits."),
 ("אֲנִי צָרִיךְ לְהִתְרַחֵץ.", "I need to wash.", "Ani tsarich lehitrachets."),
 ("הַסֶּרֶט מַתְחִיל, אֲנַחְנוּ מִתְרַגְּשִׁים.", "The film is starting, we are excited.", "Ha-seret matchil, anachnu mitragshim."),
 ("אֲנִי מִתְגַּעְגֵּעַ לַמִּשְׁפָּחָה.", "I miss my family.", "Ani mitga'agea la-mishpacha."),
 ("תִּתְקַשֵּׁר אֵלַי כְּשֶׁתַּגִּיעַ.", "Call me when you arrive. (to a man)", "Titkasher elai kshetagi'a."),
 ("הַשַּׂחְקָנִים מִתְאַמְּנִים כָּל בֹּקֶר.", "The players train every morning.", "Ha-sachkanim mit'amnim kol boker."),
], topic="a2-hitpael")

c.T("a2-doctor", "At the Doctor", "כּוֹאֵב לִי · יֵשׁ לִי חֹם · אֲנִי מַרְגִּישׁ לֹא טוֹב",
 "Say what hurts with כּוֹאֵב לִי + the body part: כּוֹאֵב לִי הָרֹאשׁ ('my head hurts'); with a feminine or plural part, כּוֹאֶבֶת / כּוֹאֲבוֹת. 'I have a fever' is יֵשׁ לִי חֹם. The doctor may ask מָה מַרְגִּישׁ? or מָה כּוֹאֵב?",
 "In Israel you register with a קֻפַּת חוֹלִים ('sick fund'), a health organisation that runs the clinics and covers your doctor visits.",
 [("A", "מָה כּוֹאֵב לְךָ?", "What hurts?"), ("B", "כּוֹאֵב לִי הַגָּרוֹן וְיֵשׁ לִי חֹם.", "My throat hurts and I have a fever.")])
c.L(8, "At the Doctor", "אֵצֶל הָרוֹפֵא", [
 ("אֲנִי מַרְגִּישׁ לֹא טוֹב.", "I don't feel well.", "Ani margish lo tov."),
 ("כּוֹאֵב לִי הָרֹאשׁ.", "My head hurts.", "Ko'ev li ha-rosh."),
 ("יֵשׁ לִי חֹם מֵאֶתְמוֹל.", "I've had a fever since yesterday.", "Yesh li chom me-etmol."),
 ("כּוֹאֶבֶת לִי הַבֶּטֶן.", "My stomach hurts.", "Ko'evet li ha-beten."),
 ("קַח אֶת הַתְּרוּפָה שָׁלוֹשׁ פְּעָמִים בַּיּוֹם.", "Take the medicine three times a day.", "Kach et ha-trufa shalosh pe'amim ba-yom."),
 ("אַתָּה צָרִיךְ לָנוּחַ.", "You need to rest.", "Ata tsarich lanu'ach."),
 ("יֵשׁ לִי תּוֹר לָרוֹפְאָה בְּיוֹם שֵׁנִי.", "I have an appointment with the doctor on Monday.", "Yesh li tor la-rof'a be-yom sheni."),
 ("רְפוּאָה שְׁלֵמָה!", "Get well soon!", "Refu'a shlema!"),
], topic="a2-doctor")

c.T("a2-clothes", "Buying Clothes", "מִדָּה · לִמְדֹּד · זֶה גָּדוֹל עָלַי",
 "In a clothes shop: מָה הַמִּדָּה שֶׁלְּךָ? ('what's your size?'), אֶפְשָׁר לִמְדֹּד? ('can I try it on?'). Say how it fits with עָלַי ('on me'): זֶה קָטָן עָלַי ('it's small on me'), זֶה יָפֶה עָלַיִךְ ('it looks nice on you', to a woman).",
 "End-of-season sales are called סוֹף עוֹנָה ('end of season'), and the big ones come in January and August.",
 [("A", "אֶפְשָׁר לִמְדֹּד אֶת הַחֻלְצָה?", "Can I try on the shirt?"), ("B", "כֵּן, חֲדַר הַמְּדִידָה שָׁם.", "Yes, the fitting room is there.")])
c.L(9, "Buying Clothes", "קוֹנִים בְּגָדִים", [
 ("אֲנִי מְחַפֶּשֶׂת שִׂמְלָה לַחֲתֻנָּה.", "I'm looking for a dress for a wedding.", "Ani mechapeset simla la-chatuna."),
 ("אֶפְשָׁר לִמְדֹּד אֶת הַמִּכְנָסַיִם?", "Can I try on the trousers?", "Efshar limdod et ha-michnasayim?"),
 ("יֵשׁ מִדָּה יוֹתֵר גְּדוֹלָה?", "Is there a bigger size?", "Yesh mida yoter gdola?"),
 ("הַחֻלְצָה הַזֹּאת קְטַנָּה עָלַי.", "This shirt is small on me.", "Ha-chultsa ha-zot ktana alai."),
 ("זֶה יָפֶה עָלַיִךְ!", "That looks nice on you! (to a woman)", "Ze yafe alayich!"),
 ("כַּמָּה עוֹלוֹת הַנַּעֲלַיִם?", "How much are the shoes?", "Kama olot ha-na'alayim?"),
 ("יֵשׁ הֲנָחָה הַיּוֹם?", "Is there a discount today?", "Yesh hanacha ha-yom?"),
 ("אֲנִי אֶקְנֶה אֶת זֶה.", "I'll buy this one.", "Ani ekne et ze."),
], topic="a2-clothes")

c.T("a2-apartment", "Renting an Apartment", "דִּירָה לְהַשְׂכָּרָה · שְׂכַר דִּירָה · חֲדָרִים",
 "Israeli flats are counted by rooms including the living room: a דִּירַת שְׁלוֹשָׁה חֲדָרִים has two bedrooms and a salon. Rent is שְׂכַר דִּירָה, the landlord is בַּעַל הַבַּיִת, and a balcony is מִרְפֶּסֶת. Most flats have a מַמָּ\"ד, a reinforced safe room.",
 "Many Israeli flats have a שֶׁמֶשׁ־boiler on the roof: a solar water heater, required on new buildings since the 1980s.",
 [("A", "כַּמָּה חֲדָרִים יֵשׁ בַּדִּירָה?", "How many rooms does the flat have?"), ("B", "שְׁלוֹשָׁה חֲדָרִים וּמִרְפֶּסֶת.", "Three rooms and a balcony.")])
c.L(10, "Renting an Apartment", "שׂוֹכְרִים דִּירָה", [
 ("אֲנַחְנוּ מְחַפְּשִׂים דִּירָה בְּתֵל אָבִיב.", "We are looking for a flat in Tel Aviv.", "Anachnu mechapsim dira be-Tel Aviv."),
 ("כַּמָּה עוֹלֶה שְׂכַר הַדִּירָה?", "How much is the rent?", "Kama ole schar ha-dira?"),
 ("יֵשׁ בַּדִּירָה מִרְפֶּסֶת גְּדוֹלָה.", "The flat has a big balcony.", "Yesh ba-dira mirpeset gdola."),
 ("הַמִּטְבָּח קָטָן אֲבָל נָעִים.", "The kitchen is small but pleasant.", "Ha-mitbach katan aval na'im."),
 ("אֶפְשָׁר לִרְאוֹת אֶת הַדִּירָה מָחָר?", "Can we see the flat tomorrow?", "Efshar lir'ot et ha-dira machar?"),
 ("הַדִּירָה בַּקּוֹמָה הַשְּׁלִישִׁית.", "The flat is on the third floor.", "Ha-dira ba-koma ha-shlishit."),
 ("יֵשׁ מַעֲלִית בַּבִּנְיָן?", "Is there a lift in the building?", "Yesh ma'alit ba-binyan?"),
 ("הַשְּׁכֵנִים שֶׁלָּנוּ נֶחְמָדִים.", "Our neighbours are nice.", "Ha-shchenim shelanu nechmadim."),
], topic="a2-apartment")

c.T("a2-phone", "On the Phone", "הַלּוֹ · מִי מְדַבֵּר? · אֶפְשָׁר לְדַבֵּר עִם…?",
 "Phone calls start with הַלּוֹ? or כֵּן? Ask for someone with אֶפְשָׁר לְדַבֵּר עִם…? and say who you are with מְדַבֵּר / מְדַבֶּרֶת + your name ('X speaking'). If the line is bad: לֹא שׁוֹמְעִים ('I can't hear'). End with יַאלְלָה בַּי or simply בַּי.",
 "Israelis often finish calls with the English 'bye' — or 'yalla bye', a mix of Arabic and English.",
 [("A", "הַלּוֹ, מִי מְדַבֵּר?", "Hello, who's speaking?"), ("B", "מְדַבֶּרֶת דָּנָה. אֶפְשָׁר לְדַבֵּר עִם יוֹסִי?", "It's Dana. Can I speak to Yosi?")])
c.L(11, "On the Phone", "בַּטֵּלֵפוֹן", [
 ("הַלּוֹ, מִי מְדַבֵּר?", "Hello, who's speaking?", "Halo, mi medaber?"),
 ("מְדַבֵּר דָּוִד.", "David speaking.", "Medaber David."),
 ("אֶפְשָׁר לְדַבֵּר עִם רוּת?", "Can I speak with Rut?", "Efshar ledaber im Rut?"),
 ("הִיא לֹא בַּבַּיִת עַכְשָׁו.", "She isn't home right now.", "Hi lo ba-bayit achshav."),
 ("אֲנִי אֶתְקַשֵּׁר אַחַר כָּךְ.", "I'll call later.", "Ani etkasher achar kach."),
 ("לֹא שׁוֹמְעִים אוֹתְךָ טוֹב.", "I can't hear you well. (to a man)", "Lo shom'im otcha tov."),
 ("תַּשְׁאִיר הוֹדָעָה, בְּבַקָּשָׁה.", "Leave a message, please. (to a man)", "Tashir hoda'a, bevakasha."),
 ("שָׁלַחְתִּי לְךָ הוֹדָעָה.", "I sent you a message. (to a man)", "Shalachti lecha hoda'a."),
], topic="a2-phone")

c.T("a2-feelings", "How Do You Feel?", "אֲנִי מַרְגִּישׁ… · שָׂמֵחַ · עָצוּב · כּוֹעֵס · מְפַחֵד",
 "Talk about feelings with אֲנִי מַרְגִּישׁ / מַרְגִּישָׁה + an adjective, or just the adjective: אֲנִי עָצוּב ('I'm sad'). Feeling words agree in gender: שָׂמֵחַ / שְׂמֵחָה (happy), עָצוּב / עֲצוּבָה (sad), כּוֹעֵס / כּוֹעֶסֶת (angry), עָיֵף / עֲיֵפָה (tired). 'Afraid of' is מְפַחֵד מִ…",
 "To say 'I'm bored' Hebrew uses the dative: מְשַׁעֲמֵם לִי, literally 'it's boring to me'.",
 [("A", "לָמָּה אַתְּ עֲצוּבָה?", "Why are you sad?"), ("B", "כִּי הַחָבֵר שֶׁלִּי עוֹזֵב.", "Because my friend is leaving.")])
c.L(12, "How Do You Feel?", "רְגָשׁוֹת", [
 ("אֲנִי שָׂמֵחַ לִרְאוֹת אוֹתְךָ.", "I'm happy to see you.", "Ani same'ach lir'ot otcha."),
 ("הִיא עֲצוּבָה הַיּוֹם.", "She is sad today.", "Hi atsuva ha-yom."),
 ("לָמָּה אַתָּה כּוֹעֵס?", "Why are you angry? (to a man)", "Lama ata ko'es?"),
 ("הַיֶּלֶד מְפַחֵד מִכְּלָבִים.", "The boy is afraid of dogs.", "Ha-yeled mefached mi-klavim."),
 ("אֲנִי מַרְגִּישָׁה הַרְבֵּה יוֹתֵר טוֹב.", "I feel much better. (woman)", "Ani margisha harbe yoter tov."),
 ("אֲנַחְנוּ דּוֹאֲגִים לְךָ.", "We're worried about you. (to a man)", "Anachnu do'agim lecha."),
 ("הוּא גֵּאֶה בַּבַּת שֶׁלּוֹ.", "He is proud of his daughter.", "Hu ge'e ba-bat shelo."),
 ("מְשַׁעֲמֵם לִי.", "I'm bored.", "Mesha'amem li."),
], topic="a2-feelings")

c.T("a2-holidays", "Holidays and Shabbat", "שַׁבָּת שָׁלוֹם · חַג שָׂמֵחַ · שָׁנָה טוֹבָה",
 "Each occasion has its greeting: שַׁבָּת שָׁלוֹם on Friday and Saturday, חַג שָׂמֵחַ ('happy holiday') for any festival, שָׁנָה טוֹבָה at the new year (רֹאשׁ הַשָּׁנָה), and חַג פֶּסַח שָׂמֵחַ at Passover. On Shabbat many shops close from Friday afternoon until Saturday night.",
 "On Yom Kippur Israeli roads are almost empty of cars, and children ride bikes down the middle of the highways.",
 [("A", "שַׁבָּת שָׁלוֹם!", "Shabbat shalom!"), ("B", "שַׁבָּת שָׁלוֹם! מָה אַתֶּם עוֹשִׂים בַּשַּׁבָּת?", "Shabbat shalom! What are you doing on Shabbat?")])
c.L(13, "Holidays and Shabbat", "חַגִּים וְשַׁבָּת", [
 ("בְּיוֹם שִׁשִּׁי בָּעֶרֶב אוֹכְלִים אֲרוּחַת שַׁבָּת.", "On Friday evening people eat a Shabbat dinner.", "Be-yom shishi ba-erev ochlim aruchat shabat."),
 ("בְּפֶסַח אוֹכְלִים מַצָּה.", "At Passover people eat matzah.", "Be-Pesach ochlim matsa."),
 ("בַּחֲנֻכָּה מַדְלִיקִים נֵרוֹת.", "At Hanukkah people light candles.", "Ba-Chanuka madlikim nerot."),
 ("חַג שָׂמֵחַ לְכָל הַמִּשְׁפָּחָה!", "Happy holiday to the whole family!", "Chag same'ach le-chol ha-mishpacha!"),
 ("בְּרֹאשׁ הַשָּׁנָה אוֹכְלִים תַּפּוּחַ בִּדְבַשׁ.", "At Rosh Hashanah people eat apple with honey.", "Be-Rosh Hashana ochlim tapu'ach bi-dvash."),
 ("הַחֲנֻיּוֹת סְגוּרוֹת בַּשַּׁבָּת.", "The shops are closed on Shabbat.", "Ha-chanuyot sgurot ba-shabat."),
 ("בְּפוּרִים הַיְּלָדִים מִתְחַפְּשִׂים.", "At Purim the children dress up.", "Be-Purim ha-yeladim mitchapsim."),
 ("שָׁנָה טוֹבָה וּמְתוּקָה!", "A good and sweet year!", "Shana tova u-metuka!"),
], topic="a2-holidays")

c.T("a2-directions", "Asking the Way", "יָשָׁר · לְיָמִין · לִשְׂמֹאל · בַּפִּנָּה · עַד הָרַמְזוֹר",
 "Directions: תֵּלֵךְ יָשָׁר ('go straight'), תִּפְנֶה לְיָמִין / לִשְׂמֹאל ('turn right / left'), עַד הָרַמְזוֹר ('as far as the traffic light'), בַּפִּנָּה ('on the corner'), מוּל ('opposite'), לְיַד ('next to'). Directions are given with the future tense used as a polite command.",
 "Israelis are famously happy to give directions — sometimes even when they aren't sure of the way.",
 [("A", "סְלִיחָה, אֵיפֹה הַדֹּאַר?", "Excuse me, where is the post office?"), ("B", "תֵּלֵךְ יָשָׁר וְתִפְנֶה לִשְׂמֹאל בָּרַמְזוֹר.", "Go straight and turn left at the lights.")])
c.L(14, "Asking the Way", "אֵיךְ מַגִּיעִים?", [
 ("סְלִיחָה, אֵיפֹה תַּחֲנַת הָרַכֶּבֶת?", "Excuse me, where is the train station?", "Slicha, eifo tachanat ha-rakevet?"),
 ("תֵּלֵךְ יָשָׁר עַד הָרַמְזוֹר.", "Go straight as far as the traffic light. (to a man)", "Telech yashar ad ha-ramzor."),
 ("תִּפְנֶה לְיָמִין בַּפִּנָּה.", "Turn right at the corner. (to a man)", "Tifne le-yamin ba-pina."),
 ("הַבַּנְק מוּל הַדֹּאַר.", "The bank is opposite the post office.", "Ha-bank mul ha-do'ar."),
 ("זֶה רָחוֹק מִכָּאן?", "Is it far from here?", "Ze rachok mi-kan?"),
 ("זֶה בְּעֵרֶךְ עֶשֶׂר דַּקּוֹת בָּרֶגֶל.", "It's about ten minutes on foot.", "Ze be-erech eser dakot ba-regel."),
 ("הַמָּלוֹן לְיַד הַיָּם.", "The hotel is next to the sea.", "Ha-malon le-yad ha-yam."),
 ("תּוֹדָה רַבָּה, עָזַרְתָּ לִי מְאֹד.", "Thanks a lot, you helped me a lot. (to a man)", "Toda raba, azarta li me'od."),
], topic="a2-directions")

c.T("a2-frequency", "Always, Sometimes, Never", "תָּמִיד · בְּדֶרֶךְ כְּלָל · לִפְעָמִים · אַף פַּעַם לֹא",
 "How often: תָּמִיד (always), בְּדֶרֶךְ כְּלָל (usually), לִפְעָמִים (sometimes), כִּמְעַט אַף פַּעַם (hardly ever), אַף פַּעַם לֹא (never — note the לֹא: אַף פַּעַם לֹא הָיִיתִי שָׁם, 'I've never been there'). Also כָּל יוֹם (every day), פַּעַם בְּשָׁבוּעַ (once a week).",
 "Hebrew needs the double negative: אַף אֶחָד לֹא בָּא is literally 'nobody didn't come', and it's correct.",
 [("A", "אַתָּה הוֹלֵךְ לְחֶדֶר כֹּשֶׁר?", "Do you go to the gym?"), ("B", "לִפְעָמִים. בְּדֶרֶךְ כְּלָל אֲנִי רָץ לְיַד הַיָּם.", "Sometimes. Usually I run by the sea.")])
c.L(15, "Always, Sometimes, Never", "תָּמִיד, לִפְעָמִים, אַף פַּעַם", [
 ("אֲנִי תָּמִיד שׁוֹתֶה קָפֶה בַּבֹּקֶר.", "I always drink coffee in the morning.", "Ani tamid shote kafe ba-boker."),
 ("בְּדֶרֶךְ כְּלָל הִיא נוֹסַעַת בְּאוֹטוֹבּוּס.", "She usually goes by bus.", "Be-derech klal hi nosa'at be-otobus."),
 ("לִפְעָמִים אֲנַחְנוּ אוֹכְלִים בְּמִסְעָדָה.", "Sometimes we eat at a restaurant.", "Lif'amim anachnu ochlim be-mis'ada."),
 ("אַף פַּעַם לֹא הָיִיתִי בְּאֵילַת.", "I've never been to Eilat.", "Af pa'am lo hayiti be-Eilat."),
 ("הוּא רָץ פַּעַם בְּשָׁבוּעַ.", "He runs once a week.", "Hu rats pa'am be-shavu'a."),
 ("אַף אֶחָד לֹא בָּא.", "Nobody came.", "Af echad lo ba."),
 ("כָּל יוֹם אֲנִי לוֹמֵד מִלִּים חֲדָשׁוֹת.", "Every day I learn new words.", "Kol yom ani lomed milim chadashot."),
 ("הֵם כִּמְעַט אַף פַּעַם לֹא בַּבַּיִת.", "They're hardly ever at home.", "Hem kim'at af pa'am lo ba-bayit."),
], topic="a2-frequency")

c.T("a2-modal", "Allowed, Forbidden, Worth It", "מֻתָּר · אָסוּר · כְּדַאי · חַיָּבִים + infinitive",
 "These words never change form and are followed by an infinitive: מֻתָּר ('it's allowed'), אָסוּר ('it's forbidden'), כְּדַאי ('it's worth it, you should'), אִי אֶפְשָׁר ('it's impossible'). Add לְ + a person to make it personal: אָסוּר לְךָ ('you mustn't'), כְּדַאי לָכֶם ('you should'). 'Must' is חַיָּב / חַיֶּבֶת, which does agree.",
 "You will see אָסוּר לְעַשֵּׁן ('no smoking') on signs everywhere, and לֹא כְּדַאי ('better not') in every Israeli's advice.",
 [("A", "מֻתָּר לְצַלֵּם פֹּה?", "Is it allowed to take photos here?"), ("B", "לֹא, אָסוּר. אֲבָל כְּדַאי לִרְאוֹת אֶת הַגַּן.", "No, it's forbidden. But the garden is worth seeing.")])
c.L(16, "Allowed, Forbidden, Worth It", "מֻתָּר וְאָסוּר", [
 ("אָסוּר לְעַשֵּׁן כָּאן.", "No smoking here.", "Asur le'ashen kan."),
 ("מֻתָּר לְהִכָּנֵס?", "May I come in?", "Mutar lehikanes?"),
 ("כְּדַאי לְךָ לִלְמֹד עִבְרִית.", "You should learn Hebrew. (to a man)", "Kedai lecha lilmod ivrit."),
 ("אִי אֶפְשָׁר לַחֲנוֹת פֹּה.", "You can't park here.", "I efshar lachanot po."),
 ("אֲנִי חַיֶּבֶת לָלֶכֶת עַכְשָׁו.", "I must go now. (woman)", "Ani chayevet lalechet achshav."),
 ("לֹא כְּדַאי לִנְסֹעַ בַּשָּׁעָה שְׁמוֹנֶה.", "Better not to drive at eight o'clock.", "Lo kedai linso'a ba-sha'a shmone."),
 ("אָסוּר לַיְּלָדִים לִשְׂחוֹת לְבַד.", "The children mustn't swim alone.", "Asur la-yeladim lischot levad."),
 ("כְּדַאי לְהַזְמִין מָקוֹם מֵרֹאשׁ.", "It's worth booking a table in advance.", "Kedai lehazmin makom me-rosh."),
], topic="a2-modal")

c.R(101, "Reading: A Trip to Eilat", "טִיּוּל לְאֵילַת", "Rut plans a holiday in the south.", [
 ("בַּחֹדֶשׁ הַבָּא רוּת תִּסַּע לְאֵילַת עִם הַחֲבֵרוֹת שֶׁלָּהּ.", "Next month Rut will travel to Eilat with her friends."),
 ("הֵן יִסְּעוּ בְּאוֹטוֹבּוּס, כִּי זֶה יוֹתֵר זוֹל מִמָּטוֹס.", "They will go by bus, because it's cheaper than a plane."),
 ("בְּאֵילַת תָּמִיד חַם, גַּם בַּחֹרֶף.", "In Eilat it's always hot, even in winter."),
 ("רוּת רוֹצָה לִצְלֹל וְלִרְאוֹת דָּגִים יָפִים.", "Rut wants to dive and see beautiful fish."),
 ("אִם יִהְיֶה לָהֶן זְמַן, הֵן יְבַקְּרוּ גַּם בַּמִּדְבָּר.", "If they have time, they will also visit the desert."),
 ("רוּת אוֹמֶרֶת שֶׁזֶּה יִהְיֶה הַטִּיּוּל הֲכִי טוֹב שֶׁלָּהּ.", "Rut says it will be her best trip."),
], [
 ("How will they travel to Eilat?", ["By bus", "By plane", "By train", "By car"], 0),
 ("Why did they choose that way?", ["It's cheaper", "It's faster", "It's more fun", "Rut is afraid of flying"], 0),
 ("What does Rut want to see?", ["Beautiful fish", "Mountains", "A museum", "Snow"], 0),
 ("What will they visit if they have time?", ["The desert", "Jerusalem", "A market", "A castle"], 0),
])
c.save()
