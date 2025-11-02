from Auto import Auto


# Személyautó osztály, az Auto leszármazottja
class Szemelyauto(Auto):

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, valto_tipus: str, ajtok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        # Ellenőrizzük a váltó típusát és az ajtók számát
        if valto_tipus not in ["kézi", "automata"]:
            raise ValueError("A váltó típusa csak 'kézi' vagy 'automata' lehet.")
        if ajtok_szama not in [3, 4, 5]:
            raise ValueError("Az ajtók száma csak 3, 4 vagy 5 lehet.")
        self._valto_tipus = valto_tipus
        self._ajtok_szama = ajtok_szama

    # Személyautó adatainak kiírása
    def __str__(self):
        foglalas_db = len(self._berlesek)
        statusz = "szabad" if foglalas_db == 0 else f"{foglalas_db} napra foglalt"
        return (f"Személyautó | Rendszám: {self._rendszam} | "
                f"Típus: {self._tipus} | Váltó: {self._valto_tipus} | "
                f"Ajtók: {self._ajtok_szama} | Díj: {self._berleti_dij} Ft/nap | "
                f"Státusz: {statusz}")
