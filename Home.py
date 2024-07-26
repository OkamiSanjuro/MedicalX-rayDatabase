import streamlit as st

def set_background():
    st.markdown(
         """
         <style>
         @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
         
         .stApp {
             background: linear-gradient(to bottom right, #f0f4f7, #d9e2ec);
             background-attachment: fixed;
             color: #212121;
             font-family: 'Roboto', sans-serif;
         }
         .title {
             font-size: 48px;
             font-weight: 700;
             color: #ffffff;
             text-align: center;
             padding: 20px;
             background: rgba(0, 150, 136, 0.8);
             border-radius: 10px;
             margin-top: 20px;
             text-shadow: 2px 2px 4px #000000;
             animation: fadeInDown 1.5s;
         }
         .subheader {
             font-size: 28px;
             color: #ffffff;
             background: #00796B;
             padding: 10px;
             border-radius: 10px;
             margin-top: 30px;
             margin-bottom: 10px;
         }
         .subsubheader {
             font-size: 22px;
             color: #ffffff;
             background: #004D40;
             padding: 8px;
             border-radius: 8px;
             margin-top: 20px;
             margin-bottom: 10px;
         }
         .content {
             font-size: 16px;
             line-height: 1.2;
             text-align: justify;
             margin: 20px;
             padding: 20px;
             background: #ffffff;
             border-radius: 10px;
             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
         }
         .content ul {
             margin-left: 20px;
         }
         .content li {
             margin-bottom: 10px;
         }
         .content p {
             margin-bottom: 10px;
         }
         .content a {
             color: #00796B;
             text-decoration: none;
         }
         .content a:hover {
             text-decoration: underline;
         }
         @keyframes fadeInDown {
             0% {
                 opacity: 0;
                 transform: translateY(-20px);
             }
             100% {
                 opacity: 1;
                 transform: translateY(0);
             }
         }
         @keyframes fadeIn {
             0% {
                 opacity: 0;
             }
             100% {
                 opacity: 1;
             }
         }
         </style>
         """,
         unsafe_allow_html=True
     )

