from pynput import keyboard
import os
import time
import random




def updateboard():
        gameboard =  [['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.']]
        os.system('cls')
        hirviox = hirvio["x"]
        hirvioy = hirvio["y"]
        gameboard[hirvioy].pop()
        gameboard[hirvioy].insert(hirviox, "*")
        ypositio = gameboard[9]
        ypositio.pop()
        ypositio.insert(Positio, "A")
        for line in gameboard:
            print(' '.join(line))

def move():
     time.sleep(0.2)
     return 1

def game(aika):
    global lasku
    global hirvio
    global Positio
    global x, y
    global gameboard
    global start
    global end
    global hirvio_y
    global hirvio_x
    start = time.perf_counter()
    hirvio_x = random.randint(1, 8)
    hirvio_y = random.randint(1, 3)
    hirvio = {"x" : hirvio_x, "y" : hirvio_y}
    gameboard =  [['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.']]
    x = [0,1,2,3,4,5,6,7]
    y = [0,1,2,3,4,5,6,7,8,9]
    Positio = 0
    ypositio = gameboard[9]
    ypositio.pop()
    ypositio.insert(Positio, "A")
    for line in gameboard:
        print(' '.join(line))
    lasku = 0
    while True:
        with keyboard.Events() as events:
            for event in events:
                lasku += 1
                if lasku % 2 != 0: 
                    if event.key == keyboard.Key.left:
                        Positio -= move()
                        updateboard()
                    if event.key == keyboard.Key.right:
                        Positio += move()
                        updateboard()
                    if event.key == keyboard.Key.space:
                        count = 9
                        gameboard[hirvio_y].pop()
                        gameboard[hirvio_y].insert(hirvio_x, "*")
                        while count > hirvio_y:
                            count -= 1
                            try:
                                gameboard[count][Positio] = "^"
                            except:
                                 gameboard[count][-1] = "^"
                            time.sleep(0.5)
                            os.system('cls')
                            gameboard[9].pop(0)

                            if "A" not in gameboard[9]:
                                    gameboard[9].insert(Positio, "A")

                            else:
                                gameboard[9].insert(0, ".")
                                try:
                                    gameboard[count + 1][Positio] = "."
                                except:
                                     gameboard[count + 1][-1] = "."


                            for line in gameboard:
                                    print(' '.join(line))
                        end = time.perf_counter()
                        if end - start < aika:
                            if "*" in gameboard[hirvio_y]:
                                return "Häviö"
                            if "*" not in gameboard[hirvio_y]:
                                return "Voitto"
                        if end - start > aika:
                            return "Häviö"
                    else:
                         continue

            

         
        
    
  
