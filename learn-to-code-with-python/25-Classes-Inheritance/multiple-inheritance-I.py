# it is possible to inherit from more that one class

class idk1():
    def use(self):
        print("This is idk1")
    
class idk2():
    def use(self):
        print("This is idk2")

class idk3(idk1, idk2):
    pass

i_dont_know = idk3()
print(idk3.mro())
# This is the python method that returns the order that python will look for attributes in an instance

# It goes in the order that it was inputed


i_dont_know.use()