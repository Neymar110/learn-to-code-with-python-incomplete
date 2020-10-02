class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income
    
    def enter_club(self):
        if self.age < 21:
            return "Access denied!"
        else:
            return "Access granted!"
    def play_show(self):
        self.income += 5