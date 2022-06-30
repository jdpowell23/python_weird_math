from math import add, sub, multi, div
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(1,2,3,5),11)
        self.assertEquals(add(-1,0),-1)
        self.assertEquals(add(-1,-1,-1,-1),-4)
        self.assertEquals(add(-1,1),0)

class TestSub(unittest.TestCase):        
    def test_sub(self):
        self.assertEquals(sub(4,2),2)
        self.assertEquals(sub(4,2,2,2),-2)
        self.assertEquals(sub(40,2,2,2,-50),84)
        
class TestMulti(unittest.TestCase):
    def test_sub(self):
        self.assertEquals(multi(2,2),4)

class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEquals(div(4,2),2)