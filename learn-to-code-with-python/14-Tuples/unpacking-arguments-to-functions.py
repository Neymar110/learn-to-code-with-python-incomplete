def multiplication (a, b):
    return a * b
numbers = (1, 2)
print(multiplication(*numbers))
tuple  =  (True, "Apple", 3, 3.5, False)

*first_two, others1, others2, others3 = tuple
print(first_two, others1, others2, others3)