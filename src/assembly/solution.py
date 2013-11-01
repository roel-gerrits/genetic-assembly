
class Solution(object):
    
    def __init__(self, factory):
        self.route = list()
        self.factory = factory
        
    
    def add_block_to_route(self, block):
        self.route.append(block)
         
    
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
    