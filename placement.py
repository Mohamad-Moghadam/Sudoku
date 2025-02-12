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
    colours(board, row, column, inserted[2])
    return board


def colours(board, row, column, value):
    is_valid = check_number_row_col(board) and check_3x3_square(board)
    print("Conditions valid:", is_valid)
    if check_number_row_col(board) and check_3x3_square(board):
        board[row][column] = f"\033[92m{value}\033[0m"
    else:
        board[row][column] = f"\033[91m{value}\033[0m"
    return board

    """
    Here we place the inserted numbers.
    
    ---------------------------
    returns:
        updated board
    """
