
from concurrent.futures import ThreadPoolExecutor

from genetic.pool import Pool
from genetic.bio import Bio

class BioTester(object):
    
    def __init__(self):
        self.pool = None
        self.bio_id = 0
        
        self.biopools = list()
        
        self.bio_map = dict()
        self.pool_map = dict()
        self.running = list()
        
        self.workers = 4
        
        self.executor = ThreadPoolExecutor(max_workers = self.workers)
        
    
    def set_pool(self, pool):
        if not isinstance(pool, Pool):
            raise TypeError("'pool' argument must be an instance of Pool")
    
        self.pool = pool
    
    
    def add_bio(self, bio):
        if not isinstance(bio, Bio):
            raise TypeError("'bio' argument must be an instance of Bio")
        
        if self.pool is None:
            raise ValueError("pool is not set")
        
        pool = self.pool.clone()
        state = "pending"
        self.biopools.append(bio, pool, state)
    
    
    def run(self):
        
        done = False
        
        while not done:
            done = True
            
            for bio, pool, state in self.biopools:
                if state == "pending":
                    
                    self.workers.submit(bio.iterate, pool)
                    
            
                elif state == "working":
                    continue
                
                elif state == "finished":
                    continue
            
        
    
    def new_bio_id(self):
        bio_id = self.bio_id
        self.bio_id += 1
        return bio_id