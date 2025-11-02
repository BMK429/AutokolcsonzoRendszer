from datetime import datetime
from Berles import Berles

# Autókölcsönző osztály, amely az összes autót és bérlést kezeli
class Autokolcsonzo:
    def __init__(self, kolcsonzo_nev: str):
        self._kolcsonzo_nev = kolcsonzo_nev
        self._autok = []                     # Lista a raktáron lévő autókról

    @property
    def kolcsonzo_nev(self):
        return self._kolcsonzo_nev

    # Autó hozzáadása a rendszerhez
    def hozzaad_auto(self, auto):
        self._autok.append(auto)

    # Az összes autó és státuszuk listázása
    def autok_listazasa(self):
        if not self._autok:
            print("Nincs autó a rendszerben.")
            return
        for auto in self._autok:
            print(auto)

    # Az összes aktív bérlés listázása
    def berlesek_listazasa(self):
        if not any(auto.berlesek for auto in self._autok):
            print("Nincs aktív bérlés.")
            return
        print("\n--- Aktív bérlések ---")
        for auto in self._autok:
            for berles in auto.berlesek:
                print(berles)

    # Autó bérlése a rendszám, bérlő és dátum alapján
    def auto_berlese(self, auto_rendszam: str, berlo_nev: str, datum_str: str):
        auto = next((a for a in self._autok if a.rendszam == auto_rendszam), None)
        if not auto:
            raise ValueError(f"Nincs ilyen rendszám: {auto_rendszam}")

        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()

        except ValueError:
            raise ValueError("Dátum formátuma: ÉÉÉÉ-HH-NN")

        uj_berles = Berles(auto, datum, berlo_nev)
        auto.berles_hozzaadasa(uj_berles)
        print(f"Bérlés sikeres: {uj_berles}")
        return auto.berleti_dij

    # Bérlés lemondása a rendszám, bérlő és dátum alapján
    def berles_lemondasa(self, auto_rendszam: str, berlo_nev: str, datum_str: str):
        auto = next((a for a in self._autok if a.rendszam == auto_rendszam), None)
        if not auto:
            raise ValueError(f"Nincs ilyen rendszám: {auto_rendszam}")

        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Dátum formátuma: ÉÉÉÉ-HH-NN")

        auto.berles_torlese(berlo_nev, datum)
        print(f"A {auto_rendszam} rendszámú autó bérlése ({datum}) lemondva.")
