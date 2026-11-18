"""Content source for data/hebrew-src/b1.json. Run: HE_DICT=<folder with kaikki Hebrew jsonl> python3 write_b1.py"""
import os
os.environ.setdefault("HE_DICT", "/private/tmp/claude-501/-Users-omar/3e230d6a-2df5-44ac-a5be-c38644d3169b/scratchpad/he-dict")
from author_he import Course
c = Course("b1", "b1", start=1)

c.T("b1-hifil", "Hifil Verbs: מַזְמִין, הִזְמַנְתִּי", "present מַ…ִי · past הִ…ְ…ַ · future אַ…ִי · infinitive לְהַ…ִי",
 "Hifil verbs often mean 'to make something happen'. Present starts with מַ (מַזְמִין, 'invites, orders'), past with הִ (הִזְמַנְתִּי, 'I invited'), future with אַ / תַּ / יַ (אַזְמִין, 'I will invite'), and the infinitive with לְהַ (לְהַזְמִין). Common ones: מַתְחִיל (starts), מַרְגִּישׁ (feels), מַסְבִּיר (explains), מַמְלִיץ (recommends).",
 "Many hifil verbs come from the same root as a simpler verb: גָּדַל 'grew' → הִגְדִּיל 'enlarged'; לָבַשׁ 'wore' → הִלְבִּישׁ 'dressed someone'.",
 [("A", "הִזְמַנְתָּ כְּבָר שֻׁלְחָן?", "Have you already booked a table?"), ("B", "עוֹד לֹא. אַזְמִין עַכְשָׁו.", "Not yet. I'll book now.")])
c.L(1, "Invite, Explain, Recommend", "בִּנְיַן הִפְעִיל", [
 ("הִזְמַנְתִּי אֶת כָּל הַחֲבֵרִים לַמְּסִבָּה.", "I invited all my friends to the party.", "Hizmanti et kol ha-chaverim la-mesiba."),
 ("הַמּוֹרָה מַסְבִּירָה אֶת הַשִּׁעוּר.", "The teacher explains the lesson.", "Ha-mora masbira et ha-shi'ur."),
 ("אֲנִי מַמְלִיץ עַל הַמִּסְעָדָה הַזֹּאת.", "I recommend this restaurant.", "Ani mamlits al ha-mis'ada ha-zot."),
 ("הַסֶּרֶט הִתְחִיל בְּשָׁעָה תֵּשַׁע.", "The film started at nine.", "Ha-seret hitchil be-sha'a tesha."),
 ("מָחָר אַזְמִין כַּרְטִיסִים.", "Tomorrow I'll order tickets.", "Machar azmin kartisim."),
 ("הוּא לֹא הִצְלִיחַ לִמְצֹא עֲבוֹדָה.", "He didn't manage to find a job.", "Hu lo hitsli'ach limtso avoda."),
 ("אֶפְשָׁר לְהַזְמִין מוֹנִית?", "Can I order a taxi?", "Efshar lehazmin monit?"),
 ("הֵם הֶחְלִיטוּ לַעֲבֹר דִּירָה.", "They decided to move house.", "Hem hechlitu la'avor dira."),
], topic="b1-hifil")

c.T("b1-nifal", "Nifal: Things That Happen", "נִפְתַּח (was opened, opens) · נִסְגַּר · נִכְנַס · נִשְׁאַר",
 "Nifal verbs start with נִ in the past (נִפְתַּח, 'opened / was opened') and the present (נִפְתָּח). They are often passive or 'happening by itself': הַדֶּלֶת נִסְגְּרָה ('the door closed'). Some everyday verbs live only here: נִכְנַס (entered), נִשְׁאַר (stayed), נִפְגַּשׁ (met), נִרְדַּם (fell asleep).",
 "The infinitive of nifal starts with לְהִ and has a dagesh in the first root letter: לְהִכָּנֵס (to enter), לְהִפָּגֵשׁ (to meet).",
 [("A", "מָתַי נִפָּגֵשׁ?", "When shall we meet?"), ("B", "בּוֹא נִפָּגֵשׁ לְיַד הַקּוֹלְנוֹעַ.", "Let's meet next to the cinema.")])
c.L(2, "Things That Happen", "בִּנְיַן נִפְעַל", [
 ("הַחֲנוּת נִפְתַּחַת בְּשָׁעָה תֵּשַׁע.", "The shop opens at nine.", "Ha-chanut niftachat be-sha'a tesha."),
 ("נִכְנַסְנוּ לַבַּיִת בְּשֶׁקֶט.", "We went into the house quietly.", "Nichnasnu la-bayit be-sheket."),
 ("נִשְׁאַרְתִּי בָּעֲבוֹדָה עַד מְאֻחָר.", "I stayed at work until late.", "Nisharti ba-avoda ad me'uchar."),
 ("הַיֶּלֶד נִרְדַּם מַהֵר.", "The boy fell asleep quickly.", "Ha-yeled nirdam maher."),
 ("נִפְגַּשְׁנוּ בָּאוּנִיבֶרְסִיטָה.", "We met at the university.", "Nifgashnu ba-universita."),
 ("הַמִּכְתָּב נִשְׁלַח אֶתְמוֹל.", "The letter was sent yesterday.", "Ha-michtav nishlach etmol."),
 ("הַסֵּפֶר נִכְתַּב לִפְנֵי מֵאָה שָׁנָה.", "The book was written a hundred years ago.", "Ha-sefer nichtav lifnei me'a shana."),
 ("אֲנִי לֹא יָכוֹל לְהִכָּנֵס.", "I can't get in.", "Ani lo yachol lehikanes."),
], topic="b1-nifal")

