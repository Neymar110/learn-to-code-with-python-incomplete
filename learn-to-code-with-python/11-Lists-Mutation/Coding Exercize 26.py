# def push_or_pop(list_of_numbers):
#     finished_list = []
#     for every_number in list_of_numbers:
#         if every_number > 5:
#             finished_list.append(every_number)
#         else:
#             del finished_list[-1]
#     return finished_list

# def delete_all (inputed_list, target):
#     while target in inputed_list:
#         inputed_list.remove(target)
#     print(inputed_list)

def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in message:
        encrypted_letter_index_position = (alphabet.index(letter) + 2)  26
        encrypted += alphabet[encrypted_letter_index_position]
    return encrypted