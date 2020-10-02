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

info_to_del = ["Name", "Size", "Age", "Height"]
def deleting_func(your_list, i):
    for every_item in your_list:
        if hasattr(i, every_item):
            delattr(i, every_item)
        else:
            print(f"The attribute {every_item} is not found in the class")

deleting_func(info_to_del, Isaac)
