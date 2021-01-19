from tkinter import * 
from unittest.mock import Mock
from random import randint

def coinflip():
    num = randint(1, 3)
    if num == 2:
        return "Heads"
    else:
        return "Tails"

Example = Mock(side_effect = coinflip)

window = Tk()
window.title = ('Test')

my_canvas = Canvas(window, width = 800)
my_canvas.pack()

frame = Frame(window, width = 8, height = 5)
frame.pack()

window.mainloop()
