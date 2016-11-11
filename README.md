# ISJ<br><br>
#Project 1 12/12<br>
Scripting Languages projects<br><br>
<br><br>
S využitím regulárních výrazů a programu sed, jazyka Perl (sed 's/before/after/g' můžete nahradit perl -ne 's/before/after/g; print;', nebo využít program s2p), případně jazyka Python, pokud jej už ovládáte, vytvořte skript pro unixový příkazový interpret (shell), nebo program v jazyce Python, který na řádcích, obsahujících řetězec xkcd, nahradí text, odpovídající regulárnímu výrazu bu.*ls, řetězcem \[gikuj]..n|a.\[alt]|\[pivo].l|i..o|\[jocy]e|sh|di|oo (nahrazujeme skutečně řetězcem, žádné znaky zde nemají speciální význam). <br><br>
Program dále na řádcích, obsahujících znaky = a [ (znaky "rovná se" a "levá hranatá závorka"), a současně neobsahujích znak ! (neobsahujících znak "vykřičník"), nahradí výskyty řetězce xkcd za vaše fakultní uživatelské jméno (tedy např. za xnovak01).<br><br>
<br><br>
Jako první řádek skriptu uveďte tzv. shebang (viz https://en.wikipedia.org/wiki/Shebang_%28Unix%29), který umožní spuštění skriptu na fakultním serveru merlin, takže např.:<br><br>
\#!/usr/bin/env bash<br><br>
nebo<br><br>
\#!/usr/bin/env python3<br><br>
<br><br>
Název souboru se skriptem musí odpovídat tvaru login.sh nebo login.py (tedy např. xnovak01.sh).<br><br>
 <br><br>
Aplikujte svůj program na zdrojový kód "zápisníku" http://nbviewer.jupyter.org/url/norvig.com/ipython/xkcd1313.ipynb (tedy soubor z adresy http://norvig.com/ipython/xkcd1313.ipynb). Výsledek (zápisník s nahrazením) pojmenujte login.ipynb (tedy např. xnovak01.ipynb).<br><br>
<br><br>
Zjistěte, co v upraveném zápisníku vrátí volání funkce mistakes(vas_login, winners, losers), tedy např.:<br><br>
mistakes(xnovak01, winners, losers)<br><br>
a napiště příslušný řádek výstupu do samostatného souboru, pojmenovaném login.mistakes (tedy např. xnovak01.mistakes)<br><br>
<br><br>
Výsledek odevzdejte prostřednictvím WIS jako komprimovaný "balíček" ve formátu .tgz nebo .zip a pojmenujte login.format (tedy např. xnovak01.tgz). Musí obsahovat vlastní skript, případně všechny další odkazované soubory, zdrojovou i výslednou podobu zápisníku a soubor .mistakes.<br><br>
<br><br>
Projekt bude hodnocen automaticky, při nedodržení názvových konvencí nebo dalších pravidel bohužel nebudete moci získat body.<br>
#Project 2 14/14<br>
Implementujte v Pythonu nebo Ruby třídu Polynomial, která bude pracovat s polynomy reprezentovanými jako seznamy (v Ruby pole). Například 2x^3 - 3x + 1 bude  reprezentováno jako [1,-3,0,2] (seznam začíná nejnižším řádem, i když se polynomy většinou zapisují opačně).<br>
<br>
Instance třídy bude možné vytvářet několika různými způsoby:<br>
pol1 = Polynomial([1,-3,0,2])<br>
pol2 = Polynomial(1,-3,0,2)<br>
pol3 = Polynomial(x0=1,x3=2,x1=-3)<br>
<br>
Volání funkce print() vypíše polynom v obvyklém formátu:<br>
\>>> print(pol2)<br>
2x^3 - 3x + 1<br>
<br>
Polynomy bude možné sčítat a umocňovat nezápornými celými čísly:<br>
\>>> print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))<br>
2x^3 + x^2 - x + 1<br>
\>>> print(Polynomial(-1, 1) ** 2)<br>
x^2 - 2x  + 1<br>
<br>
A budou fungovat metody derivative() - derivace a at_value() - hodnota polynomu pro zadané x - obě pouze vrací výsledek, nemění samotný polynom:<br>
\>>> print(pol1.deriv())<br>
6x^2 - 3<br>
\>>> print(pol1.at_value(2))<br>
11<br>
\>>> print(pol1.at_value(2,3))<br>
35<br>
(pokud jsou zadány 2 hodnoty, je výsledkem rozdíl mezi hodnotou at_value() druhého a prvního parametru - může sloužit pro výpočet určitého integrálu, ale ten nemá být implementován)<br>
<br>
Nezapomeňte na dokumentační řetězce.<br>
#Project 3 14/14<br>
S využitím modulu cProfile zjistěte, kolikrát je volána funkce lev() ve skriptu dostupném na https://www.fit.vutbr.cz/study/courses/ISJ/private/lev.py.<br>
Výsledek uložte do souboru lev.cProfile_output.<br>
<br>
Pomocí time zjistěte, jak dlouho běží skript dostupný na https://www.fit.vutbr.cz/study/courses/ISJ/private/nonpalindrom_words_existing_reversed.py na souboru staženém z https://www.fit.vutbr.cz/study/courses/ISJ/private/words30000.txt. Upravte skript tak, aby se daný čas co možná nejvíc zkrátil a aby bylo možné zpracovat i podstatně větší soubor stažený z https://www.fit.vutbr.cz/study/courses/ISJ/private/words.txt. Upravený skript pojmenujte ve formatu login_nonpalindrom_words_existing_reversed.py (tedy např. xnovak01_nonpalindrom_words_existing_reversed.py) a odevzdejte.<br>
Výstup z time ./`id -u -n`_nonpalindrom_words_existing_reversed.py words.txt odevzdejte jako words.time_output.<br>
<br>
Změřte čas běhu skriptů dostupných na adresách https://www.fit.vutbr.cz/study/courses/ISJ/private/sekv.py a https://www.fit.vutbr.cz/study/courses/ISJ/private/para.py a odevzdejte je jako sekv.time_output a para.time_output. Do souboru why.txt napište třípísmennou zkratku, která vysvětlí, proč se reálný čas běhu paralelní verze neblíží polovině běhu sekvenční verze. Soubor why.txt odevzdejte. <br>
Upravte skript para.py tak, aby reálný čas zpracování odpovídal zhruba polovině času běhu sekvenční verze. Upravenou verzi pojmenujte ve formatu login_para.py (tedy např. xnovak01_para.py) a odevzdejte.
