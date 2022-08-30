from enum import Enum

DIMENSION_BOARD = 8
 
class Alpha(Enum): # enum class to have columns as numbers when iterating
    a, b, c, d, e, f, g, h = 0, 1, 2, 3, 4, 5, 6, 7

ways = 64 # total ways without removing anything is 64 ways
board = [[0] * DIMENSION_BOARD for i in range(DIMENSION_BOARD)] #create board and initialize all by 0

rook = input()
knight = input()

board[int(rook[1])-1][Alpha[rook[0]].value] = 1 # place in the location desired the rook by placing 1 instead of 0
# rook[1] - 1 is used because it moves from 1 to 8 not from 0 to 7 which is what we need for index

for i in range(DIMENSION_BOARD): # place 'r' in any location the rook can attack
    if not board[int(rook[1])-1][i] == 1:
        board[int(rook[1])-1][i] = 'r'

for i in range(DIMENSION_BOARD): # place 'r' in any location the rook can attack
    if not board[i][Alpha[rook[0]].value] == 1:
        board[i][Alpha[rook[0]].value] = 'r'

board[int(knight[1])-1][Alpha[knight[0]].value] = 1 # place in the location desired the rook by placing 1 instead of 0
# rook[1] - 1 is used because it moves from 1 to 8 not from 0 to 7 which is what we need for index

for i in range(DIMENSION_BOARD):
    for j in range(DIMENSION_BOARD):
        if board[i][j] == 1 or board[i][j] == 'r': # if location is filled or rook can attack
            ways -= 1
        elif (i-1 >= 0 and j-2 >= 0) and not board[i-1][j-2] == 'r' and board[i-1][j-2] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i-1 >= 0 and j+2 < DIMENSION_BOARD) and not board[i-1][j+2] == 'r' and board[i-1][j+2] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i+1 < DIMENSION_BOARD and j-2 >= 0) and not board[i+1][j-2] == 'r' and board[i+1][j-2] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i+1 < DIMENSION_BOARD and j+2 < DIMENSION_BOARD) and not board[i+1][j+2] == 'r' and board[i+1][j+2] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i-2 >= 0 and j-1 >= 0) and not board[i-2][j-1] == 'r' and board[i-2][j-1] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i-2 >= 0 and j+1 < DIMENSION_BOARD) and not board[i-2][j+1] == 'r' and board[i-2][j+1] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i+2 < DIMENSION_BOARD and j-1 >= 0) and not board[i+2][j-1] == 'r' and board[i+2][j-1] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1
        elif (i+2 < DIMENSION_BOARD and j+1 < DIMENSION_BOARD) and not board[i+2][j+1] == 'r' and board[i+2][j+1] == 1: # if knight can attack and it is not already counted among rook attacks
            ways -= 1

print(ways)