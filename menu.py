"""

the menu is located in this file


"""

import json
import pprint
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
            game_mode = input()
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


def game(difficulty):

    if difficulty == 1:
        for _ in range(1):
            n = randint(1, 8)
            row1 = [[n, None, n + 1], [None, n + 2, None], [None, None, None]]
            row2 = [[None, n + 2, None], [n, None, None], [n + 1, None, None]]
            row3 = [[None, n, None, None], [n + 2, None, None], [None, None, n + 1]]
        print(row1, row2)


menu()
