import random

def Minipelikivipaperisakset():
    pisteet = 0
    Vastaukset = ["Kivi", "Paperi", "Sakset"]
    Valinta = random.choice(Vastaukset)
    Pelaaja = input("Kivi, Paperi, Sakset?: ")
    if Pelaaja == Valinta:
        print("Tasapeli!")
        return "Häviö"
    elif Pelaaja.lower() == "kivi":
        if Valinta == "Paperi":
            print("Hävisit! Vastustaja valitsi paperin.")
            return "Häviö"
        else:
            print("Voitit! Vastustaja valitsi sakset.")
            return "Voitto"
    elif Pelaaja.lower() == "paperi":
        if Valinta == "Sakset":
            print("Hävisit! Vastustaja valitsi sakset.")
            return "Häviö"
        else:
            print("Voitit! Vastustaja valitsi kiven.")
            return "Voitto"
    elif Pelaaja.lower() == "sakset":
        if Valinta == "Kivi":
            print("Hävisit! Vastustaja valitsi kiven.")
            return "Häviö"
        else:
            print("Voitit! Vastustaja valitsi paperin.")
            return "Voitto"
    else:
        print("Hävisit! Sinun piti kirjoittaa joko Kivi, Paperi tai Sakset")
        return "Häviö"
