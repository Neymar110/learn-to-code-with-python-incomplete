import unittest

class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before all tests")
    
    def setUp(self):
        print("This will run Before Each Test")
    def test_stuff(self):
        self.assertEqual(1, 1)
    def test_more_stuff(self):
        self.assertEqual([], [])
    @classmethod
    def tearDownClass(cls):
        print("This will run Once")
    
    def tearDown(self):
        print("This Will Run after each test")

unittest.main()