phone_number = "1234 1234 1234 1234 "
print(phone_number.replace("1234", "4321"))
phone_number += phone_number.replace("1234", "4321")
print("",phone_number)