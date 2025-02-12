def finish_game(board):
    Isgood1 = check_empty(board)
    Isgood2 = check_number_row_col(board)
    Isgood3 = check_3x3_square(board)
    if Isgood1 == False and Isgood2 == True and Isgood3 == True:
        return False