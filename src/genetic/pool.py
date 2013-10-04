
from genetic.chromosome import Chromosome
import operator

class Pool(object):
    
    def __init__(self):
        self.pool = list()
        
        self.termination_generations = None
        self.termination_fitness = None
        self.crossover_rate = 0
        self.mutation_rate = 0
        self.population_size = 0
        
        self.pool = list()

    
    def set_termination(self, generations=None, fitness=None):
        if generations is None and fitness is None:
            raise ValueError("Either generations or fitness must be set")
        
        self.termination_fitness = fitness
        self.termination_generations = generations
        
        
    def set_crossover_rate(self, rate):
        self.crossover_rate = rate
        
        
    def set_mutation_rate(self, rate):
        self.mutation_rate = rate
        
        
    def set_population_size(self, size):
        self.population_size = size
        
        
    def add_chromosome(self, chrom):
        if not isinstance(chrom, Chromosome):
            raise TypeError("'chrom' argument must be an instance of Chromosome")
        
        self.pool.append(chrom)


    def iterate(self):
        pass
    

    def get_fittest(self):
        pass
    
    
    def select(self, amount):
        self.pool.sort(key=operator.attrgetter('fitness'))
        self.pool = self.pool[0:amount]
        
    
    def mutate(self, amount):
        pass
    
