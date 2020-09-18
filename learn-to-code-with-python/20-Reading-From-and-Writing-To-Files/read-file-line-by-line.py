with open("cupcakes.txt") as cup:
    count = 0
    for every_line in cup:
        count += 1
        print(every_line.strip())

print(count)