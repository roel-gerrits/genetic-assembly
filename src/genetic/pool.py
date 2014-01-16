
from genetic.chromosome import Chromosome
import operator
from random import choice
import copy

class Pool(object):
    
    def __init__(self):
        self.pool = list()
        
        
    def add(self, chrom):
        if not isinstance(chrom, Chromosome):
            raise TypeError("'chrom' argument must be an instance of Chromosome")
        
        self.pool.append(chrom)
        
        
    def remove(self, chrom):
        try:
            self.pool.remove(chrom)
        except ValueError:
            pass
    

    def fittest(self):
        self.pool.sort(key=operator.methodcaller('fitness'))
        
        if len(self.pool) > 0:
            return self.pool[0]
        else:
            return None
        
        
    def sort(self):
        self.pool.sort(key=operator.methodcaller('fitness'))
        
        
    def skim(self, amount):
        self.pool = self.pool[0:amount]
    
    
    def select(self, amount):
        self.pool.sort(key=operator.methodcaller('fitness'))
        self.pool = self.pool[0:amount]
    
    
    def __len__(self):
        return len(self.pool)
    
    
    def pick_random(self):
        return choice(self.pool)
    
    
    def clone(self):
        p = Pool()
        for chrom in self.pool:
            p.add(copy.deepcopy(chrom))
            
        return p
    