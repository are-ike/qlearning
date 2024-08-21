import numpy as np
import random
from environment import QlearningEnv
#import pygame
#from traffic import Traffic
from utils import copy_list
import copy
import pickle

# map_width = 20000
# map_height = 20000

# map = pygame.Surface((map_width,map_height))

distances = {
    0: {1: 173.12}, 
    1: {0: 173.12, 2: 117.76}, 
    2: {1: 117.76, 3: 635.71, 4: 26.92}, 
    3: {4: 622.05, 59: 61.71, 60: 83.97}, 
    4: {5: 300.00, 6: 27.83}, 
    5: {6: 297.17, 96: 32.28}, 
    6: {8: 11.03, 34: 53.42}, 
    8: {2: 14.05, 61: 48.60}, 
    10: {2: 310.62}, 
    11: {5: 54.46, 98: 3}, 
    12: {11: 216.70, 13: 18.38}, 
    13: {12: 19.04, 14: 63.24}, 
    14: {13: 62.82, 15: 31.32}, 
    15: {14: 30.00, 16: 25.02, 37: 114.93}, 
    16: {17: 39.26}, 
    17: {15: 25.05, 18: 44.73}, 
    18: {65: 4.00, 86: 88.24}, 
    19: {20: 59.18, 66: 4.00}, 
    20: {21: 28.28, 67: 79.52}, 
    21: {22: 87.11, 68: 4.00}, 
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
    37: {38: 6.00, 39: 245.08}, 
    38: {37: 6.00}, 
    39: {79: 3.00, 81: 60.06}, 
    40: {36: 348.01, 81: 17.86}, 
    41: {81: 11.22}, 
    42: {83: 41.34, 85: 17.53}, 
    43: {101: 1.00, 102: 81.28}, 
    44: {43: 58.09, 45: 38.95}, 
    45: {44: 38.95, 87: 14.00, 88: 1.00},
    46: {44: 104.73, 91: 1.00}, 
    47: {46: 75.45}, 
    48: {49: 78.56, 99: 6.00}, 
    49: {48: 82.96, 51: 310.99, 64: 62.10}, 
    50: {47: 56.23, 64: 27.59}, 
    51: {49: 310.99}, 
    52: {53: 11.11, 54: 61.78, 85: 186.64}, 
    53: {52: 11.11, 54: 11.11}, 
    54: {52: 61.78, 53: 11.11, 55: 116.91}, 
    55: {54: 116.91, 92: 18.48, 93: 22.46}, 
    56: {57: 14.78, 92: 73.86, 95: 1.00 }, 
    57: {56: 14.78}, 
    58: {93: 121.72, 59: 13.42, 60: 64.23}, 
    59: {3: 61.71, 58: 13.42}, 
    60: {3: 79.79, 58: 64.23}, 
    61: {62: 146.25, 63: 1.00}, 
    62: {9: 134.62, 63: 6.36}, 
    63: {61: 1.00, 62: 6.36}, 
    64: {49: 62.10, 50: 27.59, 90: 2.00}, 
    65: {86: 4.00}, 
    66: {19: 4.00}, 
    67: {20: 79.52}, 
    68: {21: 4.00}, 
    69: {70: 8.55, 71: 310.10}, 
    70: {69: 8.55}, 
    71: {28: 17.98, 72: 4.44}, 
    73: {28: 4.76}, 
    74: {24: 142.97}, 
    75: {32: 273.05, 76: 88.39}, 
    76: {75: 73.87, 77: 148.29}, 
    77: {76: 148.29, 78: 55.88}, 
    78: {30: 30.29, 77: 49.75}, 
    79: {39: 3.00}, 
    80: {40: 17.58}, 
    81: {41: 11.22, 80: 16.61, 82: 125.34}, 
    82: {80: 108.83, 83: 47.92}, 
    83: {82: 48.40, 85: 51.31}, 
    84: {42: 15.34}, 
    85: {48: 133.55, 52: 186.64, 84: 20.44}, 
    86: {19: 25.84, 65: 4.00},
    87: {45: 14.00},
    88: {45: 1.00},
    90: {64: 2.00},
    91: {46: 1.00},
    92: {55: 18.48, 56: 73.86, 95: 1.00 },
    93: {55: 22.46, 58: 121.72, 94: 23.71},
    94: {93: 23.71},
    95: {92: 1.00, 56: 1.00 },
    96: {12: 240.73, 97: 5.00},
    97: {96: 5.00},
    98: {11: 3.00},
    99: {84: 122.42, 100: 6.00},
    100: {99: 5.00},
    101: {43: 1.00, 102: 1.00},
    102: {84: 223.24},
}

#carpark_idxs = [26,27,35,53,57,59,63,64,65,66,67,68,70,79,86,87,88,89,90,91,94,95]
carpark_idxs = [0,26,27,35,38,53,57,59,63,65,66,67,68,70,79,87,88,90,91,94,95,97,98,100,101]


def argmax(dict):
    return max(dict, key=dict.get)

def maxa(dict):
    return max(dict.values())

#Q-Learning

env = QlearningEnv(distances, carpark_idxs, map)

# #Hyperparameters
max_epsilon = 1.0           
min_epsilon = 0.05           
decay_rate = 0.0005 #0.00005
convergence_threshold = 0.01


