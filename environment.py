import gymnasium
import numpy as np
from gymnasium.spaces import Box, Dict
from traffic import Traffic
from utils import copy_list

class QlearningEnv(gymnasium.Env):
    def __init__(self, distances, carparks, map):
        super(QlearningEnv, self).__init__()

        self.size =9

        self.observation_space = Dict({
            "distance": Box(high=10000, low=-10000, shape=(self.size, self.size)), 
            "traffic": Box(high=1, low=0, shape=(self.size, self.size))
            })
        self.action_space = Box(high=1, low=0, shape=(self.size,))

        self.current_observation = None
        self.current_action = None
        self.agent_position = None     
        self.traffic_matrix = None
        self.qtable = None
        self.distances = distances
        self.carparks = carparks
        self.traffic_obj = None
        self.agent_is_moving = False
        self.visited = {}
        self.map = map

    def step(self, action): 
        #self.traffic_obj.start_agent(self.agent_position, action)
        distance = self.distances[self.agent_position][action]
        traffic = self.traffic_matrix[self.agent_position][action]

        reward = - (distance/10) - (11*traffic)

        self.agent_position = action
        if self.agent_position in self.visited.keys(): 
            self.visited[self.agent_position] += 1 
        else:
            self.visited[self.agent_position] = 1 

        self.update_traffic()

        terminated = action in self.avail_carparks
        leaving = action not in self.distances.keys()

        if terminated: reward += 500
        if leaving: reward -= 1000
        if action in self.carparks and not terminated: reward -= 100
        reward -= (self.visited[self.agent_position] - 1) * 100

        return action, reward, terminated, leaving, distance, traffic, self.visited
        

    def reset(self, seed=None, options=None): 
        if not options:
            super().reset(seed=seed)
            total_cars = self.generate_traffic()
            self.avail_carparks = self.np_random.choice(self.carparks, size=self.np_random.choice(range(3, len(self.carparks) + 1)), replace=False)
            position = self.get_agent_start_position()
            self.agent_position = position[0]
            self.visited[self.agent_position] = 1
        else:
            super().reset(seed=seed)
            total_cars = self.generate_traffic(choice=options["traffic"])
            self.avail_carparks = options["carparks"]
            #position = options["start"]
            self.agent_position = options["start"]
            self.visited[self.agent_position] = 1

        #traffic = Traffic(self.traffic_matrix, self.get_traffic, self.set_traffic,self.map, position)
        #traffic.set_agent_is_moving = self.set_agent_is_moving
        #elf.traffic_obj = traffic
        #print(position)
        #traffic.start_simulation()


        
        return self.agent_position, total_cars, self.avail_carparks

    def render(self): pass
  
    def close(self): 
        self.traffic_obj.quit()
    
    def action_sample(self):
        options = []

        for key, value in self.distances.items():
            if key == self.agent_position:
                for key2, _ in value.items():
                    options.append(key2)

        return self.np_random.choice(options)
    
    def get_agent_start_position(self):
        i_options = [pos for pos in self.distances.keys() if pos not in self.carparks]
        i = self.np_random.choice(i_options)
        j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]

        while not j_options:
            i = self.np_random.choice(i_options)
            j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]
        j = self.np_random.choice(j_options)

        return (i,j)

    def generate_traffic(self, choice=None):
        if not choice: choice = self.np_random.choice(['light', 'medium', 'heavy'])
        traffic = copy_list(self.distances, False)
        total = 0

        for key, value in traffic.items():
            for key2, value2 in value.items():
                if value2 < 10 or key2 in self.carparks:
                    if choice == 'heavy':
                        traffic[key][key2] = self.np_random.choice([0,1])
                    else:
                        traffic[key][key2] = 0

                if value2 > 10 and value2 <= 50:
                    if choice == 'light':
                        traffic[key][key2] = 0
                    elif choice == 'medium':
                        traffic[key][key2] = self.np_random.choice([0,1])
                    else:
                        traffic[key][key2] = self.np_random.choice([1,2])
         
                if value2 > 50 and value2 <= 100:
                    if choice == 'light':
                        traffic[key][key2] = self.np_random.choice([0,1])
                    elif choice == 'medium':
                        traffic[key][key2] = self.np_random.choice([1,2])
                    else:
                        traffic[key][key2] = self.np_random.choice([2,3])

                if value2 > 100 and value2 <= 200:
                    if choice == 'light':
                        traffic[key][key2] = self.np_random.choice([0,1,2])
                    elif choice == 'medium':
                        traffic[key][key2] = self.np_random.choice([2,3])
                    else:
                        traffic[key][key2] = self.np_random.choice([3,4])
        
                if value2 > 200 and value2 <= 300:
                    if choice == 'light':
                        traffic[key][key2] = self.np_random.choice([0,1,2,3])
                    elif choice == 'medium':
                        traffic[key][key2] = self.np_random.choice([4,5])
                    else:
                        traffic[key][key2] = self.np_random.choice([5,6,7])

                if value2 > 300:
                    if choice == 'light':
                        traffic[key][key2] = self.np_random.choice([0,1,2,3])
                    elif choice == 'medium':
                        traffic[key][key2] = self.np_random.choice([4,5])
                    else:
                        traffic[key][key2] = self.np_random.choice([5,6,7])

                total += traffic[key][key2]

        self.traffic_matrix = traffic
        return total
    
    def get_traffic(self):
        return self.traffic_matrix
    
    def set_traffic(self, new_traffic):
        self.traffic_matrix = new_traffic

    def update_traffic(self):
        prob1 = 0.6
        prob2 = 0.9

        for key, value in self.traffic_matrix.items():
            for key2, val2 in value.items():
                if val2:
                    rand = self.np_random.uniform(0, 1)
                    if rand <= prob1:
                        val = self.np_random.choice([0,1,2])
                    elif rand > prob1 and rand <= prob2:
                        val = self.np_random.choice([3,4])
                    else:
                        val = self.np_random.choice(range(5,8))
                    
                    if val == 0: continue
                    if val <= val2:
                        if key2 in self.traffic_matrix: 
                            options = list(self.traffic_matrix[key2].keys())
    
                            for _ in range(val):
                                to_node = self.np_random.choice(options)
                                self.traffic_matrix[key2][to_node] +=1
                            self.traffic_matrix[key][key2] -= val
                        else: 
                            self.traffic_matrix[key][key2] -= val

                    if val > val2:
                        if key2 in self.traffic_matrix: 
                            options = list(self.traffic_matrix[key2].keys())
                            
                            for _ in range(val2):
                                to_node = self.np_random.choice(options)
                                self.traffic_matrix[key2][to_node] +=1
                            self.traffic_matrix[key][key2] -= val2
                        else:
                            self.traffic_matrix[key][key2] -= val2


                        





