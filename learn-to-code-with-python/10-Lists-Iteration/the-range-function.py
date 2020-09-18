def Vowel_percentage_calculator(string):
    total = 0
    for every_letter in string:
        if every_letter == "A" or every_letter =="a" or every_letter =="E" or every_letter =="e" or every_letter =="I" or every_letter =="i" or every_letter =="O" or every_letter =="o" or every_letter =="U" or every_letter =="u":
            total = every_letter.count("A", "E", "I")
            total += every_letter.count("O", "U", "a")
            total += every_letter.count("e", "i", "o")
            total += every_letter.count("u")
    print(total)
Vowel_percentage_calculator("Apple")          


