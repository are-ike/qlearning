types = {
    "O": 1,
    "T": 2,
    "C": 3,
    "G": 4
}

class Node:

    def __init__(self, index, x, y, type, to_nodes):
        self.index = index
        self.x = x
        self.y = y
        self.type = type
        self.to_nodes = to_nodes
    
    #draw node