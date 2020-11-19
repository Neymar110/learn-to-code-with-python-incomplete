import unittest

class Truthiness_or_Falsiness_Test(unittest.TestCase):
    def test_Truthiness(self):
        self.assertTrue(3 < 5)
        self.assertTrue(" ")
        self.assertTrue(["Isaac"])
        self.assertTrue(-1)
        # This Will basically test for the items truthy value
    def test_Falseiness(self):
        self.assertFalse(0)
        self.assertFalse([])
        # This Will basically test for the items falsy value

unittest.main()