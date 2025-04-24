# https://www.handymath.com/cgi-bin/ethanolwater3.cgi?spcfgrv=&conc=&concv=&volwght=&calcvolwght=&entrytable=Show+Table+in+Volume+Percent+Ethanol

encore_une_fois = True

print("© Paul Keller\n "
      "22/04/2025 \n "
      "Free distribution under MIT License for more information see: https://opensource.org/license/mit\n"
      "")

def correct_main():
    alk = float(input("alkohol[Vol.%]: "))
    dichte = 2 * 10 ** (-5) * alk ** 2 - 0.0015 * alk + 0.9982
    print(f"Die Dichte würde {round(dichte, 5)} g/cm^3 betragen")

while encore_une_fois:
    correct_main()
    if not input("Möchtest du das Programm wiederholen? Drücke ENTER zum Wiederhoelen, irgendetwas anderes falls nicht!") == "":
        encore_une_fois = False
        print("Danke für das Benutzen dieses Programms!")
        input("")

