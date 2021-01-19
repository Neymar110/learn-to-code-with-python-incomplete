import unittest

class Superstars(untitest.Testcase):
    def __init__(name, club, price):
        self.name = name
        self.club = club
        self.price = price
    
    def test_name_iniquality(self):
        self.assertE