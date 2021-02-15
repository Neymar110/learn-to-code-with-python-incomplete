import unittest

class Test_product_function(unittest.TestCase):
    def test_multiplication_function(self):
        self.assertEqual(multiplication(1, 2), 2)

def multiplication(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    unittest.main()