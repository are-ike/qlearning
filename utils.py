import pygame

def generate_empty_matrix(node_number):
    space = []
    for _ in range(node_number):
        space.append([0]*node_number)
    return space

def draw_item(img_src, scale, angle=0):
    def draw(position):
        surf = pygame.image.load(img_src).convert_alpha()
        scaled_surf = pygame.transform.scale(surf, scale)
        rotated_surf = pygame.transform.rotate(scaled_surf, angle)
        rect = rotated_surf.get_rect(topleft = position)

        return (rotated_surf, rect)
    
    return draw

def copy_list(list, zero=True):
    new_list = {}
    for key, value in list.items():
        new_sub_list = {}
        for key2, val in value.items():
            new_sub_list[key2] = 0 if zero else val
        new_list[key] = new_sub_list

    return new_list

# def get_img(type):
#             if(type == 1): return 'images/build1.png'
#             if(type == 2): return 'images/build2.png'
#             if(type == 3): return 'images/gate.png'
   # draw_fn = draw_item(get_img(node["type"]), (250,250)) 
            # self.screen.blit(*draw_fn(pos))

 # def draw_road(self, position, length, angle):
    #     draw_fn = self.draw_item('images/road3.png', (400,length), angle) 
    #     return draw_fn(position)
  
# def draw_edge(self,screen,road):
    #     def get_angle(direction):
    #         if(direction == "left"): return 270
    #         if(direction == "right"): return 90
    #         if(direction == "up"): return 180
    #         if(direction == "down"): return 0

    #     screen.blit(*self.draw_road(road["position"], road["length"], get_angle(road["direction"])))  

    # def draw_green (self): 
    #     for item in green:
    #         pos = item["position"]
    #         size = item["size"]
    #         pygame.draw.rect(self.screen,'#0d4b0d', pygame.Rect(pos[0], pos[1], size[0], size[1]))


    # def draw_building (self, color):
    #      pygame.draw.rect(self.screen,color, pygame.Rect(0,0,1200,800))

            # def draw_car(self, position, angle):
    #     draw_fn = self.draw_item('images/car.png', (70,70), angle) 
    #     return draw_fn(position)
                # for car in self.car_objects:
            #     value = self.draw_car(**car.draw_car())
            #     self.car_rects.append(value)
            #     screen.blit(*value)

        # if frames == 0:
        #     Car.traffic_matrix[self.from_node][self.to_node] -= 1
        
        #     self.from_node = self.to_node
        #     self.select_to_node()

        #     Car.traffic_matrix[self.from_node][self.to_node] += 1
        #     #remove car
        # else:
        #     self.frames_left = frames

    # def update_position(self, x=None, y=None):
    #     self.position = (x if x else self.position[0], y if y else self.position[1])

        # def draw_node(self,screen,node):
    #     screen.blit(*self.draw_building(node["position"])) 

                # if len(self.car_rects) and len(self.car_objects):
            #     for car in self.car_objects:
            #         if car.frames_left > 0:
            #              car.update_position(car.position[0] + 10)

            # pygame.draw.rect(screen,'#268b07', pygame.Rect(0,0,1200,800)) 232323
            #pygame.draw.rect(screen,'#0d4b0d', pygame.Rect(0,0,1200,800))
          
            # for node in mappings["nodes"]:
            #     self.draw_node(screen, node)

            # for edge in mappings["edges"]:
            #     self.draw_edge(screen, edge)

        # for road in self.roads:
        #     road.draw(self.map) #Drawing road here so that road shows during loop

        # for car in self.cars:
        #     car.start(self.map)
            #for _  in range(100): continue
            #pygame.time.delay(2000)

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


# roads = [
#     {
#         "edges": [
#             {
#                 "from_node": 0,
#                 "to_node": 1,
#                 "direction": "down"
#             },
#             {
#                 "from_node": 1,
#                 "to_node": 0,
#                 "direction": "up"
#             },
#         ],
#         "coordinates": (790,330,120,400),
#         "one_way": False
#     },
#     {
#         "edges": [
#             {
#                 "from_node": 1,
#                 "to_node": 2,
#                 "direction": "down"
#             },
#             {
#                 "from_node": 2,
#                 "to_node": 1,
#                 "direction": "up"
#             },
#         ],
#         "coordinates": (790,730,120,400),
#         "one_way": False
#     },
#     {
#         "edges": [
#             {
#                 "from_node": 2,
#                 "to_node": 3,
#                 "direction": "left"
#             },
#             {
#                 "from_node": 3,
#                 "to_node": 2,
#                 "direction": "right"
#             },
#         ],
#         "coordinates": (90,1130,700,120),
#         "one_way": True
#     },
#     {
#         "edges": [
#             {
#                 "from_node": 2,
#                 "to_node": 5,
#                 "direction": "down"
#             },
#             {
#                 "from_node": 5,
#                 "to_node": 2,
#                 "direction": "up"
#             },
#         ],
#         "coordinates": (790,1250,120,400),
#         "one_way": False
#     },
#     {
#         "edges": [
#             {
#                 "from_node": 3,
#                 "to_node": 4,
#                 "direction": "down"
#             },
#             {
#                 "from_node": 4,
#                 "to_node": 3,
#                 "direction": "up"
#             },
#         ],
#         "coordinates": (0,1250,120,400),
#         "one_way": False
#     },
#     {
#         "edges": [
#             {
#                 "from_node": 4,
#                 "to_node": 5,
#                 "direction": "right"
#             },
#             {
#                 "from_node": 5,
#                 "to_node": 4,
#                 "direction": "left"
#             },
#         ],
#         "coordinates": (90,1650,700,120),
#         "one_way": False
#     },
# ]

# roundabouts = [
#     {
#         "position": pos(850,270),
        
#     }
# ]

# green = [
#     {
#         "position": pos(130,130),
#         "size": siz(240,140),
#     },
#     {
#         "position": pos(220,270),
#         "size": siz(60,500),
#     },
#     {
#         "position": pos(50,270),
#         "size": siz(60,500),
#     },
# ]

# misc = [
#     {
#         "position": pos(80,80),
#         "size": siz(240,140),
#     },
#     {
#         "position": pos(170,220),
#         "size": siz(60,500),
#     },
# ]






            





