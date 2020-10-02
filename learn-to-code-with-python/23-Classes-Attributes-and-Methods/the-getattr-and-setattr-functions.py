info = {
    "Name" : "Isaac Irungu",
    "Age" : 13,
    "Nationality" : "Kenya",
    "Shoe_size" : 6.5
}

class Basketball_Player():
    def __init__(self,dict):
        for every_key, every_item in dict.items():
            setattr(self, every_key, every_item)
    
Isaac = Basketball_Player(info)

print(Isaac.Shoe_size)
