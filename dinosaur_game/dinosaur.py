import pygame

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

    def draw(self):
        """
        draws all things related to the dinosaur class
        """
        pygame.draw.rect(self.win, (0,0,255), (self.x, self.y, 70, 90), 1)