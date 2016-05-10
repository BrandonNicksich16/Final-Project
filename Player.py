#Player.py
#Brandon Nicksich
#5/5/16

""" Create player classes for Main program """

import pygame
class Player1(pygame.sprite.Sprite):
    """ This class represents player 1 in the main game"""

    def __init__(self, x = 200, y = 200, hp = 1, baseSpeed = 1, baseAttack = 1):
        super(Player1,self).__init__()
        image = pygame.image.load("blueman.png").convert()
        image.set_colorkey((255, 255, 255))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x, y):
        """ Change the speed of the player """
        self.change_x += x

    def update(self):
        """ Find a new position for the player """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        while self.rect.x < 0:
            self.rect.x += 1
        while self.rect.x > 685:
            self.rect.x -= 1
        
        
        
        

pygame.init()
