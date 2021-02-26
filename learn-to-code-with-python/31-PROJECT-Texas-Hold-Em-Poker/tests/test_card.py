import unittest
from poker.card import Card



class CardTest(unittest.TestCase):
    def test_knows_its_rank_index(self):
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)
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
        self.assertEqual(Card.RANKS, ("2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace"))

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
    
    def test_figures_out_if_two_cards_are_equal(self):
        self.assertEqual(Card("2", "Hearts"), Card("2", "Hearts"))
    
    def test_card_can_sort_itself_with_another(self):
        queen_of_spades = Card("Queen", "Spades")
        king_of_spades = Card("King", "Spades")
        evaluation = queen_of_spades < king_of_spades
        self.assertEqual(evaluation,
        True,
        "The sort algorithim is not sorting the lower card first")


    def test_sorts_cards(self):
        two_of_spades = Card("2", "Spades")
        five_of_diamonds = Card("5", "Diamonds")
        five_of_hearts = Card("5", "Hearts")
        eight_of_hearts = Card("8", "Hearts")
        ace_of_cloves = Card("Ace", "Cloves")
    
        unsorted_order = [
            ace_of_cloves,
            five_of_hearts,
            eight_of_hearts,
            two_of_spades,
            five_of_diamonds
        ]
        unsorted_order.sort()

        self.assertEqual(unsorted_order, [
            two_of_spades,
            five_of_hearts,
            five_of_diamonds,
            eight_of_hearts,
            ace_of_cloves]
        )