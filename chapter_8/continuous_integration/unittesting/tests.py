from django.test import TestCase
import unittest
# Create your tests here.


def sqr(x):
    x*x



class SqrTest(unittest.TestCase):
    def test_1(self):
        '''This is test 1 (assert if true)'''
        self.assertTrue(sqr(10), 10)

    def test_2(self):
        '''This is test2 (assert if false)'''
        self.assertFalse(sqr(100), 99999)




if __name__ == '__main__':
    unittest.main()

