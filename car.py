import random
from mapping import mappings

FRAMES = 60
random.seed(12)

class Car:
    traffic_matrix = []
    distance_matrix = []

    def __init__(self, from_node):
        self.from_node = from_node
        self.to_node = None
        self.position = None
        self.angle = None
        self.frames_left = None


    @staticmethod
    def generate_empty_matrix(node_number):
        space = []
        for _ in range(node_number):
            space.append([0]*node_number)
        return space

    def generate_traffic_matrix(distance_matrix):
        size = len(distance_matrix)
        matrix = Car.generate_empty_matrix(size)

        for i in range(size):
            for j in range(size):
                if distance_matrix[i][j]:
                    #matrix[i][j] = random.randint(0,2)
                    matrix[i][j] = 1

        Car.traffic_matrix = matrix
        Car.distance_matrix = distance_matrix
    
    def select_to_node (self):
        options = []
        
        for i, to_node in enumerate(Car.distance_matrix[self.from_node]):
            if to_node:
                options.append(i)
                
        self.to_node = options[random.randint(0,len(options)-1)]
    
    def draw_car(self):
        if self.position == None:
            edge = None
            for edges in mappings["edges"]:
                for ed in edges["edges"]:
                    if ed[0] == self.from_node and ed[1] == self.to_node:
                        edge = edges
            
            if not edge: return

            self.frames_left = 400
            #math.ceil((edge["length"] / 6.94) * FRAMES)

            if edge["right"] == self.from_node: 
                self.angle = 180
                self.position = (edge["position"][0] + edge["length"] - 80, edge["position"][1] + 140)
            if edge["left"] == self.from_node: 
                self.angle = 0
                self.position = (edge["position"][0] , edge["position"][1] + 185)
            if edge["up"] == self.from_node: 
                self.angle = 90
                self.position = (edge["position"][0] , edge["position"][1])
            if edge["down"] == self.from_node: 
                self.angle = 270
                self.position = (edge["position"][0] , edge["position"][1])

        values = {
            "position": self.position,
            "angle": self.angle,
        }

        return values

    def move(self, frames):
        if frames == 0:
            Car.traffic_matrix[self.from_node][self.to_node] -= 1
        
            self.from_node = self.to_node
            self.select_to_node()

            Car.traffic_matrix[self.from_node][self.to_node] += 1
            #remove car
        else:
            self.frames_left = frames

    def update_position(self, x=None, y=None):
        self.position = (x if x else self.position[0], y if y else self.position[1])

