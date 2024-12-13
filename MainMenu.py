import os
import Yksinpeli
import minigame1 as m1
import minigame2 as m2
import minigame3 as m3
import minigame4 as m4
import kpsminipeli as m5
import boardgame
import Hirsipuuminipeli as hangman
import simppelikolikkominipeli as coin
import Sanan_arvaus_minipeli as m6

while True:
    os.system('cls')
    menu = [["............................"],[".           Peli           ."],[".                          ."],[".                          ."],[".(S)ingle, (M)ulti, (F)ree ."],["............................"]]
    for row in menu:
        print(" ".join(map(str,row)))
    valinta = input()
    #Singleplayer
    if valinta == "s":
        menu2 = [["............................"],[".                          ."],[".                          ."],[".                          ."],[".     (3)        (5)       ."],["............................"]]
        os.system('cls')
        for row in menu2:
            print(row)
        pituus = input("Kuinka pitkän pelin haluat pelata? ")

        if int(pituus) == 3:
            Yksinpeli.Game(3)
        if int(pituus) == 5:
            Yksinpeli.Game(5)

            #Multiplayer
    if valinta == 'm':
            #Luo ruudun
        os.system('cls')
        pelaajamaara = [["............................"],[".     Montako Pelaajaa?    ."],[".                          ."],[".                          ."],[".   (2)      (3)     (4)   ."],["............................"]]
        for row in pelaajamaara:
            print(" ".join(map(str,row)))
            #Päättää pelaajamäärän
        valinta = input()
        if valinta == '2':
            os.system('cls')
            boardgame.Turns(2)

        if valinta == '3':
            os.system('cls')
            boardgame.Turns(3)
        if valinta == '4':
            os.system('cls')
            boardgame.Turns(4)
            
    if valinta == 'f':
        os.system('cls')
        valikko = [["............................"],[".   Mitä  Peliä  Haluat    ."],[".         Pelata?          ."],[".(1)Type   (2)XO   (3)Ammu ."],[".(4)Laske  (5)KPS  (6)Puu  ."],[".(7)Coin   (8)Sana         ."],["............................"]]
        for line in valikko:
            print(' '.join(line))
        kysy = input("")
        if kysy == '1':
            os.system('cls')
            print([["............................"],[".       Vaikeustaso        ."],[".                          ."],[".                          ."],[".     (1)   (2)  (3)       ."],["............................"]])
            diff = input("")
            if diff == '1':
                mg = m1.startgame(12)
            if diff == '2':
                mg = m1.startgame(9)
            if diff == '3':
                mg = m1.startgame(6)
        if kysy == '2':
            os.system('cls')
            mg = m2.Game()
        if kysy == '3':
            os.system('cls')
            print([["............................"],[".       Vaikeustaso        ."],[".                          ."],[".                          ."],[".     (1)   (2)  (3)       ."],["............................"]])
            diff = input("")
            if diff == '1':
                mg = m3.game(12)
            if diff == '2':
                mg = m3.game(9)
            if diff == '3':
                mg = m3.game(6)
        if kysy == '4':
            os.system('cls')
            print([["............................"],[".       Vaikeustaso        ."],[".                          ."],[".                          ."],[".     (1)   (2)  (3)       ."],["............................"]])
            diff = input("")
            if diff == '1':
                mg = m4.Laskentaminipeli(12)
            if diff == '2':
                mg = m4.Laskentaminipeli(9)
            if diff == '3':
                mg = m4.Laskentaminipeli(6)
        if kysy == '5':
            os.system('cls')
            mg = m5.Minipelikivipaperisakset()

        if kysy == '6':
            os.system('cls')
            mg = hangman.hirsipuu()

        if kysy == '7':
            os.system('cls')
            mg = coin.coinflip()
        
        if kysy == '8':
            os.system('cls')
            mg = m6.piilotettu_sana_peli()

