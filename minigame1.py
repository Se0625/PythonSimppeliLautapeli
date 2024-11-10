#Kirjoitus minipeli
from inputimeout import inputimeout
import random

def startgame(aika):
    wordlist = ['koira', 'kissa', 'helikopteri', 'lentokone', 'hius', 'kyy', 'koe']
    kierros = 0
    while kierros < 2:
        try:
            word = random.choice(wordlist)
            print(word)
            time = inputimeout(prompt="Kirjoita tämän sanan:", timeout=aika)

            if time == word:
                kierros += 1
            else:
                print("Väärin")
                time = "Time's up!"
                break
        except Exception:
            time = "Time's up!"
            print(time)
            break
    if time == "Time's up!":
        print("Hävisit!")
        return "Häviö"
    else:
        print("Voitit!")
        return "Voitto"

