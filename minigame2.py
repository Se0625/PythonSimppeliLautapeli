import random
def userturn():

    empty_cell = False
    while not empty_cell:
        coords = input("Anna kaksi koordinaattia 1-3 pilkulla eroteltuna: ")
        user_x, user_y = coords.split(',')
        user_x = int(user_x)
        user_y = int(user_y)

        if board[user_y - 1][user_x - 1] == '.':
            board[user_y - 1][user_x - 1] = 'X'
            empty_cell = True

def botturn():

    empty_cell = False
    while not empty_cell:
        bot_x = random.randint(0, 2)
        bot_y = random.randint(0, 2)

        if board[bot_y][bot_x] == '.':
            board[bot_y][bot_x] = 'O'
            empty_cell = True

def printboard():
        for y in range(3):
            print("".join(board[y]))
        print()

def Game():
    global board
    board = [
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.']
]
    turn = 0
    for turn in range(9):
        userturn()
        botturn()
        printboard()
        turn += 1
        #Voitto logiikka pelaajalle
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' or board[0][2] == "X" and board[1][2] == "X" and board [2][2] == 'X':
            print("Nice")
            return "Voitto"
        #Voitto logiikka botille
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' or board[0][2] == "O" and board[1][2] == "O" and board [2][2] == 'O':
            print("Ei niin Nice")
            return "Häviö"

        
        if turn >= 9:
            print("Tasapeli")
            return "Häviö"

            