def train(episodes, alpha, gamma, q_table, decay_rate=decay_rate):
    rewards = 0
    timesteps = 0
    distance_travelled = 0
    total_cars = 0
    cars_seen = 0
    has_converged = False
    true_convergence = False
    eps_to_convergence = episodes
    successful_episodes = 0
    

    for episode in range(1, episodes + 1):
        prev_q_table = copy.deepcopy(q_table) 
        deadend = False
        #Decay epsilon
        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
        
        state, init_cars, avail_parks = env.reset()
        done = False
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_sample()
            else:
                action = argmax(q_table[state])

            next_state, reward, done, deadend, distance, cars, visited = env.step(action) 
            

            #metrics
            rewards += reward
            timesteps += 1
            distance_travelled += distance
            cars_seen += cars

            if deadend: 
                done = True
            
            old_value = q_table[state][action]
            next_max = maxa(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state][action] = new_value

            state = next_state
           
        
        total_cars += init_cars

        if not deadend: 
            successful_episodes += 1

        if convergence(prev_q_table, q_table) and not has_converged:
            has_converged = True
            eps_to_convergence = episode

        if convergence(prev_q_table, q_table) and has_converged:
            if episode == 0.5 * episodes + eps_to_convergence:
                true_convergence = True

        if not convergence(prev_q_table, q_table) and has_converged:
            has_converged = False
            eps_to_convergence = episodes
            if true_convergence: true_convergence = False
        

    return (
        prev_q_table, 
        q_table, 
        avail_parks, 
        rewards, 
        timesteps, 
        distance_travelled, 
        has_converged, 
        true_convergence, 
        eps_to_convergence, 
        cars_seen, 
        total_cars,
        successful_episodes,
        episodes)

def calc_metrics(metrics):
    prev_q_table, q_table, avail_parks, rewards, timesteps, distance_travelled, has_converged, true_convergence, eps_to_convergence, cars_seen, total_cars, successful_episodes, episodes = metrics
    avg_reward = rewards / episodes
    avg_timesteps = timesteps / episodes
    avg_distance = distance_travelled / episodes
    cars_perc = (cars_seen / total_cars) * 100
    success_rate = (successful_episodes / episodes) * 100

    # print(prev_q_table)
    print(q_table)
    print('\n\n ================================================')
    print(
        f"Episodes: {episodes} \n" +
        f"Available Carparks: {avail_parks} \n" +
        f"Average Reward per Episode: {avg_reward} \n" +  
        f"Average Timesteps per Episode: {avg_timesteps} \n" + 
        f"Average Distance Traveled per Episode: {avg_distance} \n" + 
        f"Convergence: {has_converged} \n" +  
        f"True Convergence: {true_convergence}  \n" + 
        f"Episodes to Convergence: {eps_to_convergence} \n" + 
        f"Percentage of Cars Encountered: {cars_perc} \n" +
        f"Number of Cars Encountered: {cars_seen} \n" +
        f"Number of Cars: {total_cars} \n" +
        f"Success Rate: {success_rate} \n" 
        )

def convergence(prev_table, curr_table):
    highest_con = 0
    for key, value in prev_table.items():
        for key2, _ in value.items():
            diff = abs(prev_table[key][key2] - curr_table[key][key2])
            if diff > highest_con:
                highest_con = diff

    if highest_con < convergence_threshold:
        return True
    return False

# q_table = copy_list(distances)
# q_table[9] = {0: 0}
# q_table[72] = {0: 0}

# result = train(alpha=0.1, gamma=0.6, q_table=q_table, episodes=1)
# calc_metrics(result)




# traffic = Traffic([[0, 0, 0],[0, 0, 0],[0, 0, 0]], lambda x : "o",  lambda x : "o", map, (0,1))
# traffic.start_simulation()
# traffic.run_simulation()

learning_rates = [0.1, 0.3, 0.5, 0.7]
discount_factors = [0.1, 0.6, 0.8, 0.95]
def tune():
    episodes = 10000
    num = 1
    for rate in learning_rates:
        for disc in discount_factors:
            q_table = copy_list(distances)
            q_table[9] = {0: 0}
            q_table[72] = {0: 0}

            result = train(alpha=rate, gamma=disc, q_table=q_table, episodes=episodes)

            with open(f'q_table{num}.pkl', 'wb') as data:
                pickle.dump(q_table, data)
            num+= 1

            print(f"{rate} {disc} \n -------------------------- \n")
            calc_metrics(result)
tune()
def random_carparks():
    return np.random.choice(carpark_idxs, size=np.random.choice(range(3, len(carpark_idxs) + 1)), replace=False)

def generate_scenarios(cs, times):
    options = []
    carpark_scenarios =[[27, 35, 38, 53, 90], [63, 64, 87, 26], [87,  91], [35, 64], [0, 59, 95, 57, 63, 64, 26, 27]]
    carpark_scenarios =[[88,90,91,94,95], [0,26,27,35], [53,57,59,63,95], [88,66], [26,43,90,0,70,35]]
    carpark_scenarios.append(random_carparks())
    carpark_scenarios.append(random_carparks())

    traffic_scenarios = ["light", "medium", "heavy"]

    for node in [pos for pos in distances.keys() if pos not in carpark_idxs]:
        for traffic in traffic_scenarios:
            for carpark in carpark_scenarios:
                option = {
                    "traffic": traffic,
                    "carparks": carpark,
                    "start": node
                }

                options.append(option)


    