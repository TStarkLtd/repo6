

# Tic Tac Toe

import random



def drawBoard(board, n):

    # This function prints out the board that it was passed.
    # "board" is a list of strings representing the board (ignore index 0)
    #print board
    for i in range(1,n+1):
        for j in range(1,n+1):
            #print n*(i-1)+j
            print '{:>4s}'.format(str(board[n*(i-1)+j])),
            if j%n:
                print(' |'),
            else:
                print(' ')
        if i%n:
            print('-'*(n*(n+2)))
    print ''


def inputPlayerName():

    # Lets the player type which name they want to be.
    # Returns a list with the player names.

    names = ['Player 1','Player 2']
	
    i = 0

    while (i < len(names)):

        print('Enter name for Player %s' %(i+1))

        names[i] = raw_input()
		
        i +=1

    print ''
    return names



def whoGoesFirst():

    # choose the player who goes first.
    return 1



def playAgain():

    # This function returns True if the player wants to play again, otherwise it returns False.

    print('Do you want to play again? (yes or no)')

    return raw_input().lower().startswith('y')



def makeMove(board, letter, move):

    board[move] = letter



def isWinner(bo, le, n):

    # Given a board and a player letter, this function returns True if that player has won.

# Horizontal
    for i in range(0,n):
        cnt = 0
        for j in range(0,n):
            if bo[i*n+1+j] == le :
                cnt +=1
        if cnt == n:
            return True
# Vertical
    for i in range(1,n+1):
        cnt = 0
        for j in range(0,n):
            if bo[i+j*n] == le :
                cnt +=1
        if cnt == n:
            return True
# Diagonal 1
    cnt = 0
    for i in range(0,n):
        if bo[i*(n+1)+1] == le :
            cnt +=1
        if cnt == n:
            return True
# Diagonal 2
    cnt = 0
    for i in range(0,n):
        if bo[i*(n-1)+n] == le :
            cnt +=1
        if cnt == n:
            return True

    return False


def isSpaceFree(board, move, n):

    # Return true if the passed move is free on the passed board.

    return board[move] in  range(1,n**2+1)



def getPlayerMove(board, n, ply, plyLetter):

    # Let the player type in their move.

    move = ''

    while move not in [str(x) for x in range(1,n**2+1)] or not isSpaceFree(board, int(move), n):

        print('%s What is your next move to place %s into: (1-%s)' % (ply, plyLetter, n**2))

        move = raw_input()

    return int(move)


def isBoardFull(board, n):

    # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, n**2+1):

        if isSpaceFree(board, i, n):

            return False

    return True




print ''
print('Welcome to Tic Tac Toe!')
print ''

N = 3

while True:

    dimen = ''
    while dimen not in [str(x) for x in range(1,10)]:
        print('What is your favourite dimension: (1-%s)' % (9))
        dimen = raw_input()
        N = int(dimen)

    # Reset the board
    theBoard = []
    theBoard.extend(range(0,N**2+1))

    player1, player2 = inputPlayerName()

    print ''

    playerLetter = ['X','O']

    turn = whoGoesFirst()

    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 1:

            # Player 1 turn.

            drawBoard(theBoard, N)

            move = getPlayerMove(theBoard, N, player1, playerLetter[turn-1])

            makeMove(theBoard, playerLetter[turn-1], move)

            drawBoard(theBoard, N)


            if isWinner(theBoard, playerLetter[turn-1], N):
                print('***************Winner***************')
                drawBoard(theBoard, N)

                print('Hooray! %s You have won the game!' % player1)

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard, N):

                    drawBoard(theBoard, N)

                    print('The game is a tie!')

                    break

                else:

                    turn = 2



        else:

            # Player 2 turn.

            move = getPlayerMove(theBoard, N, player2, playerLetter[turn-1])

            makeMove(theBoard, playerLetter[turn-1], move)



            if isWinner(theBoard, playerLetter[turn-1], N):
                print('***************Winner***************')
                drawBoard(theBoard, N)

                print('Hooray! %s You have won the game!' % player2)

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard, N):

                    drawBoard(theBoard, N)

                    print('The game is a tie!')

                    break

                else:

                    turn = 1



    if not playAgain():

        break