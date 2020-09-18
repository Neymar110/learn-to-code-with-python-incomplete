# In the below code, there is a instance of a closure

# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory

def football_players():
    players = ["Raheem Sterling", "Lionek Messi", "Luis Suarez", "Cristiano Ronaldo"]
    def anything ():
        return players
    return anything

the_func = football_players()
print(the_func())

# In the above code, the football players function is only used on line number 9.

# The computer then throws it out of memory along with its variables as it is not used anywhere else in the program

# In the football players function there is a nested function called anything.

# The anything function returns the players list that is in the enclosing scope

# So the anything function it required to retain the players list in memory

# And that is how closures work!!