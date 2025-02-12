"""
the menu is located in this file
"""

from check import *
from placement import *
from colours import *
import json
from random import randint


def menu():
    print("What is your name? ")
    name = input()
    print(f"\nWelcome {name}. \n1. Start game \n2. Exit game\n ")
    choice = int(input())

    if choice == 1:
        print(
            f"\nwhich mode do you wanna play? \n1. Easy \n2. Medium \n3. Hard \n4. Exit\n"
        )
        game_mode = int(input())
        if game_mode == 1:
            game(1)
        elif game_mode == 2:
            game(2)
        elif game_mode == 3:
            game(3)
        elif game_mode == 4:
            return
    elif choice == 2:
        return


"""
Here is the menu of the game and where the first sheet is generated.


returns
--------
int:
    passes the level of difficulty to the game function.
    """


def game(difficulty):

    if difficulty == 1:
        a = randint(1, 9)
        b = randint(1, 9)
        c = randint(1, 9)
        while b == a or b == c or a == c:
            b = randint(1, 9)
            c = randint(1, 9)
        board = [
            [None, None, a, None, c, None, None, None, b],
            [None, b, None, a, None, None, None, None, c],
            [c, None, None, b, None, None, None, a, None],
            [None, None, None, None, None, a, c, b, None],
            [None, None, c, None, b, None, None, None, a],
            [None, a, b, None, None, c, None, None, None],
            [None, c, None, None, None, b, a, None, None],
            [a, None, None, c, None, None, b, None, None],
            [b, None, None, None, a, None, None, c, None],
        ]
        print(f"\n")
        printing(board, a, b, c)
        while True:
            print(
                f"please enter the number of row, column and the number you want to place:\n"
            )
            place = list(map(int, input().split()))
            place[0] = place[0] - 1
            place[1] = place[1] - 1
            board = update(board, place)
            print(f"\n")
            printing(board, a, b, c)
            check_number_row_col(board)
            check_3x3_square(board)

    elif difficulty == 2:
        a = randint(1, 9)
        b = randint(1, 9)
        while b == a:
            b = randint(1, 9)
        board = board = [
            [None, None, a, None, None, None, None, None, b],
            [None, b, None, a, None, None, None, None, None],
            [None, None, None, b, None, None, None, a, None],
            [None, None, None, None, None, a, None, b, None],
            [None, None, None, None, b, None, None, None, a],
            [None, a, b, None, None, None, None, None, None],
            [None, None, None, None, None, b, a, None, None],
            [a, None, None, None, None, None, b, None, None],
            [b, None, None, None, a, None, None, None, None],
        ]
        print(f"\n")
        printing(board, a, b, 0)
        while True:
            print(
                f"please enter the number of row, column and the number you want to place:\n"
            )
            place = list(map(int, input().split()))
            place[0] = place[0] - 1
            place[1] = place[1] - 1
            board = update(board, place)
            print(f"\n")
            printing(board, a, b, 0)
            check_number_row_col(board)
            check_3x3_square(board)

    elif difficulty == 3:
        a = randint(1, 9)

        board = board = [
            [None, None, a, None, None, None, None, None, None],
            [None, None, None, a, None, None, None, None, None],
            [None, None, None, None, None, None, None, a, None],
            [None, None, None, None, None, a, None, None, None],
            [None, None, None, None, None, None, None, None, a],
            [None, a, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, a, None, None],
            [a, None, None, None, None, None, None, None, None],
            [None, None, None, None, a, None, None, None, None],
        ]
        print(f"\n")
        printing(board, a, 0, 0)
        while True:
            print(
                f"please enter the number of row, column and the number you want to place:\n"
            )
            place = list(map(int, input().split()))
            place[0] = place[0] - 1
            place[1] = place[1] - 1
            board = update(board, place)
            print(f"\n")
            printing(board, a, 0, 0)
            check_number_row_col(board)
            check_3x3_square(board)


"""

here is the start of the game.
depending on the number, it gives the list of the sheet.

---------------
parameters:
difficulty (int): The level of difficulty chosen in menu function.

---------------
three lists:
    each list belongs to a row.
    """

menu()
