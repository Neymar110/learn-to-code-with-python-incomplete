def super_sum (list):
    total = 0
    for every_word in list:
        if "s" in every_word:
            index = every_word.find("s")
            total += index
    print(total)
super_sum(["Happines", "sing"])