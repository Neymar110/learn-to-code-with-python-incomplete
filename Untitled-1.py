txt = input("What opperation would you like to do.")
def Git(text):
    if "commit" in text:
        print("You have items to add before you commit!")
    
    elif "add" in text:
        print("You have added the files, its now awaiting your commit")

Git(txt)