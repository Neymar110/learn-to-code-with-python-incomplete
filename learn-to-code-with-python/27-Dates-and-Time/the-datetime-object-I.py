from datetime import datetime

example1 = datetime(2000, 6, 6, 10, 59, 12)
#                   Year month day hour minute second

print(example1.now())
print(example1.today())

# These two class methods are equal and return a up do date datetime object
print(example1.year)
print(example1.month)
print(example1.day)
print(example1.hour)
print(example1.minute)
print(example1.second)


print(example1.weekday())

# this o, 6, 6, 10, 59, 12bject is mutable
example1 = example1.replace(2020, 6, 6, 10, 59, 12)
print(example1.year)
