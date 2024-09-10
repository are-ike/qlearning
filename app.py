import copy
import numpy as np
from main import evall

def argmax(dict):
    return max(dict, key=dict.get)

q_table = {0: {1: np.float64(202.17842231630857)}, 1: {0: np.float64(253.6433701654311), 2: np.float64(167.51263419469572)}, 2: {1: np.float64(197.07577930875814), 3: np.float64(211.5792897443714), 4: np.float64(137.01379357397798)}, 3: {4: np.float64(130.11007105881384), 59: np.float64(273.0631179208947), 60: np.float64(167.56364436796886)}, 4: {5: np.float64(153.49773804208698), 6: np.float64(171.94863631869248)}, 5: {6: np.float64(166.2133220984237), 96: np.float64(218.86071934576964)}, 6: {8: np.float64(175.16408662665202), 34: np.float64(205.44175053015772)}, 8: {2: np.float64(163.92166092914732), 61: np.float64(217.33723632662253)}, 10: {2: np.float64(163.17779868320446)}, 11: {5: np.float64(174.9109360954256), 98: np.float64(270.0377558808626)}, 12: {11: np.float64(219.00710573902836), 13: np.float64(138.2803610662276)}, 13: {12: np.float64(174.45257394376642), 14: np.float64(137.8620247899293)}, 14: {13: np.float64(138.3915077297601), 15: np.float64(170.385936874839)}, 15: {14: np.float64(133.09210488043257), 16: np.float64(133.31790419828096), 37: np.float64(213.51919977537887)}, 16: {17: np.float64(166.14613362849897)}, 17: {15: np.float64(167.04981179696273), 18: np.float64(211.2155668019434)}, 18: {65: np.float64(266.4548275703541), 86: np.float64(207.93996939112182)}, 19: {20: np.float64(213.76514931624038), 66: np.float64(269.44221346593474)}, 20: {21: np.float64(217.60179752847128), 67: np.float64(268.11087348324145)}, 21: {22: np.float64(138.11270830797616), 68: np.float64(271.5473116175993)}, 22: {23: np.float64(171.6576636476762)}, 23: {24: np.float64(170.1210169705509), 69: np.float64(217.9309260623918)}, 24: {15: np.float64(156.45000570976015), 22: np.float64(135.66043695316225), 25: np.float64(216.9334348391145)}, 25: {24: np.float64(166.061296000227), 26: np.float64(268.2485717293546), 27: np.float64(273.97514535424546)}, 26: {25: np.float64(219.04413464300717)}, 27: {25: np.float64(218.4917236352253)}, 28: {29: np.float64(108.2418158714311)}, 29: {74: np.float64(134.68058836656354), 30: np.float64(81.20878774381356)}, 30: {29: np.float64(107.27954044657558), 31: np.float64(65.04365943602598), 78: np.float64(63.481886027799696)}, 31: {30: np.float64(83.4864384885891)}, 32: {33: np.float64(163.43080685294376), 75: np.float64(92.38861399601338)}, 33: {32: np.float64(124.95666540593572), 34: np.float64(206.97835188245787)}, 34: {6: np.float64(168.45111459980504), 33: np.float64(165.8963904690619), 35: np.float64(266.63760814702187)}, 35: {34: np.float64(216.3527935940943)}, 36: {16: np.float64(130.39190814962166)}, 37: {38: np.float64(271.42521345611124), 39: np.float64(203.61668521086995)}, 38: {37: np.float64(214.80040948592838)}, 39: {79: np.float64(270.0516209919573), 81: np.float64(87.58418590991177)}, 40: {36: np.float64(102.8661060468883), 81: np.float64(87.21812650324551)}, 41: {81: np.float64(86.5366949043568)}, 42: {83: np.float64(135.9764474332386), 85: np.float64(171.95479379214714)}, 43: {101: np.float64(273.95415874784186), 102: np.float64(85.87737311308045)}, 44: {43: np.float64(215.3848476637115), 45: np.float64(219.67954751112018)}, 45: {44: np.float64(172.17509120850505), 87: np.float64(269.7819719002381), 88: np.float64(272.03833674345947)}, 46: {44: np.float64(174.4140822002826), 91: np.float64(270.94560523680695)}, 47: {46: np.float64(220.6870158916941)}, 48: {49: np.float64(173.04581385193285), 99: np.float64(216.77393199651289)}, 49: {48: np.float64(175.26448810339767), 51: np.float64(131.91298409035613), 64: np.float64(215.91846103127511)}, 50: {47: np.float64(176.47393753226174), 64: np.float64(217.43096626801264)}, 51: {49: np.float64(173.73299275121082)}, 52: {53: np.float64(271.0211181046088), 54: np.float64(216.66369982934827), 85: np.float64(169.3289600945744)}, 53: {52: np.float64(213.27853094347398), 54: np.float64(215.9021626590692)}, 54: {52: np.float64(217.27100832009245), 53: np.float64(268.0858498102266), 55: np.float64(174.22793291192698)}, 55: {54: np.float64(216.54459434581997), 92: np.float64(219.68963431761958), 93: np.float64(210.95375599126686)}, 56: {57: np.float64(270.4388327245282), 92: np.float64(219.3901178594965), 95: np.float64(275.1510150043298)}, 57: {56: np.float64(218.98529718914796)}, 58: {93: np.float64(213.88523041451467), 59: np.float64(272.19463491473545), 60: np.float64(168.69974455813167)}, 59: {3: np.float64(214.17760556097284), 58: np.float64(216.81913885744297)}, 60: {3: np.float64(213.28735041137196), 58: np.float64(206.85768818365887)}, 61: {62: np.float64(217.86410088974492), 63: np.float64(271.8316408867156)}, 62: {9: np.float64(-np.inf), 63: np.float64(273.0568644192279)}, 63: {61: np.float64(215.16298858951131), 62: np.float64(217.11794744265205)}, 64: {49: np.float64(173.3324558120794), 50: np.float64(168.75710485256616), 90: np.float64(270.1738113921856)}, 65: {86: np.float64(214.0202294206195)}, 66: {19: np.float64(216.91677020934537)}, 67: {20: np.float64(215.61083673397187)}, 68: {21: np.float64(219.4406902834062)}, 69: {70: np.float64(274.58553065085397), 71: np.float64(66.36148117570993)}, 70: {69: np.float64(219.23511812644023)}, 71: {28: np.float64(87.11803114774247), 72: np.float64(-np.inf)}, 73: {28: np.float64(86.67335951337984)}, 74: {24: np.float64(169.83325618553485)}, 75: {32: np.float64(129.20709899873225), 76: np.float64(75.68541631974576)}, 76: {75: np.float64(104.81745442693196), 77: np.float64(62.853589063803135)}, 77: {76: np.float64(80.36657144391398), 78: np.float64(68.70931176696529)}, 78: {30: np.float64(85.7157184732775), 77: np.float64(65.68039922703349)}, 79: {39: np.float64(217.48019001691745)}, 80: {40: np.float64(82.24014546008216)}, 81: {41: np.float64(64.1997083808547), 80: np.float64(61.69804043877931), 82: np.float64(108.86989571759696)}, 82: {80: np.float64(63.06117412994661), 83: np.float64(137.50234633941926)}, 83: {82: np.float64(106.42703391626036), 85: np.float64(171.26676634706823)}, 84: {42: np.float64(135.8641324370955)}, 85: {48: np.float64(175.07270166621777), 52: np.float64(215.71288615327916), 84: np.float64(103.9539772658988)}, 86: {19: np.float64(218.32584086024585), 65: np.float64(266.4940460856527)}, 87: {45: np.float64(218.9457005389325)}, 88: {45: np.float64(219.69823214415487)}, 90: {64: np.float64(218.07728267955568)}, 91: {46: np.float64(218.93661043657175)}, 92: {55: np.float64(170.99072550090708), 56: np.float64(220.19380120778072), 95: np.float64(275.45224419808386)}, 93: {55: np.float64(175.17191724053146), 58: np.float64(215.6943289030683), 94: np.float64(273.16727433238873)}, 94: {93: np.float64(216.61563887483035)}, 95: {92: np.float64(217.47365144693526), 56: np.float64(219.3764780259696)}, 96: {12: np.float64(174.41839995380573), 97: np.float64(268.7594214476127)}, 97: {96: np.float64(216.5480895378247)}, 98: {11: np.float64(217.92146552182487)}, 99: {84: np.float64(107.73304363990005), 100: np.float64(271.1461337454662)}, 100: {99: np.float64(218.6828267118327)}, 101: {43: np.float64(217.58880459113692), 102: np.float64(85.63182106172334)}, 102: {84: np.float64(106.75617543294081)}, 9: {0: -np.inf}, 72: {0: -np.inf}}
carparks = [0,26,27,35,38,53,57,59,63,65,66,67,68,70,79,87,88,90,91,94,95,97,98,100,101,105]
available_carparks = [26]

