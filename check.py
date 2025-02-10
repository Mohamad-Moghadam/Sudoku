"""
1. check board is empty or no

in this file, it is checked whether the game has come to an end or not.



"""


def check_empty(row1):
    for row in range(9):
        for col in range(3):
            if row1[row][col] == None:
                return True
    else:
        return False
