with open("my_file.txt", "a") as my_file:
    my_file.write("And in line number 3 we have, the amazing, the astounding, Grill.Isxac")

with open("my_file.txt", "r") as my_file:
    for every_line in my_file:
        print(every_line)