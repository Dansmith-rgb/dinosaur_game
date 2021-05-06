import pygame
import os

class Cactus(object):

    def __init__(self, win, x):
        self.x = x
        self.y = 450
        self.win = win
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "sing_large_cac.png")), (84,84))
        self.passed = False

    def draw(self):
        
        self.win.blit(self.img, (self.x, self.y))

    def move(self):
        self.x -=15

    def collision(self, dinosaur, win):
        dinosaur_mask = dinosaur.get_mask()
        top_mask = pygame.mask.from_surface(self.img)
        
        top_offset = (self.x - dinosaur.x, self.y - round(dinosaur.y))
        
        #cactustop_offset = (self.x - cactus.x, self.top - round(cactus_mask.overlap(top_mask,top_offset)))
        t_point = dinosaur_mask.overlap(top_mask, top_offset)

        if t_point: 
            return True

        return False


    