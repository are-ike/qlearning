import gymnasium
import numpy as np
from gymnasium.spaces import Box, Dict
from traffic import Traffic

class QlearningEnv(gymnasium.Env):
    def __init__(self, distance_matrix, carparks, map):
        super(QlearningEnv, self).__init__()

        self.size = len(distance_matrix)

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
        self.distance_matrix = distance_matrix
        self.carparks = carparks
        self.traffic_obj = None
        self.agent_is_moving = False

        self.map = map

    def step(self, action): 
        #if not self.traffic_obj.agent_started: 
        #self.traffic_obj.set_agent_is_moving = self.set_agent_is_moving
        print(self.traffic_matrix)
        self.traffic_obj.start_agent(self.agent_position, action)

        #self.traffic_obj.run_simulation(loop=True)

        reward = - (self.distance_matrix[self.agent_position][action]/100) - (10*(self.traffic_matrix[self.agent_position][action] -1))

        self.agent_position = action

        terminated = action in self.carparks

        return action, reward, terminated
        

    def reset(self, seed=None, options=None): 
        super().reset(seed=seed)

        self.generate_traffic()

        position = self.get_agent_start_position()
        self.agent_position = position[0]

        traffic = Traffic(self.traffic_matrix, self.get_traffic, self.set_traffic,self.map, position)
        #traffic.set_agent_is_moving = self.set_agent_is_moving
        self.traffic_obj = traffic
        
        traffic.start_simulation()

        obs = None
        info = None
        
        return self.agent_position

    def render(self): pass
  
    def close(self): 
        self.traffic_obj.quit()
    
    def action_sample(self):
        options = []

        for i, y in np.ndenumerate(self.distance_matrix[self.agent_position]):
            if y > 0:
                options.append(i)

        return self.np_random.choice(options)[0]
    
    def setup_simulation(self):pass

    def is_valid_action(self, action):
        if self.distance_matrix[self.agent_position][action]: return True 
        return False

    def set_agent_is_moving(self, value):
        self.set_agent_is_moving = value
    
    def get_agent_start_position(self):
        i = self.np_random.integers(0, self.size)
        j = self.np_random.integers(0, self.size)

        while self.traffic_matrix[i][j] != 1 or i == j or i in self.carparks:
            if 1 not in self.traffic_matrix[i] or i in self.carparks:
                i = self.np_random.integers(0, self.size)
            j = self.np_random.integers(0, self.size)

        return (i,j)

    def generate_traffic(self):
        #self.traffic_matrix = [[0,2,0,0,0,0], [2,0,0,0,0,0], [0,0,0,1,0,1], [0,0,0,0,0,0], [0,0,0,0,0,1], [0,0,0,0,0,0]]
        #self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,0,1], [0,0,1,0,1,0]]
        self.traffic_matrix = [[0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,0,0,1], [0,0,1,0,1,0]]
    
    def get_traffic(self):
        return self.traffic_matrix
    
    def set_traffic(self, new_traffic):
        self.traffic_matrix = new_traffic



