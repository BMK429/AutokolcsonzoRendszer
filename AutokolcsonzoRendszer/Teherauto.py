from Auto import Auto

# Teherautó osztály, az Auto leszármazottja
class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, terhelhetoseg: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._terhelhetoseg = terhelhetoseg             # Teherbírás kg-ban

    # Teherautó adatainak kiírása
    def __str__(self):
        foglalas_db = len(self._berlesek)
        statusz = "szabad" if foglalas_db == 0 else f"{foglalas_db} napra foglalt"
        return (f"Teherautó | Rendszám: {self._rendszam} | "
                f"Típus: {self._tipus} | "
                f"Terhelhetőség: {self._terhelhetoseg} kg | "
                f"Díj: {self._berleti_dij} Ft/nap | "
                f"Státusz: {statusz}")

