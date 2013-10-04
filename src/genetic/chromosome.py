
class Chromosome(object):
    
    def fitness(self):
        raise NotImplementedError()
    
    def crossover(self, other):
        raise NotImplementedError()
    
    def mutate(self):
        raise NotImplementedError()