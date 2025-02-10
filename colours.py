"""



in this file we change the colours of the numbers to be more user friendly.




"""

from menu import *


def colours(board):
    for i in range(len(board)):
        if i == 0:
            print("┌")
        elif i == 81:
            print("┐")
        else:
            print("─")
