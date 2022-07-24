import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
BLACK = ( 0,   0,   0)
# load images
sun_img = pygame.image.load('D:\Downloads\sun.jpg')
bg_img = pygame.image.load('D:\Downloads/background1.jpg')



run = True
while run:

     screen.blit(bg_img, (0, 0))
     screen.blit(sun_img, (100, 100))
     pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()