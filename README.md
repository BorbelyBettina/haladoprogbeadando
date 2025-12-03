Dokumentáció:

  Áttekintés: 
Ez egy egyszerű, de hatékony parancssori képszerkesztő program, amellyel egyszerre 
több képet lehet módosítani. A program a megadott input_images mappában lévő 
összes képet feldolgozza, és a módosított változatokat az output_images mappába 
menti. 

Szükséges könyvtárak:  
  • Pillow 
  
Funkciók: 
A program a következő műveleteket tudja elvégezni: 
1. Átméretezés – százalékosan vagy fix mérettel 
2. Forgatás – bármilyen szöggel  
3. Kivágás – megadott koordináták alapján 
4. Formátum konvertálás – pl. PNG - JPG 
5. Több művelet egy lépésben – pl. átméretez + forgat + JPG-vé alakít 
6. Output mappa teljes törlése

Részletes leírás a menüpontokról: 
1. Képek átméretezése 
  • Kér egy méretet három formában: 
    o 50% → az eredeti méret 50%-a 
    o 800x600 → pontosan ennyi pixel 
    o 800 → csak szélesség 800 px, magasság arányosan 
  • Mentés: képnév_800x600.jpg vagy képnév_400x300.jpg stb. 
2. Képek forgatása 
  • Bármilyen egész számú szöget megadhatsz (pl. 90, -45, 180) 
  • expand=True → a kép nem lesz levágva forgatás után 
  • Mentés: képnév_rot90.png 
3. Képek kivágása 
  • Kér négy értéket: bal, fent, jobb, lent (pixelben, 0-tól számítva) 
  • Automatikusan korrigálja, ha rossz koordinátákat adnál meg 
  • Mentés: képnév_crop_100_50_500_400.jpg 
4. Formátum konvertálás 
  • Pl. minden képet JPG-vé vagy PNG-vé alakít 
  • RGBA - RGB automatikus konverzió JPG mentésnél (háttér fehér lesz) 
  • Mentés: képnév_conv_jpg.jpg 
5. Több művelet egyszerre (batch) 
  • Kiválaszthatod, hogy melyik műveleteket akarod egyszerre 
  • A műveletek ebben a sorrendben futnak: 
    1. Átméretezés 
    2. Forgatás 
    3. Kivágás 
    4. Formátum váltás 
  • Minden képhez egy eredmény kerül ki: képnév_batch.jpg 
6. Output mappa ürítése 
  • Törli az összes fájlt az output_images mappából. 
7. Kilépés

Hibakezelés: 
• Minden hibát kiír a konzolra, de a többi kép feldolgozását folytatja. 
• Nem töri meg a futást egy hibás kép miatt. 


10 mondat: 
Ez a Python program egy egyszerű képfeldolgozó eszköz, amely az input_images mappában található képeken végez különböző műveleteket, majd az eredményt az output_images mappába menti.
A felhasználó átméretezheti a képeket százalékos arány vagy konkrét szélesség és magasság alapján.
Lehetőség van a képek forgatására tetszőleges szögben, valamint kivágására megadott koordináták szerint.
A program támogatja a formátumok közötti konvertálást (pl. JPG - PNG).
Az összes művelet egyesíthető batch módban, ahol több módosítás egyszerre alkalmazható. Van lehetőség az output mappa teljes törlésére is.
A felhasználói interakció menü alapú, könnyen követhető választásokkal.
A képek mentésekor automatikusan kezelve van a formátum és a színtér konverzió.
Hibakezelés be van építve a képfájlok feldolgozásához és mentéséhez.
A program a PIL (Pillow) könyvtárat használja a képfeldolgozáshoz.
A fő ciklus lehetővé teszi a folyamatos használatot kilépésig.
