import unittest

class Identity_Test_Class(unittest.TestCase):
    def test_identity(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)
        self.assertIs(a, c)

unittest.main()

# In the first assertIs when run it will return True as they are the same object in the computers memory

# In the second assertIs when run it will return False as they are alike but are not stored in the same place in the computers memory

# Since B is referencing A the assertIs will return True as they are the same object in the computers memory unlike C which is similar in its contents but not held in the same place in memory 