import pygame

class Background(object, pygame.sprite.Sprite):

    def __init__(self,x, y):
        pass
        """
    def collide(self, bird, win):
        
        returns if a point is colliding with the pipe
        :param bird: Bird object
        :return: Bool
        
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False
"""