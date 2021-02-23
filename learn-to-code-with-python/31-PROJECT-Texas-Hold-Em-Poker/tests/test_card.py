import unittest
from poker.card import Card



class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "2", suit = "Hearts")
        self.assertEqual(card.rank, "2")
    
    def test_has_suit(self):
        card = Card(rank = "2", suit = "Cloves")
        self.assertEqual(card.suit, "Cloves")

    def test_has_string_repr_with_rank_and_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_technical_repr(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), f"Card('5', 'Diamonds')")
    
    def test_has_13_possible_ranks(self):
        self.assertEqual(Card.RANKS, ("2","3","4","5","6","7","8","9","10","Jack","Queens","King", "Ace"))

    def test_has_4_suits(self):
        self.assertEqual(Card.SUITS, ("Hearts", "Cloves", "Spades", "Diamonds"))
    
    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")
    
    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Heart")

    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(cards[0], Card("2", "Hearts"))
        self.assertEqual(cards[-1], Card("Ace", "Diamonds"))
    
    def test_figures_out_if_two_carda_are_equal(self):
        self.assertEqual(Card("2", "Hearts"), Card("2", "Hearts"))