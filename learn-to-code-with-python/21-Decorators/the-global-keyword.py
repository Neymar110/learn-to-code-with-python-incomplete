Best_football_player = "Messi"

def func():
    Best_football_player = "Ronaldo"

func()
print(Best_football_player)

# In the above code a Best_football_player variable is declared on a global scope

# The func function is then defined and makes a Best_football_player variable on a local scope

# Then on line 6 we test to see whether the Best_football_player variable has been changed but we see "Messi" printed twice on the right-hand side

Best_Basketball_players = "Kobe Bryant"

print(Best_Basketball_players)

def func1():
    global Best_Basketball_players
    Best_Basketball_players = "Steven Curry"

print(Best_Basketball_players)

# In the above code a Best_Basketball_player variable is declared on a global scope


# The func1 function is then defined and uses the global keyword to tell the function that every_time Best_Basketball_player is called in it its referencing the one in the global scope instead of creating a new variable

# It then changes the Best_Basketball_player variable on a global scope

# Then on line 22 we test to see whether the Best_Basketball_player variable has been changed but we see "Steven Curry" printed once on the right-hand side