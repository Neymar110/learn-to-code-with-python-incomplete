class Mall():
    def __init__(self, acers, owner):
        self.acers = acers
        self.owner = owner
   
    @staticmethod
    def Pineapple():
        return "Mall not Found"

class Store(Mall):
    a = ""

print(Store.Pineapple())