c.T("b1-would", "I Would…: הָיִיתִי + present", "הָיִיתִי רוֹצֶה (I would like) · אִלּוּ… הָיִיתִי…",
 "'Would' is the past of 'to be' + a present-tense verb: הָיִיתִי רוֹצֶה ('I would like'), הוּא הָיָה בָּא ('he would come'). For imagined situations use אִם or the more formal אִלּוּ: אִם הָיָה לִי כֶּסֶף, הָיִיתִי נוֹסֵעַ ('if I had money, I would travel').",
 "הָיִיתִי רוֹצֶה / רוֹצָה is the polite way to order or ask for something, a step up from אֲנִי רוֹצֶה.",
 [("A", "מָה הָיִיתָ עוֹשֶׂה עִם מִילְיוֹן שֶׁקֶל?", "What would you do with a million shekels?"), ("B", "הָיִיתִי קוֹנֶה בַּיִת לְיַד הַיָּם.", "I'd buy a house by the sea.")])
c.L(3, "I Would…", "הָיִיתִי…", [
 ("הָיִיתִי רוֹצֶה כּוֹס מַיִם, בְּבַקָּשָׁה.", "I would like a glass of water, please.", "Hayiti rotse kos mayim, bevakasha."),
 ("אִם הָיָה לִי זְמַן, הָיִיתִי לוֹמֵד גִּיטָרָה.", "If I had time, I would learn guitar.", "Im haya li zman, hayiti lomed gitara."),
 ("הִיא הָיְתָה בָּאָה, אֲבָל הִיא חוֹלָה.", "She would come, but she's sick.", "Hi hayta ba'a, aval hi chola."),
 ("מָה הָיִיתָ עוֹשֶׂה בִּמְקוֹמִי?", "What would you do in my place?", "Ma hayita ose bi-mkomi?"),
 ("הָיִינוּ שְׂמֵחִים לַעֲזֹר.", "We would be happy to help.", "Hayinu smechim la'azor."),
 ("אִם הָיָה חַם, הָיִינוּ הוֹלְכִים לַיָּם.", "If it were hot, we would go to the beach.", "Im haya cham, hayinu holchim la-yam."),
 ("הוּא הָיָה צָרִיךְ לְהִתְקַשֵּׁר.", "He should have called.", "Hu haya tsarich lehitkasher."),
 ("הָיִיתִי שְׂמֵחָה לְבַקֵּר אֶתְכֶם.", "I'd be happy to visit you. (woman)", "Hayiti smecha levaker etchem."),
], topic="b1-would")

c.T("b1-kdei", "In Order To and So That", "כְּדֵי לְ… (in order to) · כְּדֵי שֶׁ… + future (so that)",
 "'In order to' is כְּדֵי + infinitive: אֲנִי לוֹמֵד כְּדֵי לַעֲבֹד בְּיִשְׂרָאֵל. When the subject changes, use כְּדֵי שֶׁ + future: אֲנִי מַסְבִּיר לְאַט כְּדֵי שֶׁתָּבִין ('I explain slowly so that you understand').",
 "In everyday speech you will also hear בִּשְׁבִיל לְ… with the same meaning as כְּדֵי לְ…",
 [("A", "לָמָּה אַתָּה קָם כָּל כָּךְ מֻקְדָּם?", "Why do you get up so early?"), ("B", "כְּדֵי לָרוּץ לִפְנֵי הַחֹם.", "To run before the heat.")])
c.L(4, "In Order To", "כְּדֵי", [
 ("אֲנִי לוֹמֵד עִבְרִית כְּדֵי לַעֲבֹד בְּיִשְׂרָאֵל.", "I'm learning Hebrew in order to work in Israel.", "Ani lomed ivrit kdei la'avod be-Yisra'el."),
 ("הִיא קָמָה מֻקְדָּם כְּדֵי לָרוּץ.", "She gets up early in order to run.", "Hi kama mukdam kdei larutz."),
 ("הוּא חוֹסֵךְ כֶּסֶף כְּדֵי לִקְנוֹת דִּירָה.", "He is saving money to buy a flat.", "Hu chosech kesef kdei liknot dira."),
 ("דַּבֵּר לְאַט כְּדֵי שֶׁאָבִין.", "Speak slowly so that I understand.", "Daber le'at kdei she-avin."),
 ("סָגַרְתִּי אֶת הַחַלּוֹן כְּדֵי שֶׁלֹּא יִהְיֶה קַר.", "I closed the window so it wouldn't be cold.", "Sagarti et ha-chalon kdei shelo yihye kar."),
 ("בָּאנוּ מֻקְדָּם כְּדֵי לִמְצֹא מָקוֹם.", "We came early to find a seat.", "Banu mukdam kdei limtso makom."),
 ("הִיא כָּתְבָה רְשִׁימָה כְּדֵי לֹא לִשְׁכֹּחַ.", "She wrote a list so as not to forget.", "Hi katva reshima kdei lo lishko'ach."),
 ("צָרִיךְ כַּרְטִיס כְּדֵי לְהִכָּנֵס.", "You need a ticket to get in.", "Tsarich kartis kdei lehikanes."),
], topic="b1-kdei")

