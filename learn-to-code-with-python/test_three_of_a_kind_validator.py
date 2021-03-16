import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):

            three = Card(rank = "3", suit = "Cloves"),
            six = Card(rank = "6", suit = "Spades"),
            self.king_of_cloves = Card(rank = "King", suit = "Cloves"),
            self.king_of_diamonds = Card(rank = "King", suit = "Diamonds"),
            self.king_of_hearts = Card(rank = "King", suit = "Hearts"),
        ]

        self.cards = [
            three,
            six,
            self.king_of_cloves,
            self.king_of_diamonds,
            self.king_of_hearts
        ]


    def test_validates_that_cards_have_exactly_the_of_same_rank(self):

        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(validator.is_valid(), True)
    
    def test_return_three_of_a_kind_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(validator.valid_card(),
        [
            self.king_of_cloves,
            self.king_of_diamonds,
            self.king_of_hearts
        ])