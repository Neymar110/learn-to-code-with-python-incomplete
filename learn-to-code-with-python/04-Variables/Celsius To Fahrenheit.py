# Design a Python program that asks the user for a temperature in Fahrenheit.

# The program should convert the temperature to Celsius and print out a message with the value.

# When dealing with any numeric values in this problem, prefer floating point values to integers.

# Fahrenheit to Celsius Formula
# Subtract 32 from the Fahrenheit temperature.

# Multiply the result by (5 / 9).

# Example:

# 100 Fahrenheit

# 100 - 32 = 68

# 68 multiplied by (5 / 9) is 37.77

# 37.77 Celsius

# Questions for this assignment
# Paste your code below. Feel free to provide a brief explanation of how it works as well.

Number = input("Write Any Temperarture In Celsius (Digits Only) And Ill convert it into Fahrenheit. ")
Number1 = float(Number)
Number1 /= 5
Number1 *= 9
Number1 += 32
print("The Answear is ", Number1, "degrees Celsius")