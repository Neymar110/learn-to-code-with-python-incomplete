# def length_match (list_of_strings, integer):
#     total = 0
#     for every_string in list_of_strings:
#         if len(every_string) == integer:
#             total += 1
#     return total
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)

# def sum_from (num1 = 1, num2 = 5):
#     total = 0
#     for every_num in range(num1, num2 + 1):
#         total += every_num
#     print(total)
# sum_from()

def same_index_values(list1, list2):
    index_list = []
    for index1, item1 in enumerate(list2):
        for index2, item2 in enumerate(list1):
            if item1 == item2 and index1 == index2:
                index_list.append(index1)
    return index_list
same_index_values(["cat", "dog", "kangaroo", "mouse"],["cat", "dog", "kangaroo", "mouse", ""] )