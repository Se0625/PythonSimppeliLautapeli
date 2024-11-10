import random
import time

def coinflip():
    noppa = random.randint(1,2)
    veikkaus = int(input("Veikkaa onko kolikko Kruuna (1) vai Klaava (2): "))
    if noppa == veikkaus:
        print ("Valitsit oikein!")
        return "Voitto"
    else:
        print ("Aijai, väärä valinta! haluatko vielä saada toisen mahdollisuuden voittaa tämän?")
        viimeinenmahdollisuus = int(input("Valitse uusi mahdollisuus (1) tai älä (2): "))
        if viimeinenmahdollisuus == 1:
            häviöpeli()
        else:
            print ("Valitsit häviön.")
            return "Häviö"

def häviöpeli():
    numero = int(input("Heitetään vaan noppaa, valitse numero 1-6: "))
    print ("Heitetään noppaa...")
    time.sleep(1)
    print ("Noppa:", random.randint(1,6))
    time.sleep(0.2)
    print ("Noppa:", random.randint(1,6))
    time.sleep(0.4)
    print ("Noppa:", random.randint(1,6))
    time.sleep(0.1)
    print ("Noppa:", random.randint(1,6))
    time.sleep(0.3)
    print ("Noppa:", random.randint(1,6))
    oikeanumero = random.randint(1,6)
    time.sleep(0.1)
    print ("Noppa:", oikeanumero)
    if oikeanumero == numero:
        print ("Onnittelut! veikkasit oikein!")
        return "Voitto"
    else:
        print ("Taas väärin! Nyt kyllä hävisit!")
        return "Häviö"