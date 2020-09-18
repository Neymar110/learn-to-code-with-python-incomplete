file_name = "my_file.txt"
with open(file_name, "w") as file_object:
    file_object.write("Hello File its Isaac!!!")
with open(file_name, "r") as file_obj:
    for every_line in file_obj:
        print(every_line)