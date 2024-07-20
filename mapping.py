# def find_node_high_indegree
# def mapping(dist_matrx):
    
mappings = {
    "nodes": [
        {
            "id": 2,
            "position": (100,100),
            "car_park": True
        },
        {
            "id": 1,
            "position": (500,100),
            "car_park": False
         },
        {
            "id": 0,
            "position": (900,100),
            "car_park": False
         },
    ],

    "edges": [
        {
            "position": (257,197), 
            "direction": "right",
            "length": 400,
            "edges": [(1,2), (2,1)],
            "left": 2,
            "right": 1,
            "down": None,
            "up": None,
        },
        {
            "position": (747,197), 
            "direction": "right",
            "length": 300,
            "edges": [(1,0), (0,1)],
            "left": 1,
            "right": 0,
            "down": None,
            "up": None,
        },
        # {
        #     "position": (500,350), 
        #     "direction": "down",
        #     "length": 500,
        #     "edges": [(1,4)],
        #     "left": None,
        #     "right": None,
        #     "down": 4,
        #     "up": 1,
        # },
    ]
}






            





