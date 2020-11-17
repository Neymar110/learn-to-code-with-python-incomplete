from datetime import date

isaac = date(2007, 4, 6)

print(type(isaac))
print(isaac)
print(isaac.year)
print(isaac.month)
print(isaac.day)


# These Date Objects Are Immutable so the cant change
# isaac.day = 12

#  There is also a Today class method on the date class that retrun todays date
today = date.today()
print(today)
