import gymnasium
import numpy as np
from gymnasium.spaces import Box, Dict
from traffic import Traffic
from utils import copy_list
from routes import routes, freq

traffic_count ={
    'light': range(20,31), 'medium': range(30,46), 'heavy': range(45, 71)
}
class QlearningEnv(gymnasium.Env):
    def __init__(self, distances, carparks, hotspots, map):
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
        self.hotspots = hotspots
        self.cars = []
        self.avail_carparks = []

    def step(self, action): 
        #self.traffic_obj.start_agent(self.agent_position, action)
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

        terminated = action in self.avail_carparks
        leaving = action not in self.distances.keys()

        norm_dist = -10*((self.distance_traveled/700)**2)
        norm_traf = -10*((self.cars_seen/10)**2)

        reward = norm_dist + norm_traf

        if terminated: reward += 1000
        if leaving: reward -= 500
        if action in self.carparks and not terminated: reward += 100
        reward -= (self.visited[self.agent_position] - 1) * 5

        return action, reward, terminated, leaving, distance, traffic, self.visited
        

    def reset(self, episode, episodes, seed=None, options=None): 
        if not options:
            super().reset(seed=seed)
            total_cars = self.generate_traffic3()
            #self.update_traffic2()

            if episode <= episodes * 0.7:
                self.avail_carparks = self.carparks
            else:
                self.avail_carparks = self.np_random.choice(self.carparks, size=self.np_random.choice(range(3, len(self.carparks) + 1)), replace=False)

            position = self.get_agent_start_position()
            self.agent_position = position[0]
            self.distance_traveled = 0
            self.cars_seen = 0
            self.visited = {}
            self.visited[self.agent_position] = 1
        else:
            super().reset(seed=seed)
            total_cars = self.generate_traffic3(choice=options["traffic"])
            self.avail_carparks = options["carparks"]
            #position = options["start"]
            self.distance_traveled = 0
            self.cars_seen = 0
            self.visited = {}
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
        # i_options = [pos for pos in self.distances.keys() if pos not in self.carparks]
        # i = self.np_random.choice(i_options)
        # j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]

        # while not j_options:
        #     i = self.np_random.choice(i_options)
        #     j_options = [pos for pos in self.distances[i].keys() if pos not in self.carparks]
        # j = self.np_random.choice(j_options)
        i_options = [pos for pos in self.distances.keys()]
        i = self.np_random.choice(i_options)
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
        if not choice: choice = self.np_random.choice(['light', 'medium', 'heavy'])
        
        traffic = copy_list(self.distances)
        total = 0

        def get_route():
            type = self.np_random.choice(['high', 'med', 'low', 'avg'], p=[0.5,0.3,0.1,0.1])
            idx = self.np_random.choice(range(len(freq[type])))
            subset = freq[type][idx]
            options = [r for r in routes if set(subset).issubset(set(r))]
            idx = self.np_random.choice(range(len(options)))
            return options[idx]
                                  

        total = self.np_random.choice(traffic_count[choice])
        cars = [Car(get_route(), self.get_traffic, self.set_traffic, update_int=np.random.randint(0, 5)) for _ in range(total)]

        self.traffic_matrix = traffic
        self.cars = cars
        return total

    def calc_traff(self, dist, choice,edge):
        prob = self.np_random.uniform(0,1)

        if choice == 'light':
            if edge in self.hotspots: return self.np_random.choice([1,2])
            if prob < 0.05:
                if dist > 100: return self.np_random.choice([1,2])
                if dist > 10: return self.np_random.choice([0,1]) 
            return 0

        else:
            if edge in self.hotspots: 
                #if dist <= 150 and dist >= 50: return self.np_random.choice([2,3])
                if dist > 150: return self.np_random.choice([2,3]) 
                return self.np_random.choice([1,2]) 
            if (prob < 0.07 and choice == 'medium') or (prob < 0.09 and choice == 'heavy'):
                if dist > 100: return self.np_random.choice([1,2])
                if dist > 10: return self.np_random.choice([0,1])
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

    def update_traffic2(self):
        for car in self.cars:
            car.update()
                        


class Car:
    def __init__(self, route, get_traffic, set_traffic, update_int):
        self.route = route
        self.position = 0
        self.get_traffic = get_traffic
        self.set_traffic = set_traffic
        self.update_count = 0
        self.update_int = update_int
        #print(update_int, route)

    def update(self):
        if len(self.route) - 1 == self.position: return
        if self.update_count < self.update_int:
            self.update_count +=1
            return
        
        traffic = self.get_traffic() 
        i = self.route[self.position]
        if self.position > 0:
            k = self.route[self.position - 1]
            traffic[k][i] -= 1

        self.position +=1
        j = self.route[self.position]
        #print(i,j)
        traffic[i][j] += 1
        self.set_traffic(traffic)
        #self.update_count = 0



