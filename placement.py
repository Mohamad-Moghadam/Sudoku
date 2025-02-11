"""

in this file, we decide where the player have set their numbers and whether it is possible to do so or not.

"""


def update(board, inserted):
    row = inserted[0]
    column = inserted[1]
    board[row][column] = inserted[2]
    return board
