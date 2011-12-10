class Variable(object):

    def __init__(self):
        self.mul = 1
    
    def __call__(self, n):
        return n * self.mul
        
    def __rmul__(self, n):
        self.mul = n
        return self


variable = Variable()
