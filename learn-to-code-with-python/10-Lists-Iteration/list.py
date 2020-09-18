
def in_list (list, finding):
    for lists in list:
        if finding not in lists:
            print("continue")
            continue
        print("it's In the list")
in_list([[1,2,3],[3,2,1],[-1, -2, -3]], -1)
