import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "9", suit = "Cloves"),
            Card(rank = "10", suit = "Cloves"),
            Card(rank = "Jack", suit = "Cloves"),
            Card(rank = "Queen", suit = "Cloves"),
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Cloves"),
            Card(rank = "Jack", suit = "Cloves"),
            Card(rank = "Queen", suit = "Cloves"),
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Cloves"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten   = Card(rank = "10", suit = "Cloves")
        jack  = Card(rank = "Jack", suit = "Cloves")
        queen = Card(rank = "Queen", suit = "Cloves")
        king  = Card(rank = "King", suit = "Cloves")
        ace   = Card(rank = "Ace", suit = "Cloves")

        cards = [
            Card(rank = "2", suit = "Spades"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace
            ]
        )
