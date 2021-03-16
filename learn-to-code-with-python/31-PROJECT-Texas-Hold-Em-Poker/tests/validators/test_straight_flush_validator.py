import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    # def setUp(self):
    #     self.three_of_cloves = Card(rank = "3", suit = "Cloves")
    #     self.four_of_cloves  = Card(rank = "4", suit = "Cloves")
    #     self.five_of_cloves  = Card(rank = "5", suit = "Cloves")
    #     self.six_of_cloves   = Card(rank = "6", suit = "Cloves")
    #     self.seven_of_cloves = Card(rank = "7", suit = "Diamonds")
    #     self.king_of_cloves = Card(rank = "King", suit = "Cloves")
    #     self.ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")

    #     self.cards = [
    #         self.three_of_cloves,
    #         self.four_of_cloves,
    #         self.five_of_cloves,
    #         self.six_of_cloves,
    #         self.seven_of_cloves,
    #         self.king_of_cloves,
    #         self.ace_of_diamonds
    #     ]

    def test_determines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        
        cards = [
            Card(rank = "3", suit = "Cloves"),
            Card(rank = "4", suit = "Cloves"),
            Card(rank = "5", suit = "Cloves"),
            Card(rank = "6", suit = "Cloves"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(validator.is_valid(), False)

    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        
        cards = [
            Card(rank = "3", suit = "Cloves"),
            Card(rank = "4", suit = "Cloves"),
            Card(rank = "5", suit = "Cloves"),
            Card(rank = "6", suit = "Cloves"),
            Card(rank = "7", suit = "Cloves"),
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(validator.is_valid(), True)
    
    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        three = Card(rank = "3", suit = "Cloves")
        four  = Card(rank = "4", suit = "Cloves")
        five  = Card(rank = "5", suit = "Cloves")
        six   = Card(rank = "6", suit = "Cloves")
        seven = Card(rank = "7", suit = "Cloves")

        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),[
                three,
                four,
                five,
                six,
                seven
            ]
        )