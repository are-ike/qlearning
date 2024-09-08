import pygame
from mapping2 import roads
from sys import exit
from road import Road
from car import Car
from agent_car import Agent
import cProfile

screen_width = 800
screen_height = 600

map_width = 6000
map_height = 6000
class TestSimulation:
    def __init__(self, traffic, get_traffic=None, set_traffic=None, name='Q-learning Agent', before_loop=None, during_loop=None):
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
        self.traffic = traffic
        self.agent = None
        self.get_traffic = get_traffic
        self.set_traffic = set_traffic
    
    def build_display(self):
        pygame.draw.rect(self.map,'#0d4b0d', pygame.Rect(pygame.Rect(0,0,map_width,map_height)))
        self.draw_buildings()
        self.draw_misc()
        #self.during_loop()
 
    def draw_buildings(self):
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(40,2180,40,240)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(400,2050,400,100)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(1220,2020,200,100)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(1770,2020,200,100)))

    def draw_misc(self):pass
        #self.roads.draw(self.map)
    
    def texts(self):
        font = pygame.font.Font(None, 24)

        text = font.render("UNILAG First Gate", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = (40, 2150)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (120, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (120, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (820, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (820, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (1620, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (1620, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (2320, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (2320, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (3020, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (3020, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (3520, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (3520, 2345)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (4120, 2240)
        self.map.blit(text, text_rect)

        text = font.render("University Road", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (4120, 2345)
        self.map.blit(text, text_rect)

        text = font.render("Faculty of Environmental Science", True, '#000000')
        text_rect = text.get_rect()
        text_rect.topleft = (420, 2100)
        self.map.blit(text, text_rect)

        text = font.render("Sports Center Parking Lot", True, '#ffffff')
        text_rect = text.get_rect()
        text_rect.topleft = (1000, 450)
        self.map.blit(text, text_rect)

        text = font.render("St Thomas More", True, '#000000')
        text_rect = text.get_rect()
        text_rect.topleft = (1240,2040)
        self.map.blit(text, text_rect)

        text = font.render("Chapel of COL", True, '#000000')
        text_rect = text.get_rect()
        text_rect.topleft = (1780,2040)
        self.map.blit(text, text_rect)


    def run_simulation(self):
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
            self.texts()
            self.cars.draw(self.map)
            self.agents.draw(self.map)
            self.cars.update()
            # print(self.agent.get_is_moving(), 1)
            self.agents.update()
            # print(self.agent.get_is_moving(), 4)

            camera_x = self.agent.rect.centerx - screen_width // 2
            camera_y = self.agent.rect.centery - screen_height // 2

            # Ensure the camera stays within map boundaries
            camera_x = max(0, min(camera_x, map_width - screen_width))
            camera_y = max(0, min(camera_y, map_height - screen_height))

            # Blit the portion of the map that the camera can see onto the screen
            self.screen.blit(self.map, (0, 0), pygame.Rect(camera_x, camera_y, screen_width, screen_height))

            #####################
            # self.viewport_x = max(0, min(self.viewport_x, map_width - screen_width))
            # self.viewport_y = max(0, min(self.viewport_y, map_height - screen_height))

            # # Blit the portion of the map corresponding to the viewport onto the screen
            # self.screen.blit(self.map, (0, 0), (self.viewport_x, self.viewport_y, screen_width, screen_height))

            pygame.display.update()
            self.clock.tick(60)
            
            if not self.agent.get_is_moving(): return
            

    def init_simulation(self, agent_pos):
        pygame.init()
        pygame.display.set_caption(self.name) 
        for road in roads:
            new_road = Road(coordinates=road['coordinates'], edges=road['edges'])
            self.roads.add(new_road)

            for edg in road['edges']:
                if edg['from_node'] is not None and edg['to_node'] is not None:
                    traffic = self.traffic[edg['from_node']][edg['to_node']]
                    if traffic:
                        for _ in range(traffic):
                            new_car = Car(self.map, edg['from_node'], edg['to_node'],edg['direction'] , new_road)
                            new_car.update_traffic = self.set_traffic
                            new_car.get_traffic = self.get_traffic
                            self.cars.add(new_car)
                    if edg["from_node"] == agent_pos[0] and edg["to_node"] == agent_pos[1]:
                        print(0)
                        agent = Agent(self.map, edg["from_node"], edg["to_node"], edg["direction"], new_road)
                        self.agents.add(agent)
                        self.agent = agent

        Car.set_cars(self.cars)
        Car.set_agent(self.agent)
        Car.set_roads(self.roads)

    
# sim = TestSimulation()
# sim.init_simulation()
# sim.run_simulation()