c.T("b1-reported", "He Said That…: Reported Speech", "הוּא אָמַר שֶׁ… · הִיא שָׁאֲלָה אִם… · הֵם סִפְּרוּ שֶׁ…",
 "Reported speech in Hebrew is simple: keep the original tense. If Dana said 'I'm tired', you report דָּנָה אָמְרָה שֶׁהִיא עֲיֵפָה ('Dana said that she is tired'), with no change to the past. Yes/no questions are reported with אִם ('whether'): הוּא שָׁאַל אִם אֲנִי בָּא.",
 "This is a common mistake for English speakers: don't shift the tense. 'He said he would come' is הוּא אָמַר שֶׁהוּא יָבוֹא — future, not past.",
 [("A", "מָה הוּא אָמַר?", "What did he say?"), ("B", "הוּא אָמַר שֶׁהוּא יְאַחֵר קְצָת.", "He said he'll be a bit late.")])
c.L(5, "He Said That…", "הוּא אָמַר שֶׁ…", [
 ("דָּנָה אָמְרָה שֶׁהִיא עֲיֵפָה.", "Dana said that she was tired.", "Dana amra shehi ayefa."),
 ("הוּא אָמַר שֶׁהוּא יָבוֹא מָחָר.", "He said he would come tomorrow.", "Hu amar shehu yavo machar."),
 ("הִיא שָׁאֲלָה אִם אֲנִי רוֹצֶה קָפֶה.", "She asked if I wanted coffee.", "Hi sha'ala im ani rotse kafe."),
 ("הֵם סִפְּרוּ שֶׁהֵם הָיוּ בְּאֵילַת.", "They told us they had been to Eilat.", "Hem siperu shehem hayu be-Eilat."),
 ("הַמּוֹרֶה הִסְבִּיר שֶׁהַבְּחִינָה קָשָׁה.", "The teacher explained that the exam was hard.", "Ha-more hisbir sheha-bchina kasha."),
 ("שָׁאַלְתִּי אוֹתוֹ מָתַי הוּא מַגִּיעַ.", "I asked him when he was arriving.", "Sha'alti oto matai hu magi'a."),
 ("הִיא כָּתְבָה שֶׁהַכֹּל בְּסֵדֶר.", "She wrote that everything was fine.", "Hi katva sheha-kol be-seder."),
 ("אָמַרְתִּי לוֹ שֶׁאֲנִי לֹא יָכוֹל.", "I told him I couldn't.", "Amarti lo she-ani lo yachol."),
], topic="b1-reported")

c.T("b1-opinion", "Giving Your Opinion", "לְדַעֲתִי · אֲנִי חוֹשֵׁב שֶׁ… · אֲנִי מַסְכִּים / לֹא מַסְכִּים",
 "Opinions: לְדַעֲתִי ('in my opinion'), אֲנִי חוֹשֵׁב / חוֹשֶׁבֶת שֶׁ… ('I think that'), נִרְאֶה לִי שֶׁ… ('it seems to me'). Agree with אֲנִי מַסְכִּים עִם… or simply נָכוֹן ('right'). Disagree politely: אֲנִי לֹא בָּטוּחַ ('I'm not sure') or יֵשׁ בָּזֶה מַשֶּׁהוּ, אֲבָל… ('there's something in that, but…').",
 "Israeli conversation is known for being direct: interrupting to disagree is normal, and nobody takes it personally.",
 [("A", "לְדַעֲתִי הַסֶּרֶט הָיָה מְשַׁעֲמֵם.", "In my opinion the film was boring."), ("B", "אֲנִי לֹא מַסְכִּים, הוּא הָיָה מְעַנְיֵן!", "I disagree, it was interesting!")])
c.L(6, "In My Opinion", "לְדַעֲתִי", [
 ("לְדַעֲתִי זֶה רַעֲיוֹן טוֹב.", "In my opinion it's a good idea.", "Le-da'ati ze ra'ayon tov."),
 ("אֲנִי חוֹשֶׁבֶת שֶׁהוּא צוֹדֵק.", "I think he's right. (woman)", "Ani choshevet shehu tsodek."),
 ("נִרְאֶה לִי שֶׁיֵּרֵד גֶּשֶׁם.", "It seems to me it will rain.", "Nir'e li sheyered geshem."),
 ("אֲנִי מַסְכִּים אִתְּךָ לְגַמְרֵי.", "I completely agree with you.", "Ani maskim itcha legamrei."),
 ("אֲנִי לֹא בָּטוּחַ שֶׁזֶּה נָכוֹן.", "I'm not sure that's true.", "Ani lo batu'ach sheze nachon."),
 ("מָה דַּעֲתְךָ עַל הַתׇּכְנִית?", "What do you think of the plan?", "Ma da'atcha al ha-tochnit?"),
 ("מִצַּד אֶחָד זֶה יָקָר, מִצַּד שֵׁנִי זֶה נוֹחַ.", "On one hand it's expensive, on the other it's convenient.", "Mi-tsad echad ze yakar, mi-tsad sheni ze no'ach."),
 ("זֶה תָּלוּי.", "It depends.", "Ze talui."),
], topic="b1-opinion")

