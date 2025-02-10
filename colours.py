"""



in this file we change the colours of the numbers to be more user friendly.




"""


def printing(board):
    for i in range(len(board)):
        if board[i] == None:
            board[i] = " "
        if (
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
            print(f"{board[i]}│")

        print()
