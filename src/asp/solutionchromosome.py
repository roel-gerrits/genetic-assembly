
import random

from genetic.chromosome import Chromosome
from assembly.solution import Solution

class SolutionChromosome(Chromosome):
    
    def __init__(self, solution):
        if not isinstance(solution, Solution):
            raise TypeError("'solution' argument must be an instance of Solution")
        
        self.solution = solution
        
        
    def fitness(self):
        return len(self.solution)
    
    
    def crossover(self, other):
        incision_point = random.randint(1, self.solution.count() - 2)
        
        print (incision_point)
        
        #raise NotImplementedError()
    
    
    def __repr__(self):
        return repr(self.solution)