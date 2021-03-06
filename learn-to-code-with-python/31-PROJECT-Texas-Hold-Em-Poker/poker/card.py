class Card():
    RANKS = ("2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace")

    SUITS = ("Hearts", "Cloves", "Spades", "Diamonds") 

    @classmethod
    def create_standard_52_cards(cls):
        
        return [
            cls(Rank, Suit)
            for Suit in cls.SUITS
            for Rank in cls.RANKS
            ]

    def __init__(self, rank, suit):
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")
        
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other_card):
        return self.rank_index < other_card.rank_index
    