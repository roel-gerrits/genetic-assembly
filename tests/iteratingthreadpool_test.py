
import unittest

from concurrent.futures import wait, as_completed
from util.iteratingexecutor import IteratingThreadPoolExecutor


class Iteratable(object):
    
    def __init__(self, size):
        self.list = iter(range(size))
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        print(self.i)
        self.i += 1
        return next(self.list) 


class Test(unittest.TestCase):

    def test(self):
        itpe = IteratingThreadPoolExecutor(max_workers=2)
        
        futures = list()

        futures.append(itpe.submit(iter(Iteratable(100))))
        futures.append(itpe.submit(iter(Iteratable(100))))
        futures.append(itpe.submit(iter(Iteratable(100))))
        futures.append(itpe.submit(iter(Iteratable(100))))

        for future in as_completed(futures):
            print(future)
        
        itpe.shutdown(True)
        



if __name__ == "__main__":
    unittest.main()
