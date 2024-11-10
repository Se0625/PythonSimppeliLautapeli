import os
import random
import minigame1 as writing
import minigame2 as tictactoe
import minigame3 as shootergame
import minigame4 as mathgame
import kpsminipeli as kps
import Hirsipuuminipeli as hangman
import simppelikolikkominipeli as coin

def Game(length):
    global aika
    lives = 2
    aika = 15
    score = 0
    kierros = 0
    os.system('cls')
    while length > score:
        kierros +=1
        if kierros >= 2:
            aika -= 3
        print("Sinulla on ", lives, " elämää ja ", score, " pistettä")
        if lives == 0:
            print("Game Over")
            return "Häviö"
        minigamepicker = random.randint(1, 7)
        if minigamepicker == 1:
            minigame = writing.startgame(aika)


        elif minigamepicker == 2:
            minigame = tictactoe.Game()

        elif minigamepicker == 3:
            minigame = shootergame.game(aika)


        elif minigamepicker == 4:
            minigame = mathgame.Laskentaminipeli(aika)
            
                
        elif minigamepicker == 5:
            minigame = kps.Minipelikivipaperisakset()
        
        elif minigamepicker == 6:
            minigame = hangman.hirsipuu() 

        elif minigamepicker == 7:
            minigame = coin.coinflip()
                 
        if minigame == "Voitto":
            score += 1
            os.system('cls')
        if minigame == "Häviö":
            lives -= 1
            os.system('cls')