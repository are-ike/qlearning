def posy(*coor):
    return (coor[0],coor[1] + 500,coor[2],coor[3])


roads = [
    #gate to sports center top
    {
        "edges": [
            {
                "from_node": 71,
                "to_node": 28,
                "direction": "down"
            },
        ],
        "coordinates": posy(120,170,40,40),
    },
    {
        "edges": [
            {
                "from_node": 71,
                "to_node": 72,
                "direction": "left"
            },
        ],
        "coordinates": posy(100,90,20,90),
    },
    {
        "edges": [
            {
                "from_node": 104,
                "to_node": 71,
                "direction": "left"
            },
        ],
        "coordinates": posy(120,90,40,90),
    },
    {
        "edges": [
            {
                "from_node": 103,
                "to_node": 104,
                "direction": "left"
            },
        ],
        "coordinates": posy(160,90,290,90),
    },
    {
        "edges": [
            {
                "from_node": 103,
                "to_node": 124,
                "direction": "up"
            },
            {
                "from_node": 124,
                "to_node": 103,
                "direction": "down"
            },
        ],
        "coordinates": posy(410,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 69,
                "to_node": 103,
                "direction": "left"
            },
        ],
        "coordinates": posy(450,90,290,90),
    },
    {
        "edges": [
            {
                "from_node": 69,
                "to_node": 70,
                "direction": "up"
            },
            {
                "from_node": 70,
                "to_node": 69,
                "direction": "down"
            },
        ],
        "coordinates": posy(700,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 69,
                "to_node": 103,
                "direction": "left"
            },
        ],
        "coordinates": posy(450,90,290,90),
    },
    {
        "edges": [
            {
                "from_node": 23,
                "to_node": 69,
                "direction": "left"
            },
        ],
        "coordinates": posy(740,90,110,90),
    },
    {# rb 
        "edges": [
            {
                "from_node": 22,
                "to_node": 23,
                "direction": "left"
            },
        ],
        "coordinates": posy(850,90,120,90),
    },
    {
        "edges": [
            {
                "from_node": 23,
                "to_node": 24,
                "direction": "down"
            },
        ],
        "coordinates": posy(810,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 24,
                "to_node": 22,
                "direction": "up"
            },
        ],
        "coordinates": posy(930,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 125,
                "to_node": 104,
                "direction": "down"
            },
        ],
        "coordinates": posy(140,70,40,20),
    },
    #gate to sports center bottom
    {
        "edges": [
            {
                "from_node": 73,
                "to_node": 28,
                "direction": "right"
            },
        ],
        "coordinates": posy(100,200,20,90),
    },
    {
        "edges": [
            {
                "from_node": 28,
                "to_node": 29,
                "direction": "right"
            },
        ],
        "coordinates": posy(120,200,80,90),
    },
    {
        "edges": [
            {
                "from_node": 29,
                "to_node": 126,
                "direction": "right"
            },
        ],
        "coordinates": posy(200,200,280,90),
    },
    {
        "edges": [
            {
                "from_node": 126,
                "to_node": 127,
                "direction": "down"
            },
            {
                "from_node": 127,
                "to_node": 126,
                "direction": "up"
            },
        ],
        "coordinates": posy(440,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 126,
                "to_node": 74,
                "direction": "right"
            },
        ],
        "coordinates": posy(480,200,80,90),
    },
    {
        "edges": [
            {
                "from_node": 74,
                "to_node": 128,
                "direction": "down"
            },
            {
                "from_node": 128,
                "to_node": 74,
                "direction": "up"
            },
        ],
        "coordinates": posy(520,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 74,
                "to_node": 24,
                "direction": "right"
            },
        ],
        "coordinates": posy(560,200,290,90),
    },
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
        "coordinates": posy(810,290,70,70),
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
        "coordinates": posy(810,360,110,70),
    },
    
    #sports center to access top
    {
        "edges": [
            {
                "from_node": 21,
                "to_node": 22,
                "direction": "left"
            },
        ],
        "coordinates": posy(970,90,170,90),
    },
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
        "coordinates": posy(1080,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 20,
                "to_node": 21,
                "direction": "left"
            },
        ],
        "coordinates": posy(1140,90,60,90),
    },
    {
        "edges": [
            {
                "from_node": 20,
                "to_node": 67,
                "direction": "up"
            },
            {
                "from_node": 67,
                "to_node": 20,
                "direction": "down"
            },
        ],
        "coordinates": posy(1160,-70,70,160),
    },
    {
        "edges": [
            {
                "from_node": 19,
                "to_node": 20,
                "direction": "left"
            },
        ],
        "coordinates": posy(1200,90,120,90),
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
        "coordinates": posy(1270,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 86,
                "to_node": 19,
                "direction": "left"
            },
        ],
        "coordinates": posy(1320,90,50,90),
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
        "coordinates": posy(1350,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 18,
                "to_node": 86,
                "direction": "left"
            },
        ],
        "coordinates": posy(1370,90,180,90),
    },
    {
        "edges": [
            {
                "from_node": 18,
                "to_node": 65,
                "direction": "up"
            },
            {
                "from_node": 65,
                "to_node": 18,
                "direction": "down"
            },
        ],
        "coordinates": posy(1510,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 17,
                "to_node": 18,
                "direction": "left"
            },
        ],
        "coordinates": posy(1550,90,90,90),
    },
    {# rb 
        "edges": [
            {
                "from_node": 17,
                "to_node": 185,
                "direction": "left"
            },
        ],
        "coordinates": posy(1600,180,70,20),
    },

    #sports center to access btm
    {
        "edges": [
            {
                "from_node": 24,
                "to_node": 183,
                "direction": "right"
            },
        ],
        "coordinates": posy(850,200,640,90),
    },
    {
        "edges": [
            {
                "from_node": 183,
                "to_node": 185,
                "direction": "right"
            },
        ],
        "coordinates": posy(1490,200,150,90),
    },
    {
        "edges": [
            {
                "from_node": 184,
                "to_node": 183,
                "direction": "up"
            },
        ],
        "coordinates": posy(1420,290,70,20),
    },

    #access to dli left
    {
        "edges": [
            {
                "from_node": 185,
                "to_node": 173,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,290,90,60),
    },
    {
        "edges": [
            {
                "from_node": 173,
                "to_node": 14,
                "direction": "right"
            },
            {
                "from_node": 14,
                "to_node": 173,
                "direction": "left"
            },
        ],
        "coordinates": posy(1730,310,20,70),
    },
    {
        "edges": [
            {
                "from_node": 173,
                "to_node": 184,
                "direction": "left"
            },
        ],
        "coordinates": posy(1620,310,20,70),
    },
    {
        "edges": [
            {
                "from_node": 173,
                "to_node": 172,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,350,90,130),
    },
    {
        "edges": [
            {
                "from_node": 172,
                "to_node": 13,
                "direction": "right"
            },
            {
                "from_node": 13,
                "to_node": 172,
                "direction": "left"
            },
        ],
        "coordinates": posy(1730,430,20,70),
    },
    {
        "edges": [
            {
                "from_node": 172,
                "to_node": 180,
                "direction": "left"
            },
            {
                "from_node": 180,
                "to_node": 172,
                "direction": "right"
            },
        ],
        "coordinates": posy(1620,430,20,70),
    },
    {
        "edges": [
            {
                "from_node": 172,
                "to_node": 171,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,480,90,40),
    },
    {
        "edges": [
            {
                "from_node": 171,
                "to_node": 179,
                "direction": "left"
            },
            {
                "from_node": 179,
                "to_node": 171,
                "direction": "right"
            },
        ],
        "coordinates": posy(1620,510,20,70),
    },
    {
        "edges": [
            {
                "from_node": 171,
                "to_node": 12,
                "direction": "right"
            },
            {
                "from_node": 12,
                "to_node": 171,
                "direction": "left"
            },
        ],
        "coordinates": posy(1730,510,20,70),
    },
    {
        "edges": [
            {
                "from_node": 171,
                "to_node": 175,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,520,90,160),
    },
    {
        "edges": [
            {
                "from_node": 175,
                "to_node": 174,
                "direction": "right"
            },
            {
                "from_node": 174,
                "to_node": 175,
                "direction": "left"
            },
        ],
        "coordinates": posy(1730,640,20,70),
    },
    {
        "edges": [
            {
                "from_node": 175,
                "to_node": 176,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,680,90,110),
    },
    {
        "edges": [
            {
                "from_node": 176,
                "to_node": 178,
                "direction": "left"
            },
            {
                "from_node": 178,
                "to_node": 176,
                "direction": "right"
            },
        ],
        "coordinates": posy(1620,750,20,70),
    },
    {
        "edges": [
            {
                "from_node": 176,
                "to_node": 11,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,790,90,160),
    },
    {
        "edges": [
            {
                "from_node": 11,
                "to_node": 98,
                "direction": "left"
            },
            {
                "from_node": 98,
                "to_node": 11,
                "direction": "right"
            },
        ],
        "coordinates": posy(1620,910,20,70),
    },
    {
        "edges": [
            {
                "from_node": 11,
                "to_node": 170,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,950,90,110),
    },
    {
        "edges": [
            {
                "from_node": 170,
                "to_node": 5,
                "direction": "right"
            },
            {
                "from_node": 5,
                "to_node": 170,
                "direction": "left"
            },
        ],
        "coordinates": posy(1730,1020,20,70),
    },
    {
        "edges": [
            {
                "from_node": 170,
                "to_node": 6,
                "direction": "down"
            },
        ],
        "coordinates": posy(1640,1060,90,630),
    },

    #access to dli right
    {
        "edges": [
            {
                "from_node": 14,
                "to_node": 15,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,290,90,60),
    },
    {
        "edges": [
            {
                "from_node": 181,
                "to_node": 14,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,350,90,80),
    },
    {
        "edges": [
            {
                "from_node": 13,
                "to_node": 181,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,430,90,50),
    },
    {
        "edges": [
            {
                "from_node": 181,
                "to_node": 182,
                "direction": "right"
            },
            {
                "from_node": 181,
                "to_node": 182,
                "direction": "left"
            },
        ],
        "coordinates": posy(1840,390,20,70),
    },
    {
        "edges": [
            {
                "from_node": 12,
                "to_node": 13,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,480,90,40),
    },
    {
        "edges": [
            {
                "from_node": 174,
                "to_node": 12,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,520,90,160),
    },
    {
        "edges": [
            {
                "from_node": 174,
                "to_node": 177,
                "direction": "right"
            },
            {
                "from_node": 174,
                "to_node": 177,
                "direction": "left"
            },
        ],
        "coordinates": posy(1840,640,20,70),
    },
    {
        "edges": [
            {
                "from_node": 96,
                "to_node": 174,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,680,90,320),
    },
    {
        "edges": [
            {
                "from_node": 5,
                "to_node": 96,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,1000,90,60),
    },
    {
        "edges": [
            {
                "from_node": 96,
                "to_node": 97,
                "direction": "right"
            },
            {
                "from_node": 96,
                "to_node": 97,
                "direction": "left"
            },
        ],
        "coordinates": posy(1840,940,20,70),
    },
    {
        "edges": [
            {
                "from_node": 5,
                "to_node": 169,
                "direction": "right"
            },
            {
                "from_node": 5,
                "to_node": 169,
                "direction": "left"
            },
        ],
        "coordinates": posy(1840,1020,20,70),
    },
    {
        "edges": [
            {
                "from_node": 4,
                "to_node": 5,
                "direction": "up"
            },
        ],
        "coordinates": posy(1750,1060,90,630),
    },

    #access to cits top
    {# rb 
        "edges": [
            {
                "from_node": 16,
                "to_node": 17,
                "direction": "left"
            },
        ],
        "coordinates": posy(1640,90,200,90),
    },
    {
        "edges": [
            {
                "from_node": 15,
                "to_node": 16,
                "direction": "up"
            },
        ],
        "coordinates": posy(1800,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 36,
                "to_node": 16,
                "direction": "left"
            },
        ],
        "coordinates": posy(1840,90,100,90),
    },
    {
        "edges": [
            {
                "from_node": 36,
                "to_node": 129,
                "direction": "up"
            },
            {
                "from_node": 129,
                "to_node": 36,
                "direction": "down"
            },
        ],
        "coordinates": posy(1900,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 40,
                "to_node": 36,
                "direction": "left"
            },
        ],
        "coordinates": posy(1940,90,740,90),
    },
    {
        "edges": [
            {
                "from_node": 80,
                "to_node": 40,
                "direction": "left"
            },
        ],
        "coordinates": posy(2680,90,120,90),
    },
    {
        "edges": [
            {
                "from_node": 40,
                "to_node": 81,
                "direction": "down"
            },
        ],
        "coordinates": posy(2640,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 81,
                "to_node": 80,
                "direction": "up"
            },
        ],
        "coordinates": posy(2760,180,70,20),
    },

    #access to cits btm
    {
        "edges": [
            {
                "from_node": 185,
                "to_node": 15,
                "direction": "right"
            },
        ],
        "coordinates": posy(1640,200,200,90),
    },
    {
        "edges": [
            {
                "from_node": 15,
                "to_node": 132,
                "direction": "right"
            },
        ],
        "coordinates": posy(1840,200,70,90),
    },
    {
        "edges": [
            {
                "from_node": 132,
                "to_node": 37,
                "direction": "right"
            },
        ],
        "coordinates": posy(1910,200,160,90),
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
        "coordinates": posy(2030,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 37,
                "to_node": 130,
                "direction": "right"
            },
        ],
        "coordinates": posy(2070,200,310,90),
    },
    {
        "edges": [
            {
                "from_node": 130,
                "to_node": 39,
                "direction": "right"
            },
        ],
        "coordinates": posy(2380,200,190,90),
    },
    {
        "edges": [
            {
                "from_node": 131,
                "to_node": 130,
                "direction": "up"
            },
            {
                "from_node": 130,
                "to_node": 131,
                "direction": "down"
            },
        ],
        "coordinates": posy(2340,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 39,
                "to_node": 81,
                "direction": "right"
            },
        ],
        "coordinates": posy(2570,200,110,90),
    },
    {
        "edges": [
            {
                "from_node": 79,
                "to_node": 39,
                "direction": "up"
            },
            {
                "from_node": 39,
                "to_node": 79,
                "direction": "down"
            },
        ],
        "coordinates": posy(2530,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 41,
                "to_node": 81,
                "direction": "up"
            },
            {
                "from_node": 81,
                "to_node": 41,
                "direction": "down"
            },
        ],
        "coordinates": posy(2640,290,70,20),
    },

    #cits to science rb top
    {
        "edges": [
            {
                "from_node": 135,
                "to_node": 80,
                "direction": "left"
            },
        ],
        "coordinates": posy(2800,90,220,90),
    },
    {
        "edges": [
            {
                "from_node": 135,
                "to_node": 82,
                "direction": "down"
            },
            {
                "from_node": 82,
                "to_node": 135,
                "direction": "up"
            },
        ],
        "coordinates": posy(2980,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 134,
                "to_node": 135,
                "direction": "left"
            },
        ],
        "coordinates": posy(3020,90,90,90),
    },
    {
        "edges": [
            {
                "from_node": 134,
                "to_node": 83,
                "direction": "down"
            },
            {
                "from_node": 83,
                "to_node": 134,
                "direction": "up"
            },
        ],
        "coordinates": posy(3070,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 42,
                "to_node": 134,
                "direction": "left"
            },
        ],
        "coordinates": posy(3110,90,80,90),
    },
    {
        "edges": [
            {
                "from_node": 134,
                "to_node": 136,
                "direction": "up"
            },
            {
                "from_node": 136,
                "to_node": 134,
                "direction": "down"
            },
        ],
        "coordinates": posy(3070,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 84,
                "to_node": 42,
                "direction": "left"
            },
        ],
        "coordinates": posy(3190,90,120,90),
    },
    {
        "edges": [
            {
                "from_node": 42,
                "to_node": 85,
                "direction": "down"
            },
        ],
        "coordinates": posy(3150,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 84,
                "direction": "up"
            },
        ],
        "coordinates": posy(3270,180,70,20),
    },

    #cits to science rb btm
    {
        "edges": [
            {
                "from_node": 81,
                "to_node": 82,
                "direction": "right"
            },
        ],
        "coordinates": posy(2680,200,340,90),
    },
    {
        "edges": [
            {
                "from_node": 82,
                "to_node": 83,
                "direction": "right"
            },
        ],
        "coordinates": posy(3020,200,90,90),
    },
    {
        "edges": [
            {
                "from_node": 83,
                "to_node": 137,
                "direction": "down"
            },
            {
                "from_node": 137,
                "to_node": 83,
                "direction": "up"
            },
        ],
        "coordinates": posy(3070,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 83,
                "to_node": 85,
                "direction": "right"
            },
        ],
        "coordinates": posy(3110,200,80,90),
    },

    #science rb to senate top
    {
        "edges": [
            {
                "from_node": 141,
                "to_node": 84,
                "direction": "left"
            },
        ],
        "coordinates": posy(3310,90,160,90),
    },
    {
        "edges": [
            {
                "from_node": 99,
                "to_node": 141,
                "direction": "left"
            },
        ],
        "coordinates": posy(3470,90,90,90),
    },
    {
        "edges": [
            {
                "from_node": 100,
                "to_node": 141,
                "direction": "down"
            },
            {
                "from_node": 141,
                "to_node": 100,
                "direction": "up"
            },
        ],
        "coordinates": posy(3440,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 100,
                "to_node": 99,
                "direction": "down"
            },
            {
                "from_node": 99,
                "to_node": 100,
                "direction": "up"
            },
        ],
        "coordinates": posy(3520,70,70,20),
    },
    {
        "edges": [
            {
                "from_node": 140,
                "to_node": 99,
                "direction": "left"
            },
        ],
        "coordinates": posy(3560,90,20,90),
    },
    {
        "edges": [
            {
                "from_node": 48,
                "to_node": 140,
                "direction": "up"
            },
        ],
        "coordinates": posy(3540,180,70,20),
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(3580,90,90,200),
    },

    #science rb to senate btm
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 138,
                "direction": "right"
            },
        ],
        "coordinates": posy(3110,200,260,90),
    },
    {
        "edges": [
            {
                "from_node": 139,
                "to_node": 138,
                "direction": "up"
            },
            {
                "from_node": 138,
                "to_node": 139,
                "direction": "down"
            },
        ],
        "coordinates": posy(3330,290,70,20),
    },
    {
        "edges": [
            {
                "from_node": 138,
                "to_node": 48,
                "direction": "right"
            },
        ],
        "coordinates": posy(3370,200,210,90),
    },

    #senate down
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
        "coordinates": posy(3580,290,90,160),
    },
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
        "coordinates": posy(3670,400,120,90),
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
        "coordinates": posy(3750,380,70,20),
    },
    {
        "edges": [
            {
                "from_node": 64,
                "to_node": 50,
                "direction": "right"
            },
            {
                "from_node": 50,
                "to_node": 64,
                "direction": "left"
            },
        ],
        "coordinates": posy(3790,400,60,90),
    },
    {
        "edges": [
            {
                "from_node": 50,
                "to_node": 145,
                "direction": "down"
            },
            {
                "from_node": 145,
                "to_node": 50,
                "direction": "up"
            },
        ],
        "coordinates": posy(3810,490,70,20),
    },
    {
        "edges": [
            {
                "from_node": 50,
                "to_node": 47,
                "direction": "up"
            },
        ],
        "coordinates": posy(3850,290,90,200),
    },
    {
        "edges": [
            {
                "from_node": 49,
                "to_node": 142,
                "direction": "down"
            },
            {
                "from_node": 142,
                "to_node": 49,
                "direction": "up"
            },
        ],
        "coordinates": posy(3580,450,90,240),
    },
    {
        "edges": [
            {
                "from_node": 143,
                "to_node": 142,
                "direction": "left"
            },
            {
                "from_node": 142,
                "to_node": 143,
                "direction": "right"
            },
        ],
        "coordinates": posy(3560,620,20,70),
    },
    {
        "edges": [
            {
                "from_node": 142,
                "to_node": 146,
                "direction": "right"
            },
            {
                "from_node": 146,
                "to_node": 142,
                "direction": "left"
            },
        ],
        "coordinates": posy(3670,600,280,90),
    },
    {
        "edges": [
            {
                "from_node": 147,
                "to_node": 146,
                "direction": "down"
            },
            {
                "from_node": 146,
                "to_node": 147,
                "direction": "up"
            },
        ],
        "coordinates": posy(3910,580,70,20),
    },
    {
        "edges": [
            {
                "from_node": 146,
                "to_node": 51,
                "direction": "right"
            },
            {
                "from_node": 51,
                "to_node": 146,
                "direction": "left"
            },
        ],
        "coordinates": posy(3950,600,100,90),
    },
    {
        "edges": [
            {
                "from_node": 51,
                "to_node": 144,
                "direction": "up"
            },
            {
                "from_node": 144,
                "to_node": 51,
                "direction": "down"
            },
        ],
        "coordinates": posy(4010,580,70,20),
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(4050,600,100,90),
    },

    #senate up
    {
        "edges": [
            {
                "from_node": 47,
                "to_node": 46,
                "direction": "up"
            },
        ],
        "coordinates": posy(3850,140,90,150),
    },
    {
        "edges": [
            {
                "from_node": 46,
                "to_node": 44,
                "direction": "up"
            },
        ],
        "coordinates": posy(3850,-70,90,210),
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
        "coordinates": posy(3940,250,20,70),
    },
    {
        "edges": [
            {
                "from_node": 44,
                "to_node": 45,
                "direction": "up"
            },
            {
                "from_node": 45,
                "to_node": 44,
                "direction": "down"
            },
        ],
        "coordinates": posy(3850,-210,90,140),
    },
    {
        "edges": [
            {
                "from_node": 45,
                "to_node": 88,
                "direction": "right"
            },
            {
                "from_node": 88,
                "to_node": 45,
                "direction": "left"
            },
        ],
        "coordinates": posy(3940,-250,20,70),
    },
    {
        "edges": [
            {
                "from_node": 45,
                "to_node": 87,
                "direction": "left"
            },
            {
                "from_node": 87,
                "to_node": 45,
                "direction": "right"
            },
        ],
        "coordinates": posy(3820,-250,30,70),
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "left"
            },
        ],
        "coordinates": posy(3850,-260,90,50),
    },
    {
        "edges": [
            {
                "from_node": 44,
                "to_node": 43,
                "direction": "left"
            },
        ],
        "coordinates": posy(3730,-110,120,90),
    },
    {
        "edges": [
            {
                "from_node": 43,
                "to_node": 102,
                "direction": "left"
            },
        ],
        "coordinates": posy(3360,-110,400,90),
    },
    {
        "edges": [
            {
                "from_node": 102,
                "to_node": 101,
                "direction": "down"
            },
            {
                "from_node": 101,
                "to_node": 102,
                "direction": "up"
            },
        ],
        "coordinates": posy(3380,-20,70,20),
    },
    {
        "edges": [
            {
                "from_node": 43,
                "to_node": 101,
                "direction": "down"
            },
            {
                "from_node": 101,
                "to_node": 43,
                "direction": "up"
            },
        ],
        "coordinates": posy(3720,-20,70,20),
    },
    {
        "edges": [
            {
                "from_node": 102,
                "to_node": 84,
                "direction": "down"
            },
        ],
        "coordinates": posy(3270,-110,90,230),
    },

]