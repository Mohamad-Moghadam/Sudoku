"""



in this file we change the colours of the numbers to be more user friendly.


"""


def printing(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:  # Print horizontal separator every 3 rows
            print("-------------------------------------")
        for j in range(len(board[i])):
            cell = str(board[i][j]) if board[i][j] is not None else " "
            end_char = " │ " if (j + 1) % 3 == 0 and j != 8 else " "
            print(cell.center(3), end=end_char)
        print()


"""if board[i] == None:
            board[i] = " "
        if i % 9 == 8:
            print(f"{board[i]}")
        elif (
            i % 3 == 2
            and i != 8
            and i != 17
            and i != 26
            and i != 35
            and i != 44
            and i != 53
            and i != 62
            and i != 71
            and i != 80
        ):
            print(f"{board[i]}│", end="")
        else:
            print(f"{board[i]}", end="")
        if i == 26 or i == 53:
            print("___________")
"""
