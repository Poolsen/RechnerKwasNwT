# https://laffort.com/wp-content/uploads/Protocols/DE_Table_Convertisseur.pdf ACHTUNG: DIESE QUELLE GIBT VON MEHREREN QUELLEN WIDERLEGTE FALSCHE ANGABEN ÜBER DEN ZUSAMMENHANG VON DICHTE UND G/L ZUCKER AN!
import numpy
from scipy.optimize import fsolve

def main():
    selection_base, selection_to = user_selection()
    calculation(selection_base, selection_to)

def user_selection():
    selection_base = input("Drücke \n"
                           "a für Oechsle\n"
                           "b für Zuckerkonzentration\n"
                           "als gegebene Variable\n"
                           "Deine Wahl: ")

    match selection_base:
        case "a":
            selection_base = "Oechsle"
        case "b":
            selection_base = "Zuckerkonzentration"
        case _:
            selection_base = "Not found"

    selection_to = input(f"Drücke \n"
                        f"a für {selection_base} in Zuckerkonzentration\n"
                        f"b für {selection_base} in Alkoholgehalt\n"
                        f"c für {selection_base} in Oechsle\n"
                        "Deine Wahl: ")

    match selection_to:
        case "a":
            selection_to = "Zuckerkonzentration"
        case "b":
            selection_to = "Alkoholgehalt"
        case "c":
            selection_to = "Oechsle"
        case _:
            selection_to = "Not found"

    print(f"Umrechnung von {selection_base} in {selection_to}")
    return selection_base, selection_to

def calculation(selection_base, selection_to):
    wert_base = float(input(f"Bitte gib deinen Wert für {selection_base} an: "))
    # von Oechsle in ..-
    if selection_base == "Oechsle":
        match selection_to:
            case "Zuckerkonzentration":
                wert_to = -3e-5 * wert_base**3 + 7.7e-3 * wert_base**2 + 1.913 * wert_base
            case "Alkoholgehalt":
                wert_to = (-3e-5 * wert_base**3 + 7.7e-3 * wert_base**2 + 1.913 * wert_base) / 18
            case _:
                wert_to = "Nope"

    #von Zucker zu ...
    elif selection_base == "Zuckerkonzentration":
        match selection_to:
            case "Oechsle":
                wert_to = fsolve(lambda x: -3e-5 * x ** 3 + 7.7e-3 * x ** 2 + 1.913 * x - wert_base, numpy.array([wert_base * 2]))[0]
            case "Alkoholgehalt":
                wert_to = wert_base / 18
            case _:
                wert_to = "Nope"
    else:
        wert_to = "Nope"

    try:
        wert_to = round(wert_to, 4)
    except TypeError:
        pass
    print(wert_to)

encore_une_fois = True

print("© Paul Keller\n "
      "22/04/2025 \n "
      "Free distribution under MIT License for more information see: https://opensource.org/license/mit\n"
      "")

while encore_une_fois:
    print("DIESES PROGRAMM IST OUTDATED UND INKORREKT. FÜR KORREKTE WERTE BENUTZE correct_main.py")
    main()
    if not input("Möchtest du das Programm wiederholen? Drücke ENTER zum Wiederhoelen, irgendetwas anderes falls nicht!") == "":
        encore_une_fois = False
        print("Danke für das Benutzen dieses Programms!")
        input("")
