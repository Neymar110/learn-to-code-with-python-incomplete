def factors (inputed_number):
    final_list = []
    for every_number in range(1, inputed_number + 1):
        if every_number % 2 == 0:
            final_list.append(every_number)
    return final_list
factors(10)