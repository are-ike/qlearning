import pygame

class Road:
    def __init__(self, coordinates, edges):
        self.coordinates = coordinates
        self.edges = edges
        self.rect = None

    def draw(self, map):
        rect = pygame.draw.rect(map,'#232323', pygame.Rect(pygame.Rect(self.coordinates)))
        self.rect = rect

   