Spent = input("How Much Did You Spend Today $")
Liability_Or_Asset = input("Was It A Liability Or An Asset ")
Bank = input("What Was Your Bank Total $") 
Bank1 = float(Bank)
Spent1 =float(Spent)
Bank1 -= Spent1

print("You have a ", Spent1, Liability_Or_Asset, "And Your New bank Total is $", Bank1)