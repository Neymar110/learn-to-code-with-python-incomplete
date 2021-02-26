import unittest
from poker.hand import Hand
from poker.card import Card

class Hand_Test(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        ace_of_spades = Card("Ace", "Spades")
        six_of_cloves = Card("6", "Cloves")
        cards = [ace_of_spades, six_of_cloves]
        
        hand = Hand(cards = cards)

        self.assertEqual(hand.cards, [six_of_cloves, ace_of_spades])

    def test_figures_out_high_card_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Diamonds"),
        Card(rank = "7", suit = "Cloves")]

        hand = Hand(cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_pair_is_best_rank(self):
        cards = [Card(rank = "5", suit = "Spades"),
        Card(rank = "5", suit = "Cloves")]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 'Pair')
    
    def test_figures_out_two_pair_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Spades"),
        Card(rank = "5", suit = "Cloves"),
        Card(rank = "King", suit = "Hearts"),
        Card(rank = "Ace", suit = "Cloves"),
        Card(rank = "King", suit = "Diamonds")]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), "Two Pair")

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [Card(rank = "King", suit = "Cloves"),
        Card(rank = "King", suit = "Hearts"),
        Card(rank = "King", suit = "Diamonds"),
        Card(rank = "3", suit = "Cloves"),
        Card(rank = "6", suit = "Spades")]

        hand = Hand(cards = cards)

        self.assertEqual(hand.best_rank(), "Three of a Kind")

    def test_figures_out_straght_is_best_rank(self):
        cards = [Card(rank = "6", suit = "Hearts"),
        Card(rank = "7", suit = "Cloves"),
        Card(rank = "8", suit = "Spades"),
        Card(rank = "9", suit = "Diamonds"),
        Card(rank = "10", suit = "Cloves")]
    
        hand = Hand(cards = cards)
        
        self.assertEqual(hand.best_rank(),
        "Straight")

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [Card(rank = "6", suit = "Hearts"),
        Card(rank = "7", suit = "Diamonds")]
        hand = Hand(cards = cards)
        
        self.assertEqual(hand.best_rank(), "High Card")
    
