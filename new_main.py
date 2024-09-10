import numpy as np
import random
from environment import QlearningEnv
from utils import copy_list
import copy
import pickle
import math
import time
import cProfile

distances = {
    0: {1: 176.00},
    1: {0: 176.00, 167: 14.72},
    2: {167: 103.37, 3: 641.40, 4: 26.92},
    3: {163: 8.54, 164: 80.65},
    4: {5: 300.00, 6: 27.83},
    5: {96: 32.07, 169: 11.55, 170: 9.31}, 
    6: {8: 9.59, 121: 21.14},
    8: {2: 14.05, 122: 20.53}, 
    10: {2: 310.62}, 
    11: {170: 53.37, 98: 3.00}, 
    12: {171: 8.83, 13: 18.10}, 
    13: {172: 9.35, 181: 25.77}, 
    14: {15: 33.40, 173: 8.99}, 
    15: {16: 23.82, 132: 36.04}, 
    16: {17: 39.26}, 
    17: {185: 24.48, 18: 44.73}, 
    18: {65: 4.00, 86: 88.24}, 
    19: {20: 59.18, 66: 4.00}, 
    20: {21: 28.28, 67: 79.52}, 
    21: {22: 87.11, 68: 4.00}, 
    22: {23: 21.73}, 
    23: {24: 15.76, 69: 39.69}, 
    24: {183: 319.15, 22: 15.88, 25: 5.00}, 
    25: {24: 5.00, 27: 10.00}, 
    27: {25: 10.00}, 
    28: {29: 40.82}, 
    29: {126: 139.00, 30: 38.36}, 
    30: {29: 38.36, 31: 16.8, 78: 29.68}, 
    31: {30: 16.8, 105: 133.47, 189: 2.00}, 
    32: {33: 49.32, 118: 151.13}, 
    33: {32: 46.77, 120: 235.98}, 
    34: {35: 1.00, 120: 57.66, 121: 33.51}, 
    35: {34: 1.00}, 
    36: {16: 51.83, 129: 3.00}, 
    37: {38: 6.00, 130: 153.63}, 
    38: {37: 6.00}, 
    39: {79: 1.00, 81: 57.18}, 
    40: {36: 348.01, 81: 17.86}, 
    41: {81: 11.22}, 
    42: {134: 39.41, 85: 17.53}, 
    43: {101: 1.00, 102: 81.28}, 
    44: {43: 58.09, 45: 38.95}, 
    45: {44: 38.95, 87: 14.00, 88: 1.00},
    46: {44: 104.73, 91: 1.00}, 
    47: {46: 75.45}, 
    48: {49: 78.56, 140: 8.40}, 
    49: {48: 82.96, 142: 119.80, 64: 62.10}, 
    50: {47: 56.23, 64: 27.59, 145: 4.00}, 
    51: {146: 49.51, 144: 1.00}, 
    52: {53: 11.11, 157: 6.17, 159: 17.64}, 
    53: {52: 11.11, 54: 11.11}, 
    54: {159: 39.49, 53: 11.11, 161: 94.26}, 
    55: {92: 18.48, 93: 22.46, 161: 22.82}, 
    56: {57: 14.78, 92: 73.86, 95: 1.00 }, 
    57: {56: 14.78}, 
    58: {93: 121.72, 59: 4.00, 60: 63.01}, 
    59: {163: 50.00, 58: 4.00}, 
    60: {163: 81.58}, 
    61: {62: 146.25, 63: 1.00}, 
    62: {9: 95.72, 123: 3.00}, 
    63: {61: 1.00, 120: 1.00, 123: 1.00}, 
    64: {49: 62.10, 50: 27.59, 90: 2.00}, 
    65: {18: 4.00, 86: 4.00}, 
    66: {19: 4.00}, 
    67: {20: 79.52}, 
    68: {21: 4.00}, 
    69: {70: 2.00, 103: 144.09}, 
    70: {69: 2.00}, 
    71: {28: 17.98, 72: 4.44}, 
    73: {28: 4.76}, 
    74: {24: 143.24, 128: 2.00}, 
    75: {114: 7.65, 116: 85.29}, 
    76: {75: 74.13, 112: 30.43}, 
    77: {108: 28.27, 110: 92.48}, 
    78: {30: 29.68, 107: 22.03}, 
    79: {39: 1.00}, 
    80: {40: 17.58}, 
    81: {41: 11.22, 80: 16.61, 82: 123.63}, 
    82: {83: 45.82, 135: 8.17}, 
    83: {85: 51.31, 134: 8.41, 137: 3.00}, 
    84: {42: 15.34}, 
    85: {138: 40.65, 148: 23.89, 84: 20.44}, 
    86: {19: 25.84, 65: 4.00},
    87: {45: 14.00},
    88: {45: 1.00},
    90: {64: 2.00},
    91: {46: 1.00},
    92: {55: 18.48, 56: 73.86, 95: 1.00 },
    93: {55: 22.46, 58: 121.72, 94: 27.64},
    94: {93: 27.64, 186: 3.00, 187: 3.00},
    95: {92: 1.00, 56: 1.00 },
    96: {174: 160.45, 97: 5.00},
    97: {96: 5.00},
    98: {11: 3.00},
    99: {100: 5.00, 141: 43.17},
    100: {99: 5.00, 141: 3.00},
    101: {43: 1.00, 102: 1.00},
    102: {84: 223.24, 101: 1.00},
    103: {104: 145.57, 124: 2.00},
    104: {71: 18.90},
    105: {31: 133.47, 106: 74.83, 190: 2.00},
    106: {105: 74.83},
    107: {77: 28.86},
    108: {78: 28.00, 109: 34.45},
    109: {108: 34.45},
    110: {77: 92.48, 111: 2.00, 112: 26.67},
    111: {110: 2.00},
    112: {76: 30.43, 110: 26.67, 113: 2.00},
    113: {112: 2.00},
    114: {76: 80.73, 115: 22.75},
    115: {114: 22.75},
    116: {75: 85.29, 117: 40.66, 118: 38.56},
    117: {116: 40.66},
    118: {32: 151.13, 116: 38.56, 119: 57.53},
    119: {118: 57.53},
    120: {33: 235.98, 34: 57.66, 63: 1.00},
    121: {6: 21.14, 34: 33.51, 122: 16.39},
    122: {61: 28.73},
    123: {62: 3.00, 63: 1.00},
    124: {103: 2.00},
    125: {104: 2.00},
    126: {74: 41.82, 127: 2.00},
    127: {126: 2.00},
    128: {74: 2.00},
    129: {36: 3.00},
    130: {39: 94.77, 131: 3.00},
    131: {130: 3.00},
    132: {37: 77.91, 133: 2.00},
    133: {132: 2.00},
    134: {83: 8.41, 135: 46.48, 136: 3.00},
    135: {80: 107.91, 82: 8.17},
    136: {134: 3.00},
    137: {83: 3.00},
    138: {48: 93.43, 139: 4.00},
    139: {138: 4.00},
    140: {99: 6.00},
    141: {84: 80.18, 100: 3.00},
    142: {49: 119.80, 146: 139.44, 143: 4.00},
    143: {142: 4.00},
    144: {51: 1.00},
    145: {50: 4.00},
    146: {51: 49.51, 142: 139.44, 147: 1.00},
    147: {146: 1.00},
    148: {85: 23.89, 149: 2.00, 150: 16.10},
    149: {148: 2.00},
    150: {148: 16.10, 151: 17.14, 157: 31.29},
    151: {150: 17.14, 152: 2.00, 153: 27.10},
    152: {151: 2.00},
    153: {151: 27.10, 154: 24.35, 155: 27.59},
    154: {153: 24.35},
    155: {153: 27.59, 156: 2.00, 157: 69.85},
    156: {155: 2.00},
    157: {150: 31.29},
    158: {191: 4.00},
    159: {52: 17.64, 54: 39.49, 160: 3.00},
    160: {159: 3.00},
    161: {54: 94.26, 55: 22.82, 162: 2.00},
    162: {161: 2.00},
    163: {3: 8.54, 165: 133.32},
    164: {60: 5.67, 188: 5.67},
    165: {4: 492.54, 166: 6.00},
    166: {165: 6.00},
    167: {1: 14.72, 2: 103.37, 168: 6.00}, -
    168: {167: 6.00}, -
    169: {5: 11.55},
    170: {5: 9.31, 6: 314.11},
    171: {175: 80.03, 12: 8.83, 179: 6.00},
    172: {13: 9.35, 171: 17.62, 180: 6.00},
    173: {172: 64.83, 14: 8.99, 184: 2.00},
    174: {12: 80.25, 175: 8.96, 177: 2.00},
    175: {174: 8.96, 176: 57.12},
    176: {11: 79.56, 178: 3.00},
    177: {174: 2.00},
    178: {176: 3.00},
    179: {171: 6.00},
    180: {172: 6.00},
    181: {14: 37.71, 182: 6.00},
    182: {181: 6.00},
    183: {185: 34.37},
    184: {183: 4.00},
    185: {15: 11.80, 173: 32.09},
    186: {94: 3.00},
    187: {94: 3.00},
    188: {58: 63.01},
    189: {31: 63.01},
    190: {105: 2.00},
    191: {52: 6.17, 155: 69.85, 158: 4.00},
}

