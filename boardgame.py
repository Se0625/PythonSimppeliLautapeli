import random
import time
import os
from pynput import keyboard
import kpsminipeli as kps
import minigame4 as matematiikka
import minigame1 as writing
import minigame2 as tictactoe
import Triviankysymykset_samuel as trivia
import simppelikolikkominipeli as coin
import Hirsipuuminipeli as hangman
import minigame3 as shootergame


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def roll_dice():        
    roll = random.randint(1,6)
    #Tarvitaan time.sleep(), sillä noppaa heitetään kun spacebar painetaan ja releasataan 
    time.sleep(0.7)           
    return roll     
                                                                                                                                   
                                  
def getPlayers(Player_amount):
    Player_amount -= 1
    p_id = 0
    global players
    players = []
    
    while p_id <= Player_amount:
        p_id += 1
        player = {}
        player.update({"player":f"{p_id}"})
        player.update({"position":0})
        player.update({"roll":0})
        players.append(player)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
def CheckWinner():
    player_list = []
    player_pos_list = []
    for listed_p in players:
        player_list.append(listed_p)
        player_pos_list.append(listed_p.get("position"))
    for pelaaja in player_list:
        if pelaaja.get("position") == max(player_pos_list):
            return f"Pelaaja{pelaaja.get('player')} voitti!"

def createBoard():
    global board
    board = []
    for square in range(55):
        number = random.randint(1,3)
        if number == 1:
            square = "[ ]"
            board.append(square)
        if number == 2:
            square = "[M]"
            board.append(square)
        if number == 3:
            square = "[T]"
            board.append(square)
    return board

def Turns(amount):
    createBoard()
    getPlayers(amount)   
    global finished
    player_id = -1
    finished = False
    while finished == False:
        for player in players:
            player_id += 1
            if player_id > amount - 1:
                player_id = 0
            print(f"Pelaaja{player_id + 1}, heitä noppaa painamalla backspace ")
            with keyboard.Events() as events:
                for event in events: 
                    if event.key == keyboard.Key.backspace:
                        players[player_id]["roll"] = roll_dice()
                        players[player_id]["position"] += players[player_id].get("roll")
                        print(f"Pelaaja{player_id + 1} heitti: ",players[player_id].get("roll"))
                        time.sleep(1)
                        try:
        #Player minigame detection
                            if board[players[player_id].get("position") - 1] == "[M]":
                                board[players[player_id].get("position") - 1] = "[1, M]"
                                countdown = 3
                                for i in range(3):
                                        time.sleep(1)
                                        print(f"Minipeli alkaa {countdown}...")
                                        countdown -= 1
                                game = random.randint(1,7)
                                if game == 1:
                                    result = kps.Minipelikivipaperisakset()
                                elif game == 2:
                                    result = matematiikka.Laskentaminipeli(10)
                                elif game == 3:
                                    result = writing.startgame(7)
                                elif game == 4: 
                                        result = tictactoe.Game()
                                elif game == 5:
                                        result = coin.coinflip()
                                elif game == 6:
                                        result = hangman.hirsipuu()
                                elif game == 7:
                                        result = shootergame.game(10)
                                                
                                if result == "Voitto":
                                        players[player_id]["roll"] = roll_dice()
                                        players[player_id]["position"] += players[player_id].get("roll")
                                        print(f"Pelaaja{player_id + 1}, onnea! Heitit: ",players[player_id]["roll"])
                                        board[players[player_id].get("position") - 1] = f"[{player_id + 1}, M]"
                                    
                                if result == "Häviö":
                                        board[players[player_id].get("position") - 1] = f"[{player_id + 1}, M]"
                                        continue
        #Player Trivia detection
                            if board[players[player_id].get("position") - 1] == "[T]":
                                    
                                    result = trivia.triviapelifunktio()

                                    if result == "Voitto":
                                        players[player_id]["roll"] = roll_dice()
                                        players[player_id]["position"] += players[player_id].get("roll")
                                        print(f"Pelaaja{player_id + 1}, onnea! Heitit: ",players[player_id]["roll"])
                                        board[players[player_id].get("position") - 1] = f"[{player_id + 1}, T]"
                                    
                                    if result == "Häviö":
                                        print("Menet yhden taaksepäin, tyhmä aasi!")
                                        players[player_id]["position"] -= 1
                                        board[players[player_id].get("position") - 1] = f"[{player_id + 1}, T]"

                            if board[players[player_id].get("position") - 1] == "[ ]":
                                    board[players[player_id].get("position") - 1] = f"[{player_id + 1}]"

                            else:    
                                board[players[player_id].get("position") - 1] = f"[{player_id + 1}]"
                        except:
                            board[-1] = f"[{player_id + 1}]"      
                        break

                if player_id + 1 == amount:
                    time.sleep(1.5)
                    print()
                    os.system('cls')
                    print(" ".join(board))
                    createBoard() 
                    for player in players:
                        if player.get("position") >= 56:
                            finished = True   
                        if finished == True:
                            print(CheckWinner())
                            break
                        if player["player"] == players[-1]["player"]:
                            break
                             

 
