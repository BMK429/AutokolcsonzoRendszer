from abc import ABC, abstractmethod
from datetime import date

# Absztrakt osztály, amely az összes autótípus közös tulajdonságait definiálja.
# Tárolja az autó adatait és az aktuális bérléseket.
class Auto(ABC):

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self._rendszam = rendszam           # Autó rendszáma
        self._tipus = tipus                 # Autó típusa / modellje
        self._berleti_dij = berleti_dij     # Napi bérleti díj
        self._berlesek = []                 # Lista, amely a Berles objektumokat tartalmazza


    # Tulajdonságok a védett attribútumok elérésére
    @property
    def rendszam(self):
        return self._rendszam

    @property
    def tipus(self):
        return self._tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    @property
    def berlesek(self):
        return self._berlesek

    # Ellenőrzi, hogy az autó elérhető-e egy adott napon
    def elerheto(self, datum: date) -> bool:
        return all(b.datum != datum for b in self._berlesek)


    # Hozzáadja a bérlést, ha az autó szabad a megadott dátumra
    def berles_hozzaadasa(self, berles):
        if not isinstance(berles.datum, date):
            raise TypeError("A dátumnak date típusúnak kell lennie.")
        if not self.elerheto(berles.datum):
            raise ValueError(f"Az autó {berles.datum}-ra már foglalt.")
        self._berlesek.append(berles)


    # Lemondja a bérlést a bérlő neve és dátum alapján
    def berles_torlese(self, berlo_nev: str, datum: date):
        berles = next((b for b in self._berlesek if b.berlo_nev == berlo_nev and b.datum == datum), None)
        if not berles:
            raise ValueError("Nincs ilyen bérlés.")
        self._berlesek.remove(berles)


    # Az autó adatainak szöveges megjelenítése. Különböző autótípusoknál eltérő.
    @abstractmethod
    def __str__(self):
        pass
