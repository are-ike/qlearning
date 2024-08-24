import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, coordinates, from_node, to_node, direction):
        pygame.sprite.Sprite.__init__(self)
        self.coordinates = coordinates
        self.image = pygame.Surface((coordinates[2], coordinates[3]))
        self.rect = self.image.get_rect()
        self.from_node = from_node
        self.to_node = to_node
        self.rect.topleft = (coordinates[0], coordinates[1])
        self.image.fill('#232323')

    def draw(self, map):
        rect = pygame.draw.rect(map,'#232323', pygame.Rect(pygame.Rect(self.coordinates)))
        self.rect = rect
        
        

   