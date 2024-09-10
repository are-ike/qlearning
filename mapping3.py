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

    #science
    {
        "edges": [
            {
                "from_node": 85,
                "to_node": 148,
                "direction": "down"
            },
            {
                "from_node": 148,
                "to_node": 85,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,290,90,70),
    },
    {
        "edges": [
            {
                "from_node": 148,
                "to_node": 149,
                "direction": "left"
            },
            {
                "from_node": 149,
                "to_node": 148,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,320,20,70),
    },
    {
        "edges": [
            {
                "from_node": 148,
                "to_node": 150,
                "direction": "down"
            },
            {
                "from_node": 150,
                "to_node": 148,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,360,90,50),
    },
    {
        "edges": [
            {
                "from_node": 150,
                "to_node": 157,
                "direction": "right"
            },
            {
                "from_node": 157,
                "to_node": 150,
                "direction": "left"
            },
        ],
        "coordinates": posy(3280,370,60,70),
    },
    {
        "edges": [
            {
                "from_node": 150,
                "to_node": 151,
                "direction": "down"
            },
            {
                "from_node": 151,
                "to_node": 150,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,410,90,50),
    },
    {
        "edges": [
            {
                "from_node": 151,
                "to_node": 152,
                "direction": "left"
            },
            {
                "from_node": 152,
                "to_node": 151,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,420,20,70),
    },
    {
        "edges": [
            {
                "from_node": 151,
                "to_node": 153,
                "direction": "down"
            },
            {
                "from_node": 153,
                "to_node": 151,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,460,90,50),
    },
    {
        "edges": [
            {
                "from_node": 153,
                "to_node": 154,
                "direction": "right"
            },
            {
                "from_node": 154,
                "to_node": 153,
                "direction": "left"
            },
        ],
        "coordinates": posy(3280,470,50,70),
    },
    {
        "edges": [
            {
                "from_node": 153,
                "to_node": 155,
                "direction": "down"
            },
            {
                "from_node": 155,
                "to_node": 153,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,510,90,60),
    },
    {
        "edges": [
            {
                "from_node": 155,
                "to_node": 156,
                "direction": "left"
            },
            {
                "from_node": 156,
                "to_node": 155,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,530,20,70),
    },
    {
        "edges": [
            {
                "from_node": 155,
                "to_node": 157,
                "direction": "down"
            },
            {
                "from_node": 157,
                "to_node": 155,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,570,90,140),
    },
    {
        "edges": [
            {
                "from_node": 158,
                "to_node": 157,
                "direction": "left"
            },
            {
                "from_node": 157,
                "to_node": 158,
                "direction": "right"
            },
        ],
        "coordinates": posy(3280,640,20,70),
    },
    {
        "edges": [
            {
                "from_node": 157,
                "to_node": 52,
                "direction": "down"
            },
            {
                "from_node": 52,
                "to_node": 157,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,710,90,20),
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
        "coordinates": posy(3280,720,20,70),
    },
    {
        "edges": [
            {
                "from_node": 52,
                "to_node": 159,
                "direction": "down"
            },
            {
                "from_node": 159,
                "to_node": 52,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,730,90,40),
    },
    {
        "edges": [
            {
                "from_node": 159,
                "to_node": 160,
                "direction": "left"
            },
            {
                "from_node": 160,
                "to_node": 159,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,730,20,70),
    },
    {
        "edges": [
            {
                "from_node": 159,
                "to_node": 54,
                "direction": "down"
            },
            {
                "from_node": 54,
                "to_node": 159,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,770,90,80),
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
        "coordinates": posy(3280,810,20,70),
    },
    {
        "edges": [
            {
                "from_node": 54,
                "to_node": 161,
                "direction": "down"
            },
            {
                "from_node": 161,
                "to_node": 54,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,850,90,190),
    },
    {
        "edges": [
            {
                "from_node": 161,
                "to_node": 162,
                "direction": "left"
            },
            {
                "from_node": 162,
                "to_node": 161,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,1000,20,70),
    },
    {
        "edges": [
            {
                "from_node": 161,
                "to_node": 55,
                "direction": "down"
            },
            {
                "from_node": 55,
                "to_node": 161,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,1040,90,50),
    },
    {
        "edges": [
            {
                "from_node": 55,
                "to_node": 92,
                "direction": "right"
            },
            {
                "from_node": 92,
                "to_node": 55,
                "direction": "left"
            },
        ],
        "coordinates": posy(3280,1000,40,90),
    },
    {
        "edges": [
            {
                "from_node": 92,
                "to_node": 95,
                "direction": "up"
            },
            {
                "from_node": 95,
                "to_node": 92,
                "direction": "down"
            },
        ],
        "coordinates": posy(3300,980,70,20),
    },
    {
        "edges": [
            {
                "from_node": 92,
                "to_node": 56,
                "direction": "right"
            },
            {
                "from_node": 56,
                "to_node": 92,
                "direction": "left"
            },
        ],
        "coordinates": posy(3320,1000,150,90),
    },
    {
        "edges": [
            {
                "from_node": 95,
                "to_node": 56,
                "direction": "down"
            },
            {
                "from_node": 56,
                "to_node": 95,
                "direction": "up"
            },
        ],
        "coordinates": posy(3440,980,70,20),
    },
    {
        "edges": [
            {
                "from_node": 56,
                "to_node": 57,
                "direction": "right"
            },
            {
                "from_node": 57,
                "to_node": 56,
                "direction": "left"
            },
        ],
        "coordinates": posy(3470,1000,30,90),
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "right"
            },
        ],
        "coordinates": posy(3500,1000,50,90),
    },
    {
        "edges": [
            {
                "from_node": 55,
                "to_node": 93,
                "direction": "down"
            },
            {
                "from_node": 93,
                "to_node": 55,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,1090,90,120),
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
        "coordinates": posy(3280,1170,60,90),
    },
    {
        "edges": [
            {
                "from_node": 94,
                "to_node": 186,
                "direction": "right"
            },
            {
                "from_node": 186,
                "to_node": 94,
                "direction": "left"
            },
        ],
        "coordinates": posy(3340,1170,20,90),
    },
    {
        "edges": [
            {
                "from_node": 94,
                "to_node": 187,
                "direction": "down"
            },
            {
                "from_node": 187,
                "to_node": 94,
                "direction": "up"
            },
        ],
        "coordinates": posy(3300,1260,70,20),
    },
    {
        "edges": [
            {
                "from_node": None,
                "to_node": None,
                "direction": "up"
            },
        ],
        "coordinates": posy(3340,1170,30,90),
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
        "coordinates": posy(3190,1210,90,240),
    },
    {
        "edges": [
            {
                "from_node": 58,
                "to_node": 59,
                "direction": "left"
            },
            {
                "from_node": 59,
                "to_node": 58,
                "direction": "right"
            },
        ],
        "coordinates": posy(3170,1410,20,70),
    },
    {
        "edges": [
            {
                "from_node": 58,
                "to_node": 60,
                "direction": "down"
            },
            {
                "from_node": 188,
                "to_node": 58,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,1450,90,130),
    },
    {
        "edges": [
            {
                "from_node": 59,
                "to_node": 163,
                "direction": "down"
            },
        ],
        "coordinates": posy(2990,1450,90,130),
    },
    {
        "edges": [
            {
                "from_node": 164,
                "to_node": 188,
                "direction": "up"
            },
            {
                "from_node": 164,
                "to_node": 60,
                "direction": "up"
            },
        ],
        "coordinates": posy(3190,1580,90,200),
    },

    #to dli btm
    {
        "edges": [
            {
                "from_node": 3,
                "to_node": 164,
                "direction": "right"
            },
        ],
        "coordinates": posy(3030,1690,160,90),
    },
    {
        "edges": [
            {
                "from_node": 2,
                "to_node": 3,
                "direction": "right"
            },
        ],
        "coordinates": posy(1750,1690,1280,90),
    },

    #to dli top
    {
        "edges": [
            {
                "from_node": 60,
                "to_node": 163,
                "direction": "left"
            },
        ],
        "coordinates": posy(3030,1580,160,90),
    },
        {
        "edges": [
            {
                "from_node": 3,
                "to_node": 163,
                "direction": "up"
            },
            {
                "from_node": 163,
                "to_node": 3,
                "direction": "down"
            },
        ],
        "coordinates": posy(2990,1670,70,20),
    },
    {
        "edges": [
            {
                "from_node": 163,
                "to_node": 165,
                "direction": "left"
            },
        ],
        "coordinates": posy(2760,1580,270,90),
    },
    {
        "edges": [
            {
                "from_node": 165,
                "to_node": 166,
                "direction": "up"
            },
            {
                "from_node": 166,
                "to_node": 165,
                "direction": "down"
            },
        ],
        "coordinates": posy(2720,1560,70,20),
    },
    {
        "edges": [
            {
                "from_node": 165,
                "to_node": 4,
                "direction": "left"
            },
        ],
        "coordinates": posy(1750,1580,1010,90),
    },

]

{
    0: {1: 350.0},
    1: {0: 350.0, 167: 30.0},
    2: {167: 210.0, 3: 1280.0, 4: 50.0},
    3: {163: 20, 164: 160.0},
    4: {5: 600.0, 6: 60.0},
    5: {96: 60.0, 169: 20.0, 170: 20},
    6: {8: 20, 121: 40.0},
    8: {2: 30.0, 122: 40.0},
    10: {2: 620.0},
    11: {170: 110.0, 98: 20},
    12: {171: 20, 13: 40.0},
    13: {172: 20, 181: 50.0},
    14: {15: 70.0, 173: 20},
    15: {16: 50.0, 132: 70.0},
    16: {17: 80.0},
    17: {185: 50.0, 18: 90.0},
    18: {65: 20, 86: 180.0},
    19: {20: 120.0, 66: 20},
    20: {21: 60.0, 67: 160.0},
    21: {22: 170.0, 68: 20},
    22: {23: 40.0},
    23: {24: 30.0, 69: 80.0},
    24: {183: 640.0, 22: 30.0, 25: 20},
    25: {24: 20, 27: 20.0},
    27: {25: 20.0},
    28: {29: 80.0},
    29: {126: 280.0, 30: 80.0},
    30: {29: 80.0, 31: 30.0, 78: 60.0},
    31: {30: 30.0, 105: 270.0},
    32: {33: 100.0, 118: 300.0},
    33: {32: 90.0, 120: 470.0},
    34: {35: 20, 120: 120.0, 121: 70.0},
    35: {34: 20},
    36: {16: 100.0, 129: 20},
    37: {38: 20, 130: 310.0},
    38: {37: 20},
    39: {79: 20, 81: 110.0},
    40: {36: 700.0, 81: 40.0},
    41: {81: 20.0},
    42: {134: 80.0, 85: 40.0},
    43: {101: 20, 102: 160.0},
    44: {43: 120.0, 45: 80.0},
    45: {44: 80.0, 87: 30.0, 88: 20},
    46: {44: 210.0, 91: 20},
    47: {46: 150.0},
    48: {49: 160.0, 140: 20},
    49: {48: 170.0, 142: 240.0, 64: 120.0},
    50: {47: 110.0, 64: 60.0, 145: 20},
    51: {146: 100.0, 144: 20},
    52: {53: 20.0, 157: 20, 159: 40.0},
    53: {52: 20.0, 54: 20.0},
    54: {159: 80.0, 53: 20.0, 161: 190.0},
    55: {92: 40.0, 93: 40.0, 161: 50.0},
    56: {57: 30.0, 92: 150.0, 95: 20},
    57: {56: 30.0},
    58: {93: 240.0, 59: 20, 60: 130.0},
    59: {163: 100.0, 58: 20},
    60: {163: 160.0, 58: 130.0},
    61: {62: 290.0, 63: 20},
    62: {9: 190.0, 123: 20},
    63: {61: 20, 120: 20, 123: 20},
    64: {49: 120.0, 50: 60.0, 90: 20},
    65: {86: 20},
    66: {19: 20},
    67: {20: 160.0},
    68: {21: 20},
    69: {70: 20, 103: 290.0},
    70: {69: 20},
    71: {28: 40.0, 72: 20},
    73: {28: 20},
    74: {24: 290.0, 128: 20},
    75: {114: 20, 116: 170.0},
    76: {75: 150.0, 112: 60.0},
    77: {108: 60.0, 110: 180.0},
    78: {30: 60.0, 107: 40.0},
    79: {39: 20},
    80: {40: 40.0},
    81: {41: 20.0, 80: 30.0, 82: 250.0},
    82: {83: 90.0, 135: 20},
    83: {85: 100.0, 134: 20, 137: 20},
    84: {42: 30.0},
    85: {138: 80.0, 148: 50.0, 84: 40.0},
    86: {19: 50.0, 65: 20},
    87: {45: 30.0},
    88: {45: 20},
    90: {64: 20},
    91: {46: 20},
    92: {55: 40.0, 56: 150.0, 95: 20},
    93: {55: 40.0, 58: 240.0, 94: 50.0},
    94: {93: 50.0},
    95: {92: 20, 56: 20},
    96: {174: 320.0, 97: 20},
    97: {96: 20},
    98: {11: 20},
    99: {100: 20, 141: 90.0},
    100: {99: 20},
    101: {43: 20, 102: 20},
    102: {84: 450.0, 101: 20},
    103: {104: 290.0, 124: 20},
    104: {71: 40.0},
    105: {31: 270.0, 106: 150.0},
    106: {105: 150.0},
    107: {77: 60.0},
    108: {78: 60.0, 109: 70.0},
    109: {108: 70.0},
    110: {77: 180.0, 111: 70.0, 112: 50.0},
    111: {110: 70.0},
    112: {76: 60.0, 110: 50.0, 113: 30.0},
    113: {112: 30.0},
    114: {76: 160.0, 115: 50.0},
    115: {114: 50.0},
    116: {75: 170.0, 117: 80.0, 118: 80.0},
    117: {116: 80.0},
    118: {32: 300.0, 116: 80.0, 119: 120.0},
    119: {118: 120.0},
    120: {33: 470.0, 34: 120.0, 63: 20},
    121: {6: 40.0, 34: 70.0, 122: 30.0},
    122: {61: 60.0},
    123: {62: 20, 63: 20},
    124: {103: 20},
    125: {104: 20},
    126: {74: 80.0, 127: 20},
    127: {126: 20},
    128: {74: 20},
    129: {36: 20},
    130: {39: 190.0, 131: 20},
    131: {130: 20},
    132: {37: 160.0, 133: 20},
    133: {132: 20},
    134: {83: 20, 135: 90.0, 136: 20},
    135: {80: 220.0, 82: 20},
    136: {134: 20},
    137: {83: 20},
    138: {48: 190.0, 139: 20},
    139: {138: 20},
    140: {99: 20},
    141: {84: 160.0, 100: 20},
    142: {49: 240.0, 146: 280.0, 143: 20},
    143: {142: 20},
    144: {51: 20},
    145: {50: 20},
    146: {51: 100.0, 142: 280.0, 147: 20},
    147: {146: 20},
    148: {85: 50.0, 149: 20, 150: 30.0},
    149: {148: 20},
    150: {148: 30.0, 151: 30.0, 157: 60.0},
    151: {150: 30.0, 152: 20, 153: 50.0},
    152: {151: 20},
    153: {151: 50.0, 154: 50.0, 155: 60.0},
    154: {153: 50.0},
    155: {153: 60.0, 156: 20, 157: 140.0},
    156: {155: 20},
    157: {52: 20, 150: 60.0, 155: 140.0, 158: 20},
    158: {157: 20},
    159: {52: 40.0, 54: 80.0, 160: 20},
    160: {159: 20},
    161: {54: 190.0, 55: 50.0, 162: 20},
    162: {161: 20},
    163: {3: 20, 165: 270.0},
    164: {60: 20},
    165: {4: 990.0, 166: 20},
    166: {165: 20},
    167: {1: 30.0, 2: 210.0, 168: 20},
    168: {167: 20},
    169: {5: 20.0},
    170: {5: 20, 6: 630.0},
    171: {175: 160.0, 12: 20, 179: 20},
    172: {13: 20, 171: 40.0, 180: 20},
    173: {172: 130.0, 14: 20, 184: 20},
    174: {12: 160.0, 175: 20, 177: 20},
    175: {174: 20, 176: 110.0},
    176: {11: 160.0, 178: 20},
    177: {174: 20},
    178: {176: 20},
    179: {171: 20},
    180: {172: 20},
    181: {14: 80.0, 182: 20},
    182: {181: 20},
    183: {15: 20, 185: 70.0},
    184: {183: 20},
    185: {15: 20.0, 173: 60.0},
}
