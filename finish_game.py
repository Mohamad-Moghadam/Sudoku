from check import *


def finish_game(board):
    Is_good1 = check_empty(board)
    Is_good2 = check_number_row_col(board)
    Is_good3 = check_3x3_square(board)
    if Is_good1 == False and Is_good2 == True and Is_good3 == True:
        print("The game is finished! well done!")
        return False