c.T("b1-interview", "A Job Interview", "קוֹרוֹת חַיִּים · נִסָּיוֹן · רֵאָיוֹן עֲבוֹדָה",
 "Useful words: רֵאָיוֹן עֲבוֹדָה (job interview), קוֹרוֹת חַיִּים (CV, 'the events of life'), נִסָּיוֹן (experience), מַשְׂכֹּרֶת (salary), מִשְׂרָה מְלֵאָה / חֶלְקִית (full-time / part-time job). Talk about experience with יֵשׁ לִי נִסָּיוֹן בְּ… and with עָבַדְתִּי בְּ… שְׁנָתַיִם ('I worked at… for two years').",
 "Israeli interviews are often informal; you may be asked about your army service, which many employers treat as work experience.",
 [("A", "סַפֵּר לִי עַל עַצְמְךָ.", "Tell me about yourself."), ("B", "עָבַדְתִּי שָׁלוֹשׁ שָׁנִים בְּחֶבְרָה גְּדוֹלָה.", "I worked for three years at a big company.")])
c.L(7, "A Job Interview", "רֵאָיוֹן עֲבוֹדָה", [
 ("שָׁלַחְתִּי קוֹרוֹת חַיִּים לַחֶבְרָה.", "I sent my CV to the company.", "Shalachti korot chayim la-chevra."),
 ("יֵשׁ לִי רֵאָיוֹן עֲבוֹדָה מָחָר.", "I have a job interview tomorrow.", "Yesh li re'ayon avoda machar."),
 ("יֵשׁ לְךָ נִסָּיוֹן בַּתְּחוּם?", "Do you have experience in the field?", "Yesh lecha nisayon ba-tchum?"),
 ("עָבַדְתִּי שְׁנָתַיִם בְּבַנְק.", "I worked at a bank for two years.", "Avadti shnatayim be-bank."),
 ("זֹאת מִשְׂרָה מְלֵאָה.", "It's a full-time job.", "Zot misra mle'a."),
 ("מָה הַמַּשְׂכֹּרֶת?", "What's the salary?", "Ma ha-maskoret?"),
 ("אֲנִי אוֹהֵב לַעֲבֹד בְּצֶוֶת.", "I like working in a team.", "Ani ohev la'avod be-tsevet."),
 ("מָתַי אַתָּה יָכוֹל לְהַתְחִיל?", "When can you start?", "Matai ata yachol lehatchil?"),
], topic="b1-interview")

c.T("b1-bank", "Money and the Bank", "חֶשְׁבּוֹן בַּנְק · כַּרְטִיס אַשְׁרַאי · לְהַעֲבִיר כֶּסֶף",
 "Banking words: חֶשְׁבּוֹן בַּנְק (bank account), כַּרְטִיס אַשְׁרַאי (credit card), לִמְשֹׁךְ כֶּסֶף (to withdraw money), לְהַעֲבִיר כֶּסֶף (to transfer money), תַּשְׁלוּמִים (instalments). Israelis often split purchases into instalments, even small ones: בְּכַמָּה תַּשְׁלוּמִים? ('in how many payments?').",
 "The ATM is called כַּסְפּוֹמָט, a blend of כֶּסֶף ('money') and 'automat'.",
 [("A", "אֶפְשָׁר לְשַׁלֵּם בְּתַשְׁלוּמִים?", "Can I pay in instalments?"), ("B", "כֵּן, עַד שְׁלוֹשָׁה תַּשְׁלוּמִים.", "Yes, up to three payments.")])
c.L(8, "Money and the Bank", "כֶּסֶף וּבַנְק", [
 ("אֲנִי רוֹצֶה לִפְתֹּחַ חֶשְׁבּוֹן בַּנְק.", "I want to open a bank account.", "Ani rotse liftoach cheshbon bank."),
 ("אֵיפֹה יֵשׁ כַּסְפּוֹמָט?", "Where is there an ATM?", "Eifo yesh kaspomat?"),
 ("הֶעֱבַרְתִּי לְךָ אֶת הַכֶּסֶף.", "I transferred the money to you.", "He'evarti lecha et ha-kesef."),
 ("אֶפְשָׁר לְשַׁלֵּם בְּכַרְטִיס אַשְׁרַאי?", "Can I pay by credit card?", "Efshar leshalem be-chartis ashrai?"),
 ("שִׁלַּמְתִּי בִּשְׁלוֹשָׁה תַּשְׁלוּמִים.", "I paid in three instalments.", "Shilamti bi-shlosha tashlumim."),
 ("אֵין לִי מְזֻמָּן.", "I don't have cash.", "Ein li mezuman."),
 ("הַבַּנְק סָגוּר בְּיוֹם שִׁשִּׁי.", "The bank is closed on Friday.", "Ha-bank sagur be-yom shishi."),
 ("אֲנַחְנוּ חוֹסְכִים לַחֻפְשָׁה.", "We're saving for the holiday.", "Anachnu choschim la-chufsha."),
], topic="b1-bank")