def main():
    set_background()

    st.markdown('<div class="title">Üdvözöljük az Orvosi Röntgenkép Adatbázisban!</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    <div class="subheader">Az alkalmazás célja</div>
    Az alkalmazás célja, hogy segítse az orvosi röntgenképek kezelését, feltöltését, keresését és állapotuk nyomon követését. A rendszer pontos és részletes adatokat gyűjt a röntgenképekről, hogy elősegítse az orvosi kutatást, oktatást valamint legfőképpen a traumatológiai diagnosztikai munkát, ezáltal javítva a betegek ellátását.
    
    <div class="subheader">Funkciók</div>
    <ul>
        <li><strong>Kép feltöltése</strong>: Új röntgenkép(ek)et tölthet fel az adatbázisba.</li>
        <li><strong>Képek keresése</strong>: Kereshet az adatbázisban található röntgenképek között különböző kritériumok alapján.</li>
        <li><strong>Státusz</strong>: Megtekintheti a feltöltött röntgenképek állapotát és statisztikáit.</li>
        <li><strong>Elérhetőség</strong>: Kapcsolatba léphet a fejlesztőkkel.</li>
    </ul>

    <div class="subheader">Használati útmutató</div>

    <div class="subsubheader">1. Kép feltöltése</div>
    <div class="content">
        <ul>
            <li>Kérjük a feltöltésre szánt képekről bizonyosodjon meg hogy anonimizálva vannak! A képeken nem szerepelhet semmilyen betegazonosító!</li>
            <li>Válassza a bal oldalsáv "Navigáció" menüjéből a "Kép feltöltése" pontot.</li>
            <li>Húzza a "Drag and drop file here" mezőbe a képet vagy válassza ki a "Browse files" gombbal s töltse fel a röntgenkép(ek)et (Max 15 MB/file).</li>
            <li><strong>Több kép feltöltése</strong>: Ha egyszerre több képet szeretne feltölteni, pipálja ki a "Több kép feltöltése" lehetőséget. Figyelem: az összes kép ugyanazokat a címkéket kapja! (kivéve a betegazonosítót)</li>
            <li>Kérem, adja meg a kötelező adatokat: korcsoport, röntgen nézet, normál vagy elváltozás típusa, melyik oldal (ha végtagról van szó), és a sérült régiók (fő régió, régió).</li>
            <li>A részletesebb adatmegadás (alrégiók, komplikációk, társuló állapotok, osztályozások) nagyban segíti a kutatást és diagnosztikát.</li>
            <li><strong>Több régió jelölése</strong>: Ha több sérült régiót szeretne megadni, pipálja ki a "Több régió jelölése" opciót. Fontos: új régió hozzáadására csak mentés után van lehetőség, jelenlegi technikai korlátok miatt. Ha mentés nélkül több új régiót hozzáad, hibaüzenet fog keletkezni!</li>
            <li>A választható súlyossági kategóriák folyamatosan bővülnek. A hosszú csöves csontoknál már elérhető a teljes AO klasszifikáció.</li>
            <li>Kattintson a "Feltöltés" gombra a kíválasztott adatok újra összegzéséhez, majd a "Megerősítés és Feltöltés" gombbal véglegesítheti a feltöltést.</li>
            <li>Kérjük várja meg a zöld "Sikeres feltöltés" feliratot mielött új képet tölt fel. Több kép feltöltésénél egyszerre, többet kell várni.</li>
        </ul>
    </div>

    <div class="subsubheader">2. Képek keresése</div>
    <div class="content">
        <ul>
            <li>Válassza a "Képek keresése" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li>Adja meg a keresési feltételeket (minimum: típus, nézet, főrégió).</li>
            <li>Kattintson a "Keresés" gombra. A találatok listája megtekinthető és letölthető.</li>
            <li>Várjon egy pár másodpercet amíg a szerver összeállítja a "Letöltés" gomb megnyomása után a .zip filet, majd kattintson a "Megerősítés s Letöltés" gombra ha le kívánja tölteni a képeket és a hozzájuk tartozó címkéket.</li>
        </ul>
    </div>

    <div class="subsubheader">3. Státusz</div>
    <div class="content">
        <ul>
            <li>Válassza a "Státusz" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li>Tekintse meg a feltöltött röntgenképek statisztikáit és a projekt aktuális fázisának állapotát.</li>
            <li>Az adatok alapján nyomon követheti a projekt előrehaladását és a hiányzó elemeket.</li>
            <li>Az első fázis lezárási kritériumai: az összes különböző csontot tartalmazó régióból, legalább két nézetből, normál és törött röntgenképeket gyüjts felnőttektől, kombinációnként legalább 50 darabot.</li>
            <li>A második fázis a különböző alrégiók feltöltése lesz előreláthatólag.</li>
            <li>Fontos: egyelőre a státusz a gyermekkori röntgeneket is számba veszi!</li>
        </ul>
    </div>

    <div class="subsubheader">4. Elérhetőség</div>
    <div class="content">
        <ul>
            <li>Válassza az "Elérhetőség" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li>Ha bármilyen észrevétele van a honlappal kapcsolatban, segítségre van szüksége vagy kérdése van, lépjen nyugodtan kapcsolatba a fejlesztőkkel.</li>
        </ul>
    </div>

    <div class="subheader">Fontos Információk</div>
    <ul>
        <li><strong>Adatbiztonság</strong>: Az összes feltöltött adat biztonságos és titkosított környezetben kerül tárolásra.</li>
        <li><strong>Frissítések és Karbantartás</strong>: Az alkalmazás rendszeresen frissül, hogy biztosítsa, hogy egyre több s kényelmesebb funkció várja az ide látogatókat.</li>
    </ul>

    Köszönjük, hogy használja az alkalmazásunkat!
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
