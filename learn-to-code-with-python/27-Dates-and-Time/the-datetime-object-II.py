from datetime import datetime, date, time

# now = datetime.today()
print(now)

# %Y is the 4 digit year, %m is the month %d is the day

print(now.strftime("%Y-%m-%d"))

#  %y is the lats 2 digits  of the year, %A is the weekday in a string, %B is the month in a string

print(now.strftime("%j"))