c.T("b1-complaint", "Complaining Politely", "יֵשׁ לִי בְּעָיָה עִם… · זֶה לֹא עוֹבֵד · אֶפְשָׁר לְהַחְלִיף?",
 "To complain: יֵשׁ לִי בְּעָיָה עִם… ('I have a problem with'), זֶה לֹא עוֹבֵד ('it doesn't work'), זֶה מְקֻלְקָל ('it's broken'). Ask for a fix: אֶפְשָׁר לְהַחְלִיף? ('can I exchange it?'), אֶפְשָׁר לְקַבֵּל אֶת הַכֶּסֶף בַּחֲזָרָה? ('can I get my money back?'). Keep the receipt: קַבָּלָה.",
 "Israeli shops must accept returns within 14 days for many goods, but only with the receipt.",
 [("A", "קָנִיתִי אֶת זֶה אֶתְמוֹל וְזֶה לֹא עוֹבֵד.", "I bought this yesterday and it doesn't work."), ("B", "יֵשׁ לָךְ קַבָּלָה?", "Do you have the receipt?")])
c.L(9, "Complaining Politely", "יֵשׁ לִי בְּעָיָה", [
 ("יֵשׁ לִי בְּעָיָה עִם הַמַּחְשֵׁב.", "I have a problem with the computer.", "Yesh li be'aya im ha-machshev."),
 ("הַמַּזְגָן לֹא עוֹבֵד.", "The air conditioner doesn't work.", "Ha-mazgan lo oved."),
 ("הַטֵּלֵפוֹן מְקֻלְקָל.", "The phone is broken.", "Ha-telefon mekulkal."),
 ("אֶפְשָׁר לְהַחְלִיף אֶת הַחֻלְצָה?", "Can I exchange the shirt?", "Efshar lehachlif et ha-chultsa?"),
 ("הִנֵּה הַקַּבָּלָה.", "Here is the receipt.", "Hine ha-kabala."),
 ("חִכִּיתִי שָׁעָה שְׁלֵמָה!", "I waited a whole hour!", "Chikiti sha'a shlema!"),
 ("אֲנִי רוֹצֶה לְדַבֵּר עִם הַמְּנַהֵל.", "I want to speak with the manager.", "Ani rotse ledaber im ha-menahel."),
 ("זֶה לֹא בְּסֵדֶר.", "That's not OK.", "Ze lo be-seder."),
], topic="b1-complaint")

c.T("b1-tech", "Phones and Computers", "אַפְּלִיקַצְיָה · סִסְמָה · לְהוֹרִיד · מִטְעָן",
 "Tech words: מַחְשֵׁב (computer), סִסְמָה (password), לְהוֹרִיד (to download, 'to bring down'), לְהַעֲלוֹת (to upload, 'to bring up'), מִטְעָן (charger), הַסּוֹלְלָה נִגְמְרָה ('the battery died'), אֵין קְלִיטָה ('no signal'). Many words are borrowed: אַפְּלִיקַצְיָה, אִינְטֶרְנֶט.",
 "Israel is famous for start-ups: the country has one of the highest numbers of start-ups per person in the world.",
 [("A", "יֵשׁ לְךָ מִטְעָן?", "Do you have a charger?"), ("B", "כֵּן, הַסּוֹלְלָה שֶׁלְּךָ נִגְמְרָה?", "Yes, did your battery die?")])
c.L(10, "Phones and Computers", "טֶכְנוֹלוֹגְיָה", [
 ("הַסּוֹלְלָה נִגְמְרָה.", "The battery died.", "Ha-solela nigmera."),
 ("אֲנִי צָרִיךְ מִטְעָן לַטֵּלֵפוֹן.", "I need a charger for the phone.", "Ani tsarich mit'an la-telefon."),
 ("שָׁכַחְתִּי אֶת הַסִּסְמָה.", "I forgot the password.", "Shachachti et ha-sisma."),
 ("הוֹרַדְתִּי אַפְּלִיקַצְיָה חֲדָשָׁה.", "I downloaded a new app.", "Horadti aplikatsya chadasha."),
 ("אֵין פֹּה קְלִיטָה.", "There's no signal here.", "Ein po klita."),
 ("הַמַּחְשֵׁב שֶׁלִּי אִטִּי מְאֹד.", "My computer is very slow.", "Ha-machshev sheli iti me'od."),
 ("תִּשְׁלַח לִי אֶת הַקֹּבֶץ.", "Send me the file.", "Tishlach li et ha-kovets."),
 ("יֵשׁ פֹּה אִינְטֶרְנֶט אַלְחוּטִי?", "Is there wifi here?", "Yesh po internet alchuti?"),
], topic="b1-tech")

c.T("b1-cooking", "In the Kitchen", "לְבַשֵּׁל · לַחְתֹּךְ · לְעַרְבֵּב · לֶאֱפוֹת · מַתְכּוֹן",
 "Recipes (מַתְכּוֹנִים) are usually written with infinitives as instructions: לַחְתֹּךְ אֶת הַבָּצָל ('chop the onion'), לְעַרְבֵּב ('mix'), לְהוֹסִיף ('add'), לְבַשֵּׁל עַל אֵשׁ קְטַנָּה ('cook on a low heat'), לֶאֱפוֹת בַּתַּנּוּר ('bake in the oven').",
 "שַׁקְשׁוּקָה — eggs cooked in a spicy tomato sauce — came to Israel with immigrants from North Africa and is now a national breakfast.",
 [("A", "מָה אַתְּ מְבַשֶּׁלֶת?", "What are you cooking?"), ("B", "שַׁקְשׁוּקָה. רוֹצֶה לִטְעֹם?", "Shakshuka. Want a taste?")])
