def str_reversed(value):
    Length = len(value) - 1
    reversed_str = ""
    if Length >= 0:
        reversed_str += value[Length]
        Length -= 1
    else:
        return reversed_str

print(str_reversed("pineapple"))
