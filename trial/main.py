import numpy as np
import random
from environment import QlearningEnv
import pygame
from traffic import Traffic


map_width = 4000
map_height = 4000

map = pygame.Surface((map_width,map_height))

carpark_idxs = [0, 3, 5]
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

distance_matrix = [[0,400,0,0,0,0], [400,0,400,0,0,0], [0,400,0,700,0,400], [0,0,700,0,400,0], [0,0,0,400,0,700], [0,0,400,0,700,0]]
env = QlearningEnv(distance_matrix, carpark_idxs, map)

#Q-Learning

q_table = np.full((size, size), -np.inf)

for dist in distances:
    i = dist[0]
    j = dist[1]
    q_table[i][j] = 0

# #Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.5


def train():
    for _ in range(100):
        print('====')
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


# traffic = Traffic([[0, 0, 0],[0, 0, 0],[0, 0, 0]], lambda x : "o",  lambda x : "o", map, (0,1))
# traffic.start_simulation()
# traffic.run_simulation()

