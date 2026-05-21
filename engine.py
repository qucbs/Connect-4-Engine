# 1. Random AI -> make the AI choose a random move
# 2. Make the AI play any winning move and block the opponents winning move
# 3. Position evaluation
# 4. Min-max algorithm (small depth, around 2-3)
# 5. Alpha-Beta Pruning

import random
import game

rows = 6
columns = 7

possible_moves = [0,1,2,3,4,5,6]
def move():
    while True:
        return random.choice(possible_moves)


