import random
import pygame
from sprite import Sprite
from utils import draw_item

FRAMES = 60
angles = {
    "up": 90,
    "left": 0,
    "right": 180,
    "down": 270
}
random.seed(12)

class Car(pygame.sprite.Sprite):
    roads = []
    cars = []
    agent = None

    def __init__(self, id, from_node, to_node, direction, road, img_src='images/car.png', car_width=76, car_height=76):
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
        self.car_width = car_width
        self.car_height = car_height
        val = self.get_rect_surf() 
        self.rect = val[1]
        self.image = val[0]
        self.id = id
        self.is_paused = False

    @staticmethod
    def set_roads(rds):
        global roads
        roads = rds

    @staticmethod
    def set_cars(crs):
        global cars
        cars = crs

    @staticmethod
    def set_agent(agt):
        global cars
        cars.append(agt)

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
        half_car_width = self.car_width - 20
        half_car_height = self.car_height - 20
        
        if self.direction == "right": 
            self.angle = 0
            self.position = (rect.left, rect.bottom - half_car_height - 8)
        if self.direction == "left": 
            self.angle = 180
            self.position = (rect.right - half_car_width, rect.top - 14)
        if self.direction == "up": 
            self.angle = 90
            self.position = (rect.right - half_car_width - 8, rect.bottom - half_car_height)
        if self.direction == "down": 
            self.angle = 270 
            self.position = (rect.left -10 , rect.top)

        draw_fn = draw_item(self.img_src, (self.car_width,self.car_height), self.angle) 
        surf_and_rect = draw_fn(self.position)
        return surf_and_rect
    
    def turn_car(self, old_direction):
        def get_angle():
            space = 8
            rect = self.road.rect
            half_car_width = self.car_width - 20
            half_car_height = self.car_height - 20

            if old_direction == "down":
                if self.direction == "right": 
                    self.position = (rect.left + space, rect.bottom - half_car_height - space)
                    return 90 #down right and up left needed?
                if self.direction == "left": 
                    self.position = (rect.right - half_car_width - space, rect.top - 14)
                    return -90 
                
            if old_direction == "up":
                if self.direction == "right": 
                    self.position = (rect.left + space, rect.bottom - half_car_height - space)
                    return -90 #down right and up left needed?
                if self.direction == "left": 
                    self.position = (rect.right - half_car_width - space, rect.top - 14)
                    return 90 
                
            if old_direction == "down" and self.direction == "up": 
                self.position = (rect.right - half_car_width - space, rect.bottom - half_car_height )
                return 180
            
            if old_direction == "up" and self.direction == "down": 
                self.position = (rect.left - 12 , rect.top + space)
                return -180
            
            if old_direction == "left":
                if self.direction == "up": 
                    self.position = (rect.right - half_car_width - space, rect.bottom - half_car_height )
                    return 270
                if self.direction == "down": 
                    self.position = (rect.left - 12 , rect.top + space)
                    return 90
                if self.direction == "right": 
                    self.position = (rect.left + space, rect.bottom - half_car_height - space)
                    return -180
                
            if old_direction == "right":
                if self.direction == "up": 
                    self.position = (rect.right - half_car_width - space, rect.bottom - half_car_height )
                    return 90
                if self.direction == "down": 
                    self.position = (rect.left - 12 , rect.top + space)
                    return -90
                if self.direction == "left": 
                    self.position = (rect.right - half_car_width - space, rect.top - 14)
                    return 180

        self.angle = self.angle + get_angle()
        self.image = pygame.transform.rotate(self.image, get_angle())  
        return self.image.get_rect(topleft = self.position)

    def update(self):
        rect = None
        if self.has_left_road():
            old_direction = self.direction
            self.select_to_node()
            
            if old_direction != self.direction:
               #self.turn_car(old_direction)
               rect_surf = self.get_rect_surf()
               rect = rect_surf[1]
               self.image = rect_surf[0]


        x = self.position[0]
        y = self.position[1]
        dist = 1.2

        #while True:

        if self.direction == "right": 
            new_position = (dist + x, y)
        if self.direction == "left": 
            new_position = (x - dist, y)
        if self.direction == "up": 
            new_position = (x, y - dist)
        if self.direction == "down": 
            new_position = (x, y + dist)
        
            # if self.is_colliding(new_position):
            #     dist -= 1
            # elif dist == 0 or not self.is_colliding(new_position):
            #     break
        if self.has_collision(new_position): return

        self.position = new_position
        if rect: self.rect = rect
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
    
    def is_colliding(self, position):
        for car in cars:
            if car.rect.collidepoint(position) and car != self:
                return True
            return False
        
    def has_collision(self, coordinates):
        def get_coor():
            if self.direction == "down": return (coordinates[0], coordinates[1], self.car_width - 20, self.car_height)
            if self.direction == "up" : return (coordinates[0] + 20, coordinates[1], self.car_width - 20, self.car_height)
            if self.direction == "left": return (coordinates[0], coordinates[1], self.car_width, self.car_height - 20)
            if self.direction == "right": return (coordinates[0], coordinates[1] + 20, self.car_width, self.car_height - 15)

        rect = pygame.rect.Rect(get_coor())
        sprite = Sprite(rect)
        #pygame.draw.rect(self.id,'#ffffff', pygame.Rect(rect))
        sprites = pygame.sprite.spritecollide(sprite, cars, False)

        if len(sprites) == 0:
            self.is_paused = False 
            return self.is_paused
        if len(sprites) == 1: 
            for car in sprites:
                if car == self:
                    self.is_paused = False 
                    return self.is_paused
        #ids = list(map(lambda car: car.id, sprites))
        #id = min(ids)

        def is_first(current_first, car): 
            pos1 = current_first.position
            pos2 = car.position
            if car.direction == "right": return pos1[0] < pos2[0]
            if car.direction == "left": return pos1[0] > pos2[0]
            if car.direction == "up": return pos1[1] > pos2[1]
            if car.direction == "down": return pos1[1] < pos2[1]

        first_car = pygame.sprite.Group()
        furthest_car = None
        for car in sprites:
            # if car.id != id:
            #     car.is_paused = True 
            # else:
            #     car.is_paused = False 
            if furthest_car: 
                if is_first(furthest_car, car):
                    furthest_car = car
            else:
                furthest_car = car
        first_car.add(furthest_car)
          
        for car in sprites:
            if car in first_car:
                car.is_paused = False 
            else:
                car.is_paused = True 

        return self.is_paused

#FLOW:
#cars are created with rect of road so they can be positioned.
#they are initially positioned in the constructor
#the draw method seems to be overriden so it doesnt seem to
#matter what code is in there. but lets just leave it
#the get_rect_surf calculates the cars position
#the update function calculates the new position, 
#moves the rect and sets the new position