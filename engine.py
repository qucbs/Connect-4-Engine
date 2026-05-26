# 1. Random AI -> make the AI choose a random move
# 2. Make the AI play any winning move and block the opponents winning move
# 3. Position evaluation
# 4. Min-max algorithm (small depth, around 2-3)
# 5. Alpha-Beta Pruning

import game
import copy
import helpers

rows = 6
columns = 7
possible_moves = [0,1,2,3,4,5,6]
ai = 2
human = 1
center_column = columns // 2

def move(board):
    for col in range(columns):
        temp_board = copy.deepcopy(board)

        if (row:= game.check_move(temp_board, col)) > -1:
            game.make_move(temp_board, row, col, ai)
            if game.check_winner(temp_board, row, col, ai):
                return col

    for col in range(columns):
        temp_board = copy.deepcopy(board)

        if (row:= game.check_move(temp_board, col)) > -1:
            game.make_move(temp_board, row, col, human)
            if game.check_winner(temp_board, row, col, human):
                return col
    
    best_score = -999
    best_move = None

    for col in range(columns):
        temp_board = copy.deepcopy(board)

        row = game.check_move(temp_board, col)
        if row == -1:
            continue
        
        # Make the move
        game.make_move(temp_board, row, col, ai)

        # Then check the eval of the board after we make the move
        eval = evaluate(temp_board)

        if eval >= best_score:
            best_score = eval
            best_move = col

    return best_move


def evaluate(board):
    evaluation = 0

    # Horizontal Window
    for row in range(rows):
        for col in range(columns - 3):

                window = [
                    board[row][col],
                    board[row][col+1],
                    board[row][col+2],
                    board[row][col+3]
                ]

                evaluation += helpers.evaluate_window(window)

    # Vertical Window 
    for row in range(rows - 3):
        for col in range(columns):

            window = [
                board[row][col],
                board[row+1][col],
                board[row+2][col],
                board[row+3][col]
            ]

            evaluation += helpers.evaluate_window(window)
    
    # Negative Diagonal Window
    for row in range(rows - 3):
        for col in range(columns - 3):

            window = [
                board[row][col],
                board[row+1][col+1],
                board[row+2][col+2],
                board[row+3][col+3]
            ]
        
            evaluation += helpers.evaluate_window(window)

# Positive Diagonal Window
    for row in range(rows - 3):
        for col in range(3, columns):

            window = [
                board[row][col],
                board[row+1][col-1],
                board[row+2][col-2],
                board[row+3][col-3]
            ]

            evaluation += helpers.evaluate_window(window)



    for row in range(rows):
        for col in range(columns):

            # Distance of a column from the center column
            distance = abs(col - center_column)

            if board[row][col] == ai:
                evaluation += 3-distance
            elif board[row][col] == human:
                evaluation -= 3-distance

    return evaluation



