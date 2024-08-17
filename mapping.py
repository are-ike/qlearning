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
    {#hostel roundabout to dli gate√
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
        "length": 173.12,
        "coordinates": (2500,330,270,519),
        "one_way": False
    },
    {#dli gate to dli roundabout√
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
        "length": 117.76,
        "coordinates": (2500,849,270,353),
        "one_way": False
    },


    {#second gate to dli roundabout√
        "edges": [
            {
                "from_node": 10,
                "to_node": 2,
                "direction": "left"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 310.62, 
        "coordinates": (2770,1202,875,120),
        "one_way": True
    },
    {#dli roundabout to carpark entrance 1√
        "edges": [
            {
                "from_node": 8,
                "to_node": 61,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 48.60, 
        #"coordinates": (2770,1350,875,120),
        "one_way": True
    },
    {#carpark entrance 1 to carpark entrance 2√
        "edges": [
            {
                "from_node": 61,
                "to_node": 62,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 146.25, 
        #"coordinates": (2770,1350,875,120),
        "one_way": True
    },
    {#carpark entrance 2 to second gate√
        "edges": [
            {
                "from_node": 62,
                "to_node": 9,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 134.62, 
        #"coordinates": (2770,1350,875,120),
        "one_way": True
    },
    {#carpark entrance 1 to carpark√
        "edges": [
            {
                "from_node": 61,
                "to_node": 63,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 1, 
        #"coordinates": (2770,1350,875,120),
        "one_way": True
    },
    {#carpark entrance 2 to carpark√
        "edges": [
            {
                "from_node": 62,
                "to_node": 64,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 6.36, 
        #"coordinates": (2770,1350,875,120),
        "one_way": True
    },


    {#dli roundabout (actual) towards fss√
        "edges": [
            {
                "from_node": 2,
                "to_node": 4,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 26.92, #
        "coordinates": (2500,1202,135,270),
        "one_way": True
    },


    {#dli roundabout (actual) towards isl 1√
        "edges": [
            {
                "from_node": 6,
                "to_node": 8,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 11.03, #
        "coordinates": (2635,1342,135,130),
        "one_way": True
    },
    {#dli roundabout (actual) towards isl 2√
        "edges": [
            {
                "from_node": 8,
                "to_node": 2,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 14.05, #
        "coordinates": (2635,1202,135,140),
        "one_way": True
    },


    {#dli roundabout (actual) towards ransome kuti√
        "edges": [
            {
                "from_node": 4,
                "to_node": 6,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 27.83, #
        "coordinates": (2500,1472,270,150),
        "one_way": True
    },


    {#dli roundabout to medical center uturn√
        "edges": [
            {
                "from_node": 2,
                "to_node": 3,
                "direction": "left"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 635.71, 
        "coordinates": (640,1202,1860,120),
        "one_way": True
    },
    {#medical center uturn to dli roundabout√
        "edges": [
            {
                "from_node": 3,
                "to_node": 4,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 622.05, #
        "coordinates": (640,1352,1860,120),
        "one_way": True
    },

    {#dli roundabout towards publishing center
        "edges": [
            {
                "from_node": 4,
                "to_node": 5,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 302.64, #
        "coordinates": (2500,1622,120,900),
        "one_way": True
    },

    {#publishing center towards dli roundabout
        "edges": [
            {
                "from_node": 5,
                "to_node": 6,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 297.17, #
        "coordinates": (2650,1622,120,900),
        "one_way": True
    },
    {#fss to publishing center
        "edges": [
            {
                "from_node": 11,
                "to_node": 5,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 54.46, #
        "coordinates": (2650,2522,120,160),
        "one_way": True
    },
    {#uturn 3 to fss
        "edges": [
            {
                "from_node": 12,
                "to_node": 11,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 216.70, #
        "coordinates": (2650,2682,120,650),
        "one_way": True
    },
    {#uturn 2 to uturn 3
        "edges": [
            {
                "from_node": 13,
                "to_node": 12,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 19.04, #
        "coordinates": (2650,3332,120,100),
        "one_way": True
    },
    {#uturn 1 to uturn 2
        "edges": [
            {
                "from_node": 14,
                "to_node": 13,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 62.82, #
        "coordinates": (2650,3432,120,200),
        "one_way": True
    },
    {#newhall rb to uturn 1
        "edges": [
            {
                "from_node": 15,
                "to_node": 14,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 30.00, #
        "coordinates": (2650,3632,120,100),
        "one_way": True
    },
    {#publishing center to uturn 3
        "edges": [
            {
                "from_node": 5,
                "to_node": 12,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 269.05, #
        "coordinates": (2500,2522,120,810),
        "one_way": True
    },
    {#uturn 3 to uturn 2
        "edges": [
            {
                "from_node": 12,
                "to_node": 13,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 18.38, #
        "coordinates": (2500,3332,120,100),
        "one_way": True
    },
    {#uturn 2 to uturn 1
        "edges": [
            {
                "from_node": 13,
                "to_node": 14,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 63.24, #
        "coordinates": (2500,3432,120,200),
        "one_way": True
    },
    {#uturn 1 to newhall roundabout
        "edges": [
            {
                "from_node": 14,
                "to_node": 15,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 31.32, #
        "coordinates": (2500,3632,120,100),
        "one_way": True
    },

    {#newhall roundabout (actual)
        "edges": [
            {
                "from_node": 15,
                "to_node": 16,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 25.02, #
        "coordinates": (2500,3732,135,135),
        "one_way": True
    },
    {#newhall roundabout (actual)
        "edges": [
            {
                "from_node": 17,
                "to_node": 15,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 25.05, #
        "coordinates": (2635,3732,135,135),
        "one_way": True
    },
    {#newhall roundabout (actual)
        "edges": [
            {
                "from_node": 16,
                "to_node": 17,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 39.26, #
        "coordinates": (2500,3867,270,135),
        "one_way": True
    },
    {#newhall roundabout to mosque lot
        "edges": [
            {
                "from_node": 17,
                "to_node": 18,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 44.73, #
        "coordinates": (2770,3882,135,120),
        "one_way": True
    },
    {#mosque lot to chapel lot
        "edges": [
            {
                "from_node": 18,
                "to_node": 19,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 116.49, #
        "coordinates": (2905,3882,350,120),
        "one_way": True
    },
    {#chapel lot to parking lot
        "edges": [
            {
                "from_node": 19,
                "to_node": 20,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 59.18, #
        "coordinates": (3255,3882,180,120),
        "one_way": True
    },
    {#parking lot to cath lot
        "edges": [
            {
                "from_node": 20,
                "to_node": 21,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 28.28, #
        "coordinates": (3435,3882,85,120),
        "one_way": True
    },
    {#cath lot to sports rb
        "edges": [
            {
                "from_node": 21,
                "to_node": 22,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 87.11, #
        "coordinates": (3520,3882,260,120),
        "one_way": True
    },
    {#sports rb (actual)
        "edges": [
            {
                "from_node": 22,
                "to_node": 23,
                "direction": "right"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 21.73, #
        "coordinates": (3780,3867,240,135),
        "one_way": True
    },
    {#sports rb (actual)
        "edges": [
            {
                "from_node": 23,
                "to_node": 24,
                "direction": "up"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 15.76, #
        "coordinates": (3900,3732,120,135),
        "one_way": True
    },
    {#sports rb (actual)
        "edges": [
            {
                "from_node": 24,
                "to_node": 22,
                "direction": "down"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 15.88, #
        "coordinates": (3780,3732,120,135),
        "one_way": True
    },
    {#sports rb (actual)
        "edges": [
            {
                "from_node": 24,
                "to_node": 15,
                "direction": "left"
            },
            # {
            #     "from_node": 2,
            #     "to_node": 1,
            #     "direction": "up"
            # },
        ],
        "length": 354.23, #
        "coordinates": (2770,3732,1060,120),
        "one_way": True
    },
    # {#dli roundabout to ransom kuti roundabout
    #     "edges": [
    #         {
    #             "from_node": 6,
    #             "to_node": 7,
    #             "direction": "right"
    #         },
    #         # {
    #         #     "from_node": 2,
    #         #     "to_node": 1,
    #         #     "direction": "up"
    #         # },
    #     ],
    #     "length": 292.30, 
    #     "coordinates": (2740,1500,877,120),
    #     "one_way": True
    # },
    
]



