# The difference method looks for the things that are in the first set inputed that aren't in the second set
# it also uses the minus or - symbol

set1 = {"Messi", "Ronaldinio", "Ronaldo", "Luis Figo", "Zlatan", "Zidane", "Neymar", "Mbappe"}

set2 = {"Ramos", "Pepe", "Ronaldinio", "Maradona", "Luis Figo"}

print(set1.difference(set2))
print(set1 - set2)

print(set2.difference(set1))
print(set2 - set1)