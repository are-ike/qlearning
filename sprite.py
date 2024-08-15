import pygame
class Sprite:

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect