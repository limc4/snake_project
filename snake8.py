"""Snake game - v8
modify quitting method
created by Charlotte"""


import pygame
import random  # allows random to be accessed
pygame.init()

# set the size of the display screen
screen = pygame.display.set_mode((1000, 720))

# upload snake_icon image in caption
game_icon = pygame.image.load('snake_icon.png')

# display the icon
pygame.display.set_icon(game_icon)

# set the caption
pygame.display.set_caption("Snake game - by Charlotte Lim")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (72, 232, 94)
yellow = (245, 228, 39)

# fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.SysFont("freesanbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()  # sets the speed at which the snake moves

def message(msg, txt_colour):
    """this function displays messages"""
    txt = msg_font.render(msg, True, txt_colour)

    # centre rectangle: 1000/2 = 500 and 720/2 = 260
    text_box = txt.get_rect(center=(500, 360))  # render method applied
    # (True smoothes the edges of the font)

    screen.blit(txt, text_box)  # draws one image into another
    # .blit(displayed, image on which to display)

# Function to run main game loop
def game_loop():
    quit_game = False
    game_over = False

    # snake will be 20 x 20 pixels
    snake_x = 490  # centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 350  # centre point vertically is (720-20 snake height)/2 = 350

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds the value of changes in the y-coordinate

    # centre point for food is random
    food_x = round(random.randrange(20, 1000 - 20)/20) * 20
    food_y = round(random.randrange(20, 720 - 20)/20) * 20

    while not quit_game:  # loop to keep game running unless quit
        # give the option to quit or play again when they die
        while game_over:
            screen.fill(white)
            message("You died! Press 'Q' to Quit or 'A' to play Again",
                    black)
            pygame.display.update()

            # check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    elif event.key == pygame.K_a:
                        game_loop()  # restart the main game loop

        for event in pygame.event.get():  # receives all events from user inputs
            if event.type == pygame.QUIT:  # checks for 'quit' event
                game_over = True

            # checks to see which key the user has pressed using K_LEFT and K_Right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20

        # checks if snake has collided with the boundaries of the screen
        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # changes screen (surface) from default black to green

        # create rectangle for snake
        pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        # create circle for food
        pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
        pygame.display.update()

        # detect if snake touches food
        if snake_x == food_x - 10 and snake_y == food_y - 10:
            # set new random position for food if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

        clock.tick(7)  # sets the speed at which each iteration of the game loop
        # runs in frames per second (fps). In this case it is set to 7fps

    pygame.quit()
    quit()

# Main routine
game_loop()
