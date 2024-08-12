def pos(num1, num2): return (num1 + 0, num2 + 0)
def siz(num1, num2): return (num1 + 0, num2 + 0)

nodes = [
    {
        "id": 0,
        "position": pos(730,30),
        "size": siz(200,100),
        "type": 1,
        "color": '#c4a484',
    },
    {
        "id": 1,
        "position": pos(600,30),
        "size": siz(100,200),
        "type": 1,
        "color": '#c4a484'
    },
]

roads = [
    {
        "edges": [
            {
                "from_node": 0,
                "to_node": 1,
                "direction": "down"
            },
            {
                "from_node": 1,
                "to_node": 0,
                "direction": "up"
            },
        ],
        "coordinates": (790,330,120,400),
        "one_way": False
    },
    {
        "edges": [
            {
                "from_node": 1,
                "to_node": 2,
                "direction": "down"
            },
            {
                "from_node": 2,
                "to_node": 1,
                "direction": "up"
            },
        ],
        "coordinates": (790,730,120,400),
        "one_way": False
    },
    {
        "edges": [
            {
                "from_node": 2,
                "to_node": 3,
                "direction": "left"
            },
            {
                "from_node": 3,
                "to_node": 2,
                "direction": "right"
            },
        ],
        "coordinates": (90,1130,700,120),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 2,
                "to_node": 5,
                "direction": "down"
            },
            {
                "from_node": 5,
                "to_node": 2,
                "direction": "up"
            },
        ],
        "coordinates": (790,1250,120,400),
        "one_way": False
    },
    {
        "edges": [
            {
                "from_node": 3,
                "to_node": 4,
                "direction": "down"
            },
            {
                "from_node": 4,
                "to_node": 3,
                "direction": "up"
            },
        ],
        "coordinates": (0,1250,120,400),
        "one_way": False
    },
    {
        "edges": [
            {
                "from_node": 4,
                "to_node": 5,
                "direction": "right"
            },
            {
                "from_node": 5,
                "to_node": 4,
                "direction": "left"
            },
        ],
        "coordinates": (90,1650,700,120),
        "one_way": False
    },
]

roundabouts = [
    {
        "position": pos(850,270),
        
    }
]

green = [
    {
        "position": pos(130,130),
        "size": siz(240,140),
    },
    {
        "position": pos(220,270),
        "size": siz(60,500),
    },
    {
        "position": pos(50,270),
        "size": siz(60,500),
    },
]

misc = [
    {
        "position": pos(80,80),
        "size": siz(240,140),
    },
    {
        "position": pos(170,220),
        "size": siz(60,500),
    },
]

# edges = [
#     {
#         , 
#         "direction": "right",
#         "length": 400,
#         
#         
#     },
#     {
#         "position": (747,197), 
#         "direction": "right",
#         "length": 300,
#         "edges": [(1,0), (0,1)],
#         "left": 1,
#         "right": 0,
#         "down": None,
#         "up": None,
#     },
#     # {
#     #     "position": (500,350), 
#     #     "direction": "down",
#     #     "length": 500,
#     #     "edges": [(1,4)],
#     #     "left": None,
#     #     "right": None,
#     #     "down": 4,
#     #     "up": 1,
#     # },
#     ]







            





