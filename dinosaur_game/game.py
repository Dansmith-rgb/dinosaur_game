import pygame
import sys
from dinosaur import Dinosaur

win = pygame.display.set_mode((1200,700))
pygame.init()
class Game():

    def __init__(self):
        self.dinosaur = Dinosaur(win, 20, 10)
        self.bg = win.fill((255,0,0))
        self.cactuses = None

    def main(self):
        clock=pygame.time.Clock()
        while True:
            
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys=pygame.key.get_pressed()
            self.draw()
            pygame.display.update()

    def draw(self):
        """
        draw all objects onto screen
        """
        self.dinosaur.draw()

if __name__ == "__main__":
    Game().main()