c.L(11, "In the Kitchen", "בַּמִּטְבָּח", [
 ("קֹדֶם צָרִיךְ לַחְתֹּךְ אֶת הַבָּצָל.", "First you need to chop the onion.", "Kodem tsarich lachtoch et ha-batsal."),
 ("לְהוֹסִיף מֶלַח וּפִלְפֵּל.", "Add salt and pepper.", "Lehosif melach u-filpel."),
 ("לְעַרְבֵּב טוֹב.", "Mix well.", "Le'arbev tov."),
 ("לֶאֱפוֹת בַּתַּנּוּר חֲצִי שָׁעָה.", "Bake in the oven for half an hour.", "Le'efot ba-tanur chatsi sha'a."),
 ("אִמָּא שֶׁלִּי מְבַשֶּׁלֶת מָרָק.", "My mom is cooking soup.", "Ima sheli mevashelet marak."),
 ("יֵשׁ לָךְ מַתְכּוֹן טוֹב לְעוּגָה?", "Do you have a good cake recipe?", "Yesh lach matkon tov le-uga?"),
 ("הָאֹכֶל קְצָת חָרִיף.", "The food is a bit spicy.", "Ha-ochel ktsat charif."),
 ("רוֹצֶה לִטְעֹם?", "Want a taste?", "Rotse lit'om?"),
], topic="b1-cooking")

c.T("b1-travel", "Travelling Abroad", "חוּ\"ל · דַּרְכּוֹן · טִיסָה · מִזְוָדָה",
 "Abroad is חוּ\"ל, short for חוּץ לָאָרֶץ ('outside the land'). At the airport: דַּרְכּוֹן (passport), טִיסָה (flight), מִזְוָדָה (suitcase), כַּרְטִיס עֲלִיָּה לַמָּטוֹס (boarding pass). Flights 'go up' and 'land': הַמָּטוֹס הִמְרִיא ('took off'), נָחַת ('landed').",
 "Israel's main airport, Ben Gurion, is known for long security questioning before departure.",
 [("A", "מָתַי הַטִּיסָה שֶׁלְּךָ?", "When is your flight?"), ("B", "מָחָר בְּשֵׁשׁ בַּבֹּקֶר, אֲנִי עוֹד לֹא אָרַזְתִּי!", "Tomorrow at six in the morning, I haven't packed yet!")])
c.L(12, "Travelling Abroad", "נוֹסְעִים לְחוּץ לָאָרֶץ", [
 ("אֵיפֹה הַדַּרְכּוֹן שֶׁלִּי?", "Where's my passport?", "Eifo ha-darkon sheli?"),
 ("הַטִּיסָה מִתְעַכֶּבֶת בְּשָׁעָה.", "The flight is delayed by an hour.", "Ha-tisa mit'akevet be-sha'a."),
 ("הַמִּזְוָדָה שֶׁלִּי כְּבֵדָה מִדַּי.", "My suitcase is too heavy.", "Ha-mizvada sheli kveda midai."),
 ("הַמָּטוֹס נָחַת בַּזְּמַן.", "The plane landed on time.", "Ha-matos nachat ba-zman."),
 ("עוֹד לֹא אָרַזְתִּי.", "I haven't packed yet.", "Od lo arazti."),
 ("הִזְמַנּוּ מָלוֹן לְיַד הַמֶּרְכָּז.", "We booked a hotel near the centre.", "Hizmanu malon le-yad ha-merkaz."),
 ("כַּמָּה זְמַן נִמְשֶׁכֶת הַטִּיסָה?", "How long is the flight?", "Kama zman nimshechet ha-tisa?"),
 ("נְסִיעָה טוֹבָה!", "Have a good trip!", "Nesi'a tova!"),
], topic="b1-travel")

c.T("b1-news", "In the News", "חֲדָשׁוֹת · לְפִי הַדִּוּוּחַ · הַמֶּמְשָׁלָה · מֶזֶג הָאֲוִיר",
 "News Hebrew uses some fixed phrases: לְפִי… ('according to'), הַיּוֹם נִמְסַר שֶׁ… ('it was reported today that'), בְּעִקְבוֹת ('following, as a result of'). Common words: הַמֶּמְשָׁלָה (the government), בְּחִירוֹת (elections), תְּאֻנָּה (accident), שְׁבִיתָה (strike), תַּחֲזִית (forecast).",
 "Many Israeli radio stations still play the news on the hour, and people in a shared taxi often ask the driver to turn it up.",
 [("A", "שָׁמַעְתָּ אֶת הַחֲדָשׁוֹת?", "Did you hear the news?"), ("B", "כֵּן, יֵשׁ שְׁבִיתָה בָּרַכֶּבֶת מָחָר.", "Yes, there's a train strike tomorrow.")])
