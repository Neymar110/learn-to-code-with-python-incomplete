import unittest

def multiplication(x, y):
    return x * y
def addition(x, y):
    return x + y

#  These Two Functions Will RUn Before and After Each Test and able to reset variables print things run functions etc... and must be named setUp and tearDown
class ST_TD_Test(unittest.TestCase):
    def setUp(self):
        print("Starting")
    def tearDown(self):
        print("Closing")
    def test_multiplication(self):
        self.assertEqual(multiplication(10, 2), 20)
    def test_addition(self):
        self.assertEqual(addition(10, 10), 20)

unittest.main()