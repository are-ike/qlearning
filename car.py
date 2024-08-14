import random
import pygame
from utils import draw_item

FRAMES = 60
angles = {
    "up": 90,
    "left": 0,
    "right": 180,
    "down": 270
}
car_size = 76
random.seed(12)

class Car(pygame.sprite.Sprite):
    roads = []
    carparks = []

    def __init__(self, from_node, to_node, direction, road, img_src='images/car.png'):
        pygame.sprite.Sprite.__init__(self)
        self.from_node = from_node
        self.to_node = to_node
        self.road = road
        self.direction = direction
        self.position = None
        self.angle = None
        self.update_traffic = None
        self.get_traffic = None
        self.img_src = img_src
        val = self.get_rect_surf() 
        self.rect = val[1]
        self.image = val[0]

    @staticmethod
    def set_roads(rds):
        global roads
        roads = rds

    @staticmethod
    def set_carparks(carpark_idxs):
        global carparks
        carparks = carpark_idxs

    def select_to_node (self):
        road_options = []
        edges_options = []
        
        for road in roads:
            for edge in road.edges:
                if edge["from_node"] == self.to_node: 
                    road_options.append(road)
                    edges_options.append(edge)
    
        #doable if i add more higher num roads?
        # idx = 0
        # while edges_options[idx]["to_node"] < self.to_node and len(edges_options)> 1:
        idx = random.randint(0, len(road_options) - 1)

        new_traffic = self.get_traffic()
        new_traffic[self.from_node][self.to_node] -= 1

        self.from_node = self.to_node
        self.to_node = edges_options[idx]["to_node"]
        self.direction = edges_options[idx]["direction"]
        self.road = road_options[idx]

        new_traffic[self.from_node][self.to_node] += 1
        
        self.update_traffic(new_traffic)
    
    def get_rect_surf(self):
        rect = self.road.rect
        space = 0
        half_car_size = car_size - 20
        
        if self.position == None: 
            if self.direction == "right": 
                self.angle = 0
                self.position = (rect.left + space, rect.bottom - half_car_size - 8)
            if self.direction == "left": 
                self.angle = 180
                self.position = (rect.right - half_car_size - space, rect.top + space)
            if self.direction == "up": 
                self.angle = 90
                self.position = (rect.right - half_car_size - space, rect.bottom - half_car_size - space)
            if self.direction == "down": 
                self.angle = 270 
                self.position = (rect.left -10 , rect.top + space)

        draw_fn = draw_item(self.img_src, (car_size,car_size), self.angle) 
        surf_and_rect = draw_fn(self.position)
        return surf_and_rect
    
    def turn_car(self, old_direction):
        def get_angle():
            space = 8
            rect = self.road.rect
            half_car_size = car_size - 20

            if old_direction == "down" or old_direction == "up":
                if self.direction == "right": 
                    self.position = (rect.left + space, rect.bottom - half_car_size - space)
                    return 90 #down right and up left needed?
                if self.direction == "left": 
                    self.position = (rect.right - half_car_size - space, rect.top - 14)
                    return -90 
                
            if old_direction == "down" and self.direction == "up": 
                self.position = (rect.right - half_car_size - space, rect.bottom - half_car_size )
                return 180
            
            if old_direction == "up" and self.direction == "down": 
                self.position = (rect.left - 12 , rect.top + space)
                return -180
            
            if old_direction == "left":
                if self.direction == "up": 
                    self.position = (rect.right - half_car_size - space, rect.bottom - half_car_size )
                    return -90
                if self.direction == "down": 
                    self.position = (rect.left - 12 , rect.top + space)
                    return 90
                if self.direction == "right": 
                    self.position = (rect.left + space, rect.bottom - half_car_size - space)
                    return -180
                
            if old_direction == "right":
                if self.direction == "up": 
                    self.position = (rect.right - half_car_size - space, rect.bottom - half_car_size )
                    return 90
                if self.direction == "down": 
                    self.position = (rect.left - 12 , rect.top + space)
                    return -90
                if self.direction == "left": 
                    self.position = (rect.right - half_car_size - space, rect.top - 14)
                    return 180

        self.angle = self.angle + get_angle()
        self.image = pygame.transform.rotate(self.image, get_angle())  

    def update(self):
        if self.has_left_road():
            old_direction = self.direction
            self.select_to_node()
            
            if old_direction != self.direction:
                self.turn_car(old_direction)

        x = self.position[0]
        y = self.position[1]
        dist = 1

        if self.direction == "right": 
            new_position = (dist + x, y)
        if self.direction == "left": 
            new_position = (x - dist, y)
        if self.direction == "up": 
            new_position = (x, y - dist)
        if self.direction == "down": 
            new_position = (x, y + dist)
        
        self.position = new_position
        self.rect.topleft = new_position

    def has_left_road(self):
        rect = self.road.rect
        half_car_size = 60

        if self.direction == "right": 
            return self.rect.right > rect.right + half_car_size
        if self.direction == "left": 
            return self.rect.left < rect.left - half_car_size
        if self.direction == "up": 
            return self.rect.top < rect.top - half_car_size
        if self.direction == "down": 
            return self.rect.bottom > rect.bottom + half_car_size
        

#FLOW:
#cars are created with rect of road so they can be positioned.
#they are initially positioned in the constructor
#the draw method seems to be overriden so it doesnt seem to
#matter what code is in there. but lets just leave it
#the get_rect_surf calculates the cars position
#the update function calculates the new position, 
#moves the rect and sets the new position