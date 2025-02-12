"""

in this file, we decide where the player have set their numbers and whether it is possible to do so or not.

"""


def update(board, locat_list):
    row = locat_list[0]
    col = locat_list[1]
    num = locat_list[2]
    if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
        board[row - 1][col - 1] = num
    else:
        print("your input is out of range")
    return board






# test_case_1
# from pprint import pprint
# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 3, 0]]
# pprint(placement(board, [1, 1 , 1]))
