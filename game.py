# Implement the check winner function
# Implement the function that returns true or false whether we can
# move on a certain square (thus it stores the value of all moves)
# This can also help us with the gravity implementation

rows = 6
columns = 7

board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

def check_move(column):

    for row in reversed(range(rows)):
        if board[row][column] == 0:
            return row

    return -1

def make_move (row, column, player):
    if player == 1:
        board[row][column] = 1;
        return True
    elif player == 2:
        board[row][column] = 2;
        return True
    else:
        print("There was an error")
        return False