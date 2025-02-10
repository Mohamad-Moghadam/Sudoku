"""



in this file we change the colours of the numbers to be more user friendly.




"""


def printing(board):
    for i in range(81):
        if i == 0:
            for j in range(81):
                if j == 0 or j % 2 == 0:
                    print(
                        f"{board[0][0]}│{board[1][0]}│{board[2][0]}│{board[3][0]}│{board[4][0]}│{board[5][0]}│{board[6][0]}│{board[7][0]}│{board[8][0]}"
                    )
                    print("─" * 40)
                elif j % 2 == 1:
                    f"{board[0][0]}│{board[1][0]}│{board[2][0]}│{board[3][0]}│{board[4][0]}│{board[5][0]}│{board[6][0]}│{board[7][0]}│{board[8][0]}"
        print()
