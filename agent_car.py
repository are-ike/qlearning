from car import Car
#from mapping import roads
from utils import draw_item

class Agent(Car):

    def __init__(self, id, from_node, to_node, direction, road):
        super().__init__(id, from_node, to_node, direction, road, img_src = 'images/agent.png', car_height=35, car_width=60)
        self.start = False
        self.is_moving = False         
        self.roads = []         

    def move(self, from_node, to_node):
        # print(from_node, to_node)
        for road in Car.get_roads():
            for edge in road.edges:
                if edge["from_node"] == from_node and edge["to_node"] == to_node:
                    self.from_node = from_node
                    self.to_node = to_node
                    self.direction = edge["direction"]
                    self.road = road

                    surf_and_rect = self.get_rect_surf()
                    self.rect = surf_and_rect[1]
                    self.image = surf_and_rect[0]
                    

    def get_is_moving(self): return self.is_moving
    def get_is_start(self): return self.start

    def update(self):
        #if not self.get_is_start(): return

        self.is_moving = True 
        #print(self.is_moving, 2)
        #self.set_is_moving(True)

        if self.has_left_road():
            #print(self.is_moving, 3)
            #old_direction = self.direction
            #self.set_is_moving(False)
            self.is_moving = False 
            
            # if old_direction != self.direction:
            #     self.turn_car(old_direction)

        x = self.position[0]
        y = self.position[1]
        dist = 1.2

        if self.direction == "right": 
            new_position = (dist + x, y)
        if self.direction == "left": 
            new_position = (x - dist, y)
        if self.direction == "up": 
            new_position = (x, y - dist)
        if self.direction == "down": 
            new_position = (x, y + dist)
        
        if self.has_collision(new_position): 
            return

        self.position = new_position
        self.rect.topleft = new_position


    def get_rect_surf(self):
        rect = self.road.rect
        half_car_width = self.car_width - 20
        half_car_height = self.car_height - 20
        
        #if not self.is_agent:
        # if self.direction == "right": 
        #     self.angle = 0
        #     self.position = (rect.left, rect.bottom - half_car_height - 8)
        # if self.direction == "left": 
        #     self.angle = 180
        #     self.position = (rect.right - half_car_width, rect.top)
        # if self.direction == "up": 
        #     self.angle = 90
        #     self.position = (rect.right - half_car_width, rect.bottom - half_car_height)
        # if self.direction == "down": 
        #     self.angle = 270 
        #     self.position = (rect.left -10 , rect.top)
        #else:
        if self.direction == "right": 
            self.angle = 0
            self.position = (rect.left, rect.bottom - half_car_height - 30)
        if self.direction == "left": 
            self.angle = 180
            self.position = (rect.right - half_car_width, rect.top + 10)
        if self.direction == "up": 
            self.angle = 90
            self.position = (rect.right - half_car_width - 6, rect.bottom - half_car_height)
        if self.direction == "down": 
            self.angle = 270 
            self.position = (rect.left +10 , rect.top)
        draw_fn = draw_item(self.img_src, (self.car_width,self.car_height), self.angle) 
        surf_and_rect = draw_fn(self.position)
        return surf_and_rect