
import unittest

from assembly.solutionfactory import SolutionFactory
from assembly.solution import Solution
from assembly.block import Block
from assembly.blocks import Blocks
from assembly.constraints import Constraints

class Test(unittest.TestCase):
    
    def get_test_blocks(self):
        b = Blocks.from_string("""1 3 3 2 3
            2 0 0 1 2
            3 2 3 0 0
            4 1 2 1 2
            5 0 2 3 3
            6 3 3 1 1
            7 0 1 0 0
            """);

        return b
    
    def test_route_length_1(self):
        s = Solution()
        
        s.add_block_to_route(Block(1, 0, 0, 0, 0))
        s.add_block_to_route(Block(5, 0, 0, 0, 0))
        s.add_block_to_route(Block(2, 0, 0, 0, 0))
        s.add_block_to_route(Block(3, 0, 0, 0, 0))
        s.add_block_to_route(Block(4, 0, 0, 0, 0))

        self.assertEqual(len(s), 14)
    
    
    def test_route_length_2(self):
        s = Solution()
        
        s.add_block_to_route(Block(1, 0, 0, 0, 0))
        s.add_block_to_route(Block(2, 0, 0, 0, 0))
        s.add_block_to_route(Block(3, 0, 0, 0, 0))
        s.add_block_to_route(Block(4, 0, 0, 0, 0))
        s.add_block_to_route(Block(5, 0, 0, 0, 0))

        self.assertEqual(len(s), 10)
    
    
    def test_route_length_3(self):
        s = Solution()

        self.assertEqual(len(s), 0)
        
        
    def test_solution_factory(self):
        b = self.get_test_blocks()
        sf = SolutionFactory(b)
        
        # We just test if no exceptions are thrown 
        # (yes i know it's bad to test based on random values)
        for _ in range(1000):
            sf.random_solution()

        
        