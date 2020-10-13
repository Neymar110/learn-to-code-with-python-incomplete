stat_dict = {
    "pace" : 0,
    "defending" : 0,
    "shooting" : 0,
}

class Stats():
    def __init__(self, dict):
        for key ,value in dict.items():
            setattr(dict, key, value)

class Position():
    def __init__(self, position):
        self.position = position
    
    def position_change(self, new_position):
        self.position = new_position

class Value():
    def __init__(self, price):
        self.price = price
    
    def change_price(self, new_price):
        self.price = new_price

class Footballer():
    def __init__(self, name, nationality, position, stat_dict):
        self.name = name
        self.nationality = nationality
        self.value = Value("1,000,000")
        self.position = Position(position)
        self.stats = Stats(stat_dict)

Messi = Footballer("Messi", "Argentina", "Right-Winger", stat_dict)

print(Messi.value.price)

Messi.value.change_price("10,000,000")

print(Messi.value.price)

print(Messi.position.position)

Messi.position.position_change("Striker")

print(Messi.position.position)

help(Messi.stats)