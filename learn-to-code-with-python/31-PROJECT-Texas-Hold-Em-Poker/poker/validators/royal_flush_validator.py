from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royale Flush"
    
    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(cards = self.cards)

        if straight_flush_validator.is_valid():
            straight_flush_cards = straight_flush_validator.valid_cards()
            is_royale = straight_flush_cards[-1].rank == "Ace"
            return is_royale
        
        return False
        
    def valid_cards(self):
        return StraightFlushValidator(cards = self.cards).valid_cards()
        


        # if not is_straight_flush:
        #     return False

        # is_royal = self.cards[-1].rank == "Ace"
        # return is_straight_flush and is_royal