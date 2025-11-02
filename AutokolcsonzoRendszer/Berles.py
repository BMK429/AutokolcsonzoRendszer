from datetime import date

# Bérlés osztály, amely egy autó bérlését reprezentálja adott dátumra
class Berles:
    def __init__(self, auto, datum: date, berlo_nev: str):
        if not isinstance(datum, date):
            raise TypeError("A dátumnak date típusúnak kell lennie.")
        if datum < date.today():
            raise ValueError("A bérlés dátuma nem lehet múltbéli.")
        self.auto = auto
        self.datum = datum
        self.berlo_nev = berlo_nev

    def __str__(self):
        return f"{self.berlo_nev} bérelte a {self.auto.rendszam} autót {self.datum}-ra, díj: {self.auto.berleti_dij} Ft"