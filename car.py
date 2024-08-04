import random
from utils import draw_item
# from mapping import mappings

FRAMES = 60
random.seed(12)

class Car:

    def __init__(self, from_node, to_node, direction, road):
        self.from_node = from_node
        self.to_node = to_node
        self.road = road
        self.direction = direction
        self.rect = None
        self.position = None
        self.angle = None
    #ifnotcontains
    def start(self, map):
        self.draw(map)
        self.move()

    def select_to_node (self):
        options = []
        
        for i, to_node in enumerate(Car.distance_matrix[self.from_node]):
            if to_node:
                options.append(i)
                
        self.to_node = options[random.randint(0,len(options)-1)]
    
    def draw(self, map):
        rect = self.road.rect
        car_size = 70
        space = 10

        if self.position == None: 
            if self.direction == "right": 
                self.angle = 180
                self.position = (rect.left + car_size, rect.top + space)
            if self.direction == "left": 
                self.angle = 0
                self.position = (rect.right - car_size, rect.bottom - car_size)
            if self.direction == "up": 
                self.angle = 90
                self.position = (rect.left, rect.bottom - car_size)
            if self.direction == "down": 
                self.angle = 270
                self.position = (rect.right - car_size, rect.top + car_size)

        draw_fn = draw_item('images/car.png', (car_size,car_size), self.angle) 
        surf_and_rect = draw_fn(self.position)
        self.rect = surf_and_rect[1]
        map.blit(*surf_and_rect)

    def move(self):
        x = self.position[0]
        y = self.position[1]
        dist = 15

        if self.direction == "right": 
            self.position = (dist + x, y)
        if self.direction == "left": 
            self.position = (x - dist, y)
        if self.direction == "up": 
            self.position = (x, y - dist)
        if self.direction == "down": 
            self.position = (x, y + dist)

