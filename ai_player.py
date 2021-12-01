import random
from consts import *
from math import inf

GAMEOBJECT_TYPES = {
    "banana": 0,
    "coin": 1,
    "cauldron": 2
}

class Player(GamePlayer):
    def __init__(self):
        self.name = "Pikachu"
        self.group = "26A"
        self.obj_values = dict()
        self.total_game_objs = None
        #self.collected_objs = [0, 0, 0]
        
    def get_my_bot(self, game_map, cur_pos):
        ''' (list, typle) -> Bot
        Returns the Bot object for this player.
        '''
        i, j = cur_pos
        bots = game_map[i][j]
        assert len(bots) != 0
        for bot in bots:
            if bot.i == self.i:
                return bot
    
    def get_delta_between_points(pt1, pt2):
        ''' (tuple<int, int>, typle<int, int>) -> tuple<int, int>
        Returns the delta-x and the delta-y between the two points.
        '''
        if pot1[0] - pt2[0] > 0:
            dy = 1
        elif pt1[0] - pt2[0] < 0:
            dy = -1
        elif pt1[1] - pt2[1] > 0:
            dx = 1
        elif pt1[1] - pt2[1] > 0:
            dx = -1
        else:
            raise ValueError
        return dy, dx

    def update_collected_objects(self): # to do
        ''' should update the self.collected_objs attribute whenever we collect a new gameobj.'''
        # if check that current pos is same as pos of game obj in the previous turn:
        # did we collect a banana, coin, or cauldron?
        # self.collected_objs = updated list
        pass
    
    
    def get_all_game_objects(self, game_map): #tested, completed
        ''' (list) -> list<GameObject>
        Returns a list of the positions of the GameObjects on the map.
        
        For example:
        If there is 1 banana, 4 coins, and 5 cauldrons, [[(x, y)], [()()(),()], [(), (), (), (), ()]] will be returned.
        
        The 0th index represents bananas, 1 represents coins, and 2 represents cauldrons.
        '''
   
        game_objs = {0:0, 1: 0, 2: 0}
        # game_info = {num_players : 0, num_game_objs : game_objs}

        for row in game_map:
            for element in row:
                if element == []:
                    continue
                else:
                    for obj in element:
                        if type(obj) == GameObject:
                            game_objs[obj.obj_type] += 1   
        return game_objs
        
    def get_distances_to_objects(self, game_map, cur_pos):
        ''' (list) -> dict<GameObject: int>
        Returns a dictionary where the keys are GameObjects
        and the value for a GameObject is its distance to the
        current player.
        '''
        pass
    
    def get_nearest_bot(self, game_map, position):
        ''' (list, tuple<int, int>) -> Bot
        Returns the nearest Bot object to the given position.
        '''
        pass
    
    def get_total_available_objects(self, game_map, obj_type):
        ''' (list) -> int
        Returns the total number of currently available objects on the grid.
        If obj_type is -1, get total of all categories. Otherwise, get
        total of the one particular object type given.
        '''
        pass
    
    def get_total_objects(self, game_map, obj_type):
        ''' (list int) -> int
        Returns the total number of the given object type, including objects
        both on the grid and those that have already been picked up.
        '''
        pass
    
    def step(self, game_map, turn, cur_pos):
        # game_map is a matrix dimensions: rows = len(game_map), cols = len(game_map[0])
        my_bot = self.get_my_bot(game_map, cur_pos)
        
    
        print('collected objs', self.collected_objects)
        if turn == 0:
           self.obj_values = get_obj_values(game_map)
           self.total_game_objs = get_game_objects(game_map)
           print("obj values: ", self.obj_values)
        else: #turn != 0:
            ''' if a bot or player has collected an object, update self.obj_values to reflect the new object values.
            more specifically:
            -if more than 50% of an object has been collected, its value changes to 0.0.
            -if a bot or us only needs one more of an object to get 50% or more of that object, its value changes to 1.0'''
            pass
        
        print("turn: ", turn)
        print("cur_pos: ", cur_pos)
        print("get closest object: ", get_closest_object_direction(game_map, cur_pos))

        pretty_print(game_map)
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                for item in game_map[i][j]:
                    if type(item) is GameObject:
                        obj_type = item.obj_type
                    
                    elif type(item) is Bot:
                        c_objs = item.collected_objects
                    
        
        
        game_objects = get_game_objects(game_map)
        print("game objects: ", game_objects)
        
            
        print(self.total_game_objs)
        print("obj values ouside if block:", self.obj_values)
        
        print("cur_pos: ", cur_pos)
        
        move_to = (2, 3)
        dy, dx = get_delta_between_points(move_to, cur_pos)
        action = get_action_for_delta(dx, dy) # dx and dy are reversed in this function
        return action



    def get_obj_values(game_map):
        ''' (list) -> dict
        Assigns a float in [0, 1] corresponding to the value of gaining one GameObject of that type.
        
        E.g. If there is 1 banana, 4 coins, and 5 cauldrons, {0: 1.0, 1: 0.25, 2: 0.2} will be returned.
        because 1/1 = 1, 1/4 = 0.25, and 1/5 = 0.2. So the banana is the most valuable in this case
        because it has a value of 1
        '''
        total = get_game_objects(game_map)
        
        for key in total:
            if total[key] == 0: # e.g. there are no bananas in the game map, total is {0:0, 1:4, 2:6}
                total[key] = 0
            else:
                total[key] = 1/total[key]

        return total
        


    def get_closest_object_direction(game_map, cur_pos): #in progress
            ''' (list, tuple) -> tuple
            Returns the  of the closest object to us (either 'up', 'down', 'left', or 'right').
            '''
            closest_objs = []
            for i in range(len(game_map)):
                for j in range(len(game_map[i])):
                    things = game_map[i][j]
                    if len(things) == 0:
                        continue
                    
                    if type(things[0]) is GameObject:
                        obj_type = things[0].obj_type
                        distance = abs(cur_pos[0] - i) + abs(cur_pos[1] - j)
                        print('distance', distance)
                        if len(closest_objs) == 0:
                            closest_objs.append(things[0].position)
                            print("when len is 0:", closest_objs)
                        else:
                            old_distance = abs(cur_pos[0] - closest_objs[0][0]) + abs(cur_pos[1] - closest_objs[0][1])
                            print("old distance", old_distance)
                            # calculates the distance between us and the game object e.g. cur_pos is (0, 5) 
                            if distance < old_distance:
                                closest_objs = [(things[0].position)]
                                print("if distance > old d:", closest_objs)
                            elif distance == old_distance:
                                closest_objs.append(things[0].position)
                                print("distance == old distance:", closest_objs)

            print("final:", closest_objs)
            
            return closest_objs
        
    def get_obj_w_highest_val(game_map, cur_pos):
        ''' reduces the closest_objs list into one tuple representing the object that has the highest value.
    if two objects are worth the same, finds the closest object with the highest value to those objects.
    Keeps on doing that until there is no two closest objects with the same value.

    In the end, if there are still two closest objects with the same value, picks one direction randomly'''
        closest_objs = get_closest_object_direction(game_map, cur_pos)
        if len(closest_objs) == 1: #  there is only one closest object
            if closest_objs[0][0] > cur_pos[0]:
                return "down"
            if closest_objs[0][0] < cur_pos[0]:
                return "up"
            if closest_objs[0][1] > cur_pos[1]:
                return "left"
            if closest_objs[0][1] < cur_pos[1]:
                return "right"
        else: # there is more than one closest object:
            #banana, coin or cauldron?
            for obj_pos in closest_objs:
                obj_type = game_map[obj_pos[0]][obj_pos[1]].obj_type
                print("obj_type: ", obj_type)
                
                
            return "up" # here for testing purposes

