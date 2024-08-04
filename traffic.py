import random
from car import Car
from road import Road
from mapping import roads
import pygame
from utils import generate_empty_matrix
from simulation import TestSimulation

class Traffic:

    def __init__(self, distance_matrix, map):
        self.distance_matrix = distance_matrix
        self.traffic_matrix = [[0,1], [1,0]]
        self.cars = []
        self.roads = []
        self.map = map

    def get_current_traffic(self):
        return self.traffic_matrix
    
    def update_traffic(self):
        return self.traffic_matrix

    def generate_traffic_matrix(self):
        size = len(self.distance_matrix)
        matrix = generate_empty_matrix(size)

        for i in range(size):
            for j in range(size):
                if self.distance_matrix[i][j]:
                    max_traffic = 9 if self.distance_matrix[i][j] >= 900 else (self.distance_matrix[i][j] // 100)
                    matrix[i][j] = random.randint(0, max_traffic)

        self.traffic_matrix = matrix

    def generate_traffic(self):
        for road in roads:
            new_road =  Road(road["coordinates"], road["edges"])
            new_road.draw(self.map) #Drawing road here so that cars have access to road rect before loop
            
            for edge in road["edges"]:
                traffic = self.traffic_matrix[edge["from_node"]][edge["to_node"]]

                for _ in range(traffic):
                    new_car = Car(edge["from_node"], edge["to_node"], edge["direction"], new_road)
                    
                    self.cars.append(new_car)

            self.roads.append(new_road)

    def on_simulate(self):
        for road in self.roads:
            road.draw(self.map) #Drawing road here so that road shows during loop
        for car in self.cars:
            car.start(self.map)
            #pygame.time.delay(2000)

    def run_simulation(self):
        simulation = TestSimulation('Q-Learning Agent', self.map, self.generate_traffic, self.on_simulate)
        simulation.run_simulation()
        