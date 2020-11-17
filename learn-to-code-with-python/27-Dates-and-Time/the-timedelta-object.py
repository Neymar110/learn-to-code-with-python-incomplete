from datetime import datetime, timedelta

birthday = datetime(2007, 4, 6)
today = datetime.now()

life_span = today-birthday

print(life_span)

print(life_span.total_seconds())

# Info: The timedelta class does not accept years or months

two_hundred_days = timedelta(days = 200)

print(life_span + two_hundred_days)

