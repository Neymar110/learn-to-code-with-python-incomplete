import tkinter as tk

def test_func():
    entry = search_bar.get()
    print(entry)

window = tk.Tk()
window.title("Web Browser")
canvas = tk.Canvas(height = 500 ,width = 500)
canvas.pack()
orange_frame = tk.Frame(window, bg = "#FCA311")
orange_frame.place(relheight = 5, relwidth = 7)
blue_frame = tk.Frame(orange_frame, bg = "#14213D")
blue_frame.place(height = 370, width = 450, x = 28, y = 90)
button = tk.Button(orange_frame, text = "Search", bg = "white", command = test_func)
button.place(height = 35, width = 100, x = 375, y = 30)
search_bar = tk.Entry(orange_frame)
search_bar.place(height = 25 ,x = 30, y = 35, width = 330)
tk.Place()
label = tk.Label(blue_frame)
label.place(width = 430, x = 10, y = 9, height = 350)

window.mainloop()