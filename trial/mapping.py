def pos(num1, num2): return (num1 + 0, num2 + 0)
def siz(num1, num2): return (num1 + 0, num2 + 0)

nodes = [
    {
        "id": 0,
        "position": pos(2410,30),
        "size": siz(200,100),
        "type": 1,
        "color": '#c4a484',
    },
    {
        "id": 1,
        "position": pos(2300,30),
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

