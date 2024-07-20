import pygame
from mapping import mappings
from car import Car
from sys import exit

class TestSimulation:
    def __init__(self, name, distance_matrix):
        self.name = name
        self.distance_matrix = distance_matrix
        self.car_objects = []
        self.car_rects = []
    
    def draw_item(self, img_src, scale, angle=0):
        def draw(position):
            surf = pygame.image.load(img_src).convert_alpha()
            scaled_surf = pygame.transform.scale(surf, scale)
            rotated_surf = pygame.transform.rotate(scaled_surf, angle)
            rect = rotated_surf.get_rect(topleft = position)

            return (rotated_surf, rect)
        
        return draw
    
    def draw_building(self, position):
        draw_fn = self.draw_item('images/building2.png', (250,250)) 
        return draw_fn(position)
    
    def draw_car(self, position, angle):
        draw_fn = self.draw_item('images/car.png', (70,70), angle) 
        return draw_fn(position)
    
    def draw_road(self, position, length, angle):
        draw_fn = self.draw_item('images/road3.png', (400,length), angle) 
        return draw_fn(position)
    
    def draw_node(self,screen,node):
        screen.blit(*self.draw_building(node["position"])) 

    def draw_edge(self,screen,road):
        def get_angle(direction):
            if(direction == "left"): return 270
            if(direction == "right"): return 90
            if(direction == "up"): return 180
            if(direction == "down"): return 0

        screen.blit(*self.draw_road(road["position"], road["length"], get_angle(road["direction"])))  

    def generate_cars(self):
        Car.generate_traffic_matrix(self.distance_matrix)

        for i, nodes in enumerate(Car.traffic_matrix):
            for to_node in nodes:
                if to_node:
                    for _ in range(to_node):
                        new_car = Car(i)
                        new_car.select_to_node()
                        self.car_objects.append(new_car)



    def run_simulation(self):
        pygame.init()
        screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption(self.name) 
        clock = pygame.time.Clock()

        self.generate_cars()
 
        # grass_surf = pygame.image.load('images/grass.png').convert()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if len(self.car_rects) and len(self.car_objects):
                for car in self.car_objects:
                    if car.frames_left > 0:
                         car.update_position(car.position[0] + 10)

            # pygame.draw.rect(screen,'#268b07', pygame.Rect(0,0,1200,800))
            pygame.draw.rect(screen,'#306b40', pygame.Rect(0,0,1200,800))
          
            for node in mappings["nodes"]:
                self.draw_node(screen, node)

            for edge in mappings["edges"]:
                self.draw_edge(screen, edge)
                  
            for car in self.car_objects:
                value = self.draw_car(**car.draw_car())
                self.car_rects.append(value)
                screen.blit(*value)
    

            pygame.display.update()
            clock.tick(60)