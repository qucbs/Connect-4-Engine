# 1. Random AI -> make the AI choose a random move
# 2. Make the AI play any winning move and block the opponents winning move
# 3. Position evaluation
# 4. Min-max algorithm (small depth, around 2-3)
# 5. Alpha-Beta Pruning

import random
import game
import copy

rows = 6
columns = 7
possible_moves = [0,1,2,3,4,5,6]
ai = 2
human = 1


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
    
    while True:
        return random.choice(possible_moves)



