import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class PairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_cloves  = Card(rank = "5", suit = "Cloves")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts   = Card(rank = "King", suit = "Hearts")
        self.ace_of_cloves    = Card(rank = "Ace", suit = "Cloves")
        self.ace_of_spades    = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.five_of_cloves,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_cloves,
            self.ace_of_spades
        ]
    def test_validates_that_cards_have_atleast_two_pairs_of_same_rank(self):
        
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_return_collection_of_cards_that_have_pairs(self):
        
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_cloves,
                self.ace_of_spades   
            ]

        )