sentence = "I am learning how to code"
finished_sentence = ""
for every_letter in sentence:
    if every_letter == " ":
       every_letter = "!"
    finished_sentence += every_letter
print(finished_sentence)
