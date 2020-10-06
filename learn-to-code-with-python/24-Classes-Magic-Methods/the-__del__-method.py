import time

# the time module has a sleep method that lets us pause the function for the inputed seconds then continues the function

class GarbageCollection():
    def __del__(self):
        print(f"This program is done using this variable {self} so ill delete it...")

variable = GarbageCollection()

#the __del__method is invoked when deleting the object before re-assinging it to 5

variable = 5

time.sleep(variable)

print("It is done")

# and the print statement will print at the end of the function but AFTER the 5 seconds


