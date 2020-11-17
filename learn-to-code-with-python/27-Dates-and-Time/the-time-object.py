from datetime import time

my_first_time_obj = time(10, 57, 30)

print(my_first_time_obj.hour)
print(my_first_time_obj.minute)
print(my_first_time_obj.second)

# This time object is immutable and incapable of change
# my_first_time_obj.hour = 10
