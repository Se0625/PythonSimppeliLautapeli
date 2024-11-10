import random
vanha_kysymys = None
def triviapelifunktio():
    global vanha_kysymys
    
    while True:
        kysymyksen_numero = random.randint(1, 15)
        if kysymyksen_numero != vanha_kysymys:
            vanha_kysymys = kysymyksen_numero
            break
    if kysymyksen_numero == 1:
        kysymys1 = input("Minä vuonna toinen maailmansota loppui?: ")
        if kysymys1 == '1945':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print("Oikea vastaus olisi ollut 1945.")
            return "Häviö"
    if kysymyksen_numero == 2:
        kysymys2 = input("Minä vuonna talvisota loppui?: ")
        if kysymys2 == '1939':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print("Oikea vastaus olisi ollut 1939!")
            return "Häviö"
    if kysymyksen_numero == 3:
        kysymys3 = input("Minä vuonna Länsi-Rooma kaatui?: ")
        if kysymys3 == '476':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print("Oikea vastaus olisi 476!")
            return "Häviö"
    if kysymyksen_numero == 4:
        kysymys4 = input("Milloin Byzantti kaatui?: ")
        if kysymys4 == '1453':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print("Oikea vastaus olisi ollut 1453!")
            return "Häviö"
    if kysymyksen_numero == 5:
        kysymys5 = input("kuka voitti presidentinvaalit amerikassa 2016?: ")
        if kysymys5.lower() == 'donald trump':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Oikea vastaus olisi Donald Trump!')
            return "Häviö"
    if kysymyksen_numero == 6:
        kysymys6 = input("Mikä on maailmaan suurin mantere?: ")
        if kysymys6.lower() == 'aasia':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Oikea vastaus olisi Aasia!')
            return "Häviö"
    if kysymyksen_numero == 7:
        kysymys7 = input("Mikä on maailmaan suurin maa?: ")
        if kysymys7.lower() == 'venäjä':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Oikea vastaus olisi Venäjä!')
            return "Häviö"
    if kysymyksen_numero == 8:
        kysymys8 = input("Kuka teki nämä trivia kysymykset?: ")
        if kysymys8.lower() == 'samuel':
            print('Oikein! Samuel teki tämän trivian!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Tämän trivia pelin teki Samuel!!!')
            return "Häviö"
    if kysymyksen_numero == 9:
        kysymys9 = input("Kuka maalasi Mona Lisa maalauksen?: ")
        if kysymys9.lower() == 'leonardo da vinci':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Maalauksen maalasi Leonardo Da Vinci!')
            return "Häviö"
    if kysymyksen_numero == 10:
        kysymys10 = input("Mikä on Tšekin pääkaupunki?: ")
        if kysymys10.lower() == 'praha':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Se on Praha! Kaupunki niin hieno että se on kuin suoraan lastensadusta!')
            return "Häviö"
    if kysymyksen_numero == 11:
        kysymys11 = input("Mikä on maailman pisin eläin?: ")
        if kysymys11.lower() == 'kirahvi':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Se on oikeasti kirahvi!')
            return "Häviö"
    if kysymyksen_numero == 12:
        kysymys12 = input("Kuka on kirjoittanut kirjan jonka nimi on Leviathan (1651)?: ")
        if kysymys12.lower() == 'thomas hobbes':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Kirjan on kirjoittanut Thomas Hobbes!')
            return "Häviö"
    if kysymyksen_numero == 13:
        kysymys13 = input("Mikä on saksaksi Kebab?")
        if kysymys13.lower() == 'döner':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print("Väärin! Kebab on saksaksi döner!!!")
            return "Häviö"
    if kysymyksen_numero == 14:
        kysymys14 = input("Mikä joki virtaa Turun läpi?: ")
        if kysymys14.lower() == 'aurajoki':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Turun kaupungissa virtaa asiallinen ja kuuluisa Aurajoki!')
            return "Häviö"
    if kysymyksen_numero == 15:
        kysymys15 = input("Mikä on Viron pääkaupunki?: ")
        if kysymys15.lower() == 'tallinna':
            print('Oikein!')
            return "Voitto"
        else:
            print('Väärin!')
            print('Tallinna on Viron pääkaupunki!')
            return "Häviö"
