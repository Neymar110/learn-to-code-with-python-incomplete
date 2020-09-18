total = 0
def accept_stuff(*args):
    total = 0
    for every_element in args:
        if every_element > total:
            total = every_element
    print(total)
accept_stuff(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,     00)
