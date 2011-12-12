class Variable(object):

    def __init__(self):
        self._a = 1
        self._b = 0
        
    def _clone(self, mul, add, last_a=None):
        clone = Variable()
        clone._a = mul
        clone._b = add
        if last_a:
            clone._last_a = last_a
        return clone
    
    def __call__(self, n):
        return n * self._a + self._b
        
    def __rmul__(self, n):
        return self._clone(self._a * n, self._b, last_a=n)
        
    def __mul__(self, n):
        return self.__rmul__(n)
        
    def __add__(self, n):
        a = self._a
        b = self._b
        if isinstance(n, Variable):
            a += n._a
        else: 
            b += n
        return self._clone(a, b)
        
    def __radd__(self, n):
        return self.__add__(n)
        
    def __sub__(self, n):
        a = self._a
        b = self._b
        if isinstance(n, Variable):
            a -= n._a
        else:
            b -= n
        return self._clone(a, b)
        
    def __rsub__(self, n):
        return self._clone(self._a - self._last_a * 2, self._b + n)



variable = Variable()
