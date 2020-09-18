def fancy_concatenate (user_input):
    finished_string = ""
    for every_list in user_input:
        for every_string in every_list:
            finished_string += every_string
    print(finished_string)
fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])