import unittest

class Inclusion_Test(unittest.TestCase):
    def test_inclustion(self):
        self.assertIn(1, [1,2,3])
        self.assertIn(50, range(0, 100))

    def test_uninclusion(self):
        self.assertNotIn(10, (9, 11, 100))
        self.assertNotIn("s", "Apple")

# The first Argument is the item you are looking to find and the second is the contatiner to look in (Must Be Iterable Object)