class Company():
    pass

class Phone(Company):
    pass
class Apple(Phone):
    def __init__(self):
        self.company = "Apple"
iPhone = Apple()

try: print(iPhone.company)

except NameError:
    print("None")

else:
    print("This will only print if the try block worked without raising an exception.")

finally:
    print("This will always print.")

# A else block will only run if the try block works successfully, compared to the finally block which will run no matter what happens



