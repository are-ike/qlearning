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
    3: {4: 622.05, 59: 61.71, 60: 83.97}, 
    4: {5: 302.64, 6: 27.83}, 
    5: {6: 297.17, 12: 269.05}, 
    6: {8: 11.03, 34: 53.42}, 
    8: {2: 14.05, 61: 48.60}, 
    10: {2: 310.62}, 
    11: {5: 54.46}, 
    12: {11: 216.70, 13: 18.38}, 
    13: {12: 19.04, 14: 63.24}, 
    14: {13: 62.82, 15: 31.32}, 
    15: {14: 30.00, 16: 25.02, 37: 114.93}, 
    16: {17: 39.26}, 
    17: {15: 25.05, 18: 44.73}, 
    18: {19: 116.49, 65: 12.41}, 
    19: {20: 59.18, 66: 7.21}, 
    20: {21: 28.28, 67: 79.52}, 
    21: {22: 87.11, 68: 9.69}, 
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
    36: {16: 51.83}, 
    37: {38: 9.22, 39: 245.08}, 
    38: {37: 9.22}, 
    39: {79: 6.70, 81: 60.06}, 
    40: {36: 348.01, 81: 17.86}, 
    41: {81: 11.22}, 
    42: {83: 41.34, 85: 17.53}, 
    43: {84: 218.10, 86: 1}, 
    44: {43: 63.49, 45: 38.95}, 
    45: {44: 38.95, 87: 14.00, 88: 1},
    46: {44: 104.73, 91: 1}, 
    47: {46: 75.45}, 
    48: {49: 78.56, 84: 129.21, 89: 22.66}, 
    49: {48: 82.96, 50: 88.22, 51: 310.99}, 
    50: {47: 56.23, 49: 88.22, 90: 2}, 
    51: {49: 310.99}, 
    52: {53: 11.11, 54: 61.78, 85: 186.64}, 
    53: {52: 11.11, 54: 11.11}, 
    54: {52: 61.78, 53: 11.11, 55: 116.91}, 
    55: {54: 116.91, 92: 18.48, 93: 22.46}, 
    56: {57: 14.78, 92: 73.86, 95: 1 }, 
    57: {56: 14.78}, 
    58: {93: 121.72, 59: 13.42, 60: 64.23}, 
    59: {3: 61.71, 58: 13.42}, 
    60: {3: 79.79, 58: 64.23}, 
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
    80: {40: 17.58}, 
    81: {41: 11.22, 80: 16.61, 82: 125.34}, 
    82: {80: 108.83, 83: 47.92}, 
    83: {82: 48.40, 85: 51.31}, 
    84: {42: 15.34}, 
    85: {48: 133.55, 52: 186.64, 84: 20.44}, 
    92: {55: 18.48, 56: 73.86, 95: 1 },
    93: {55: 22.46, 58: 121.72, 94: 23.71},
    94: {93: 23.71},
    95: {92: 1, 56: 1 },
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