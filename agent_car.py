from car import Car
#from mapping import roads

class Agent(Car):

    def __init__(self, from_node, to_node, direction, road):
        super().__init__(from_node, to_node, direction, road, img_src = 'images/agent.png')
        self.start = False
        self.is_moving = False         
        self.roads = []         

    def move(self, from_node, to_node):
        #self.start = True

        for road in self.roads:
            for edge in road.edges:
                if edge["from_node"] == from_node and edge["to_node"] == to_node:
                    print(from_node, to_node)
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
        #self.set_is_moving(True)

        if self.has_left_road():
            #old_direction = self.direction
            #self.set_is_moving(False)
            self.is_moving = False 
            
            # if old_direction != self.direction:
            #     self.turn_car(old_direction)

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


