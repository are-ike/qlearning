import pygame
from mapping2 import roads
from sys import exit
from road import Road

screen_width = 800
screen_height = 600

map_width = 8000
map_height = 8000
class TestSimulation:
    def __init__(self, name=None, map=None, before_loop=None, during_loop=None):
        self.name = name
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.map = pygame.Surface((map_width,map_height))
        self.viewport_x = 0
        self.viewport_y = 0
        self.clock = pygame.time.Clock()
        self.during_loop = during_loop
        self.before_loop = before_loop
        self.cars = pygame.sprite.Group()
        self.roads = pygame.sprite.Group()
        self.agents = pygame.sprite.Group()
    
    def build_display(self):
        pygame.draw.rect(self.map,'#0d4b0d', pygame.Rect(pygame.Rect(0,0,map_width,map_height)))
        self.draw_buildings()
        self.draw_misc()
        #self.during_loop()
 
    def draw_buildings(self):
        pass

    def draw_misc(self):
        self.roads.draw(self.map)
        

    def run_simulation(self):
        i = 0
        for road in roads:
            self.roads.add(Road(coordinates=road['coordinates'], edges=road['edges'], color=i))
            i = 1 if i == 0 else 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.during_loop()
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.viewport_x -= 50
            if keys[pygame.K_RIGHT]:
                self.viewport_x += 50
            if keys[pygame.K_UP]:
                self.viewport_y -= 50
            if keys[pygame.K_DOWN]:
                self.viewport_y += 50
        
            self.build_display()

            # self.roads.draw(self.map)
            # self.cars.draw(self.map)
            # self.cars.update()
            # self.agents.draw(self.map)
            # #if loop:
            # self.agents.update()

            self.viewport_x = max(0, min(self.viewport_x, map_width - screen_width))
            self.viewport_y = max(0, min(self.viewport_y, map_height - screen_height))

            # Blit the portion of the map corresponding to the viewport onto the screen
            self.screen.blit(self.map, (0, 0), (self.viewport_x, self.viewport_y, screen_width, screen_height))

            pygame.display.update()
            self.clock.tick(60)

    def init_simulation(self):
        pygame.init()
        # pygame.display.set_caption(self.name) 
        # self.before_loop(self.roads, self.cars, self.agents)


sim = TestSimulation()
sim.init_simulation()
sim.run_simulation()