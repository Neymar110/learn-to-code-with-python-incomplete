class FootbalPlayers():
    def __init__(self, name, team, price):
        self.player = name
        self.team = team
        self.price = price

Ronaldo = FootbalPlayers("Cristiano Ronaldo", "Juventus", "1,000,000")
Messi = FootbalPlayers("Lionel Messi", "Barcelona", "1,000,000")

print(Messi.player)
print(Messi.team)
print(Messi.price)