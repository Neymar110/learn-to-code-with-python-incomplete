import unittest

list1 = []
class TestListMethods(unittest.TestCase):
    def test_append(self):
        self.assertEqual(len(list1), 0) # The First Argument Should Be an Operatiion and The Second Should Be The Return Value of That Operation
        self.assertEqual(["Apple", "Orange", "Pear", "Banana"].index("Banana"), 3)



if __name__ == "__main__":
    unittest.main()

# unittest only runs the functions whose names start with test