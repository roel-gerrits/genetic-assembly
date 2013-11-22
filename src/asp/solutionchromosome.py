
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
        incision_point = random.randint(1, self.solution.count() - 1)
        
        child_a = self.solution.splice(0, incision_point)
        parent_a = self.solution.splice(incision_point)
        child_b = other.solution.splice(0, incision_point)
        parent_b = other.solution.splice(incision_point)
        
        child_a.complete_from_factory(parent_b)
        child_b.complete_from_factory(parent_a)
        
        
        return [SolutionChromosome(child_a), SolutionChromosome(child_b)]
    
    
    def mutate(self):
        factory = self.solution.factory
        return SolutionChromosome(factory.random_solution())
        
    
    def __repr__(self):
        return repr(self.solution)
