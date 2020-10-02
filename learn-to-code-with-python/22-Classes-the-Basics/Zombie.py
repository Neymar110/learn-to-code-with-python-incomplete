class Game():
    def __init__(self, name, age_restriction, date_of_creation):
        self.name = name
        self.age_restriction = age_restriction
        self.date_of_creation = date_of_creation
        self.price = "Free"
Fortnite = Game("Fortnite", 12, "July 25th 2017")
Valorant = Game("Valorant", 16, "June 2nd 2020")
League_of_Legends = Game("League of Legends", 15, "October 27 2009")

game = input("Which game would you like info on? ['Fortnite', 'Valorant', 'League_of_Legends']. ")
info = input("What would you like info on? ['date_of_creation', 'age restriction']")
print(game.info)

# playername = input("What is the players name? ")
# playerprice = input("What is their price? ")
# playerteam = input("What team do they play for? ")
# playerpossition = input("What possition do they play? ")
# class PlayerBase():
#     def __init__(self, team, price):
#         self.price = playerprice
#         self.team = playerteam
#         self.name = playername
#         self.possition = playerpossition

#     def _get_club(self):
#         return self.playerteam

#     def _set_club(self, arg):
#         return self.playerteam = club

#     club = property(_get_club, _set_club)
# playername = PlayerBase(playerteam, playerprice)

# print(f"\nPlayer Info: {playername.name} is a {playername.possition} that plays for {playername.team} and is valued at {playername.price}.")

# answer = input("Are you done creating your player base?")

# while answer == "No" or answer == "no":
#     playername = input("What is the players name? ")
#     playerprice = input("What is their price? ")
#     playerteam = input("What team do they play for? ")
#     playerpossition = input("What possition do they play? ")

        