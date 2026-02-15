"""Snake game - v4
collision detection
created by Charlotte"""

import pygame
import time  # allows sleep to be accessed
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

# fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.SysFont("freesanbold.ttf", 30)

clock = pygame.time.Clock()  # sets the speed at which the snake moves

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 490  # centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # centre point vertically is (720-20 snake height)/2 = 350

snake_x_change = 0  # holds the value of changes in the x-coordinate
snake_y_change = 0  # holds the value of changes in the y-coordinate

while not quit_game:  # loop to keep game running unless quit
    for event in pygame.event.get():  # receives all events from user inputs
        if event.type == pygame.QUIT:  # checks for 'quit' event
            quit_game = True

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
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)  # changes screen (surface) from default black to green

    # create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)  # sets the speed at which each iteration of the game loop
    # runs in frames per second (fps). In this case it is set to 5fps

pygame.quit()
quit()