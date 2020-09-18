b = {1, 2, 3, 4, 5}
a = {1, 2, 3}

# In the above, set A is a subset of set B
# Basically all the elements in set A are contained in set B

# In the above, set B is a superset of set A
# It basically has all of set A's elements plus more

print(a.issubset(b))
# Is A a subset of B : True

print(b.issuperset(a))
# Is B a superset of A : True

# The issubset method can also be invoked or used with the < opperator

print(a <= b)
# Is A a subset or equal to B : True

print(b >= a)
# Is B a superset or equal to set A : True

print(b.issubset(a))
# Is B a subset of A: False
# B is a superset not a subset

print(a.issuperset(b))
# Is A a superset of B : False
# A is a subset of B