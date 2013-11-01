

import unittest
from genetic.bio import Bio
from genetic.pool import Pool
from assembly.solutionfactory import SolutionFactory
from assembly.blocks import Blocks
from asp.solutionchromosome import SolutionChromosome

class Test(unittest.TestCase):
    

    def test_iter(self):
        b = Blocks.from_string("""1 3 3 2 3
            2 0 0 1 2
            3 2 3 0 0
            4 1 2 1 2
            5 0 2 3 3
            6 3 3 1 1
            7 0 1 0 0
            """);
            
        sf = SolutionFactory(b)
        
        pool = Pool()

        for _ in range(100):
            s = sf.random_solution()
            pool.add(SolutionChromosome(s))
        
        bio = Bio(100, 1, 0, 50)
        bio.set_pool(pool)

         
        for x in bio:
            print(pool.fittest())

    
if __name__ == "__main__":
    unittest.main()
