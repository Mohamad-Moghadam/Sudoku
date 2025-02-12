"""

in this file, we decide where the player have set their numbers and whether it is possible to do so or not.

"""

from check import *


def update(board, inserted, a, b, c):
    row = inserted[0]
    column = inserted[1]
    if board[row][column] == a or board[row][column] == b or board[row][column] == c:
        print("You can't change the initial sheet!")
        return board
    board[row][column] = inserted[2]
    colours(board, inserted)
    return board


def colours(board, inserted):
    if check_number_row_col(board) and check_3x3_square(board):
        inserted[2] = f"\033[92m{inserted[2]}\033[0m"
    else:
        inserted[2] = f"\033[91m{inserted[2]}\033[0m"
    return board

    """
    Here we place the inserted numbers.
    
    ---------------------------
    returns:
        updated board
    """
