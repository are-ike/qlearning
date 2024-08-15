import numpy as np
import random
from environment import QlearningEnv
import pygame

map_width = 4000
map_height = 4000

map = pygame.Surface((map_width,map_height))

#carpark_idxs = [0, 3, 5]
carpark_idxs = [0]

size = 6

distance_matrix = np.zeros([size, size])

# add distances
distances = [
    (0,1,400), 
    (1,0,400), (1,2,400), 
    (2,1,400), (2,3,700), (2,5,400),
    (3,2,700), (3,4,400),
    (4,3,400), (4,5,700),
    (5,2,400), (5,4,700),
    ]

for dist in distances:
    i = dist[0]
    j = dist[1]
    k = dist[2]
    distance_matrix[i][j] = k

#distance_matrix = [[0,400,0,0,0,0], [400,0,400,0,0,0], [0,400,0,700,0,400], [0,0,700,0,400,0], [0,0,0,400,0,700], [0,0,400,0,700,0]]
env = QlearningEnv(distance_matrix, carpark_idxs, map)

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


def train():
    for _ in range(100):
        
        state = env.reset()
        done = False
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_sample()
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done = env.step(action)
            #print(state, action, next_state, reward, done)

            old_value = q_table[state][action]
            next_max = np.max(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state][action] = new_value

            state = next_state

    return q_table

table = train()
print(table)









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