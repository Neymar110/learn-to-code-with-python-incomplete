# def factorial(num1):
#     apple = num1 -1
#     procces = 1
#     fruit = num1 * apple
#     if apple >= procces:
#         print(apple)
#     if apple == procces:
#         print(fruit)
#         return
#     factorial(apple)
# factorial(9)

# def factorial (num1):
#     a = num1 - 1
#     print(num1)
#     #fact = a * num1
#     #print(fact)
#     if a > 1:
#         fact = factorial(a) * fact
#         return fact
#     else:   
#         print(fact)
#         return fact


def factorial(int1):
    if int1 == 1:
        return int1
    else:
        return int1*factorial(int1-1)

print(factorial(100))