import pygame
from mapping3 import roads
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
    def __init__(self, traffic=None, get_traffic=None, set_traffic=None, name='Q-learning Agent', before_loop=None, during_loop=None):
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
        #self.draw_buildings()
        #self.draw_misc()
        #self.during_loop()
 
    def draw_buildings(self):
        pygame.draw.rect(self.map,'#0d4b0d', pygame.Rect(pygame.Rect(0,0,map_width,map_height)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(40,2180,40,240)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(400,2050,400,100)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(1220,2020,200,100)))
        pygame.draw.rect(self.map,'#808080', pygame.Rect(pygame.Rect(1770,2020,200,100)))

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

    def draw_misc(self):
        self.roads.draw(self.map)
        

    def run_simulation(self):
        # i = 0
        for road in roads:
            self.roads.add(Road(coordinates=road['coordinates'], edges=road['edges']))
        # #     i = 1 if i == 0 else 0
        pygame.init()
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
            # self.texts()

            self.roads.draw(self.map)
            #self.cars.draw(self.map)
            # self.agents.draw(self.map)
            #self.cars.update()
            # # print(self.agent.get_is_moving(), 1)
            # self.agents.update()
            # print(self.agent.get_is_moving(), 4)

            # camera_x = self.agent.rect.centerx - screen_width // 2
            # camera_y = self.agent.rect.centery - screen_height // 2

            # # Ensure the camera stays within map boundaries
            # camera_x = max(0, min(camera_x, map_width - screen_width))
            # camera_y = max(0, min(camera_y, map_height - screen_height))

            # # Blit the portion of the map that the camera can see onto the screen
            # self.screen.blit(self.map, (0, 0), pygame.Rect(camera_x, camera_y, screen_width, screen_height))

            #####################
            self.viewport_x = max(0, min(self.viewport_x, map_width - screen_width))
            self.viewport_y = max(0, min(self.viewport_y, map_height - screen_height))

            # Blit the portion of the map corresponding to the viewport onto the screen
            self.screen.blit(self.map, (0, 0), (self.viewport_x, self.viewport_y, screen_width, screen_height))
            
            pygame.display.update()
            self.clock.tick(60)
            
            # if not self.agent.get_is_moving(): return
            

    def init_simulation(self, agent_pos=None):
        pygame.init()
        pygame.display.set_caption(self.name) 
        for road in roads:
            new_road = Road(coordinates=road['coordinates'], edges=road['edges'])
            self.roads.add(new_road)

            for edg in road['edges']:
                if edg['from_node'] is not None and edg['to_node'] is not None:
                    traffic = 0 if edg['from_node'] not in self.traffic else self.traffic[edg['from_node']][edg['to_node']]
                    #traffic = 1
                    if traffic:
                        for _ in range(traffic):
                            new_car = Car(self.map, edg['from_node'], edg['to_node'],edg['direction'] , new_road)
                         
                            new_car.update_traffic = self.set_traffic
                            new_car.get_traffic = self.get_traffic
                            self.cars.add(new_car)
                    # if edg["from_node"] == agent_pos[0] and edg["to_node"] == agent_pos[1]:
                    #     print(0)
                    #     agent = Agent(self.map, edg["from_node"], edg["to_node"], edg["direction"], new_road)
                    #     self.agents.add(agent)
                    #     self.agent = agent

        Car.set_cars(self.cars)
        #Car.set_agent(self.agent)
        Car.set_roads(self.roads)

