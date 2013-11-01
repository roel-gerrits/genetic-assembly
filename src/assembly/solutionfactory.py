
import random

from assembly.constraints import Constraints
from assembly.blocks import Blocks
from assembly.solution import Solution

class SolutionFactory(object):
    
    def __init__(self, blocks):
        if not isinstance(blocks, Blocks):
            raise TypeError("'blocks' argument must be an instance of Blocks")
        
        self.blocks = blocks
        self.constraints = Constraints.from_blocks(blocks)
        
    
    def random_solution(self):
        
        # apply guided search
        solution = Solution(self)

        blocks_placed = set()
        blocks_todo = set(self.blocks)
        
        while len(blocks_todo) > 0:
            
            candidates = self.pick_candidates(blocks_todo, blocks_placed)
            
            the_chosen_one = random.choice(list(candidates))
            
            solution.add_block_to_route(the_chosen_one)

            blocks_todo.remove(the_chosen_one)
            blocks_placed.add(the_chosen_one)
        
        return solution
            
            
    def pick_candidates(self, available, placed):
        candidates = set()
        
        for block in available:
            constraints = self.constraints.get_constraints(block)
            
            for constraint in constraints:
                if constraint not in placed:
                    break
            
            else:
                candidates.add(block)
            
        return candidates
    
    