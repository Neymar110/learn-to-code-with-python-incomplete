class FilmMaker():
    def give_interview(self):
        print("I love making movies!")

class Director(FilmMaker):
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(Screenwriter, Director):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()

print(JackOfAllTrades.mro())


# On line 16 python it told to look for the attribute "give_interview".

# It will then look starting at "Screenwriter", then its parent class "FilmMaker",
# then "Director" which is also inheritiong from "FilmMaker", ut instead of looking there again, it only counts the last occurance of the "FilmMaker" class being a super class (in director).

#When a class appeares twice when looking for the attribute it will use the seccond occurance of the super class in the mro order