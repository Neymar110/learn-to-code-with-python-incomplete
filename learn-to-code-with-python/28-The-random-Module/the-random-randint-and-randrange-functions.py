import random

# random.random will return a random float
print(random.random())

#  The random.randint will return a random integer between the first argument and the second argument. Both Values and Inclusive
print(random.randint(0, 10))

# The random.randrange takes 3 arguments the firs is the starting point (inclusive) the second the the ending point (exclusive) and the third is the sequence (in jumps of)
print(random.randrange(0, 80, 10))