def long_strings(list_of_strings):
    finished_list = []
    for every_word in list_of_strings:
        if len(every_word) >= 5:
            finished_list.append(every_word)
    return finished_list
long_strings(['Apple', 'telkom', 'and', 'pizza'])