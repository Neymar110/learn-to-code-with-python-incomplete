import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Heart")
        self.assertEqual(card.rank, "Queen")
    
    def test_has_suit(self):
        card = Card(rank = "2", suit = "clubs")
        self.assertEqual(card.suit, "clubs")
