import numpy as np
import random
#from environment import QlearningEnv
import pygame
from traffic import Traffic

map_width = 20000
map_height = 20000

map = pygame.Surface((map_width,map_height))

#carpark_idxs = [0, 3, 5]
carpark_idxs = [0]

size = 6

distance_matrix = np.zeros([size, size])

# add distances
# distances = [
#     (0,1,400), 
#     (1,0,400), (1,2,400), 
#     (2,1,400), (2,3,700), (2,5,400),
#     (3,2,700), (3,4,400),
#     (4,3,400), (4,5,700),
#     (5,2,400), (5,4,700),
#     ]

distances = {
    0: {1: 173.12}, 
    1: {0: 173.12, 2: 117.76}, 
    2: {1: 117.76, 3: 635.71, 4: 26.92}, 
    3: {4: 622.05}, 
    4: {5: 302.64, 6: 27.83}, 
    5: {6: 297.17, 12: 269.05}, 
    6: {8: 11.03, 34: 53.42}, 
    # 7,2,400), 
    8: {2: 14.05, 61: 48.60}, 
    #9,2,400}, 
    10: {2: 310.62}, 
    11: {5: 54.46}, 
    12: {11: 216.70, 13: 18.38}, 
    13: {12: 19.04, 14: 63.24}, 
    14: {13: 62.82, 15: 31.32}, 
    15: {14: 30.00, 16: 25.02}, 
    16: {17: 39.26}, 
    17: {15: 25.05, 18: 44.73}, 
    18: {19: 116.49}, 
    19: {20: 59.18}, 
    20: {21: 28.28}, 
    21: {22: 87.11}, 
    22: {23: 21.73}, 
    23: {24: 15.76, 69: 39.69}, 
    24: {15: 354.23, 22: 15.88, 25: 14.26}, 
    25: {24: 14.26, 26: 8.01, 27: 25.03}, 
    26: {25: 8.01}, 
    27: {25: 25.03}, 
    28: {29: 40.82}, 
    29: {74: 180.94, 30: 32.15}, 
    30: {29: 32.15, 31: 180.82, 78: 30.29}, 
    31: {30: 180.82}, 
    32: {33: 50.58, 75: 273.05}, 
    33: {32: 46.77, 34: 291.19}, 
    34: {6: 53.42, 33: 291.19, 35: 3.00}, 
    35: {34: 3.00}, 
    61: {62: 146.25, 63: 1}, 
    62: {9: 134.62, 64: 6.36}, 
    63: {61: 1}, 
    64: {62: 6.36}, 
    69: {70: 8.55, 71: 310.10}, 
    70: {69: 8.55}, 
    71: {28: 17.98, 72: 4.44}, 
    73: {28: 4.76}, 
    74: {24: 142.97}, 
    75: {32: 273.05, 76: 88.39}, 
    76: {75: 73.87, 77: 148.29}, 
    77: {76: 148.29, 78: 55.88}, 
    78: {30: 30.29, 77: 49.75}, 
}

for dist in distances:
    i = dist[0]
    j = dist[1]
    k = dist[2]
    distance_matrix[i][j] = k

#distance_matrix = [[0,400,0,0,0,0], [400,0,400,0,0,0], [0,400,0,700,0,400], [0,0,700,0,400,0], [0,0,0,400,0,700], [0,0,400,0,700,0]]
#env = QlearningEnv(distance_matrix, carpark_idxs, map)

#Q-Learning

q_table = np.full((size, size), -np.inf)

for dist in distances:
    i = dist[0]
    j = dist[1]
    q_table[i][j] = 0

#Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.5


# def train():
#     for _ in range(100):
        
#         state = env.reset()
#         done = False
        
#         while not done:
#             if random.uniform(0, 1) < epsilon:
#                 action = env.action_sample()
#             else:
#                 action = np.argmax(q_table[state])

#             next_state, reward, done = env.step(action)
#             #print(state, action, next_state, reward, done)

#             old_value = q_table[state][action]
#             next_max = np.max(q_table[next_state])

#             new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
#             q_table[state][action] = new_value

#             state = next_state

#     return q_table

#table = train()
#print(table)


traffic = Traffic([[0, 0, 0],[0, 0, 0],[0, 0, 0]], lambda x : "o",  lambda x : "o", map, (0,1))
traffic.start_simulation()
traffic.run_simulation()






# def generate_distance_matrix(distance_matrix):
#     distance_matrix[1][0] = 200
#     distance_matrix[1][4] = 400
#     distance_matrix[1][5] = 500

#     distance_matrix[2][1] = 100
#     distance_matrix[2][3] = 300

#     distance_matrix[4][0] = 200
#     distance_matrix[4][6] = 300

#     distance_matrix[5][2] = 200
#     distance_matrix[5][9] = 300

#     distance_matrix[6][4] = 300
#     distance_matrix[6][5] = 200
#     distance_matrix[6][7] = 300

#     distance_matrix[8][6] = 300
#     distance_matrix[8][7] = 100

#     distance_matrix[9][8] = 200
#     distance_matrix[9][10] = 400
#     distance_matrix[9][11] = 200

#     distance_matrix[10][3] = 400
#     distance_matrix[10][9] = 400

# def generate_start_node(): 
#     randint = 0
#     while randint in carpark_idxs:
#         randint = random.randint(1, 10)
#     return randint

# distance_matrix = generate_empty_matrix(12)
# generate_distance_matrix(distance_matrix)

# traffic_matrix = generate_traffic_matrix(distance_matrix)

# current_node = generate_start_node()
# print(distance_matrix, 'boo', traffic_matrix)
#[0,400,0],[400,0,300],[0,300,0]

# traffic = Traffic([[0, 400],[400, 0]], carpark_idxs, map)
# traffic.run_simulation()

# arguments = {
#     "distance": distance_matrix,
#     "traffic": traffic_matrix,
#     "position": current_node,
#     "seed": 100   
# }