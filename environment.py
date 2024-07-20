import gymnasium
import numpy as np

from gymnasium.spaces import Box, Discrete, Dict

class QlearningEnv(gymnasium.Env):
    def __init__(self, arguments):
        super(QlearningEnv, self).__init__()
        self.observation_space = Dict({"distance": Box(high=500, low=0, shape=()), "traffic": Box(arguments["traffic"])})
        self.action_space = None
        self.current_node = arguments["position"]      #the node the agent is currently in
        self.seed = arguments["seed"]
        self.qtable = None

    def generate_action_space(self):
        possible_nodes = filter(lambda node : node != (0, 0), self.observation_space)
        self.action_space = Discrete(possible_nodes)

    # def reset(self):
    #     node_number = self.observation_space._shape[0]
    #     self.qtable = np.zeros((node_number, node_number))    #generate empty q table

    #     self.generate_action_space()

    # def step(self, action):

    def getvalues(self):
        self.generate_action_space()
        print(self.observation_space, self.action_space)
        







    # def step(self, action):


