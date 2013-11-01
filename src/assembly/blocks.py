
from io import StringIO
from assembly.block import Block

class Blocks(object):
    
    def __init__(self):
        self.blocks = dict()
        self.levels = dict()
        
    
    @staticmethod
    def from_string(string):
        s = StringIO(string)
        
        blocks = Blocks()
        
        while True:
            line = s.readline()
        
            line = line.strip()
            
            if len(line) == 0:
                break
            
            b = Block.from_string(line)
            
            blocks.add_block(b)
        
        return blocks
            
            
    def add_block(self, b):
        self.blocks[b.nr] = b
        level = b.level()
        
        if not level in self.levels.keys():
            self.levels[level] = list()
            
        self.levels[level].append(b)
        
        
    def on_level(self, lvl):
        return self.levels.get(lvl, [])

    
    def __len__(self):
        return len(self.blocks)
    
    
    def __iter__(self):
        return iter(self.blocks.values())
        
        
