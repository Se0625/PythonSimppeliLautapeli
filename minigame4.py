import random
from inputimeout import inputimeout
def Laskentaminipeli(time):
    try:
        time = int(time)
        Laskuntyyppi = random.randint(1,4)
        if Laskuntyyppi == 1:
            numeroyksi = random.randint(0, 100)
            numerokaksi = random.randint(0, 100)
            tulos = numeroyksi + numerokaksi
            print ("Mikä on",numeroyksi,"+",numerokaksi,"? Sinulla on", time, "sekuntia aikaa!")
            vastaus = int(inputimeout(prompt='Vastaus: ', timeout=time))
            if vastaus == tulos:
                print ("Hienoa, oikein meni!")
                return "Voitto"
            else:
                print ("Väärin meni, oikea vastaus olisi ollut", tulos,"!")
                return "Häviö"
        elif Laskuntyyppi == 2:
            numeroyksi = random.randint(0, 100)
            numerokaksi = random.randint(0, 100)
            tulos = numeroyksi - numerokaksi
            print ("Mikä on",numeroyksi,"-",numerokaksi,"? Sinulla on 10 sekunttia aikaa!")
            vastaus = int(inputimeout(prompt="Vastaus: ", timeout=time))
            if vastaus == tulos:
                print ("Hienoa, oikein meni!")
                return "Voitto"
            else:
                print ("Väärin meni, oikea vastaus olisi ollut", tulos,"!")
                return "Häviö"
        elif Laskuntyyppi == 3:
            numeroyksi = random.randint(0, 100)
            numerokaksi = random.randint(0, 10)
            tulos = numeroyksi * numerokaksi
            print ("Mikä on",numeroyksi,"*",numerokaksi,"? Sinulla on 10 sekunttia aikaa!")
            vastaus = int(inputimeout(prompt='Vastaus: ', timeout=time))
            if vastaus == tulos:
                print ("Hienoa, oikein meni!")
                return "Voitto"
            else:
                print ("Väärin meni, oikea vastaus olisi ollut", tulos,"!")
                return "Häviö"
        elif Laskuntyyppi == 4:
            numeroyksi = random.randint(0, 25)
            tulos = numeroyksi * numeroyksi
            print ("Mikä on numeron",numeroyksi,"Potenssi? Sinulla on 10 sekunttia aikaa!")
            vastaus = int(inputimeout(prompt='Vastaus: ', timeout=time))
            if vastaus == tulos:
                print ("Hienoa, oikein meni!")
                return "Voitto"
            else:
                print ("Väärin meni, oikea vastaus olisi ollut", tulos,"!")
                return "Häviö"
    except:
        return "Häviö"
        print ("Aika loppui!")
