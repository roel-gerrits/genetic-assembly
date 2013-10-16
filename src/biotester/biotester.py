
from util.iteratingexecutor import IteratingThreadPoolExecutor

from genetic.pool import Pool
from genetic.bio import Bio
from genetic.pooltracker import PoolTracker

class BioTester(object):
    
    def __init__(self):
        self.pool = None
        self.bio_id = 0
        
        self.biopools = list()
        
        self.bio_map = dict()
        self.pool_map = dict()
        self.running = list()
        
        self.workers = 4
        
        self.executor = IteratingThreadPoolExecutor(max_workers = self.workers)
        
    
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
        tracker = PoolTracker()
        
        bio.set_pool(pool)
        bio.set_tracker(tracker)
        
        self.executor.submit(bio)
        
        return tracker
    