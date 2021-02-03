import tkinter as tk

window = tk.Tk()
window.title("Calculator")
canvas = tk.Canvas(height = 350 ,width = 400)
canvas.pack()
orange_frame = tk.Frame(window, bg = "#4A525A")
orange_frame.place(relheight = 5, relwidth = 7)

operation = None

def clear_func():
    current = e.get()
    e.delete(0,  len(current))

def button_click(number):
    global current
    current = e.get()
    e.delete(0,  len(current))
    e.insert(0, str(current) + str(number))

def button_add():
    global num1
    current = e.get()
    num1 = float(e.get())
    e.delete(0,  len(current) + 1)
    global operation
    operation = "add"

def button_sub():
    global num1
    current = e.get()
    num1 = float(e.get())
    e.delete(0,  len(current) + 1)
    global operation
    operation = "subtract"

def button_mult():
    global num1
    current = e.get()
    num1 = float(e.get())
    e.delete(0,  len(current) + 1)
    global operation
    operation = "multiply"

def button_div():
    global num1
    current = e.get()
    num1 = float(e.get())
    e.delete(0,  len(current) + 1)
    global operation
    operation = "div"

def equals_func():
    num2 = float(e.get())
    e.delete(0,  len(current) + 1)
    if operation == "add":
        e.insert(0, int(num1)+int(num2))
    elif operation == "subtract":
        e.insert(0, int(num1)-int(num2))
    elif operation == "multiply":
        e.insert(0, int(num1)*int(num2))
    else:
        e.insert(0, int(num1)/int(num2))
e = tk.Entry(orange_frame, width = 46, bg = "#F4F4F9")
e.place(y = 50, x = 60, height = 30)

num_button_1 = tk.Button(orange_frame, text = "1", command = lambda: button_click(1), bg = "#010400", fg = "white", font = "Algerian")
num_button_1.place(width = 70, x = 60, height = 60, y = 200)

num_button_2 = tk.Button(orange_frame, text = "2", command = lambda: button_click(2), bg = "#010400", fg = "white", font = "Algerian")
num_button_2.place(y = 200,x = 130, width = 70, height = 60)

num_button_3 = tk.Button(orange_frame, text = "3", command = lambda: button_click(3), bg = "#010400", fg = "white", font = "Algerian")
num_button_3.place(y = 200,x = 200, width = 70, height = 60)

num_button_4 = tk.Button(orange_frame, text = "4", command = lambda: button_click(4), bg = "#010400", fg = "white", font = "Algerian")
num_button_4.place(width = 70, x = 60, height = 60, y = 140)

num_button_5 = tk.Button(orange_frame, text = "5", command = lambda: button_click(5), bg = "#010400", fg = "white", font = "Algerian")
num_button_5.place(y = 140,x = 130, width = 70, height = 60)

num_button_6 = tk.Button(orange_frame, text = "6", command = lambda: button_click(6), bg = "#010400", fg = "white", font = "Algerian")
num_button_6.place(y = 140,x = 200, width = 70, height = 60)

num_button_7 = tk.Button(orange_frame, text = "7", command = lambda: button_click(7), bg = "#010400", fg = "white", font = "Algerian")
num_button_7.place(width = 70, x = 60, height = 60, y = 80)

num_button_8 = tk.Button(orange_frame, text = "8", command = lambda: button_click(8), bg = "#010400", fg = "white", font = "Algerian")
num_button_8.place(y = 80,x = 130, width = 70, height = 60)

num_button_9 = tk.Button(orange_frame, text = "9", command = lambda: button_click(9), bg = "#010400", fg = "white", font = "Algerian")
num_button_9.place(y = 80,x = 200, width = 70, height = 60)

num_button_0 = tk.Button(orange_frame, text = "0", command = lambda: button_click(0), bg = "#010400", fg = "white", font = "Algerian")
num_button_0.place(y = 260,x = 130, width = 70, height = 60)

clear_button = tk.Button(orange_frame, text = "Clear", command = clear_func, bg = "#24272B", font = "Pacifico")
clear_button.place(width = 70, x = 60, height = 60, y = 260)

equals_button = tk.Button(orange_frame, text = "=", command = equals_func, bg = "#247BA0", font = "Algerian")
equals_button.place(y = 260,x = 200, width = 70, height = 60)

div_button = tk.Button(orange_frame, text = "÷", command = button_div, font = "Pacifico")
div_button.place(y = 80,x = 270, width = 70, height = 60)

multiplication_button = tk.Button(orange_frame, text = "x", command = button_mult, font = "Pacifico")
multiplication_button.place(y = 140,x = 270, width = 70, height = 60)

addition_button = tk.Button(orange_frame, text = "+", command = button_add, font = "Pacifico")
addition_button.place(y = 200,x = 270, width = 70, height = 60)

minus_button = tk.Button(orange_frame, text = "-", command = button_sub, font = "Pacifico")
minus_button.place(y = 260,x = 270, width = 70, height = 60)

window.mainloop()