# def factorial(num1):
#     apple = num1
#     procces = 1
#     if num1 <= procces:
#         print apple
#     apple -= procces
#     if apple = procces:
#         return

# def while_loop(num1):
#     adding_number = 1
#     while adding_number < num1:
#         adding_number += 1
#         print(adding_number)
#     if adding_number == num1:
#         print("Your Done!")
# while_loop(91)

def factorials(user_input):
    num1 = user_input - 1
    if user_input == 1:
        print('Your Done')
        return user_input
    else:
        # print(user_input)
        return user_input * factorials(num1)
print(factorials(4))

