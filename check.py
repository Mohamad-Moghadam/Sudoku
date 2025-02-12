
"""

in this file, it is checked whether the game has come to an end or not.



"""

"""

1. It checks if the board is empty

"""


def check_empty(Arr):
    for row in range(9):
        for col in range(9):
            if Arr[row][col] == None:
                return True
    else:
        return False


"""
2. Checks whether the entered number meets all the conditions or not
2.1: conditions: number in row, number in column
2.2: number in 3*3 square
"""


def check_number_row_col(Arr):
    for row in range(9):
        seen = set()
        for col in range(9):
            num = Arr[row][col]
            if num != None:
                if num in seen:
                    return False
                seen.add(num)

    for col in range(9):
        seen = set()
        for row in range(9):
            num = Arr[row][col]
            if num != None:
                if num in seen:
                    return False
                seen.add(num)

    return True


def check_3x3_square(Arr):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            unique_numbers = set()
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    if Arr[x][y] == None:
                        continue
                    if Arr[x][y] in unique_numbers:
                        return False
                    unique_numbers.add(Arr[x][y])
    return True


# test_case_1
# print(check_3x3_square([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 9, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 9]]))


# test_case_2
# print(check_3x3_square([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 9, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 0]]))


# test_case_3
# print(check_empty([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 0]]))


# test_case_3
# print(check_number_row_col([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 0]]))


# test_case_4
# print(check_number_row_col([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 3, 0]]))


# test_case_5
# print(check_number_row_col([[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 0]]))
