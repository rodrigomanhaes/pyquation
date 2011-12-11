class Variable(object):

    def __init__(self):
        self.mul = 1
        self.add = 0
    
    def __call__(self, n):
        return n * self.mul + self.add
        
    def __rmul__(self, n):
        self.mul = n
        return self
        
    def __add__(self, n):
        self.add = n
        return self


variable = Variable()
