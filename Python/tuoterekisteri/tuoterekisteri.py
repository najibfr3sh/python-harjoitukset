tuotteet = []

while True:
    print("\n--- TUOTEHALLINTA ---")
    print("1. Listaa tuotteet")
    print("2. Lisää tuote")
    print("3. Poista tuote")
    print("4. Näytä varaston kokonaisarvo")
    print("0. Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        if len(tuotteet) == 0:
            print("Varasto on tyhjä.")
        else:
            print("\n--- Varaston tuotteet ---")
            for nimi, hinta, maara in tuotteet:
                print(f"- {nimi}: {hinta:.2f} € ({maara} kpl)")

    elif valinta == "2":
        nimi = input("Tuotteen nimi: ")
        hinta = float(input("Tuotteen kappalehinta (€): "))
        maara = int(input("Määrä (kpl): "))
        tuotteet.append((nimi, hinta, maara))
        print(f"Lisätty: {nimi} ({maara} kpl)")

    elif valinta == "3":
        poistettava = input("Poistettavan tuotteen nimi: ")
        loytyi = False
        for i in range(len(tuotteet)):
            if tuotteet[i].lower() == poistettava.lower():
                tuotteet.pop(i)
                loytyi = True
                print(f"Tuote '{poistettava}' poistettu.")
                break
        if not loytyi:
            print("Tuotetta ei löytynyt.")

    elif valinta == "4":
        kokonaisarvo = 0
        for nimi, hinta, maara in tuotteet:
            kokonaisarvo += hinta * maara
        print(f"Varaston kokonaisarvo: {kokonaisarvo:.2f} €")

    elif valinta == "0":
        print("Lopetetaan ohjelma...")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