carpark_idxs = [0,25,27,35,38,53,57,59,63,65,66,67,68,70,79,87,88,90,91,94,95,97,98,100,101,105]


def argmax(dict):
    return max(dict, key=dict.get)

def maxa(dict):
    return max(dict.values())

#Q-Learning

env = QlearningEnv(distances, carpark_idxs, hotspots.keys(), map)

#Hyperparameters
max_epsilon = 1.0           
min_epsilon = 0.05           
decay_rate = 0.0005 
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
    trend = []
    
    for episode in range(1, episodes + 1):
        prev_q_table = copy.deepcopy(q_table) 
        deadend = False
        #Decay epsilon
        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
        
        state, init_cars = env.reset(episode, episodes)
        done = False
        timesteps_ep = 0
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_sample()
            else:
                action = argmax(q_table[state])

            next_state, reward, done, deadend, distance, cars, visited = env.step(action) 
            
            
            #metrics
            rewards += reward
            timesteps_ep += 1
            distance_travelled += distance
            cars_seen += cars

            if deadend or timesteps_ep >= 200: 
                done = True
            
            old_value = q_table[state][action]
            next_max = maxa(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state][action] = new_value

            state = next_state
          
        
        total_cars += init_cars
        timesteps += timesteps_ep
        if episode % 100 == 0: trend.append((episode, rewards, timesteps))
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
        rewards, 
        timesteps, 
        distance_travelled, 
        has_converged, 
        true_convergence, 
        eps_to_convergence, 
        cars_seen, 
        total_cars,
        successful_episodes,
        episodes,
        trend)

