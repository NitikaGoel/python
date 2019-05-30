import random
print('Welcome to TIC TAC TOE PROGRAM')

gameOn = True

def printBoard(board):
    print(board[7]+' '+board[8]+' '+board[9])
    print(board[4]+' '+board[5]+' '+board[6])
    print(board[1]+' '+board[2]+' '+board[3])
    

def flipcoin():
    if random.randint(0,1) == 0:
        return 'player 2'
    else:
        return 'player 1'

def chooseMarkerForEachPlayer(player):
    if player == 'player 1':
        marker = input('Player 1 choose your marker X or O : ').upper()
        if marker == 'X':
            print('Player 1 has X and Player 2 has O as marker')
            return ('X','O')
        else:
            print('Player 1 has O and Player 2 has X as marker')
            return ('O','X')
    else:
        marker = input('Player 2 choose your marker X or O : ').upper()
        if marker == 'X':
            print('Player 1 has O and Player 2 has X as marker')
            return ('O','X')
        else:
            print('Player 1 has X and Player 2 has O as marker')
            return ('X','O')

def checkifwon(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def asktocontinue():
    return input('You want to continue Y/N : ').upper()

def checkifboardisEmpty(board):
    return (board[2]=='*'or board[1] =='*'or
    board[3]=='*'or board[4] =='*'or
    board[5]=='*'or board[6] =='*'or
    board[7]=='*'or board[8] =='*' or
    board[9]=='*')

def checkifValidInput(val):
    if val in range(1,10):
        return True
    else:
        print('You did not enter no between 1 to 9. Exiting the game')
        return False

def takeUsersInput(board,player,marker):
    while True:
        retry = 1
        if player == 'player 1':
            val = int(input('Player 1 enter your number where u want to place your marker between 1 to 9: '))
            isValid = checkifValidInput(val)
            if not isValid:
                return 'gameover'
            else:
                board[val] = marker[0]
                printBoard(board)
                won = checkifwon(board,marker[0])
                if won :
                    print ('Player 1 you win the game')
                    return 'gameover'
                else:
                    empty = checkifboardisEmpty(board)
                    if empty:
                        player = 'player 2'
                        continue
                    else:
                        print('Board is full and no one won')
                        return 'gameover'
        if player == 'player 2':   
            val = int(input('Player 2 enter your number where u want to place your marker between 1 to 9 : '))
            isValid = checkifValidInput(val)
            if not isValid:
                return 'gameover'
            else:
                board[val] = marker[1]
                printBoard(board)
                won = checkifwon(board,marker[1])
                if won :
                    print ('Player 2 you win the game')
                    return 'gameover'
                else:
                    empty = checkifboardisEmpty(board)
                    if empty:
                        player = 'player 1'
                        continue
                    else:
                        print('Board is full and no one won :-|')
                        return 'gameover'


while gameOn:
    board = ['#','*','*','*','*','*','*','*','*','*']
    printBoard(board)
    # if coin flips 1, player 1 will go, otherwise player2
    print("Fliping the coin to see who goes first")
    player = flipcoin()
    print('{} goes first'.format(player))
    marker = chooseMarkerForEachPlayer(player)
    gameover = takeUsersInput(board,player,marker)
    if gameover:
        answer = asktocontinue()
        if answer == 'Y':
            continue
        else:
            gameOn = False
    
        
            
            