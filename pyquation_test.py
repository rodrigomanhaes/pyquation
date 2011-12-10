import unittest
from should_dsl import should
from pyquation import variable as x

class EquationTest(unittest.TestCase):

    def test_first_degree_equation_1(self):
        '''first degree equation with a = 1 and b = 0'''
        f = x
        f(1) |should| equal_to(1)
        f(2) |should| equal_to(2)
        f(3) |should| equal_to(3)
        f(4) |should| equal_to(4)
        
    def test_first_degree_equation_2(self):
        '''first degree equation with a =/= 1 and b = 0'''
        f = 2*x
        f(1) |should| equal_to(2)
        f(2) |should| equal_to(4)
        f(3) |should| equal_to(6)
        f(4) |should| equal_to(8)
    
    
if __name__ == '__main__':
    unittest.main()
