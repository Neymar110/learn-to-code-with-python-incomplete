import unittest

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No Dividing By Zero Please")
    return a / b

 #  The first argument is the error you expect to get, the second is the function (uninvoked), and the rest are the areguments be fed into the function args or kwargs 
class DivisionErrorTest(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, division, 10, 0)
        # Or:
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)


unittest.main()