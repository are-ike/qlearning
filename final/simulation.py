import pygame
from mapping import nodes
from sys import exit

screen_width = 1200
screen_height = 800

map_width = 20000
map_height = 20000
class TestSimulation:
    def __init__(self, name, map, before_loop, during_loop):
        self.name = name
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.map = map
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
        self.during_loop()
 
    def draw_buildings(self):
        for node in nodes:
            pos = node["position"]
            size = node["size"]
            pygame.draw.rect(self.map, '#5c4033', (pos[0], pos[1], size[0], size[1]), border_radius=10)
            pygame.draw.rect(self.map, node["color"], (pos[0] + 10, pos[1] + 10, size[0] - 20, size[1] - 20), border_radius=5)
         
    def draw_misc(self):
        #dli roundabount 1
        pygame.draw.rect(self.map,'#232323', pygame.Rect(pygame.Rect(710,140,220,200)))
        pygame.draw.circle(self.map,'#232323', (850,270), 30 + 100)
        pygame.draw.circle(self.map,'#5c4033', (850,270), 30)
        pygame.draw.rect(self.map,'#232323', pygame.Rect(pygame.Rect(910,240,120,100)))

        pygame.draw.circle(self.map,'#232323', (850,270), 30 + 100)
        pygame.draw.circle(self.map,'#5c4033', (850,270), 30)

    def run_simulation(self):

        #if len(self.cars) == 0:
            # pygame.init()
            # pygame.display.set_caption(self.name) 
            # cars = pygame.sprite.Group()
            # roads = pygame.sprite.Group()
            # agents = pygame.sprite.Group()
            #self.before_loop(self.roads, self.cars, self.agents)
            #print(agent.start, agent.is_moving)
        
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

            self.roads.draw(self.map)
            self.cars.draw(self.map)
            self.cars.update()
            self.agents.draw(self.map)
            #if loop:
            self.agents.update()

            # agent = None
            for agent_obj in self.agents:
                agent = agent_obj
            #print('run')
            #print(agent.get_is_moving() , agent.get_is_start())
            #if not agent.get_is_moving() and loop: break

            # camera_x = agent.rect.centerx - screen_width // 2
            # camera_y = agent.rect.centery - screen_height // 2

            # # Ensure the camera stays within map boundaries
            # camera_x = max(0, min(camera_x, map_width - screen_width))
            # camera_y = max(0, min(camera_y, map_height - screen_height))

            # # Blit the portion of the map that the camera can see onto the screen
            # self.screen.blit(self.map, (0, 0), pygame.Rect(camera_x, camera_y, screen_width, screen_height))

            self.viewport_x = max(0, min(self.viewport_x, map_width - screen_width))
            self.viewport_y = max(0, min(self.viewport_y, map_height - screen_height))

            # Blit the portion of the map corresponding to the viewport onto the screen
            self.screen.blit(self.map, (0, 0), (self.viewport_x, self.viewport_y, screen_width, screen_height))

            pygame.display.update()
            self.clock.tick(60)

            #if not agent.get_is_moving(): return
            # if not loop or not agent.get_is_moving(): break

    def init_simulation(self):
        pygame.init()
        pygame.display.set_caption(self.name) 
        self.before_loop(self.roads, self.cars, self.agents)
