'''
Created on Oct 3, 2013

@author: roel
'''

from assembly.blocks import Blocks
from assembly.constraints import Constraints
from genetic.bio import Bio

if __name__ == '__main__':
#     c = Constraints.from_blocks(Blocks.from_string("""1 3 3 2 3
#         2 0 0 1 2
#         3 2 3 0 0
#         4 1 2 1 2
#         5 0 2 3 3
#         6 3 3 1 1
#         7 0 1 0 0
#         """));
#         
#     c.print_depencies()

    bio = Bio(100, 0, 0, 50)
    
    runner = iter(bio)
    
    while next(runner):
        pass
    
    
