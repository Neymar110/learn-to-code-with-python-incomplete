def division_func(number):
    try:
        if number <= 0:
        #If the Number Inputed Is Negative:
            raise ValueError(f"Your Number: {number} is les than 1.")
            # Then I'll Raise A ValuesError.
        return number / number
    except ValueError as e:
    #I Then 'Catch' The Error
        return f"No Negative Numbers Allowed. {e}"
        # And Create My Own Error Message

print(division_func(-10))
