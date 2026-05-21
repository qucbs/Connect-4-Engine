import pygame
import sys
import game

pygame.init()

# Declaring Sizes
size = width, height = 700, 700
columns = 7
rows = 6
cell_size = 100
player = 1

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

while True:
    for row in range(rows):
        for col in range(columns):

            x = col * cell_size
            y = row * cell_size

            # Draw all the squares
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, white, rect, 2)

    # Now check for mouse input and quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Overide the previous text with a black rectangle
            pygame.draw.rect(screen, black, (0, 600, 700, 100))
            # Get the mouse position
            w , h = pygame.mouse.get_pos()

            print(f'Width {w} , Height {h}')
            w = (w // 100) * 100
            h = (h // 100) * 100

            # Making sure a move is not registered after clicking on the bottom bar
            if h == 600:
                continue

            for i in range(rows):
            # Checking if the move made is legal
                if (temp := game.check_move(w//100)) > -1:
                    h = temp*100
                    game.make_move(h//100, w//100, player)

                    # calc for circle
                    center = (w+50, h+50)
                    radius = (cell_size/2) - 8

                    print(f'Width {w} , Height {h}')

                    # Choosing the color
                    color = red if player == 2 else yellow

                    pygame.draw.circle(screen, color, center, radius)

                    if game.check_winner(h//100, w//100, player):
                        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                        pygame.draw.rect(screen, black, (0, 600, 700, 100))
                        screen.blit(player1_win, (180, 625)) if player == 1 else screen.blit(player2_win, (180, 625))
                        break

                    player = 3 - player

                    # turn indicator
                    screen.blit(player1_turn, (290, 625)) if player == 1 else screen.blit(player2_turn, (290, 625))

                    # Printing the board in the terminal for debugging
                    for i in range(6):
                        for j in range(7):
                            print(f' {game.board[i][j]} ', end = '')
                        print('')
                    break
            else:
                continue
    pygame.display.update()