c.L(13, "In the News", "בַּחֲדָשׁוֹת", [
 ("שָׁמַעְתָּ אֶת הַחֲדָשׁוֹת?", "Did you hear the news?", "Shamata et ha-chadashot?"),
 ("מָחָר תִּהְיֶה שְׁבִיתָה.", "Tomorrow there will be a strike.", "Machar tihye shvita."),
 ("לְפִי הַתַּחֲזִית יֵרֵד גֶּשֶׁם.", "According to the forecast it will rain.", "Lefi ha-tachazit yered geshem."),
 ("הָיְתָה תְּאֻנָּה בַּכְּבִישׁ.", "There was an accident on the road.", "Hayta te'una ba-kvish."),
 ("הַבְּחִירוֹת יִהְיוּ בַּחֹדֶשׁ הַבָּא.", "The elections will be next month.", "Ha-bchirot yihyu ba-chodesh ha-ba."),
 ("הַמֶּמְשָׁלָה הֶחְלִיטָה עַל חֹק חָדָשׁ.", "The government decided on a new law.", "Ha-memshala hechlita al chok chadash."),
 ("הַמְּחִירִים עָלוּ הַשָּׁנָה.", "Prices went up this year.", "Ha-mechirim alu ha-shana."),
 ("אֲנִי קוֹרֵא חֲדָשׁוֹת כָּל בֹּקֶר.", "I read the news every morning.", "Ani kore chadashot kol boker."),
], topic="b1-news")

c.T("b1-environment", "The Environment", "סְבִיבָה · מִחְזוּר · לַחְסֹךְ מַיִם · זִהוּם",
 "Environment words: הַסְּבִיבָה (the environment), מִחְזוּר (recycling), זִהוּם (pollution), אֶנֶרְגִּיָה מֵהַשֶּׁמֶשׁ (solar energy), לַחְסֹךְ מַיִם (to save water), שִׁנּוּי אַקְלִים (climate change).",
 "Israel recycles most of its waste water for farming, one of the highest rates in the world, because fresh water is scarce.",
 [("A", "אַתֶּם מְמַחְזְרִים בַּבַּיִת?", "Do you recycle at home?"), ("B", "כֵּן, יֵשׁ לָנוּ פַּח לְבַקְבּוּקִים.", "Yes, we have a bin for bottles.")])
c.L(14, "The Environment", "אֵיכוּת הַסְּבִיבָה", [
 ("צָרִיךְ לִשְׁמֹר עַל הַסְּבִיבָה.", "We need to protect the environment.", "Tsarich lishmor al ha-sviva."),
 ("בְּיִשְׂרָאֵל חוֹסְכִים מַיִם.", "In Israel people save water.", "Be-Yisra'el choschim mayim."),
 ("הַזִּהוּם בָּעִיר גָּדוֹל.", "Pollution in the city is high.", "Ha-zihum ba-ir gadol."),
 ("יֵשׁ לָנוּ דּוּד שֶׁמֶשׁ עַל הַגַּג.", "We have a solar water heater on the roof.", "Yesh lanu dud shemesh al ha-gag."),
 ("אֲנִי נוֹסֵעַ בְּאוֹפַנַּיִם וְלֹא בִּמְכוֹנִית.", "I ride a bike, not a car.", "Ani nose'a be-ofanayim ve-lo bi-mchonit."),
 ("שִׁנּוּי הָאַקְלִים הוּא בְּעָיָה גְּדוֹלָה.", "Climate change is a big problem.", "Shinui ha-aklim hu be'aya gdola."),
 ("זוֹרְקִים בַּקְבּוּקִים לַפַּח הַזֶּה.", "Bottles go in this bin.", "Zorkim bakbukim la-pach ha-ze."),
 ("כְּדַאי לְכַבּוֹת אֶת הָאוֹר.", "You should turn off the light.", "Kedai lechabot et ha-or."),
], topic="b1-environment")

c.T("b1-sport", "Sport and Free Time", "לְשַׂחֵק כַּדּוּרֶגֶל · לִשְׂחוֹת · לָרוּץ · תַּחְבִּיב",
 "Free time: תַּחְבִּיב (hobby), לְשַׂחֵק כַּדּוּרֶגֶל / כַּדּוּרְסַל (to play football / basketball), לִשְׂחוֹת (to swim), לָרוּץ (to run), לְטַיֵּל (to hike, to travel around). 'A fan of' is אוֹהֵד שֶׁל…, and a match is מִשְׂחָק.",
 "טִיּוּל ('a trip, a hike') is a national pastime: many Israelis go on a long backpacking trip after the army.",
 [("A", "יֵשׁ לְךָ תַּחְבִּיב?", "Do you have a hobby?"), ("B", "אֲנִי אוֹהֵב לְטַיֵּל בַּצָּפוֹן.", "I love hiking in the north.")])
c.L(15, "Sport and Free Time", "סְפּוֹרְט וּפְנַאי", [
 ("בְּשַׁבָּת אֲנַחְנוּ מְשַׂחֲקִים כַּדּוּרֶגֶל.", "On Saturday we play football.", "Be-shabat anachnu mesachakim kaduregel."),
 ("הִיא שׂוֹחָה כָּל בֹּקֶר.", "She swims every morning.", "Hi socha kol boker."),
 ("מָה הַתַּחְבִּיב שֶׁלְּךָ?", "What's your hobby?", "Ma ha-tachbiv shelcha?"),
 ("אֲנִי אוֹהֵב לְטַיֵּל בַּצָּפוֹן.", "I love hiking in the north.", "Ani ohev letayel ba-tsafon."),
 ("רָאִיתָ אֶת הַמִּשְׂחָק אֶתְמוֹל?", "Did you see the match yesterday?", "Ra'ita et ha-mischak etmol?"),
 ("הַקְּבוּצָה שֶׁלָּנוּ נִצְּחָה!", "Our team won!", "Ha-kvutsa shelanu nitscha!"),
 ("הוּא מִתְאַמֵּן בְּחֶדֶר כֹּשֶׁר.", "He works out at the gym.", "Hu mit'amen be-cheder kosher."),
 ("בַּקַּיִץ אֲנִי רָץ בָּעֶרֶב, כִּי בַּבֹּקֶר חַם מִדַּי.", "In summer I run in the evening, because mornings are too hot.", "Ba-kayits ani rats ba-erev, ki ba-boker cham midai."),
], topic="b1-sport")

