import unittest
from lab2 import *
class Test(unittest.TestCase):
    def testFlag1(self):
        self.assertEqual(flag1(str(0)),True)
        self.assertEqual(flag1(str(1)), False)
        self.assertRaises(ValueError, flag1, str(1))
    def testFunc1(self):
        self.assertEqual(func1('3','Max',{'1': [], '2': [], '3': [], '4': []}),{'1': [], '2': [], '3': ['Max'], '4': []})
        self.assertEqual(func1('1', 'Max', {'1': [], '2': [], '3': [], '4': []}),
                         {'1': ['Max'], '2': [], '3': [], '4': []})
        self.assertEqual(func1('2', 'Max', {'1': [], '2': [], '3': [], '4': []}),
                         {'1': [], '2': ['Max'], '3': [], '4': []})
        self.assertEqual(func1('4', 'Max', {'1': [], '2': [], '3': [], '4': []}),
                         {'1': [], '2': [], '3': [], '4': ['Max']})


if __name__ == '__main__':
    unittest.main()
