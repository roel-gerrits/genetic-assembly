

class BioRunner(object):
    
    def __init__(self, bio, pool):
        self.bio = bio
        self.pool = pool
        
    def iterate(self):
        pass
    
    def is_done(self):
        return self.bio.is_done()
        