'''
[[[GameObject:{0, 0| 0}], [], [GameObject:{0, 2| 2}], [], []],\
[[], [], [], [GameObject:{1, 3| 2}], []], \
[[GameObject:{2, 0| 0}], [], [], [], []], \
[[Bot:{3, 0 | b1 | [0, 0, 0]}, Bot:{3, 0 | b2 | [0, 0, 0]}], [GameObject:{3, 1| 2}], [Bot:{3, 2 | b3 | [0, 0, 0]}], [], [GameObject:{3, 4| 0}]], \
[[], [], [], [GameObject:{4, 3| 1}], [GameObject:{4, 4| 0}]]]
   
The grid of the game is represented as a two-dimensional list (matrix). Each spot in the grid
will be a list. If there is nothing in the square, the list will be empty. If there is one or
more bots in the square, there will be one or more Bot objects in the list. If there is an
object (coin, cauldron or banana), there will be a GameObject object in the list.

'''
#mylist = [[[GameObject:{0, 0| 0}], [], [GameObject:{0, 2| 2}], [], []], [[], [], [], [GameObject:{1, 3| 2}], []]]



''' Things to do:
SHAZA- make it so that get_obj_w_highest_val(game_map, cur_pos) returns the direction of the object with the highest value

ANNE- then, write a new function that keeps on looping until there are no 2 objs
with the same highest value. So if there are two closest objs (A and B) w the same value, this function will find the closest gameobjs
to A and B (say C and D). Then, of these new gameobjs, this function will determine which has the highest value. 
But if the closest objs of the closest objs (C and D) have the same value, repeat the loop.... until there is only one closest obj w the
highest value. Finally, return the direction to the ORIGINAL closest obj that has the best connections to the other closest objs.

If, after trying all routes, there is no one closest obj w the highest value, just pick one randomly.

- modify the get_obj_values function so that it accounts for what the player and bots have already collected.

ALEX - figure out way to keep track of all the objects our player has collected (get_collected_objs())

BETTY - if there are 0 bananas, 4 coins and 10 cauldrons in total, and we have so far collected 0 coins and 5 cauldrons, then the cauldron should be
worth more than the coin so that we will beat them in the cauldron category. i.e. prioritize getting over 50% in a category
- after we collect more than 50% in one category, the value of that object changes to 0. (if there are 4 coins and we've collected 3 coins,
we dont care abt collecting coins anymore.


link to tutorial on this project:
https://mcgill.zoom.us/rec/play/EQGsz2_1Dw1yN9NXCPV4VCHWGZQwxBULVWFxFwhN3KguOPYmekmfZRmOrvyLi6zIOjxIaQsDiHzfGI4O.pJ4TxoZ82DAMcn9Y?startTime=1638299251000&_x_zm_rtaid=lsqUb6rzS5aZQQsQ4mIm9A.1638324155638.874ce971415eb19dd674735661571f09&_x_zm_rhtaid=629

'''
