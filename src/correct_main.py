#keine Quelle, selbst hergeleitet

encore_une_fois = True

print("© Paul Keller\n "
      "22/04/2025 \n "
      "Free distribution under MIT License for more information see: https://opensource.org/license/mit\n"
      "")

def correct_main():
    oechsle = float(input("Oechsle[°Oe]: "))
    wasser_ml = float(input("Wasser[ml]: "))
    zucker = float(input("Zucker[g]: "))
    wasser = wasser_ml * 0.9982

    zucker_konz = zucker / (zucker + wasser) * (1 + (oechsle / 1000)) * 1000
    alk = (zucker / (zucker + wasser) * (1 + (oechsle / 1000)) * 1000) / 18
    dichte = 2 * 10 ** (-5) * alk ** 2 - 0.0015 * alk + 0.9982

    print(f"Die Zuckerkonzentration beträgt {round(zucker_konz, 4)} g/l")
    print(f"Möglicher Alkoholgehalt bei 18 g/l Zucker pro Volumenprozent Alkohol: {round(alk, 4)}%")
    print(f"Die Dichte würde {round(dichte, 5)} g/cm^3 betragen")

while encore_une_fois:
    correct_main()
    if not input("Möchtest du das Programm wiederholen? Drücke ENTER zum Wiederhoelen, irgendetwas anderes falls nicht!") == "":
        encore_une_fois = False
        print("Danke für das Benutzen dieses Programms!")
        input("")

