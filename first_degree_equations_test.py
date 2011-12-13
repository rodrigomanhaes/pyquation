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
        
    def test_4(self):
        '''with negative b'''
        f = 2*x - 1
        f(1) |should| equal_to(1)
        f(2) |should| equal_to(3)
        f(3) |should| equal_to(5)
        f(4) |should| equal_to(7)
        
    def test_5(self):
        '''supports "x*a" form'''
        f = x*2 - 1
        f(1) |should| equal_to(1)
        f(2) |should| equal_to(3)
        f(3) |should| equal_to(5)
        f(4) |should| equal_to(7)
        
    def test_6(self):
        '''supports many multiplying a's'''
        f = 2*x*3 + 1
        f(1) |should| equal_to(7)
        f(2) |should| equal_to(13)
        f(3) |should| equal_to(19)
        f(4) |should| equal_to(25)
        
    def test_7(self):
        '''supports many adding b's'''
        f = 2*x*3 + 3 - 1
        f(1) |should| equal_to(8)
        f(2) |should| equal_to(14)
        f(3) |should| equal_to(20)
        f(4) |should| equal_to(26)
        
    def test_8(self):
        '''sums two "a" members'''
        f = 2*x + 3*x + 1
        f(1) |should| equal_to(6)
        f(2) |should| equal_to(11)
        f(3) |should| equal_to(16)
        f(4) |should| equal_to(21)
        
    def test_9(self):
        '''b first'''
        f = 1 + 2*x
        f(1) |should| equal_to(3)
        f(2) |should| equal_to(5)
        f(3) |should| equal_to(7)
        f(4) |should| equal_to(9)
        
        f = 1 - 2*x
        f(1) |should| equal_to(-1)
        f(2) |should| equal_to(-3)
        f(3) |should| equal_to(-5)
        f(4) |should| equal_to(-7)
    
    def test_10(self):
        '''b first, within and last'''
        f = 1 - 2*x - 3 - 3*x + 2
        f(1) |should| equal_to(-5)
        f(2) |should| equal_to(-10)
        f(3) |should| equal_to(-15)
        f(4) |should| equal_to(-20)


if __name__ == '__main__':
    unittest.main()
    
