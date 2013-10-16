

class PoolTracker(object):
    
    def __init__(self):
        self.generations = list()
        self.current_generation = None
        
        self.bio = None
    
    
    def new_generation(self):
        gen = Generation()
        self.generations.append(gen)
        self.current_generation = gen


    def set_bio(self, bio):
        self.bio = bio
        
    
    def set_population(self, pop):
        self.current_generation.population = pop
    
    
    def set_fittest(self, fitness):
        self.current_generation.fittest = fitness
        
        
class Generation(object):
    
    def __init__(self):
        self.population = 0
        self.fittest = 0