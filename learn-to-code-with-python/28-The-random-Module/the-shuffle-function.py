from random import shuffle
from copy import copy, deepcopy

# The shuffle function has no return value, but shuffles the items in the iterable object

shopping_list = ["apples", "toilet Paper", "Eggs", "Gum", "hangers", "hotdogs"]

# Example of it returning None:
print(shuffle(shopping_list))

# But it has still done its job:
print(shopping_list)

# If there is a need to maintain order in the original list you can:
clone = shopping_list.copy() # Only works on list objects

# Or:
clone = copy(shopping_list)


# This will only return a shallow copy if you need a deep copy:
clone = deepcopy(clone)