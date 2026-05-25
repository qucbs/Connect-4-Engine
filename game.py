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

def check_move(panel, column):

    for row in reversed(range(rows)):
        if panel[row][column] == 0:
            return row

    return -1

def make_move(panel, row, column, player):
    if player == 1:
        panel[row][column] = 1;
        return True
    elif player == 2:
        panel[row][column] = 2;
        return True
    else:
        print("There was an error")
        return False


def check_winner(panel, row, column, player):
    # Vertical Check
    vertical = 0
    for i in range(rows):
        if panel[i][column] == player:
            vertical += 1
        else: vertical = 0

        if vertical > 3: return True

    # Horizontal Check
    horizontal = 0
    for j in range(columns):
        if panel[row][j] == player:
            horizontal += 1
        else: horizontal = 0

        if horizontal > 3: return True

    # For \ Diagonal (1 so that we count the starting piece)
    diagonal_1 = 1

    # Using different variables so that I can edit them
    r = row - 1
    c = column - 1
    while (r >= 0 and c >= 0):
        if panel[r][c] == player:
            diagonal_1 += 1
        else: break
        r -= 1
        c -= 1

# Plus one so that I do not count the starting piece again
    r = row + 1
    c = column + 1
    while (r < rows and c < columns):
        if panel[r][c] == player:
            diagonal_1 += 1
        else: break
        r += 1
        c += 1
    if diagonal_1 > 3: return True

    # For / Diagonal (1 so that we count the starting piece)
    diagnoal_2 = 1

    # to not count the starting piece
    r = row - 1
    c = column + 1
    while (r >= 0 and c < columns):
        if panel[r][c] == player:
            diagnoal_2 += 1
        else: break
        r -= 1
        c += 1
    
    r = row + 1
    c = column - 1
    while (r < rows and c >= 0):
        if panel[r][c] == player:
            diagnoal_2 += 1
        else: break
        r += 1
        c -= 1
    if diagnoal_2 > 3: return True

    # Return False if nobody won
    return False

def check_tie(panel):
    for i in range(columns):
        if panel[0][i] == 0:
            return False
    return True
