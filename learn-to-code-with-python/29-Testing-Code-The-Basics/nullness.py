import unittest
def explicit_return_value(a, b):
    return a + b

def implicit_return_value(a, b):
    print(a + b)


class Nullness_Test(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(implicit_return_value(4, 1))
    def test_not_none(self):
        self.assertIsNotNone(explicit_return_value(4, 1))

# The test_none method will be successfull as the implicit_return_value function doesn't return anything so it defults no None

# The test_not_none method will be successfull as the explicit_return_value function returns something