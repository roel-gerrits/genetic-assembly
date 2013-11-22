
import unittest
from genetic.bio import Bio
from genetic.pool import Pool
from assembly.solutionfactory import SolutionFactory
from assembly.blocks import Blocks
from asp.solutionchromosome import SolutionChromosome

class Test(unittest.TestCase):
    

    def test_iter(self):
        
        # parse problem
#         b = Blocks.from_string("""1 3 3 2 3
#             2 0 0 1 2
#             3 2 3 0 0
#             4 1 2 1 2
#             5 0 2 3 3
#             6 3 3 1 1
#             7 0 1 0 0
#             """);
#             
#         b = Blocks.from_string("""1 0 0 9 9
#             2 0 2 3 4
#             3 4 6 3 3
#             4 3 3 3 4
#             5 4 4 6 7
#             6 4 6 0 1
#             7 6 6 8 8
#             8 4 5 8 8
#             9 7 7 5 5
#             10 0 2 0 2
#             11 3 3 0 1
#             12 6 8 9 9
#             13 9 9 3 5
#             14 9 9 9 9
#             15 5 6 5 5
#             16 7 8 3 3
#             17 4 6 2 2
#             18 3 3 2 2
#             19 2 3 8 9
#             20 8 8 4 5
#             21 0 0 6 8
#             22 4 4 5 5
#             23 1 1 9 9
#             24 2 2 5 6
#             25 5 7 6 7
#             26 6 7 4 4
#             27 3 3 5 7
#             28 9 9 6 8
#             29 4 5 4 4
#             30 8 8 6 7
#             31 4 5 9 9
#             32 7 8 8 8
#             33 0 1 5 5
#             34 7 8 0 2
#             35 1 1 6 8
#             36 2 2 7 7
#             37 9 9 0 2
#             """);

        b = Blocks.from_string("""1 3 5 1 2
2 5 5 3 4
3 1 1 4 5
4 0 0 5 5
5 3 4 3 5
6 0 0 2 4
7 0 2 0 1
8 2 2 2 3
9 3 5 0 0
10 1 1 2 3
11 2 2 4 4
12 2 2 5 5
13 5 5 5 5
""");
                    
        # pass parsed blocks to new solution factory object
        sf = SolutionFactory(b)
        
        # create pool and fill it with random solutions
        pool = Pool()
        for _ in range(100):
            s = sf.random_solution()
            pool.add(SolutionChromosome(s))
            
        
        # create new bio, 100 generations, 100% crossover, 0% mutation, population 50
        bio = Bio(1000, 0.4, 0.2, 100)
        
        # set pool for bio
        bio.set_pool(pool)
         
        # iterate over generations
        for n in bio:
            print(n, pool.fittest())

    
if __name__ == "__main__":
    unittest.main()
