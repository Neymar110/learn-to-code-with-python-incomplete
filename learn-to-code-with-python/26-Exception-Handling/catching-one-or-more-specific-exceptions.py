def division_func(number):
    try:
        return number / number
    except TypeError as e:
        return f"No Strings Allowed!! {e}"

print(division_func("10"))