## Reflektion -KK2

## Lösning av projektet

I detta projektet, så hade jag skapat mig utav ett FastApi applikation med en enkel health point för att säkerhetsställa att Api'n fungerade som det ska. Med hjälp av Pandas, så kunde jag ladda upp upp CSV-filer för att få fram resultat på statistik och även ställa frågor till ai chatbot genom att använda funktionen describe() som ligger i pandas bibliotek.

för att testa applikationen (för att den ska fungera) så valde jag ett Netflix-dataset som jag använde från förra kunskapskontrollen (KK1) med tanke på att det dataset innehöll tillräckligt med info och data, så kände jag att det var ett bra val att återanvända det i KK2. Och utifrån det, så kunde jag bygga upp applikationen och få en bra struktur på helheten.

AI Delen av programmet är uppbyggd utav Runnable kedjan som består utav:
-PromptBuilder
-LLMRunner
-ResponseParser

PromptBuilder har som ansvar att skapa ett svar utifrån användarens fråga och tar infot och bearbetar det baserad på datasetet. Och vidarebefodrar det till SmolLM2 via pipeline (med hjälp utav LLMRunner).

och sedan så bearbetar ai modellen,besvarar på frågan och skickar sedan tillbaka infot användaren har begärt. Vilket är det ResponseParser har ansvar för.

att dela upp lösningen i flera steg gjorde att blev enklare att förstå flödet och strukturen, samt kunna felsöka problem.

## Utmaningar under arbetets gång

Det som var den största utmaningen var att få till Runnable Kedjan att fungera som det skulle. Jag stötte på några problem under utvecklingens gång, bland annat importproblem, indenteringsfel och hur de de olika klasserna inom Runnable skulle kopplas ihop.

Jag hade även dessutom ett problem med transformers importen, som angav ett felmeddlande över att importen inte kunde lösas. Men det visade sig att bilbioteket var installerad på rätt sätt, men kunde bara inte hitta rätt Python miljö att köra programmet på.

Jag hade även strul med Ai chatten i början också, på grund av att JSON-datan som skickades till endpointen inte innehöll rätt nyckel för att fungera. Men sakta men säkert så lyckades jag felsöka problemet till att få den att fungera.

## Risker och Begränsningar

risken med Ai modellen som jag implementerade i projektet inte angav rätt svar i datasetet. När jag hade testat chatbotten, så hade den genererat information som inte fanns i datasetet. Det tog jag reda på när jag hade fått statistik endast baserad på år (release-year) från datasetet och inget annat. Det visar att AI-modeller kan ge ut information helt påhittat och inte det faktiska resultatet som finns i filen.

En annan risk är Prompt injection. Som användare så kan man exempelvis skriva att chatbotten ska ignorera alla instruktioner och besvara något som inte har med datasetet att göra överhuvudtaget. För att inte riskera att hamna i en sådan situation, så skulle man kunna lägga till tydligare instruktioner i prompten, för att sedan användas i ett syfte. Vilket är läsa data och få fram statistik som man skickar.

## Vad jag har lärt mig

Under projektets gång, så har jag fått en bättre förståelse kring hur FastApi fungerar och man kan bygga upp med olika typer av endpoints. Jag har även fått en bredare och en bättre förståelse kring hur pandas kan användas i olika syften, även hur man analyserar data och läser in från csv filer.

en annan sak som jag lärde mig var utav Runnable kedjan och dess funktion i praktikens gång. Det blev tydligt enklare för mig att dela upp flödet i flera steg för att kunna förstå hur information skickas genom de olika delarna i programmet, samt att varje del har sitt egna ansvar att behandla.

Jag har även fått en lite mer bättre förståelse kring hur AI-modeller kan implementeras i python applikationer, Samt att modellen inte kan ge rätt svar hela tiden. Vilket är då upp till individen att vara källkritisk till resultatet som modellen ger ut, och kollar ifall det är baserad på fakta, eller påhittade ord som inte hör till sig i programmet.

Det som jag tar med mig utav projektet är att felsökning av problem nogrannt efter varje implementation som jag lägger till i projektet. Många av problem som jag stötte på tog jag hjälp genom att testa mig fram steg för steg, och kolla vad som sker för att säkerhetställa orsaken av problemet redan från början.
