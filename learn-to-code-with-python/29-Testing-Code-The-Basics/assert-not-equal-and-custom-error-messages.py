import unittest

def swapcase_function(string):
    copy = string.swapcase()
    return copy

class TestInequalityClass(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(swapcase_function("Apple"), "aPPLE","The Swapcase Function Is Not Returning A Swapcased String")

unittest.main()