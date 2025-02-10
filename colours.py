"""



in this file we change the colours of the numbers to be more user friendly.




"""


def printing(board):
    for i in range(81):
        for j in range(82):
            if j == 0:
                print("┌", end="")
            elif j == 80:
                print("┐")
            else:
                print("─", end="")
