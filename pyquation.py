class Variable(object):

    def __init__(self):
        self.mul = 1
        self.add = 0
        
    def _clone(self, mul, add):
        clone = Variable()
        clone.mul = mul
        clone.add = add
        return clone
    
    def __call__(self, n):
        return n * self.mul + self.add
        
    def __rmul__(self, n):
        return self._clone(self.mul * n, self.add)
        
    def __mul__(self, n):
        return self.__rmul__(n)
        
    def __add__(self, n):
        return self._clone(self.mul, self.add + n)
        
    def __sub__(self, n):
        return self._clone(self.mul, self.add - n)


variable = Variable()