traf = {0: {1: 0.0}, 1: {0: 0.0, 167: 0.0}, 2: {167: 0.0, 3: 0.0, 4: 0.0}, 3: {163: 0.0, 164: 0.0}, 4: {5: 0.0, 6: 0.0}, 5: {96: 0.0, 169: 0.0, 170: 0.0}, 6: {8: 0.0, 121: 0.0}, 8: {2: 0.0, 122: 0.0}, 10: {2: 0.0}, 11: {170: 0.0, 98: 0.0}, 12: {171: 0.0, 13: 0.0}, 13: {172: 0.0, 181: 0.0}, 14: {15: 0.0, 173: 0.0}, 15: {16: 0.0, 132: 0.0}, 16: {17: 0.0}, 17: {185: 0.0, 18: 0.0}, 18: {65: 0.0, 86: 0.0}, 19: {20: 0.0, 66: 0.0}, 20: {21: 0.0, 67: 0.0}, 21: {22: 0.0, 68: 0.0}, 22: {23: 1}, 23: {24: 0.0, 69: 0.0}, 24: {183: 0.0, 22: 0.0, 25: 0.0}, 25: {24: 0.0, 27: 0.0}, 27: {25: 0.0}, 28: {29: 0.0}, 29: {126: 0.0, 30: 0.0}, 30: {29: 0.0, 31: 0.0, 78: 0.0}, 31: {30: 0.0, 105: 0.0}, 32: {33: 0.0, 118: 0.0}, 33: {32: 0.0, 120: 0.0}, 34: {35: 0.0, 120: 0.0, 121: 0.0}, 35: {34: 0.0}, 36: {16: 0.0, 129: 0.0}, 37: {38: 0.0, 130: 0.0}, 38: {37: 0.0}, 39: {79: 0.0, 81: 0.0}, 40: {36: 0.0, 81: 0.0}, 41: {81: 0.0}, 42: {134: 0.0, 85: 0.0}, 43: {101: 0.0, 102: 0.0}, 44: {43: 0.0, 45: 0.0}, 45: {44: 0.0, 87: 0.0, 88: 0.0}, 46: {44: 0.0, 91: 0.0}, 47: {46: 0.0}, 48: {49: 0.0, 140: 0.0}, 49: {48: 0.0, 142: 0.0, 64: 0.0}, 50: {47: 0.0, 64: 0.0, 145: 0.0}, 51: {146: 0.0, 144: 0.0}, 52: {53: 0.0, 157: 0.0, 159: 0.0}, 53: {52: 0.0, 54: 0.0}, 54: {159: 0.0, 53: 0.0, 161: 0.0}, 55: {92: 0.0, 93: 0.0, 161: 0.0}, 56: {57: 0.0, 92: 0.0, 95: 0.0}, 57: {56: 0.0}, 58: {93: 0.0, 59: 0.0, 60: 0.0}, 59: {163: 0.0, 58: 0.0}, 60: {163: 0.0, 58: 0.0}, 61: {62: 0.0, 63: 0.0}, 62: {9: 0.0, 123: 0.0}, 63: {61: 0.0, 120: 0.0, 123: 0.0}, 64: {49: 0.0, 50: 0.0, 90: 0.0}, 65: {86: 0.0}, 66: {19: 0.0}, 67: {20: 0.0}, 68: {21: 0.0}, 69: {70: 0.0, 103: 0.0}, 70: {69: 0.0}, 71: {28: 0.0, 72: 0.0}, 73: {28: 0.0}, 74: {24: 0.0, 128: 0.0}, 75: {114: 0.0, 116: 0.0}, 76: {75: 0.0, 112: 0.0}, 77: {108: 0.0, 110: 0.0}, 78: {30: 0.0, 107: 0.0}, 79: {39: 0.0}, 80: {40: 0.0}, 81: {41: 0.0, 80: 0.0, 82: 0.0}, 82: {83: 0.0, 135: 0.0}, 83: {85: 0.0, 134: 0.0, 137: 0.0}, 84: {42: 0.0}, 85: {138: 0.0, 148: 0.0, 84: 0.0}, 86: {19: 0.0, 65: 0.0}, 87: {45: 0.0}, 88: {45: 0.0}, 90: {64: 0.0}, 91: {46: 0.0}, 92: {55: 0.0, 56: 0.0, 95: 0.0}, 93: {55: 0.0, 58: 0.0, 94: 0.0}, 94: {93: 0.0}, 95: {92: 0.0, 56: 0.0}, 96: {174: 0.0, 97: 0.0}, 97: {96: 0.0}, 98: {11: 0.0}, 99: {100: 0.0, 141: 0.0}, 100: {99: 0.0}, 101: {43: 0.0, 102: 0.0}, 102: {84: 0.0, 101: 0.0}, 103: {104: 0.0, 124: 0.0}, 104: {71: 0.0}, 105: {31: 0.0, 106: 0.0}, 106: {105: 0.0}, 107: {77: 0.0}, 108: {78: 0.0, 109: 0.0}, 109: {108: 0.0}, 110: {77: 0.0, 111: 0.0, 112: 0.0}, 111: {110: 0.0}, 112: {76: 0.0, 110: 0.0, 113: 0.0}, 113: {112: 0.0}, 114: {76: 0.0, 115: 0.0}, 115: {114: 0.0}, 116: {75: 0.0, 117: 0.0, 118: 0.0}, 117: {116: 0.0}, 118: {32: 0.0, 116: 0.0, 119: 0.0}, 119: {118: 0.0}, 120: {33: 0.0, 34: 0.0, 63: 0.0}, 121: {6: 0.0, 34: 0.0, 122: 0.0}, 122: {61: 0.0}, 123: {62: 0.0, 63: 0.0}, 124: {103: 0.0}, 125: {104: 0.0}, 126: {74: 0.0, 127: 0.0}, 127: {126: 0.0}, 128: {74: 0.0}, 129: {36: 0.0}, 130: {39: 0.0, 131: 0.0}, 131: {130: 0.0}, 132: {37: 0.0, 133: 0.0}, 133: {132: 0.0}, 134: {83: 0.0, 135: 0.0, 136: 0.0}, 135: {80: 0.0, 82: 0.0}, 136: {134: 0.0}, 137: {83: 0.0}, 138: {48: 0.0, 139: 0.0}, 139: {138: 0.0}, 140: {99: 0.0}, 141: {84: 0.0, 100: 0.0}, 142: {49: 0.0, 146: 0.0, 143: 0.0}, 143: {142: 0.0}, 144: {51: 0.0}, 145: {50: 0.0}, 146: {51: 0.0, 142: 0.0, 147: 0.0}, 147: {146: 0.0}, 148: {85: 0.0, 149: 0.0, 150: 0.0}, 149: {148: 0.0}, 150: {148: 0.0, 151: 0.0, 157: 0.0}, 151: {150: 0.0, 152: 0.0, 153: 0.0}, 152: {151: 0.0}, 153: {151: 0.0, 154: 0.0, 155: 0.0}, 154: {153: 0.0}, 155: {153: 0.0, 156: 0.0, 157: 0.0}, 156: {155: 0.0}, 157: {52: 0.0, 150: 0.0, 155: 0.0, 158: 0.0}, 158: {157: 0.0}, 159: {52: 0.0, 54: 0.0, 160: 0.0}, 160: {159: 0.0}, 161: {54: 0.0, 55: 0.0, 162: 0.0}, 162: {161: 0.0}, 163: {3: 0.0, 165: 0.0}, 164: {60: 0.0}, 165: {4: 0.0, 166: 0.0}, 166: {165: 0.0}, 167: {1: 0.0, 2: 0.0, 168: 0.0}, 168: {167: 0.0}, 169: {5: 0.0}, 170: {5: 0.0, 6: 0.0}, 171: {175: 0.0, 12: 0.0, 179: 0.0}, 172: {13: 0.0, 171: 0.0, 180: 0.0}, 173: {172: 0.0, 14: 0.0, 184: 0.0}, 174: {12: 0.0, 175: 0.0, 177: 0.0}, 175: {174: 0.0, 176: 0.0}, 176: {11: 0.0, 178: 0.0}, 177: {174: 0.0}, 178: {176: 0.0}, 179: {171: 0.0}, 180: {172: 0.0}, 181: {14: 0.0, 182: 0.0}, 182: {181: 0.0}, 183: {15: 0.0, 185: 0.0}, 184: {183: 0.0}, 185: {15: 0.0, 173: 0.0}}
def dd (x): 
    global traf
    traf = x
sim = TestSimulation(traffic=traf, get_traffic=lambda: traf, set_traffic=dd)
#sim.init_simulation()
sim.run_simulation()