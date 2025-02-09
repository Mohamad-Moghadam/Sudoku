"""

the menu is located in this file


"""

import json
from random import randint


def menu():
    while True:
        print("What is your name? ")
        name = input()

        print(f"\nWelcome {name}. \n1. Start game \n2. Statistics \n3. Exit game\n ")
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
                # choice == 2:
                # with open("C:\Users\USER\Desktop\kelassor\3rd week\Sudoku\statistics.json" , encoding='utf-8') as file:
                data = json.load(file)
                pprint(data)
                return
        elif choice == 3:
            return


"""
Here is the menu of the game and where the first sheet is generated.


returns
--------
json:
    shows the content of the json file
    
int:
    passes the level of difficulty to the game function.
    """


def game(difficulty):

    if difficulty == 1:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 10)
        while b == a or b == c or a == c:
            b = randint(1, 10)
            c = randint(1, 10)
        row1 = [
            [None, None, a],
            [None, c, None],
            [None, None, b],
            [None, b, None],
            [a, None, None],
            [None, None, c],
            [c, None, None],
            [b, None, None],
            [None, a, None],
        ]

        row2 = [
            [None, None, None],
            [None, None, a],
            [c, b, None],
            [None, None, c],
            [None, b, None],
            [None, None, a],
            [None, a, b],
            [None, None, c],
            [None, None, None],
        ]

        row3 = [
            [None, c, None],
            [None, None, b],
            [a, None, None],
            [a, None, None],
            [c, None, None],
            [b, None, None],
            [b, None, None],
            [None, a, None],
            [None, c, None],
        ]

        return row1, row2, row3

    elif difficulty == 2:
        a = randint(1, 10)
        b = randint(1, 10)
        while b == a:
            b = randint(1, 10)
        row1 = [
            [None, None, a],
            [None, None, None],
            [None, None, b],
            [None, b, None],
            [a, None, None],
            [None, None, None],
            [None, None, None],
            [b, None, None],
            [None, a, None],
        ]

        row2 = [
            [None, None, None],
            [None, None, a],
            [None, b, None],
            [None, None, None],
            [None, b, None],
            [None, None, a],
            [None, a, b],
            [None, None, None],
            [None, None, None],
        ]

        row3 = [
            [None, None, None],
            [None, None, b],
            [a, None, None],
            [a, None, None],
            [None, None, None],
            [b, None, None],
            [b, None, None],
            [None, a, None],
            [None, None, None],
        ]

        return row1, row2, row3

    elif difficulty == 3:
        a = randint(1, 10)

        row1 = [
            [None, None, a],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [a, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, a, None],
        ]

        row2 = [
            [None, None, None],
            [None, None, a],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, a],
            [None, a, None],
            [None, None, None],
            [None, None, None],
        ]

        row3 = [
            [None, None, None],
            [None, None, None],
            [a, None, None],
            [a, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, a, None],
            [None, None, None],
        ]

        return row1, row2, row3


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
