import numpy as np
import random
from environment import QlearningEnv
from traffic import Traffic
from simulation import TestSimulation
from utils import generate_empty_matrix
import pygame

map_width = 4000
map_height = 4000

map = pygame.Surface((map_width,map_height))

carpark_idxs = [0, 3, 7, 11]


# def generate_traffic_matrix(distance_matrix):
#     size = len(distance_matrix)
#     traffic_matrix = generate_empty_matrix(size)

#     for i in range(size):
#         for j in range(size):
#             if distance_matrix[i][j]:
#                 traffic_matrix[i][j] = random.randint(0,5)

#     return traffic_matrix

def generate_distance_matrix(distance_matrix):
    distance_matrix[1][0] = 200
    distance_matrix[1][4] = 400
    distance_matrix[1][5] = 500

    distance_matrix[2][1] = 100
    distance_matrix[2][3] = 300

    distance_matrix[4][0] = 200
    distance_matrix[4][6] = 300

    distance_matrix[5][2] = 200
    distance_matrix[5][9] = 300

    distance_matrix[6][4] = 300
    distance_matrix[6][5] = 200
    distance_matrix[6][7] = 300

    distance_matrix[8][6] = 300
    distance_matrix[8][7] = 100

    distance_matrix[9][8] = 200
    distance_matrix[9][10] = 400
    distance_matrix[9][11] = 200

    distance_matrix[10][3] = 400
    distance_matrix[10][9] = 400

def generate_start_node(): 
    randint = 0
    while randint in carpark_idxs:
        randint = random.randint(1, 10)
    return randint

distance_matrix = generate_empty_matrix(12)
generate_distance_matrix(distance_matrix)

# traffic_matrix = generate_traffic_matrix(distance_matrix)

# current_node = generate_start_node()
# print(distance_matrix, 'boo', traffic_matrix)
#[0,400,0],[400,0,300],[0,300,0]

traffic = Traffic([[0, 400],[400, 0]], map)
traffic.run_simulation()

# arguments = {
#     "distance": distance_matrix,
#     "traffic": traffic_matrix,
#     "position": current_node,
#     "seed": 100   
# }

# qlearning_env = QlearningEnv(arguments)
