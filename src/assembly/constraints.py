

class Constraints(object):

    
    def __init__(self):
        self.constraints = dict()
    
    
    @staticmethod
    def from_blocks(blocks):
        
        c = Constraints()

        lower_level_blocks = list()
        current_level_blocks = list()

        lvl = 0
        while True:
            current_level_blocks = blocks.on_level(lvl)
            
            for b1 in current_level_blocks:
                for b2 in lower_level_blocks:
                    if b1.depends_on(b2):
                        c.set_constraint(b1, b2)
                
                lower_level_blocks.append(b1)
                
            lvl += 1
            
            if len(lower_level_blocks) == len(blocks):
                break
            
        
        c.print_depencies()
                    

    def set_constraint(self, block, depends):
        if not block.nr in self.constraints.keys():
            self.constraints[block.nr] = list()
            
        if depends is not None:
            self.constraints[block.nr].append(depends)
            
        
    def print_depencies(self):
        retval = ""
        for k, v in self.constraints.items():
            depencencies = ""
            for b in v:
                depencencies += "%u, " % b.nr
                
            retval += "%u depends on %s" % (k, depencencies)
            retval += "\n" 
            
        print(retval)
        
        
