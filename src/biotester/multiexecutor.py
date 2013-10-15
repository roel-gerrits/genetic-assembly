
from concurrent.futures import ThreadPoolExecutor

class RecurringThreadPoolExecutor(object):
    
    def __init__(self, max_workers = 1):
        self.runners = list()
        self.executor = ThreadPoolExecutor(max_workers = self.workers)
        
        self.executables = list()
    
    
    def submit(self, func, *args, **kwargs):

        self.executables.append(func, *args, **kwargs)
        
    