carparks = {
    124: 'Faculty of Environmental Sciences CarPark 1',
    70: 'Faculty of Environmental Sciences CarPark 2',
    128: 'Unilag Multipurpose Hall',
    25: 'Sports Center Parking Lot',
    27: 'Sub Shopping Complex', 
    190: 'Multipurpose Hall C',
    38: 'New Hall Shopping Complex',
    101: 'Faculty of Arts Parking Lot 2',
    100: 'Faculty of Arts Parking Lot 1',
    90: 'Main Campus Car Park',
    157: 'Unilag Bookshop Parking Lot 1',
    139: 'Unilag Bookshop Parking Lot 2',
    53: 'Unilag Alumni Jubilee House Park',
    95: 'Jaja Car Park',
    59: 'UNILAG Staff School Car Park',
    63: 'Parking Lot towards Secong Gate',
    65: 'University Of Lagos Central Mosque Parking Lot',
    66: 'Chapel Of Christ Our Light Parking Lot',
    67: 'Behind Chapel Parking Lot',
    68: 'St. Thomas More Parking Lot',
    98: 'Faculty of Social Science Parking Lot',
    97: 'Complex Opposite Faculty of Social Science',
    111: 'Car Park Opposite El Kanemi Hostel',
    35: 'Unilag Consult Parking Lot',
    91: 'Faculty of Law Parking Lot',
    88: 'Faculty of Management Science Parking Lot',
    145: 'Engineering Car Park',
    57: 'Faculty of Science Car Park',
    186: 'Department of Chemical Engineering Car Park 1',
    187: 'Department of Chemical Engineering Car Park 2'
}