c.T("b1-army", "Israeli Life: Army and Studies", "צָבָא · שֵׁרוּת · מִלּוּאִים · אוּנִיבֶרְסִיטָה · תּוֹאַר",
 "Most young Israelis do military service (שֵׁרוּת צְבָאִי) at 18 — about three years for men and two for women — and afterwards many are called up for reserve duty (מִלּוּאִים) for some weeks a year. University (אוּנִיבֶרְסִיטָה) usually comes after the army; a degree is תּוֹאַר, a first degree תּוֹאַר רִאשׁוֹן.",
 "Because they start later, Israeli students are often in their mid-twenties, and many already work while studying.",
 [("A", "מָה עָשִׂיתָ אַחֲרֵי הַצָּבָא?", "What did you do after the army?"), ("B", "טִיַּלְתִּי בְּהֹדּוּ וְאָז הִתְחַלְתִּי לִלְמֹד.", "I travelled in India and then started studying.")])
c.L(16, "Army and Studies", "צָבָא וְלִמּוּדִים", [
 ("הוּא בַּצָּבָא כְּבָר שָׁנָה.", "He has been in the army for a year already.", "Hu ba-tsava kvar shana."),
 ("אַחֲרֵי הַצָּבָא הִיא טִיְּלָה בְּדָרוֹם אָמֶרִיקָה.", "After the army she travelled in South America.", "Acharei ha-tsava hi tiyla be-Darom Amerika."),
 ("אַבָּא שֶׁלִּי בְּמִלּוּאִים הַשָּׁבוּעַ.", "My dad is on reserve duty this week.", "Aba sheli be-milu'im ha-shavu'a."),
 ("אֲנִי לוֹמֶדֶת לְתוֹאַר רִאשׁוֹן.", "I'm studying for a first degree. (woman)", "Ani lomedet le-to'ar rishon."),
 ("הוּא לוֹמֵד מִשְׁפָּטִים בְּחֵיפָה.", "He studies law in Haifa.", "Hu lomed mishpatim be-Cheifa."),
 ("הַבְּחִינוֹת מַתְחִילוֹת בְּיוּנִי.", "The exams start in June.", "Ha-bchinot matchilot be-yuni."),
 ("הִיא עוֹבֶדֶת וְגַם לוֹמֶדֶת.", "She works and studies too.", "Hi ovedet ve-gam lomedet."),
 ("סִיַּמְתִּי אֶת הַתּוֹאַר בַּשָּׁנָה שֶׁעָבְרָה.", "I finished my degree last year.", "Siyamti et ha-to'ar ba-shana she-avra."),
], topic="b1-army")

c.R(101, "Reading: A New Life in Haifa", "חַיִּים חֲדָשִׁים בְּחֵיפָה", "Olga writes about her first year in Israel.", [
 ("לִפְנֵי שָׁנָה עָבַרְתִּי לְחֵיפָה עִם הַמִּשְׁפָּחָה שֶׁלִּי.", "A year ago I moved to Haifa with my family."),
 ("בַּהַתְחָלָה הָיָה לִי קָשֶׁה, כִּי לֹא הֵבַנְתִּי כִּמְעַט כְּלוּם.", "At first it was hard for me, because I understood almost nothing."),
 ("לָמַדְתִּי עִבְרִית בָּאֻלְפָּן חֲמִשָּׁה חֳדָשִׁים.", "I studied Hebrew at the ulpan for five months."),
 ("עַכְשָׁו אֲנִי עוֹבֶדֶת בְּבֵית חוֹלִים וּמְדַבֶּרֶת עִבְרִית כָּל יוֹם.", "Now I work at a hospital and speak Hebrew every day."),
 ("לְדַעֲתִי הַדָּבָר הֲכִי חָשׁוּב הוּא לֹא לְפַחֵד לִטְעוֹת.", "In my opinion the most important thing is not to be afraid of making mistakes."),
 ("אִם הָיִיתִי מַתְחִילָה מֵחָדָשׁ, הָיִיתִי מְדַבֶּרֶת יוֹתֵר מֵהַיּוֹם הָרִאשׁוֹן.", "If I were starting again, I would speak more from the first day."),
], [
 ("Where did Olga move?", ["Haifa", "Tel Aviv", "Jerusalem", "Eilat"], 0),
 ("How long did she study at the ulpan?", ["Five months", "One year", "Two weeks", "Three years"], 0),
 ("Where does she work now?", ["At a hospital", "At a bank", "At a school", "At a café"], 0),
 ("What does she think is most important?", ["Not being afraid of mistakes", "Reading newspapers", "Watching films", "Living alone"], 0),
])
c.save()
