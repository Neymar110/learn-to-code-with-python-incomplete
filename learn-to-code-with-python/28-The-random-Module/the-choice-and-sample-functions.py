from random import choice, sample, randint


# The choice function takes a iterable object (list, tuple and strings) and will return a random item that list, string or tuple
print(choice(["apple", 13, "object"]))

kids_birthday_wishlist = ["Ps5", "GTA 5", "Fall Guys: Ultimate Knockout", "Valorant Points", "Fortnite vBucks", "Pass Royale"]

# The sample function takes 2 arguments, the first being the iterable object and the second being the number of items you would like to retrieve
print(sample(kids_birthday_wishlist, 2) )