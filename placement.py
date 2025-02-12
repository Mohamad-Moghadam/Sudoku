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
    if inserted[2] == a or inserted[2] == b or inserted[2] == c:
        print(
            "Let's see... that one is totally wrong! Don't tell anyone that I helped u though😉"
        )
        return board
    board[row][column] = inserted[2]
    return board

    """
    Here we place the inserted numbers.
    
    ---------------------------
    returns:
        updated board
    """
