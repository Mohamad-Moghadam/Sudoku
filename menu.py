"""

the menu is located in this file


"""
# test_case_1
# board = [[3, " ", 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 9, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 9]]

# test_case_2

# from random import randint

# a = randint(1, 9)
# b = randint(1, 9)
# c = randint(1, 9)

# board = [
#             [None, None, a, None, c, None, None, None, b],
#             [None, b, None, a, None, None, None, None, c],
#             [c, None, None, b, None, None, None, a, None],
#             [None, None, None, None, None, a, c, b, None],
#             [None, None, c, None, b, None, None, None, a],
#             [None, a, b, None, None, c, None, None, None],
#             [None, c, None, None, None, b, a, None, None],
#             [a, None, None, c, None, None, b, None, None],
#             [b, None, None, None, a, None, None, c, None],
#         ]


def print_mode(Arr):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end = " ")
            if Arr[i][j] == None:
                print(" ", end=" ")
            else:
                print(Arr[i][j], end = " ")
        print()

# print_mode(board)