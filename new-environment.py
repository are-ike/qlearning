import gymnasium
import numpy as np
from gymnasium.spaces import Box, Dict
from utils import copy_list
from sim import TestSimulation

traffic_count ={
    'light': range(20,31), 'medium': range(30,46), 'heavy': range(45, 71)
}
class QlearningEnv(gymnasium.Env):
    def __init__(self, distances, carparks,hotspots=[]):
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
        self.distance_traveled = 0
        self.cars_seen = 0
        self.map = map
        self.sim = None
        self.hotspots = hotspots
        self.cars = []
        self.avail_carparks = []

    def step(self, action): 
        distance = self.distances[self.agent_position][action]
        traffic = self.traffic_matrix[self.agent_position][action]

        self.distance_traveled += distance
        self.cars_seen += traffic

        self.agent_position = action

        if self.agent_position in self.visited.keys(): 
            self.visited[self.agent_position] += 1 
        else:
            self.visited[self.agent_position] = 1 

        self.update_traffic3()

        terminated = action in self.carparks
        leaving = action not in self.distances.keys()

        distance_reward = -0.1*((self.distance_traveled/100)**2)
        traffic_reward = -0.2*((self.cars_seen)**2)

        reward = distance_reward + traffic_reward

        if terminated: reward += 100
        if leaving: reward -= 500
        
        reward -= (self.visited[self.agent_position] - 1) * 5

        return action, reward, terminated, leaving, distance, traffic, self.visited
        

    def reset(self, seed=None, options=None): 
        super().reset(seed=seed)
        if not options:
            total_cars = self.generate_traffic3()
            self.agent_position = self.np_random.choice(list(self.distances.keys()))
            self.distance_traveled = 0
            self.cars_seen = 0
            self.visited = {}
            self.visited[self.agent_position] = 1
        else:   
            total_cars = self.generate_traffic3(choice=options["traffic"])
            self.distance_traveled = 0
            self.cars_seen = 0
            self.visited = {}
            self.agent_position = options['start']
            self.visited[self.agent_position] = 1
        
        return self.agent_position, total_cars

    def start_sim(self, pos):
        self.sim = TestSimulation(traffic=self.traffic_matrix, get_traffic=self.get_traffic, set_traffic=self.set_traffic)
        self.sim.init_simulation(pos)

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
    
    def get_agent_start_position(self, i):
        # i_options = [pos for pos in self.distances.keys() if pos not in self.carparks]
        # i = self.np_random.choice(i_options)
        # j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]

        # while not j_options:
        #     i = self.np_random.choice(i_options)
        #     j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]
        # j = self.np_random.choice(j_options)

        i_options = [i]
        # i_options = [pos for pos in self.distances.keys()]
        # i = self.np_random.choice(i_options)
        j_options = [pos for pos in self.distances[i].keys()]

        while not j_options:
            i = self.np_random.choice(i_options)
            j_options = [pos for pos in self.distances[i].keys()]
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
    
    def generate_traffic2(self, choice=None):
        pass
        # if not choice: choice = self.np_random.choice(['light', 'medium', 'heavy'])
        
        # traffic = copy_list(self.distances)
        # total = 0

        # def get_route():
        #     type = self.np_random.choice(['high', 'med', 'low', 'avg'], p=[0.5,0.3,0.1,0.1])
        #     idx = self.np_random.choice(range(len(freq[type])))
        #     subset = freq[type][idx]
        #     options = [r for r in routes if set(subset).issubset(set(r))]
        #     idx = self.np_random.choice(range(len(options)))
        #     return options[idx]
                                  

        # total = self.np_random.choice(traffic_count[choice])
        # cars = [Car(get_route(), self.get_traffic, self.set_traffic, update_int=np.random.randint(0, 5)) for _ in range(total)]

        # self.traffic_matrix = traffic
        # self.cars = cars
        # return total

    def calc_traff(self, dist, choice,edge):
        prob = self.np_random.uniform(0,1)

        if choice == 'light':
            if edge in self.hotspots: return self.np_random.choice([1,2])
            if prob < 0.05:
                if dist > 100: return self.np_random.choice([1,2])
                if dist > 7: return self.np_random.choice([0,1]) 
            return 0

        else:
            if edge in self.hotspots: 
                #if dist <= 150 and dist >= 50: return self.np_random.choice([2,3])
                if dist > 150: return self.np_random.choice([2,3]) 
                return self.np_random.choice([1,2]) 
            if (prob < 0.07 and choice == 'medium') or (prob < 0.09 and choice == 'heavy'):
                if dist > 100: return self.np_random.choice([1,2])
                if dist > 7: return self.np_random.choice([0,1])
                return 1 
            return 0
        
        # if choice == 'heavy':
        #     if edge in self.hotspots: 
        #         if dist <= 150 and dist >= 50: return 3
        #         if dist > 150: return self.np_random.choice([4,5]) 
        #         return self.np_random.choice([1,2]) 
        #     if dist > 100: return self.np_random.choice([1,2,3])
        #     if dist > 10: return self.np_random.choice([0,1]) 
        #     return 1
            
    def generate_traffic3(self, choice=None):
        if not choice: choice = self.np_random.choice(['light', 'medium', 'heavy'])
        traffic = copy_list(self.distances)
        total = 0
        

        flat_edges = [(start, end) for start, destinations in self.distances.items() for end in destinations]
        distances = np.array([self.distances[start][end] for start, end in flat_edges])

        for (start, end), dist in zip(flat_edges, distances):
            val = self.calc_traff(dist, choice, (start, end))
            traffic[start][end] = val
            total += val
           
        self.traffic_matrix = traffic
        return total

    def update_traffic3(self):
        flat_edges = [(start, end) for start, destinations in self.traffic_matrix.items() for end in destinations]
        new_matrix = copy_list(self.traffic_matrix)

        for edge in flat_edges:
            change = self.np_random.choice(range(0,6))
            num = change if change <= self.traffic_matrix[edge[0]][edge[1]] else self.traffic_matrix[edge[0]][edge[1]]
            
            for _ in range(num):
                if edge[1] in self.traffic_matrix.keys():
                    options = list(self.traffic_matrix[edge[1]].keys())
                    hotspots = [x for x in options if (edge[1], x) in self.hotspots]
                    
                    prob = list(map(lambda x : 1/(len(options) + len(hotspots)) if (edge[1], x) not in self.hotspots else 2/(len(options) + len(hotspots)), options ))
                    to = self.np_random.choice(options, p=prob)
                    new_matrix[edge[1]][to] += 1
          
            self.traffic_matrix[edge[0]][edge[1]] -= num

        for edge in flat_edges:
            add = 0
            if edge == (10,2) or edge == (73,28): add = self.np_random.choice([0,1])
            self.traffic_matrix[edge[0]][edge[1]] += (new_matrix[edge[0]][edge[1]] + add)


