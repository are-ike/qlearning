import random
from car import Car
from road import Road
from mapping import roads
from utils import generate_empty_matrix
from simulation import TestSimulation

class Traffic:

    def __init__(self, distance_matrix, carparks, map):
        self.distance_matrix = distance_matrix
        #self.traffic_matrix = [[0,1,0,0], [1,0,1,0], [0,1,0,1], [0,0,0,0]]
        #self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,0,1], [0,0,1,0,1,0]]
        self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        self.carparks = carparks
        self.cars = []
        self.roads = []
        self.map = map

    def get_current_traffic(self):
        return self.traffic_matrix
    
    def update_traffic(self, new_traffic):
        self.traffic_matrix = new_traffic

    def generate_traffic_matrix(self):
        size = len(self.distance_matrix)
        matrix = generate_empty_matrix(size)

        for i in range(size):
            for j in range(size):
                if self.distance_matrix[i][j]:
                    max_traffic = 9 if self.distance_matrix[i][j] >= 900 else (self.distance_matrix[i][j] // 100)
                    matrix[i][j] = random.randint(0, max_traffic)

        self.traffic_matrix = matrix

    def generate_traffic(self, road_group, car_group):
        for road in roads:
            new_road =  Road(road["coordinates"], road["edges"])
            new_road.draw(self.map) #Drawing road here so that cars have access to road rect before loop
            
            for edge in road["edges"]:
                traffic = self.traffic_matrix[edge["from_node"]][edge["to_node"]]

                for _ in range(traffic):
                    new_car = Car(edge["from_node"], edge["to_node"], edge["direction"], new_road)
                    new_car.update_traffic = self.update_traffic
                    new_car.get_traffic = self.get_current_traffic

                    self.cars.append(new_car)
                    car_group.add(new_car)

            self.roads.append(new_road)
            road_group.add(new_road)
        
        #add all roads to Car
        Car.set_roads(self.roads)
        Car.set_carparks(self.carparks)

    def on_simulate(self):
        print(self.traffic_matrix)

    def run_simulation(self):
        simulation = TestSimulation('Q-Learning Agent', self.map, self.generate_traffic, self.on_simulate)
        simulation.run_simulation()
        