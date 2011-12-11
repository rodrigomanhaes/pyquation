import unittest
from should_dsl import should
from pyquation import variable as x


class FirstDegreeEquationTest(unittest.TestCase):

    def test_1(self):
        '''with a = 1 and b = 0'''
        f = x
        f(1) |should| equal_to(1)
        f(2) |should| equal_to(2)
        f(3) |should| equal_to(3)
        f(4) |should| equal_to(4)
        
    def test_2(self):
        '''with a =/= 1 and b = 0'''
        f = 2*x
        f(1) |should| equal_to(2)
        f(2) |should| equal_to(4)
        f(3) |should| equal_to(6)
        f(4) |should| equal_to(8)
        
    def test_3(self):
        '''with a and b'''
        f = 3*x + 2
        f(1) |should| equal_to(5)
        f(2) |should| equal_to(8)
        f(3) |should| equal_to(11)
        f(4) |should| equal_to(14)
    
    
if __name__ == '__main__':
    unittest.main()
    
