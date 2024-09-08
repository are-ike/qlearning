import random
from car import Car
from agent_car import Agent
from road import Road
from mapping import roads
from utils import generate_empty_matrix
from simulation import TestSimulation

class Traffic:

    def __init__(self, 
                #  distance_matrix, 
                #  carparks, 
                 traffic_matrix, get_traffic, update_traffic, map, agent_position):
        #self.distance_matrix = distance_matrix
        #self.traffic_matrix = [[0,1,0,0], [1,0,1,0], [0,1,0,1], [0,0,0,0]]
        #self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,0,1], [0,0,1,0,1,0]]
        #self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        #self.carparks = carparks
        self.cars = []
        self.roads = []
        self.map = map
        self.agent = None
        self.agent_position = agent_position
        self.traffic_matrix = traffic_matrix 
        self.get_traffic = get_traffic 
        self.update_traffic = update_traffic 
        self.simulation = None 
        # self.set_agent_is_moving = None 

    # def get_current_traffic(self):
    #     return self.traffic_matrix
    
    # def update_traffic(self, new_traffic):
    #     self.traffic_matrix = new_traffic

    # def generate_traffic_matrix(self):
    #     size = len(self.distance_matrix)
    #     matrix = generate_empty_matrix(size)

    #     for i in range(size):
    #         for j in range(size):
    #             if self.distance_matrix[i][j]:
    #                 max_traffic = 9 if self.distance_matrix[i][j] >= 900 else (self.distance_matrix[i][j] // 100)
    #                 matrix[i][j] = random.randint(0, max_traffic)

    #     self.traffic_matrix = matrix

    def start_agent(self, from_node, to_node):
        # self.agent.set_agent_is_moving = self.set_agent_is_moving
        self.agent.move(from_node, to_node)
        #print(self.agent.start)
        self.run_simulation()
        

    def generate_traffic(self, road_group, car_group, agent_group):
        for i,road in enumerate(roads):
            new_road =  Road(road["coordinates"], road["edges"])
            new_road.draw(self.map) #Drawing road here so that cars have access to road rect before loop
            
            # for j,edge in enumerate(road["edges"]):
            #     traffic = self.traffic_matrix[edge["from_node"]][edge["to_node"]]

            #     for k in range(traffic):
            #         new_car = None
            #         id = f"{i}{j}{k}"

            #         if self.agent_position[0] == edge["from_node"] and self.agent_position[1] == edge["to_node"]:
            #             agent = Agent(self.map, edge["from_node"], edge["to_node"], edge["direction"], new_road)
            #             self.agent = agent
            #             agent_group.add(agent)
            #         else:
            #             new_car = Car(self.map, edge["from_node"], edge["to_node"], edge["direction"], new_road)
            #             new_car.update_traffic = self.update_traffic
            #             new_car.get_traffic = self.get_traffic

            #             self.cars.append(new_car)
            #             car_group.add(new_car)

            self.roads.append(new_road)
            road_group.add(new_road)
    
        # self.agent.roads = self.roads
        
        # #add all roads to Car
        # Car.set_roads(self.roads)
        # Car.set_cars(self.cars)
        # Car.set_agent(self.agent)
     
        
        

    def on_simulate(self):pass
        #print(self.traffic_matrix)

    def start_simulation(self):
        simulation = TestSimulation('Q-Learning Agent', self.map, self.generate_traffic, self.on_simulate)
        self.simulation = simulation
        simulation.init_simulation()
        
    def run_simulation(self):
        self.simulation.run_simulation()