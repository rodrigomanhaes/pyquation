class Variable(object):

    def __init__(self):
        self._a = 1
        self._b = 0
        
    def _clone(self, mul, add):
        clone = Variable()
        clone._a = mul
        clone._b = add
        return clone
    
    def __call__(self, n):
        return n * self._a + self._b
        
    def __rmul__(self, n):
        return self._clone(self._a * n, self._b)
        
    def __mul__(self, n):
        return self.__rmul__(n)
        
    def __add__(self, n):
        mul = self._a
        add = self._b
        if isinstance(n, Variable):
            mul += n._a
        else:
            add += n
        return self._clone(mul, add)
        
    def __radd__(self, n):
        return self.__add__(n)
        
    def __sub__(self, n):
        return self._clone(self._a, self._b - n)
        
    def __rsub__(self, n):
        return self._clone(-self._a, self._b + n)


variable = Variable()
