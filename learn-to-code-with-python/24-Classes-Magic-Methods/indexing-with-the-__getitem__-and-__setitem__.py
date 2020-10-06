list1 = ["Samsung", "Apple"]
class Phones:
     def __init__(self, inputed_list):
         self.phones = inputed_list

list2 = Phones(list1)

print(list2.phones[1])  