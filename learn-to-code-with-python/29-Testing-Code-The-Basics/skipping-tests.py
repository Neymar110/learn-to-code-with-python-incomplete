import unittest
 
def addition(a, b):
    return a + b 
def concatenation(a, b):
    return a + b
def division(a, b):
    return a/b
def multiplication(a, b):
    a * b

class TestCode(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 10), 11)
    def test_concatenation(self):
        self.assertEqual(concatenation("Apple", "Orange"), "AppleOrange")
    def test_division(self):
        self.assertEqual(division(50, 2), 25)
    #If you need to skip a test:
    @unittest.skip("Multiplication function is not functioning0.") # Skips Argument is the Reason You Need to Skip
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 4), 8)

if __name__ == "__main__":
    unittest.main()