
from assembly.exceptions import BlockParseError

class Block(object):
    
    def __init__(self, nr, x1, y1, x2, y2):
        self.nr = nr
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    
    def level(self):
        return min(self.y1, self.y2)
    
    
    def depends_on(self, other):
        if self.level() == 0:
            return False
        
        if self.level() <= other.level():
            return False

        if other.top() != self.level() - 1:
            return False
        
        if self.left() > other.right():
            return False
        
        if self.right() < other.left():
            return False
        
        return True
    
    
    def left(self):
        return min(self.x1, self.x2)
    
    def right(self):
        return max(self.x1, self.x2)
    
    def top(self):
        return max(self.y1, self.y2)
        
        
    @staticmethod
    def from_string(string):
        
        parts = string.split()
        
        if len(parts) != 5:
            raise BlockParseError("Invalid number of parts in line")
        
        nr, x1, x2, y1, y2 = parts
        
        try:
            nr = int(nr)
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            
            b = Block(nr, x1, y1, x2, y2)
        
        except ValueError:
            raise BlockParseError("Error while converting text to integers")
        
        
        return b
    
    
    def __repr__(self):
        return "<Block %u (%u,%u) (%u,%u)>" % (self.nr, self.x1, self.y1, self.x2, self.y2)
            
        
