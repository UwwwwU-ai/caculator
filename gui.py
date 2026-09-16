import tkinter as tk
from tkinter import messagebox



# 创建主窗口，设置标题、大小、位置和背景颜色
window = tk.Tk()
window.title("Calculator")
w, h = window.maxsize()
window.geometry(f"360x560+{(w - 360) // 2}+{(h - 560) // 2}")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

# 创建了两个 Frame，一个用于显示表达式和结果，另一个用于放置按钮。
expression = tk.Frame(window, bg="#1e1e1e")
expression.grid(row = 0, column = 0)
buttons = tk.Frame(window, bg="#1e1e1e")
buttons.grid(row = 1, column = 0)

content = ''
interim = 0
number = 0
result = ''

# 创建了两个标签，一个用于显示表达式，另一个用于显示结果。标签的字体、背景颜色和前景颜色都进行了设置。
expression_label = tk.Label(expression, text= content, font=("Arial", 24), bg="#1e1e1e", fg="#ffffff")
expression_label.grid(row = 0, column = 0)

expression_result = tk.Label(expression, text="", font=("Arial", 24), bg="#1e1e1e", fg="#ffffff")
expression_result.grid(row = 1, column = 0)


def press_number(num):
    global content
    content += str(num)
    expression_label.config(text=content)

def add_operator(operator):
    global content
    content += operator
    expression_label.config(text=content)

AC_button = tk.Button(buttons, text="AC", font=("Arial", 24), bg="#ff0000", fg="#ffffff")
addsubstract_button = tk.Button(buttons, text="+/-", font=("Arial", 24), bg="#00ff00", fg="#ffffff")
percent_button = tk.Button(buttons, text = "%", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
divide_button = tk.Button(buttons, text = "/", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
product_button = tk.Button(buttons, text = "*", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
subtract_button = tk.Button(buttons, text = "-", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
add_button = tk.Button(buttons, text = "+", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
equal_button = tk.Button(buttons, text = "=", font = ("Arial",24), bg = '#00ff00', fg = '#ffffff')
zero_button = tk.Button(buttons, text = "0", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(0))
one_button = tk.Button(buttons, text = "1", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(1))
two_button = tk.Button(buttons, text = "2", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(2))
three_button = tk.Button(buttons, text = "3", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(3))
four_button = tk.Button(buttons, text = "4", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(4))
five_button = tk.Button(buttons, text = "5", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(5))
six_button = tk.Button(buttons, text = "6", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(6))
seven_button = tk.Button(buttons, text = "7", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(7))
eight_button = tk.Button(buttons, text = "8", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(8))
nine_button = tk.Button(buttons, text = "9", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number(9))
dot_button = tk.Button(buttons, text = ".", font = ("Arial",24), bg = '#0000ff', fg = '#ffffff', command=lambda: press_number('.'))
delete_button = tk.Button(buttons, text = "DEL", font = ("Arial",24), bg = '#ff0000', fg = '#ffffff')


AC_button.grid(row = 0, column = 0, sticky = "nsew")
addsubstract_button.grid(row = 0, column = 1, sticky = "nsew")
percent_button.grid(row = 0, column = 2, sticky = "nsew")
divide_button.grid(row = 0, column = 3, sticky = "nsew")
seven_button.grid(row = 1, column = 0, sticky = "nsew")
eight_button.grid(row = 1, column = 1, sticky = "nsew")
nine_button.grid(row = 1, column = 2, sticky = "nsew")
product_button.grid(row = 1, column = 3, sticky = "nsew")
four_button.grid(row = 2, column = 0, sticky = "nsew")
five_button.grid(row = 2, column = 1, sticky = "nsew")
six_button.grid(row = 2, column = 2, sticky = "nsew")
subtract_button.grid(row = 2, column = 3, sticky = "nsew")
one_button.grid(row = 3, column = 0, sticky = "nsew")
two_button.grid(row = 3, column = 1, sticky = "nsew")
three_button.grid(row = 3, column = 2, sticky = "nsew")
add_button.grid(row = 3, column = 3, sticky = "nsew")
zero_button.grid(row = 4, column = 0, sticky = "nsew")
dot_button.grid(row = 4, column = 1, sticky = "nsew")
delete_button.grid(row = 4, column = 2, sticky = "nsew")
equal_button.grid(row = 4, column = 3, sticky = "nsew")


window.mainloop()