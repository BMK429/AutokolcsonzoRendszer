from datetime import date, timedelta
from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles

# Program fő belépési pontja, interaktív menüvel
def main():

    # Egy autókölcsönző áll rendelkezésre
    kolcsonzo = Autokolcsonzo("TesztAutó Kft.")

    # Autók hozzáadása a rendszerhez
    kolcsonzo.hozzaad_auto(Szemelyauto("ABC-123", "Toyota Corolla", 10000, "kézi", 5))
    kolcsonzo.hozzaad_auto(Szemelyauto("XYZ-987", "Ford Focus", 12000, "automata", 5))
    kolcsonzo.hozzaad_auto(Szemelyauto("LMN-456", "Opel Astra", 11000, "kézi", 4))
    kolcsonzo.hozzaad_auto(Teherauto("TEH-555", "Mercedes Actros", 25000, 10000))

    # Kezdő bérlések
    kolcsonzo.auto_berlese("ABC-123", "Kovács Péter", (date.today() + timedelta(days=1)).strftime("%Y-%m-%d"))
    kolcsonzo.auto_berlese("XYZ-987", "Nagy Anna", (date.today() + timedelta(days=2)).strftime("%Y-%m-%d"))
    kolcsonzo.auto_berlese("TEH-555", "Tóth Gábor", (date.today() + timedelta(days=3)).strftime("%Y-%m-%d"))
    kolcsonzo.auto_berlese("LMN-456", "Kiss László", (date.today() + timedelta(days=4)).strftime("%Y-%m-%d"))

    # induló konzolüzenet
    print("\n=== AUTÓKÖLCSÖNZŐ RENDSZER ===")
    print(f"Kölcsönző: {kolcsonzo.kolcsonzo_nev}")
    # print("Induló autók listája és státuszuk:")
    # kolcsonzo.autok_listazasa()

    # menü
    while True:
        print("\n=== MENÜ ===")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("0. Kilépés")

        valasztas = input("Választás: ")

        if valasztas == "1":
            kolcsonzo.autok_listazasa()
        elif valasztas == "2":
            rendszam = input("Rendszám: ")
            berlo = input("Bérlő neve: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                kolcsonzo.auto_berlese(rendszam, berlo, datum)
            except Exception as e:
                print("Hiba:", e)
        elif valasztas == "3":
            rendszam = input("Rendszám: ")
            berlo = input("Bérlő neve: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                kolcsonzo.berles_lemondasa(rendszam, berlo, datum)
            except Exception as e:
                print("Hiba:", e)
        elif valasztas == "4":
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()



