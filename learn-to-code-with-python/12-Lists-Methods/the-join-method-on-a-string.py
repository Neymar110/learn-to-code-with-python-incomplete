def cleanup (user_input):
    finished_list = []
    for every_word in user_input:
        if every_word == " " or every_word == "":
            pass
        else:
            finished_list.append(every_word)
    return " ".join(finished_list)
pass
continue