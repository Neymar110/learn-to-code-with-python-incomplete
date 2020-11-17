class Mistake(Exception):
    """This Error Occurs When A Mistake Has Been Made"""

# Created The "Mistake" Parent Class. 

class NegativeNumberError(Mistake):
    """This Error Occurs When One Or More Numbers Are Negative"""
    pass

# NegativeNumberError Subclass From Mistake Superclass

def division_func(number):
    try:
        if number <= 0:
        #If the Number Inputed Is Negative:
            raise NegativeNumberError(f"Your Number: {number} is les than 1.")
            # Then I'll Raise A NegativeNumberError.
        return number / number
    except NegativeNumberError as e:
    #I Then 'Catch' The Error
        return f"No Negative Numbers Allowed. {e}"
        # And Create My Own Error Message

print(division_func(-10))
