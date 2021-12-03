import unittest
from main import print_hi_stephen, print_hi_you, print_hi_michael


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), f"Hi, Tony")

    def test_print_hi_michael(self):
        self.assertEqual(print_hi_michael(), f"Hi, Michael")

    #def test_print_hi_?(self):
        #


if __name__ == '__main__':
    unittest.main()
