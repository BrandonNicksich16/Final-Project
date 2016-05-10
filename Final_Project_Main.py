#FinalProjectMain.py
#By: Brandon Nicksich
#5/2/16

""" This is where the main game code will be """

import pygame
from Player import Player1

pygame.init()

PI = 3.14592653
HEIGHT = 700
WIDTH = 400

#Define some colours
BLACK = (0, 0, 0)
WHITE = (255 , 255, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Opening and seting the window size

size = (HEIGHT , WIDTH)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Cool Pusheen!")

done = False

clock = pygame.time.Clock()
backgroundimage = pygame.image.load("final_project_background.jpg").convert()

player1sprite = Player1()
playerList = pygame.sprite.Group()
playerList.add(player1sprite)

player2sprite = pygame.image.load("redman.png")



while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1sprite.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player1sprite.changespeed(3, 0)
                

    screen.blit(backgroundimage, [0, 0])

    playerList.draw(screen)

    #screen.blit(player1sprite, [50, 50])
    screen.blit(player2sprite, [200, 200])
    

    

    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
