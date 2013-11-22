
import random

class Solution(object):
    
    def __init__(self, factory):
        self.available_blocks = set(factory.blocks)
        self.route = list()
        self.factory = factory
        
    
    def add_block_to_route(self, block):
        self.route.append(block)
    
    
    def complete_from_factory(self, hints):

        blocks_todo = self.available_blocks.difference(self.route)
        hints = hints.route
        
        while len(blocks_todo) > 0:
            
            candidates = self.factory.pick_candidates(blocks_todo, self.route)
            
            for hint in hints:
                if hint in candidates:
                    the_chosen_one = hint
            else:
                the_chosen_one = random.choice(list(candidates))
        
            self.add_block_to_route(the_chosen_one)
            blocks_todo.remove(the_chosen_one)
                        
        
    def calc_distance(self):
        distance = 0
        prev_pos = 0
        cur_pos = 0
        
        for block in self.route:
            cur_pos = self.get_block_position(block)
            
            sub_distance = abs(cur_pos - prev_pos)
            
            prev_pos = cur_pos
            
            distance += sub_distance
        
        distance += cur_pos
        
        return distance 
    
    
    def splice(self, begin, end=None):
        s = Solution(self.factory)
        
        for block in self.route[begin : end]:
            s.add_block_to_route(block)
            
        return s
    
    
    def get_block_position(self, block):
        return block.nr
    
    
    def count(self):
        return len(self.route)
    
    
    def get_block(self, pos):
        return self.route[pos]
    
    
    def length(self):
        return self.calc_distance()
    
    
    def __len__(self):
        return self.calc_distance()
    
    
    def __repr__(self):
        
        route = "0-"
        
        for block in self.route:
            route += str(block.nr)
            route += "-"
        
        route += "0"
        
        return "<Solution %s %u>" % (route, self.length())
    
