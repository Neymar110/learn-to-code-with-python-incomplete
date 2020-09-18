
intList = ()
def typeCheck (*args):
    num_total = 0
    finished_list_of_strings = []
    for every_element in args:
        try:
            num_total += every_element
        except TypeError:
            finished_list_of_strings.append(every_element)
    print(num_total ,finished_list_of_strings)
typeCheck(123, "CHARACTER", 453, "Isaac")