start_locations = {
    1: {73: 'University of Lagos First Gate Entrance'},
    2: {126: 'University Road - WEMA Bank'},
    3: {132: 'University Road - Access Bank'},
    4: {41: 'Kosoko Drive - CITS'},
    5: {166: 'Anchor Gas'},
    6: {8: 'International School Road To Second Gate Exit'},
    7: {183: 'Unilag Petrol Station'},
    8: {176: 'Commercial Road - NITDA IT Hub'},
    9: {168: 'International School, University Of Lagos'},
    10: {10: 'University of Lagos Second Gate Entrance'},
    11: {51: 'Oduduwa Drive - Julius Berger Hall'},
    12: {142: 'Oduduwa Drive - D.K. Olukoya Laboratories'},
    13: {47: 'Senate Building'},
    14: {44: 'Zenith Bank Drive'},
    15: {115: 'Kofo Hall'},
    16: {116: 'Ransome Kuti Road - Opvine'},
    17: {32: 'Ransome Kuti Roundabout'},
    18: {1: 'Unilag Distance Learning Institute - DLI'},
    19: {83: 'University Road - Unilag Media Centre'},
    20: {49: 'Oduduwa Drive - Mariere Pass'},
    21: {135: 'University Road - Unilag Fire Service'},
    22: {155: 'Tafawa Balewa Way - Moremi Hall'},
    23: {22: 'Sports Center Roundabout'},
    24: {5: 'Commercial Road - Academic Publishing Centre'},
}

def search(node):
    temp_q_table = copy.deepcopy(q_table) 
    path = [node]
    carpark_found = False
    
    while not carpark_found:
        next_node = argmax(temp_q_table[node])
        
        if next_node in available_carparks: 
            carpark_found = True
            path.append(next_node)
        elif next_node in carparks:
            temp_q_table[node][next_node] = -np.inf
        else:
            if next_node in path:
                temp_q_table[next_node][node] = -np.inf
            else:
                path.append(next_node)
                
            node = next_node
    
    return path

def start ():
    print('Select a starting point')
    print('-------------------------')
    print('1. University of Lagos First Gate Entrance')
    print('2. University of Lagos Second Gate Entrance')
    print('3. Senate Building')
    print('4. WEMA Bank')
    print('5. NITDA Hub')
    print('\n')

    start_node = eval(input('Enter number: '))
    if start_node == 1: start_node = 73
    path = search(start_node)
    print(path)
    evall(path)

start()






# q_table = {
#     0: {1: 200, 2: 300},
#     1: {3: 20, 4: 400},
#     2: {0: 400, 1: 100},
#     3: {5: 200},
# }
# carparks = [2,4,5]
# available_carparks = [2,5]