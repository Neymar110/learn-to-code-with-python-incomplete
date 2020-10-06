
class Buisness():
    @staticmethod
    def do_work():
        print("Working!!")
    
    @staticmethod
    def slogan():
        print(f"It's All About The Money!!")

    @staticmethod
    def clean():
        print("Cleaning up the place")

class Bank(Buisness):
    @staticmethod
    def open():
        print("Opening the bank at 6:00 am!")
    
class Ecobank(Bank):
    def slogan(self):
        print("It's All About the Coustomers!!")
Standard_Chartered = Bank()

Humphrey = Ecobank()

Humphrey.do_work()

Standard_Chartered.slogan()

Humphrey.slogan()
