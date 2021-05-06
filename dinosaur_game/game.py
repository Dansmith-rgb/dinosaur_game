import pygame
import sys
from dinosaur import Dinosaur
from cactus import Cactus
import time
import os
import time
import random
import cv2

win = pygame.display.set_mode((1000,700))
pygame.init()
removed = []
#score = 0
class Game():
    
    global jumpCount, isJump
    
    def __init__(self):
        self.dinosaur = Dinosaur(win, 500-100, 450)
        self.bg_colour = win.fill((255,255,255))
        self.cactuses = [Cactus(win, 1000), Cactus(win, 1000)]
        self.bg = pygame.image.load("imgs/floor.png")
        self.timer = time.time()
        self.score = -1

    def main(self):
        isJump = False
        jumpCount = 10
        clock=pygame.time.Clock()
        score = 0
        while True:
            
            clock.tick(60)
            #gen cactuses
            if time.time() - self.timer >= random.randrange(1, 40):
                self.timer = time.time()
                self.cactuses.append(Cactus(win, 1000))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            keys = pygame.key.get_pressed()

            if not(isJump): # Checks is user is not jumping
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                # This is what will happen if we are jumping
                if jumpCount >= -10:
                    self.dinosaur.y -= (jumpCount * abs(jumpCount)/5) * 1 
                    jumpCount -= 0.5
                else: # This will execute if our jump is finished
                    jumpCount = 10
                    isJump = False
                    # Resetting our Variables 
            # del cactuses off of screen
            for cactus in self.cactuses:
                if cactus.x < -84:
                    self.cactuses.remove(cactus)
            # Check for collision between dinosaur and cactus     
            for cactus in self.cactuses:
                if cactus.collision(self.dinosaur, win):
                    return False
            self.draw()
            pygame.display.update()

    def draw(self):
        """
        draw all objects onto screen
        """
        STAT_FONT = pygame.font.SysFont("comicsans", 50)
        self.bg_colour = win.fill((255,255,255))
        win.blit(self.bg, (0,480))
        self.dinosaur.draw()
        score_label = STAT_FONT.render("Score: " + str(self.score),1,(0,0,0))
        win.blit(score_label, (700 - score_label.get_width() - 15, 10))
        
        for cactus in self.cactuses:
            cactus.draw()
            cactus.move()
            if not cactus.passed and cactus.x < self.dinosaur.x:
                print(self.score)
                self.score += 1
                cactus.passed = True
                
            
                
            
        
        

if __name__ == "__main__":
    Game().main()