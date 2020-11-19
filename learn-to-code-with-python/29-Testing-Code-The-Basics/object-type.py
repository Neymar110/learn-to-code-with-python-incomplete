import unittest

class Job():
    def work(self):
        print("WORKING")
    
class Football(Job):
    def tired(self):
        print("Resting")

Isaac = Football()


class ObjectTypeTest(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance("Apple", str)
        self.assertIsInstance(Isaac, Football)
        self.assertIsInstance(Isaac, Job)
    
    def test_is_not_instance(self):
        self.assertNotIsInstance(1, str)
        self.assertNotIsInstance("Apple", dict)
        self.assertNotIsInstance(Isaac, str)
        self.assertNotIsInstance(Job, set)

unittest.main()


