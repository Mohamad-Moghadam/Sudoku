"""



in this file we change the colours of the numbers to be more user friendly.




"""


def printing(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if j == 0:
                print("┌")
            elif j == 81:
                print("┐")
            else:
                print("─")
