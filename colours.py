"""



in this file we change the colours of the numbers to be more user friendly.


"""

board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 9, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 9],
]


def printing(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                board[i][j] = " "
            elif j % 3 == 2:
                print(f"{board[i][j]}│", end="")
            else:
                print(f"{board[i][j]}", end="")
        if i % 3 == 2:
            print(f"\n___________")
        else:
            print()


printing(board)


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
