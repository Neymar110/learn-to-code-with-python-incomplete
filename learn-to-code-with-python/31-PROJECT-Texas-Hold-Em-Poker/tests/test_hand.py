import unittest
from poker.hand import Hand
from poker.card import Card

class Hand_Test(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [Card("Ace", "Spades"), Card("6", "Cloves")]
        
        hand = Hand(cards = cards)

        self.assertEqual(hand.cards, cards)

    def test_figures_out_high_card_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Diamonds"),
        Card(rank = "7", suit = "Cloves")]

        hand = Hand(cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_pair_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Spades"),
        Card(rank = "Ace", suit = "Cloves")]

        hand = Hand(cards = cards)

        self.assertEqual(hand.best_rank(), "Pair")
    
    def test_figures_out_two_pair_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Spades"),
        Card(rank = "5", suit = "Cloves"),
        Card(rank = "King", suit = "Hearts"),
        Card(rank = "Ace", suit = "Cloves"),
        Card(rank = "King", suit = "Diamonds")]

        hand = Hand(cards = cards)

        self.assertEqual(hand.best_rank(), "Two Pair")
