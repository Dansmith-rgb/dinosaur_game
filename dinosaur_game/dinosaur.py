import pygame
import os

class Dinosaur(object):

    def __init__(self, win, x, y):
        """
        initialize the dinosoar class

        :param win: screen
        :type win: pygame.surface
        :param x: x
        :type x: int
        :param y: y
        :type y: int
        """
        self.win = win
        self.x = x
        self.y = y
        self.gravity = 9.8
        self.vel = 0
        self.tick_count = 0
        self.height = self.y
        self.img = pygame.transform.scale(pygame.image.load("./imgs/dino-test-2.png"), (100,100))

    
   
    def get_mask(self):
        """
        gets the mask for the current image of the bird
        :return: None
        """
        return pygame.mask.from_surface(self.img)
        

    def draw(self):
        """
        draws all things related to the dinosaur class
        """
        
        self.win.blit(self.img, (self.x,self.y))
        #pygame.draw.rect(self.win, (0,0,255), (self.x, self.y, 70, 90), 1)