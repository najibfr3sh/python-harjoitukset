kulut = []

while True:
    print("\n--- KULUSEURANTA ---")
    print("1. Lisää kulu")
    print("2. Näytä kulut")
    print("3. Näytä tilasto")
    print("4. Lopeta sovellus")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        nimi = input("Kulun nimi: ")
        hinta = float(input("Kulun hinta (€): "))
        kulut.append((nimi, hinta))
        print(f"Lisätty: {nimi} ({hinta:.2f} €)")

    elif valinta == "2":
        if len(kulut) == 0:
            print("Ei lisättyjä kuluja.")
        else:
            print("\n--- Kaikki kulut ---")
            for nimi, hinta in kulut:
                print(f"- {nimi}: {hinta:.2f} €")

    elif valinta == "3":
        if len(kulut) == 0:
            print("Ei kuluja tilastoitavaksi.")
        else:
            hinnat = [hinta for nimi, hinta in kulut]
            print("\n--- Tilastot ---")
            print(f"Kokonaiskulut: {sum(hinnat):.2f} €")
            print(f"Pienin kulu: {min(hinnat):.2f} €")
            print(f"Suurin kulu: {max(hinnat):.2f} €")

    elif valinta == "4":
        print("Lopetetaan sovellus...")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
