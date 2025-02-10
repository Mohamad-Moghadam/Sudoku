"""

the menu is located in this file


"""

# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 9, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 9]]



def print_mode(Arr):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end = " ")
            print(Arr[i][j], end = " ")
        print()

# print_mode(board)