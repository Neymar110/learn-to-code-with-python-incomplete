# LEGB is Local/ Enclosing Functions/ Global/ Built-in

#This is basically the order that vscode will use to find a given name (by name i mean variable, function etc...)

# Example 1:

def find_x():
    x = 10
    return x

# In this example the return looks for the x variable using the LEGB rule

# It first looks in the L or local scope and finds x

# => x = 10

# Example 2:

def find_y():
    y = 10
    def find_it():
        return y
    return find_it()

print(find_y())

# In this example find_y defines a find_it function, and find_y returns y

# The return in the find_y looks for y using the LEGB rule.

# So it starts at local and cant find the y variable in its function.

# It then moves on the E or Enclosing function and finds y

# Example 3:

z = 10

def find_z():
    return z

# In this example find_z returns z.

# It uses the LEGB rule and starts at the L and can't find it.

# It then moves to the E and it dosen't apply to it cause the function only has one scope

# It then goes to the G or Global scope and finds it and returns it

# Example 4:

def found_it():
    return len

# In the example above found it returns len
#  So the return look for len using the LEGB rule (obviously) and can't find it in L, E or G so it looks in B or Built-in and finds a len function and returns it




#PPPPPPPPPPLLLLLLLLLLSSSSSS tel me ill need this in the future