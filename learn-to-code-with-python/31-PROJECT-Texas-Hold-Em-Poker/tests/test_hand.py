import unittest
from poker.hand import Hand
from poker.card import Card

class Hand_Test(unittest.TestCase):
    def tests_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Cloves")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(repr(hand), "7 of Cloves, Ace of Diamonds")

    
    def test_receives_and_stores_cards(self):
        
        ace_of_spades = Card("Ace", "Spades")
        six_of_cloves = Card("6", "Cloves")
        cards = [ace_of_spades, six_of_cloves]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(hand.cards,[six_of_cloves, ace_of_spades])
    
    def tests_figures_out_no_cards_is_best_rank(self):
        hand = Hand()
        hand.add_cards([])
        self.assertEqual(hand.best_rank(), "No cards")

    def test_figures_out_high_card_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Diamonds"),
        Card(rank = "7", suit = "Cloves")]

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_pair_is_best_rank(self):
        cards = [Card(rank = "5", suit = "Spades"),
        Card(rank = "5", suit = "Cloves")]

        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(hand.best_rank(), 'Pair')
    
    def test_figures_out_two_pair_is_best_rank(self):
        cards = [Card(rank = "Ace", suit = "Spades"),
        Card(rank = "5", suit = "Cloves"),
        Card(rank = "King", suit = "Hearts"),
        Card(rank = "Ace", suit = "Cloves"),
        Card(rank = "King", suit = "Diamonds")]

        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(hand.best_rank(), "Two Pair")

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [Card(rank = "King", suit = "Cloves"),
        Card(rank = "King", suit = "Hearts"),
        Card(rank = "King", suit = "Diamonds"),
        Card(rank = "3", suit = "Cloves"),
        Card(rank = "6", suit = "Spades")]

        hand = Hand()
        hand.add_cards(cards = cards)

        self.assertEqual(hand.best_rank(), "Three of a Kind")

    def test_figures_out_straght_is_best_rank(self):
        cards = [Card(rank = "6", suit = "Hearts"),
        Card(rank = "7", suit = "Cloves"),
        Card(rank = "8", suit = "Spades"),
        Card(rank = "9", suit = "Diamonds"),
        Card(rank = "10", suit = "Cloves")]
    
        hand = Hand()
        hand.add_cards(cards)
        
        self.assertEqual(hand.best_rank(),
        "Straight")

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [Card(rank = "6", suit = "Hearts"),
        Card(rank = "7", suit = "Diamonds")]
        
        hand = Hand()
        
        hand.add_cards(cards = cards)
        
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_outbestrank_when_flush(self):
        cards = [Card(rank = rank, suit = "Hearts")
        for rank in ["2", "5", "8", "10", "Ace"]]
        
        hand = Hand()
        
        hand.add_cards(cards)

        self.assertEqual(hand.best_rank(), "Flush")

    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Cloves"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]
        hand = Hand()

        hand.add_cards(cards)

        self.assertEqual(hand.best_rank(), "Full House")
    
    def test_figures_out_four_os_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Cloves"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "3", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(hand.best_rank(), "Four of a Kind")
    
    def test_figures_out_striaght_flush_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Cloves"),
            Card(rank = "4", suit = "Cloves"),
            Card(rank = "5", suit = "Cloves"),
            Card(rank = "6", suit = "Cloves"),
            Card(rank = "7", suit = "Cloves")
        ]
        hand = Hand()

        hand.add_cards(cards)

        self.assertEqual(hand.best_rank(), "Straight Flush")
    
    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank = "10", suit = "Cloves"),
            Card(rank = "Jack", suit = "Cloves"),
            Card(rank = "Queen", suit = "Cloves"),
            Card(rank = "King", suit = "Cloves"),
            Card(rank = "Ace", suit = "Cloves")
        ]
        hand = Hand()

        hand.add_cards(cards)

        self.assertEqual(hand.best_rank(), "Royal Flush")