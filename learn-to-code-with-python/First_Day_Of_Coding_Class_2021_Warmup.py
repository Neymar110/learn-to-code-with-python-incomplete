class Cake_Makers():
    def __init__(self, Cakes, Price):
        self.cakes = Cakes
        self.price = Price



class Customers():
    def __init__(self, moolah, choice, bought_cakes):
        self.cash = moolah
        self.choice = choice
        self.bought_cakes = bought_cakes

class Bake_Sale():
    def Sale(owner, Buyer):
        Buyer.bought_cakes.append(owner.cakes[Buyer.choice])

Isaac = Cake_Makers(["Vanilla", "Chocolate", "Red Velvet"], [200, 200, 400])
Timothy = Customers(1000, 0, [])

School_Bake_Sale = Bake_Sale.Sale(Isaac, Timothy)

print(Timothy.bought_cakes)


