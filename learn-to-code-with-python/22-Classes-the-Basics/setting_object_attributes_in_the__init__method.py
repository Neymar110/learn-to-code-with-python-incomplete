# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
class Musical():
    def __init__(self, name):
        self.name = name
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
rent = Musical("Rent")
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
mormon = Musical("Book of Mormon")
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.
chicago = Musical("Chicago")
print(chicago.name)