def posy(*coor):
    return (coor[0],coor[1] + 2000,coor[2],coor[3])

roads = [
    #gate to ransom kuti
    {
        "edges": [
            {
                "from_node": 71,
                "to_node": 72,
                "direction": "left"
            },
        ],
        "coordinates": posy(100,200,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 69,
                "to_node": 71,
                "direction": "left"
            },
        ],
        "coordinates": posy(290,200,600,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 71,
                "to_node": 28,
                "direction": "down"
            },
        ],
        "coordinates": posy(200,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 73,
                "to_node": 28,
                "direction": "right"
            },
        ],
        "coordinates": posy(100,310,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 28,
                "to_node": 29,
                "direction": "right"
            },
        ],
        "coordinates": posy(290,310,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 29,
                "to_node": 74,
                "direction": "right"
            },
        ],
        "coordinates": posy(390,310,350,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 29,
                "to_node": 30,
                "direction": "down"
            },
            {
                "from_node": 30,
                "to_node": 29,
                "direction": "up"
            },
        ],
        "coordinates": posy(350,400,90,60),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 30,
                "to_node": 31,
                "direction": "right"
            },
            {
                "from_node": 31,
                "to_node": 30,
                "direction": "left"
            },
        ],
        "coordinates": posy(400,460,300,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 30,
                "to_node": 78,
                "direction": "left"
            },
        ],
        "coordinates": posy(300,460,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 78,
                "to_node": 77,
                "direction": "down"
            },
        ],
        "coordinates": posy(210,460,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 77,
                "to_node": 76,
                "direction": "down"
            },
            {
                "from_node": 76,
                "to_node": 77,
                "direction": "up"
            },
        ],
        "coordinates": posy(210,460,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 77,
                "to_node": 76,
                "direction": "down"
            },
            {
                "from_node": 76,
                "to_node": 77,
                "direction": "up"
            },
        ],
        "coordinates": posy(210,660,90,300),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 76,
                "to_node": 75,
                "direction": "down"
            },
        ],
        "coordinates": posy(210,660,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 75,
                "to_node": 32,
                "direction": "down"
            },
            {
                "from_node": 32,
                "to_node": 75,
                "direction": "up"
            },
        ],
        "coordinates": posy(210,860,90,400),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 32,
                "to_node": 33,
                "direction": "down"
            },
            {
                "from_node": 33,
                "to_node": 32,
                "direction": "up"
            },
        ],
        "coordinates": posy(210,1260,90,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 33,
                "to_node": 34,
                "direction": "down"
            },
            {
                "from_node": 34,
                "to_node": 33,
                "direction": "up"
            },
        ],
        "coordinates": posy(210,1350,90,400),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 34,
                "to_node": 35,
                "direction": "right"
            },
            {
                "from_node": 35,
                "to_node": 34,
                "direction": "left"
            },
        ],
        "coordinates": posy(300,1700,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 34,
                "to_node": 6,
                "direction": "right"
            },
            {
                "from_node": 6,
                "to_node": 34,
                "direction": "left"
            },
        ],
        "coordinates": posy(210,1750,90,150),
        "one_way": True
    },

    #multipurpose to access
    {
        "edges": [
            {
                "from_node": 23,
                "to_node": 69,
                "direction": "left"
            },
        ],
        "coordinates": posy(890,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 22,
                "to_node": 23,
                "direction": "left"
            },
        ],
        "coordinates": posy(1180,200,30,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 23,
                "to_node": 24,
                "direction": "down"
            },
        ],
        "coordinates": posy(1090,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 24,
                "to_node": 15,
                "direction": "right"
            },
        ],
        "coordinates": posy(1180,310,1170,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 24,
                "to_node": 22,
                "direction": "up"
            },
        ],
        "coordinates": posy(1210,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 21,
                "to_node": 22,
                "direction": "left"
            },
        ],
        "coordinates": posy(1300,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 20,
                "to_node": 21,
                "direction": "left"
            },
        ],
        "coordinates": posy(1500,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 19,
                "to_node": 20,
                "direction": "left"
            },
        ],
        "coordinates": posy(1700,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 86,
                "to_node": 19,
                "direction": "left"
            },
        ],
        "coordinates": posy(1900,200,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 18,
                "to_node": 86,
                "direction": "left"
            },
        ],
        "coordinates": posy(2050,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 17,
                "to_node": 18,
                "direction": "left"
            },
        ],
        "coordinates": posy(2250,200,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 74,
                "to_node": 24,
                "direction": "right"
            },
        ],
        "coordinates": posy(740,310,350,90),
        "one_way": True
    },
    #sports center
    {
        "edges": [
            {
                "from_node": 24,
                "to_node": 25,
                "direction": "down"
            },
            {
                "from_node": 25,
                "to_node": 24,
                "direction": "up"
            },
        ],
        "coordinates": posy(1150,400,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 25,
                "to_node": 26,
                "direction": "left"
            },
            {
                "from_node": 26,
                "to_node": 25,
                "direction": "right"
            },
        ],
        "coordinates": posy(1095,480,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 25,
                "to_node": 27,
                "direction": "right"
            },
            {
                "from_node": 27,
                "to_node": 25,
                "direction": "left"
            },
        ],
        "coordinates": posy(1195,480,250,90),
        "one_way": True
    },
    #religious lots
    {
        "edges": [
            {
                "from_node": 21,
                "to_node": 68,
                "direction": "up"
            },
            {
                "from_node": 68,
                "to_node": 21,
                "direction": "down"
            },
        ],
        "coordinates": posy(1450,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 20,
                "to_node": 67,
                "direction": "up"
            },
            {
                "from_node": 20,
                "to_node": 67,
                "direction": "down"
            },
        ],
        "coordinates": posy(1650,80,90,120),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 19,
                "to_node": 66,
                "direction": "up"
            },
            {
                "from_node": 66,
                "to_node": 19,
                "direction": "down"
            },
        ],
        "coordinates": posy(1850,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 86,
                "to_node": 65,
                "direction": "up"
            },
            {
                "from_node": 65,
                "to_node": 86,
                "direction": "down"
            },
        ],
        "coordinates": posy(2000,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 18,
                "to_node": 65,
                "direction": "up"
            },
        ],
        "coordinates": posy(2200,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(2000,50,290,70),
        "one_way": True
    },

    #acess roundabout
    {
        "edges": [
            {
                "from_node": 17,
                "to_node": 15,
                "direction": "down"
            },
        ],
        "coordinates": posy(2350,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 16,
                "to_node": 17,
                "direction": "left"
            },
        ],
        "coordinates": posy(2440,200,30,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 15,
                "to_node": 16,
                "direction": "up"
            },
        ],
        "coordinates": posy(2470,200,90,200),
        "one_way": True
    },

    #access roundabout to cits
    {
        "edges": [
            {
                "from_node": 36,
                "to_node": 16,
                "direction": "left"
            },
        ],
        "coordinates": posy(2560,200,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "left"
            },
        ],
        "coordinates": posy(2760,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 40,
                "to_node": 36,
                "direction": "left"
            },
        ],
        "coordinates": posy(2710,200,760,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 15,
                "to_node": 37,
                "direction": "right"
            },
        ],
        "coordinates": posy(2420,310,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 37,
                "to_node": 39,
                "direction": "right"
            },
        ],
        "coordinates": posy(2820,310,500,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 37,
                "to_node": 38,
                "direction": "down"
            },
            {
                "from_node": 38,
                "to_node": 37,
                "direction": "up"
            },
        ],
        "coordinates": posy(2870,400,90,150),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 39,
                "to_node": 81,
                "direction": "right"
            },
        ],
        "coordinates": posy(3320,310,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 39,
                "to_node": 79,
                "direction": "down"
            },
            {
                "from_node": 79,
                "to_node": 39,
                "direction": "up"
            },
        ],
        "coordinates": posy(3270,400,90,100),
        "one_way": True
    },

    #cits roundabout
    {
        "edges": [
            {
                "from_node": 40,
                "to_node": 81,
                "direction": "down"
            },
        ],
        "coordinates": posy(3470,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 80,
                "to_node": 40,
                "direction": "left"
            },
        ],
        "coordinates": posy(3560,200,30,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 81,
                "to_node": 80,
                "direction": "up"
            },
        ],
        "coordinates": posy(3590,200,90,200),
        "one_way": True
    },

    #cits
    {
        "edges": [
            {
                "from_node": 81,
                "to_node": 41,
                "direction": "down"
            },
            {
                "from_node": 41,
                "to_node": 81,
                "direction": "up"
            },
        ],
        "coordinates": posy(3535,400,90,100),
        "one_way": True
    },

    #cits to science
    {
        "edges": [
            {
                "from_node": 82,
                "to_node": 80,
                "direction": "left"
            },
        ],
        "coordinates": posy(3540,200,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 81,
                "to_node": 82,
                "direction": "right"
            },
        ],
        "coordinates": posy(3540,310,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "left"
            },
        ],
        "coordinates": posy(3940,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 82,
                "to_node": 83,
                "direction": "right"
            },
        ],
        "coordinates": posy(4030,310,300,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 83,
                "to_node": 82,
                "direction": "left"
            },
        ],
        "coordinates": posy(4030,200,300,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "left"
            },
        ],
        "coordinates": posy(4330,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 42,
                "to_node": 83,
                "direction": "left"
            },
        ],
        "coordinates": posy(4420,200,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 83,
                "to_node": 85,
                "direction": "right"
            },
        ],
        "coordinates": posy(4420,310,200,90),
        "one_way": True
    },
    
    #science roundabout
    {
        "edges": [
            {
                "from_node": 42,
                "to_node": 85,
                "direction": "down"
            },
        ],
        "coordinates": posy(4620,200,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 84,
                "to_node": 42,
                "direction": "left"
            },
        ],
        "coordinates": posy(4710,200,30,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 84,
                "direction": "up"
            },
        ],
        "coordinates": posy(4740,200,90,200),
        "one_way": True
    },

    #science roundabout to senate
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 48,
                "direction": "right"
            },
        ],
        "coordinates": posy(4660,310,500,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 99,
                "to_node": 84,
                "direction": "left"
            },
        ],
        "coordinates": posy(4660,200,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 48,
                "to_node": 99,
                "direction": "left"
            },
        ],
        "coordinates": posy(5060,200,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 99,
                "to_node": 100,
                "direction": "up"
            },
            {
                "from_node": 100,
                "to_node": 99,
                "direction": "down"
            },
        ],
        "coordinates": posy(5020,120,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(5160,200,120,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 48,
                "to_node": 49,
                "direction": "down"
            },
            {
                "from_node": 49,
                "to_node": 48,
                "direction": "up"
            },
        ],
        "coordinates": posy(5190,310,90,300),
        "one_way": True
    },

    #guesthouse to science roundabout
    {
        "edges": [
            {
                "from_node": 102,
                "to_node": 84,
                "direction": "down"
            },
        ],
        "coordinates": posy(4740,-300,90,500),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 43,
                "to_node": 102,
                "direction": "left"
            },
        ],
        "coordinates": posy(4740,-390,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 44,
                "to_node": 43,
                "direction": "left"
            },
        ],
        "coordinates": posy(5140,-390,550,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 102,
                "to_node": 101,
                "direction": "up"
            },
            {
                "from_node": 101,
                "to_node": 102,
                "direction": "down"
            },
        ],
        "coordinates": posy(4740,-470,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 43,
                "to_node": 101,
                "direction": "up"
            },
            {
                "from_node": 101,
                "to_node": 43,
                "direction": "down"
            },
        ],
        "coordinates": posy(5100,-470,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(4740,-570,450,100),
        "one_way": True
    },

    #senate to guesthouse
    {
        "edges": [
            {
                "from_node": 49,
                "to_node": 64,
                "direction": "right"
            },
            {
                "from_node": 64,
                "to_node": 49,
                "direction": "left"
            },
        ],
        "coordinates": posy(5190,610,300,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 50,
                "to_node": 64,
                "direction": "left"
            },
            {
                "from_node": 64,
                "to_node": 50,
                "direction": "right"
            },
        ],
        "coordinates": posy(5490,610,200,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 90,
                "to_node": 64,
                "direction": "down"
            },
            {
                "from_node": 64,
                "to_node": 90,
                "direction": "up"
            },
        ],
        "coordinates": posy(5450,530,90,80),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 50,
                "to_node": 47,
                "direction": "up"
            },
        ],
        "coordinates": posy(5690,200,90,500),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 47,
                "to_node": 46,
                "direction": "up"
            },
        ],
        "coordinates": posy(5690,-100,90,300),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 46,
                "to_node": 44,
                "direction": "up"
            },
        ],
        "coordinates": posy(5690,-390,90,300),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 44,
                "to_node": 45,
                "direction": "up"
            },
        ],
        "coordinates": posy(5690,-690,90,300),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 45,
                "to_node": 87,
                "direction": "left"
            },
        ],
        "coordinates": posy(5590,-690,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 45,
                "to_node": 88,
                "direction": "left"
            },
        ],
        "coordinates": posy(5740,-690,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 49,
                "to_node": 51,
                "direction": "down"
            },
            {
                "from_node": 51,
                "to_node": 49,
                "direction": "up"
            },
        ],
        "coordinates": posy(5190,700,90,500),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 46,
                "to_node": 91,
                "direction": "right"
            },
            {
                "from_node": 91,
                "to_node": 46,
                "direction": "left"
            },
        ],
        "coordinates": posy(5780,-140,100,90),
        "one_way": True
    },
    
    #science
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 52,
                "direction": "down"
            },
            {
                "from_node": 52,
                "to_node": 85,
                "direction": "up"
            },
        ],
        "coordinates": posy(4680,400,90,400),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 53,
                "to_node": 52,
                "direction": "left"
            },
            {
                "from_node": 52,
                "to_node": 53,
                "direction": "right"
            },
        ],
        "coordinates": posy(4770,750,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 54,
                "to_node": 52,
                "direction": "up"
            },
            {
                "from_node": 52,
                "to_node": 54,
                "direction": "down"
            },
        ],
        "coordinates": posy(4680,800,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 53,
                "to_node": 54,
                "direction": "left"
            },
            {
                "from_node": 54,
                "to_node": 53,
                "direction": "right"
            },
        ],
        "coordinates": posy(4770,950,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 54,
                "to_node": 55,
                "direction": "down"
            },
            {
                "from_node": 55,
                "to_node": 54,
                "direction": "up"
            },
        ],
        "coordinates": posy(4680,1000,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 92,
                "to_node": 55,
                "direction": "left"
            },
            {
                "from_node": 55,
                "to_node": 92,
                "direction": "right"
            },
        ],
        "coordinates": posy(4770,1150,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 92,
                "to_node": 56,
                "direction": "left"
            },
            {
                "from_node": 56,
                "to_node": 92,
                "direction": "right"
            },
        ],
        "coordinates": posy(4870,1150,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 57,
                "to_node": 56,
                "direction": "left"
            },
            {
                "from_node": 56,
                "to_node": 57,
                "direction": "right"
            },
        ],
        "coordinates": posy(5020,1150,150,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 93,
                "to_node": 55,
                "direction": "up"
            },
            {
                "from_node": 55,
                "to_node": 93,
                "direction": "down"
            },
        ],
        "coordinates": posy(4680,1200,90,100),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 93,
                "to_node": 94,
                "direction": "right"
            },
            {
                "from_node": 94,
                "to_node": 93,
                "direction": "left"
            },
        ],
        "coordinates": posy(4770,1250,100,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 93,
                "to_node": 58,
                "direction": "down"
            },
            {
                "from_node": 58,
                "to_node": 93,
                "direction": "up"
            },
        ],
        "coordinates": posy(4680,1300,90,300),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 60,
                "to_node": 58,
                "direction": "up"
            },
            {
                "from_node": 58,
                "to_node": 60,
                "direction": "down"
            },
        ],
        "coordinates": posy(4680,1600,90,200),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 59,
                "to_node": 58,
                "direction": "up"
            },
            {
                "from_node": 58,
                "to_node": 59,
                "direction": "down"
            },
        ],     
        "coordinates": posy(4280,1550,400,90),
        "one_way": True
    },
    {
        "edges": [
            {
                "from_node": 59,
                "to_node": 3,
                "direction": "down"
            },
            {
                "from_node": 3,
                "to_node": 59,
                "direction": "up"
            },
        ],
        "coordinates": posy(4190,1550,90,200),
        "one_way": True
    },
]

