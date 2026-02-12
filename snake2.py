"""Snake game - v2
allowing user to quit display screen
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

quit_game = False
while not quit_game:  # loop to keep game running unless quit
    for event in pygame.event.get():  # receives all events from user inputs
        if event.type == pygame.QUIT:  # checks for 'quit' event
            quit_game = True

pygame.quit()
quit()