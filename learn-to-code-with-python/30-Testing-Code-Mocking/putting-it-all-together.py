import unittest
from unittest.mock import MagicMock

class Actor():
    def jump_off_a_helicopter(self):
        return "Nope Not happening"

    def light_on_fire(self):
        return "Heck no!"


class Movie():
    def __init__(self, Actor):
        self.actor = Actor
    
    def start_filming(self):
        self.actor.jump_off_a_helicopter()
        self.actor.light_on_fire()

class MovieTest(unittest.TestCase):
    def test_start_filming(self):
        stunt_double = MagicMock()
        movie = Movie(stunt_double)
        
        movie.start_filming()
        stunt_double.jump_off_a_helicopter.assert_called()
        stunt_double.light_on_fire.assert_called()


if __name__ == "__main__":
    unittest.main()