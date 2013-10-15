from genetic.pool import Pool

class Bio(object):
    
    def __init__(self, generations, crossover_rate, mutation_rate, population_size):
        
        self.termination_generations = generations
        self.current_generation = 0
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population_size = population_size

    
    def is_done(self):
        return self.current_generation >= self.termination_generations
    
    
    def iterate(self, pool):
        if not isinstance(pool, Pool):
            raise TypeError("'pool' argument must be an instance of Pool")
        
        # create zombies
        self.do_mutate(pool)
        
        # have fun
        self.do_crossover(pool)
        
        # natural selection
        pool.select(self.population_size)
        
        # happy birthday!
        self.current_generation += 1
        
    
    def do_mutate(self, pool):
        count = len(pool)
        
        for _ in range(count):
            old_chrom = pool.pick_random()
            pool.remove(old_chrom)
            
            new_chrom = old_chrom.mutate()
            pool.add(new_chrom)
        
    
    def do_crossover(self, pool):
        count = len(pool)
        
        for _ in range(count):
            p1 = pool.pick_random()
            p2 = pool.pick_random()
            
            child = p1.crossover(p2)
            
            pool.add(child)
    