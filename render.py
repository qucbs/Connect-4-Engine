import pygame
import sys
import game
import engine

pygame.init()

# Declaring Sizes
size = width, height = 700, 700
columns = 7
rows = 6
cell_size = 100
current_player = 1
human = 1
ai = 2
game_over = False
winner = 0

# Declaring Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255,255,0)

# Screen
screen = pygame.display.set_mode(size)

# Font and text
font = pygame.font.SysFont("Arial", 36)
player1_turn = font.render("Player 1", False, yellow)
player2_turn = font.render("Player 2", False, red)
player1_win = font.render("Player 1 is the Winner", False, yellow)
player2_win = font.render("Player 2 is the winner", False, red)
tie = font.render("Tie!!", False, white)


screen.blit(player1_turn, (290, 625))

running = True
while running:
    if game.check_tie():
        game_over = True



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


# If the current player is human

        if current_player == human and event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            #  Get the mouse position
            w , h = pygame.mouse.get_pos()

            print(f'Width {w} , Height {h}')
            col = (w // 100)
            row = (h // 100) * 100
            print(f'Width {col} , Height {row}')

            # Making sure a move is not registered after clicking on the bottom bar
            if row == 600:
                continue

            # Check if the move made is legal
            if (row := game.check_move(col)) > -1:

                game.make_move(row, col, human)

                if game.check_winner(row, col, human):
                    winner = human
                    game_over = True
                else:
                    current_player = ai

# If the current player is AI

    if current_player == ai and not game_over:
        col = engine.move()
        if (row := game.check_move(col)) > -1:
            
            game.make_move(row, col, ai)

            if game.check_winner(row, col, ai):
                winner = ai
                game_over = True
            else:
                current_player = human



    # All rendering logic
    # Making the screen black before each render

    screen.fill(black)

    # Rendering the rectangles
    for row in range(rows):
        for col in range(columns):

            x = col * cell_size
            y = row * cell_size

            # Draw all the rectangles
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, white, rect, 2)

    # Drawing the pieces
    board = game.board

    for row in range(rows):
        for column in range(columns):

            value = board[row][column]

            center = (column*100 + 50, row*100 + 50)
            radius = (cell_size/2) - 8

            if value == 2: color = red
            elif value == 1: color = yellow
            else: continue

            pygame.draw.circle(screen, color, center, radius)


    # Rendering the text

    if game_over:
        if winner == human:
            screen.blit(player1_win, (180, 625))
        elif winner == ai:
            screen.blit(player2_win, (180, 625))
        else:
            screen.blit(tie, (315, 625))


    else:
        if current_player == human:
            screen.blit(player1_turn, (290, 625))
        else:
            screen.blit(player2_turn, (290, 625))


    pygame.display.update()
