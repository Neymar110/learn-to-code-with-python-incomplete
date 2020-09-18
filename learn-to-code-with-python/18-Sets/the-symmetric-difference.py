# The symmetric method looks for the things in set1 that not in set 2 and combines them into a set

# It also uses the caret or ^ symbol
set1 = {"Messi", "Ronaldinio", "Ronaldo", "Luis Figo", "Zlatan", "Zidane", "Neymar", "Mbappe"}

set2 = {"Ramos", "Pepe", "Ronaldinio", "Maradona", "Luis Figo"}

print(set1.symmetric_difference(set2))
print( set1 ^ set2)