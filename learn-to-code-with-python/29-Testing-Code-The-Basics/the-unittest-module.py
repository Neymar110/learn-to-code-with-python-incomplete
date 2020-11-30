import unittest

nationalities= ["Australian", "Kenya", "Ethiopia","South Africa", "Congo", "Egypt", "Nigeria", "United Kingdom", "United States", "China", "Korea", "Japan" ,"Brazil", "Argentina"]

class TestOperations(unittest.TestCase):
    def __init__(self, age, nationality, pay):
        self.age = age
        self.nationality = nationality
        self.pay = pay
        self.nationality_test_results = None
    def test_nationality(self):
        for every_nationality in nationalities:
            if every_nationality == self.nationality:
                self.nationality_test_results = True


Isaac = TestOperations(13, "Kenya", None)

Isaac.test_nationality()

print(Isaac.nationality_test_results)
unittest.main()