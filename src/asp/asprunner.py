
from concurrent.futures import as_completed

from assembly.solutionfactory import SolutionFactory
from asp.solutionchromosome import SolutionChromosome
from genetic.pool import Pool
from util.iteratingexecutor import IteratingThreadPoolExecutor
from genetic.pooltracker import PoolTracker 

class AspRunner(object):
    
    
    def __init__(self, blocks):
        self.solution_factory = SolutionFactory(blocks)
        
        self.bios = list()
        
        self.pool = self.create_pool(100)
    
    
    def add_bio(self, bio):
        tracker = PoolTracker()
        
        bio.set_tracker(tracker)
        bio.set_pool(self.pool.clone())
        
        
        self.bios.append(bio)
    
    
    def create_pool(self, n):
        # create pool and fill it with random solutions
        pool = Pool()
        for _ in range(n):
            s = self.solution_factory.random_solution()
            pool.add(SolutionChromosome(s))
            
        return pool
    
    
    def run(self):
        ex = IteratingThreadPoolExecutor(4)
        futures = list()
        
        for bio in self.bios:
            print ("adding bio", bio)
            f = ex.submit(iter(bio))
            futures.append(f)
        
        
        for future in as_completed(futures):
            print(future)
            
            e = future.exception()
            if e:
                print (e)
        
        
        
 
            
        print("shutting down")
        ex.shutdown(True)
    