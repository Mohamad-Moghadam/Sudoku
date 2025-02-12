"""

in this file, we decide where the player have set their numbers and whether it is possible to do so or not.

"""

from check import *


def update(board, inserted):
    row = inserted[0]
    column = inserted[1]
    board[row][column] = inserted[2]
    if check_number_row_col(board) and check_3x3_square(board):
        inserted[2] = f"\033[92m{inserted[2]}\033[0m"
    return board

    """
    Here we place the inserted numbers.
    
    ---------------------------
    returns:
        updated board
    """
