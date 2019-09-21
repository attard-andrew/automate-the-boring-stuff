theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# The added for loop allows 9 turns to pass where the current state of the board is printed, then 
# the user is asked to enter their move, which would be one of the keys defined: top-L, mid-M etc.
# The captured move is then assigned at the entered key with theBoard[move] = turn.  Since the game 
# is turn-based, the final conditional modifies the turn variable so that it becomes O's turn if the 
# turn value is set to X, or X's turn if the turn variable is anything BUT X (which should always be 
# O in this case)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)