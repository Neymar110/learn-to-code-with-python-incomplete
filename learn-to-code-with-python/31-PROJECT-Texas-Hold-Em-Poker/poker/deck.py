# from poker.card import Card

class Deck():
    def __init__(self):
        self.cards = []

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)