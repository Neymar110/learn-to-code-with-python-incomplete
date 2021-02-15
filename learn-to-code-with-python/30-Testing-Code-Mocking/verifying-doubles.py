import unittest
from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"
    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)
    
    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1
    

lunch = BurritoBowl.steak_special()

class TestSteakSpecial(unittest.TestCase):
    def test_protien(self):
        assert