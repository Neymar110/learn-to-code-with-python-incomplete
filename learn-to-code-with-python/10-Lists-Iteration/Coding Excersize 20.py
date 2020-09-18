def in_list (list, finding):
    if finding in list:
        for index, string in enumerate(list):
            if string == finding:
                return index
            else:
                ("Nope we didin't find anything")
    else:
        return -1  

def sum_of_values_and_indices (list_of_numbers):
    total = 0
    for index, number in enumerate(list_of_numbers):
        total += index + number
    return total

  