def calc_metrics(metrics):
    prev_q_table, q_table, rewards, timesteps, distance_travelled, has_converged, true_convergence, eps_to_convergence, cars_seen, total_cars, successful_episodes, episodes, trend = metrics
    avg_reward = rewards / episodes
    avg_timesteps = timesteps / episodes
    avg_distance = distance_travelled / episodes
    cars_perc = (cars_seen / total_cars) * 100
    success_rate = (successful_episodes / episodes) * 100

    # print(prev_q_table)
    print(q_table)
    print(trend)
    print('\n\n ================================================')
    print(
        f"Episodes: {episodes} \n" +
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
            if math.isinf(prev_table[key][key2]) and math.isinf(curr_table[key][key2]):
                diff = 0
            else:
                diff = abs(prev_table[key][key2] - curr_table[key][key2])
            if diff > highest_con:
                highest_con = diff

    if highest_con < convergence_threshold:
        return True
    return False


learning_rates = [0.1, 0.3, 0.5, 0.7]
discount_factors = [0.1, 0.6, 0.8, 0.95]

def tune():
    episodes = 1000
    num = 1
    for rate in learning_rates:
        for disc in discount_factors:
            q_table = copy_list(distances)
            q_table[9] = {0: -np.inf}
            q_table[72] = {0: -np.inf}

            result = train(alpha=rate, gamma=disc, q_table=q_table, episodes=episodes, decay_rate=0.0029)

            with open(f'q_table{num}.pkl', 'wb') as data:
                pickle.dump(q_table, data)
            num+= 1

            print(f"{rate} {disc} \n -------------------------- \n")
            calc_metrics(result)

def train2(episodes,q_table, options):
    rewards = 0
    timesteps = 0
    distance_travelled = 0
    total_cars = 0
    cars_seen = 0
    successful_episodes = 0
    
    for episode in range(1, episodes + 1):
        
        deadend = False
        done = False
       
        state, init_cars = env.reset(episode, episodes, options)
        
        while not done:
            action = argmax(q_table[state])
            
            next_state, reward, done, deadend, distance, cars, visited = env.step(action) 
            
            # print(state, next_state, visited, action)
            # print(q_table[state])

            print(f'current state: {state}')
            print('----------------------')
            for ac, vl in q_table[state].items():
                print(f'action:{ac}, value: {int(vl)}')
            print(f"selected action: {next_state}")
            print('----------------------')
            print('=====================')

            #metrics
            rewards += reward
            timesteps += 1
            distance_travelled += distance
            cars_seen += cars

            if deadend: 
                done = True

            state = next_state
          
        
        total_cars += init_cars

        if not deadend: 
            successful_episodes += 1

    return (
        rewards, 
        timesteps, 
        distance_travelled, 
        cars_seen, 
        total_cars,
        successful_episodes,
        episodes)

def calc_metrics2(metrics):
    rewards, timesteps, distance_travelled, cars_seen, total_cars, successful_episodes, episodes = metrics
    avg_reward = rewards / episodes
    avg_timesteps = timesteps / episodes
    avg_distance = distance_travelled / episodes
    cars_perc = (cars_seen / total_cars) * 100
    success_rate = (successful_episodes / episodes) * 100

    print('\n\n ================================================')
    print(
        f"Episodes: {episodes} \n" +
        f"Average Reward per Episode: {avg_reward} \n" +  
        f"Average Timesteps per Episode: {avg_timesteps} \n" + 
        f"Average Distance Traveled per Episode: {avg_distance} \n" + 
        f"Percentage of Cars Encountered: {cars_perc} \n" +
        f"Number of Cars Encountered: {cars_seen} \n" +
        f"Number of Cars: {total_cars} \n" +
        f"Success Rate: {success_rate} \n" 
        )

def evall(val):
    #num = 1
    for num in range(1):
        data = {0: {1: np.float64(202.17842231630857)}, 1: {0: np.float64(253.6433701654311), 2: np.float64(167.51263419469572)}, 2: {1: np.float64(197.07577930875814), 3: np.float64(211.5792897443714), 4: np.float64(137.01379357397798)}, 3: {4: np.float64(130.11007105881384), 59: np.float64(273.0631179208947), 60: np.float64(167.56364436796886)}, 4: {5: np.float64(153.49773804208698), 6: np.float64(171.94863631869248)}, 5: {6: np.float64(166.2133220984237), 96: np.float64(218.86071934576964)}, 6: {8: np.float64(175.16408662665202), 34: np.float64(205.44175053015772)}, 8: {2: np.float64(163.92166092914732), 61: np.float64(217.33723632662253)}, 10: {2: np.float64(163.17779868320446)}, 11: {5: np.float64(174.9109360954256), 98: np.float64(270.0377558808626)}, 12: {11: np.float64(219.00710573902836), 13: np.float64(138.2803610662276)}, 13: {12: np.float64(174.45257394376642), 14: np.float64(137.8620247899293)}, 14: {13: np.float64(138.3915077297601), 15: np.float64(170.385936874839)}, 15: {14: np.float64(133.09210488043257), 16: np.float64(133.31790419828096), 37: np.float64(213.51919977537887)}, 16: {17: np.float64(166.14613362849897)}, 17: {15: np.float64(167.04981179696273), 18: np.float64(211.2155668019434)}, 18: {65: np.float64(266.4548275703541), 86: np.float64(207.93996939112182)}, 19: {20: np.float64(213.76514931624038), 66: np.float64(269.44221346593474)}, 20: {21: np.float64(217.60179752847128), 67: np.float64(268.11087348324145)}, 21: {22: np.float64(138.11270830797616), 68: np.float64(271.5473116175993)}, 22: {23: np.float64(171.6576636476762)}, 23: {24: np.float64(170.1210169705509), 69: np.float64(217.9309260623918)}, 24: {15: np.float64(156.45000570976015), 22: np.float64(135.66043695316225), 25: np.float64(216.9334348391145)}, 25: {24: np.float64(166.061296000227), 26: np.float64(268.2485717293546), 27: np.float64(273.97514535424546)}, 26: {25: np.float64(219.04413464300717)}, 27: {25: np.float64(218.4917236352253)}, 28: {29: np.float64(108.2418158714311)}, 29: {74: np.float64(134.68058836656354), 30: np.float64(81.20878774381356)}, 30: {29: np.float64(107.27954044657558), 31: np.float64(65.04365943602598), 78: np.float64(63.481886027799696)}, 31: {30: np.float64(83.4864384885891)}, 32: {33: np.float64(163.43080685294376), 75: np.float64(92.38861399601338)}, 33: {32: np.float64(124.95666540593572), 34: np.float64(206.97835188245787)}, 34: {6: np.float64(168.45111459980504), 33: np.float64(165.8963904690619), 35: np.float64(266.63760814702187)}, 35: {34: np.float64(216.3527935940943)}, 36: {16: np.float64(130.39190814962166)}, 37: {38: np.float64(271.42521345611124), 39: np.float64(203.61668521086995)}, 38: {37: np.float64(214.80040948592838)}, 39: {79: np.float64(270.0516209919573), 81: np.float64(87.58418590991177)}, 40: {36: np.float64(102.8661060468883), 81: np.float64(87.21812650324551)}, 41: {81: np.float64(86.5366949043568)}, 42: {83: np.float64(135.9764474332386), 85: np.float64(171.95479379214714)}, 43: {101: np.float64(273.95415874784186), 102: np.float64(85.87737311308045)}, 44: {43: np.float64(215.3848476637115), 45: np.float64(219.67954751112018)}, 45: {44: np.float64(172.17509120850505), 87: np.float64(269.7819719002381), 88: np.float64(272.03833674345947)}, 46: {44: np.float64(174.4140822002826), 91: np.float64(270.94560523680695)}, 47: {46: np.float64(220.6870158916941)}, 48: {49: np.float64(173.04581385193285), 99: np.float64(216.77393199651289)}, 49: {48: np.float64(175.26448810339767), 51: np.float64(131.91298409035613), 64: np.float64(215.91846103127511)}, 50: {47: np.float64(176.47393753226174), 64: np.float64(217.43096626801264)}, 51: {49: np.float64(173.73299275121082)}, 52: {53: np.float64(271.0211181046088), 54: np.float64(216.66369982934827), 85: np.float64(169.3289600945744)}, 53: {52: np.float64(213.27853094347398), 54: np.float64(215.9021626590692)}, 54: {52: np.float64(217.27100832009245), 53: np.float64(268.0858498102266), 55: np.float64(174.22793291192698)}, 55: {54: np.float64(216.54459434581997), 92: np.float64(219.68963431761958), 93: np.float64(210.95375599126686)}, 56: {57: np.float64(270.4388327245282), 92: np.float64(219.3901178594965), 95: np.float64(275.1510150043298)}, 57: {56: np.float64(218.98529718914796)}, 58: {93: np.float64(213.88523041451467), 59: np.float64(272.19463491473545), 60: np.float64(168.69974455813167)}, 59: {3: np.float64(214.17760556097284), 58: np.float64(216.81913885744297)}, 60: {3: np.float64(213.28735041137196), 58: np.float64(206.85768818365887)}, 61: {62: np.float64(217.86410088974492), 63: np.float64(271.8316408867156)}, 62: {9: np.float64(-np.inf), 63: np.float64(273.0568644192279)}, 63: {61: np.float64(215.16298858951131), 62: np.float64(217.11794744265205)}, 64: {49: np.float64(173.3324558120794), 50: np.float64(168.75710485256616), 90: np.float64(270.1738113921856)}, 65: {86: np.float64(214.0202294206195)}, 66: {19: np.float64(216.91677020934537)}, 67: {20: np.float64(215.61083673397187)}, 68: {21: np.float64(219.4406902834062)}, 69: {70: np.float64(274.58553065085397), 71: np.float64(66.36148117570993)}, 70: {69: np.float64(219.23511812644023)}, 71: {28: np.float64(87.11803114774247), 72: np.float64(-np.inf)}, 73: {28: np.float64(86.67335951337984)}, 74: {24: np.float64(169.83325618553485)}, 75: {32: np.float64(129.20709899873225), 76: np.float64(75.68541631974576)}, 76: {75: np.float64(104.81745442693196), 77: np.float64(62.853589063803135)}, 77: {76: np.float64(80.36657144391398), 78: np.float64(68.70931176696529)}, 78: {30: np.float64(85.7157184732775), 77: np.float64(65.68039922703349)}, 79: {39: np.float64(217.48019001691745)}, 80: {40: np.float64(82.24014546008216)}, 81: {41: np.float64(64.1997083808547), 80: np.float64(61.69804043877931), 82: np.float64(108.86989571759696)}, 82: {80: np.float64(63.06117412994661), 83: np.float64(137.50234633941926)}, 83: {82: np.float64(106.42703391626036), 85: np.float64(171.26676634706823)}, 84: {42: np.float64(135.8641324370955)}, 85: {48: np.float64(175.07270166621777), 52: np.float64(215.71288615327916), 84: np.float64(103.9539772658988)}, 86: {19: np.float64(218.32584086024585), 65: np.float64(266.4940460856527)}, 87: {45: np.float64(218.9457005389325)}, 88: {45: np.float64(219.69823214415487)}, 90: {64: np.float64(218.07728267955568)}, 91: {46: np.float64(218.93661043657175)}, 92: {55: np.float64(170.99072550090708), 56: np.float64(220.19380120778072), 95: np.float64(275.45224419808386)}, 93: {55: np.float64(175.17191724053146), 58: np.float64(215.6943289030683), 94: np.float64(273.16727433238873)}, 94: {93: np.float64(216.61563887483035)}, 95: {92: np.float64(217.47365144693526), 56: np.float64(219.3764780259696)}, 96: {12: np.float64(174.41839995380573), 97: np.float64(268.7594214476127)}, 97: {96: np.float64(216.5480895378247)}, 98: {11: np.float64(217.92146552182487)}, 99: {84: np.float64(107.73304363990005), 100: np.float64(271.1461337454662)}, 100: {99: np.float64(218.6828267118327)}, 101: {43: np.float64(217.58880459113692), 102: np.float64(85.63182106172334)}, 102: {84: np.float64(106.75617543294081)}, 9: {0: -np.inf}, 72: {0: -np.inf}}

        
        result = train2(1, data, val)
    
        #print(num)
        
        # print(f"{num} \n -------------------------- \n")
        #calc_metrics2(result)

evall(73)
