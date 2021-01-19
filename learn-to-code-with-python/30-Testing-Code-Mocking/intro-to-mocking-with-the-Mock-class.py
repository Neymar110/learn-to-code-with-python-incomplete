from unittest.mock import Mock

def list_addition(list_object):
    total = 0
    for num in list_object:
        total += num
    return total

example_list = Mock()

example_list.list = [1, 9, 3]

print(list_addition(example_list.list))