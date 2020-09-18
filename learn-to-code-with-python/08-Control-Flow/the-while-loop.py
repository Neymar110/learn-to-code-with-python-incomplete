Yes_Or_No = input("Are You Married: ")
if Yes_Or_No == "Yes" or Yes_Or_No == "yes":
    Digit2 = int(input("How Old Were you When You Got Married: "))
    if Digit2 >=  18: 
        print("Congartulations")
    else: 
        print("Try Again In A Few Years")

if Yes_Or_No == "No" or Yes_Or_No == "no":
    Digit3 = int(input("How Old Are You now? "))
    if Digit3 <= 18:
        print("Maybe One Day 😂😂")
    if Digit3 >= 18:
        print("Very, Very Soon!")