
class Buisness():
    @staticmethod
    def do_work():
        print("Working!!")

    @staticmethod
    def clean():
        print("Cleaning up the place")

class Bank(Buisness):
    @staticmethod
    def open():
        print("Opening the bank at 6:00 am!")
    
class Ecobank(Bank):
    def slogan(self):
        print("The Pan African Bank")

Humphrey = Ecobank()

Humphrey.do_work()
