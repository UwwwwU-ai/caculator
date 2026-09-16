import tkinter as tk
from tkinter import messagebox




window = tk.Tk()
window.title("Calculator")
w, h = window.maxsize()
window.geometry(f"360x560+{(w - 360) // 2}+{(h - 560) // 2}")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

expression = tk.Frame(window, bg="#1e1e1e")
expression.grid(row = 0, column = 0)
buttons = tk.Frame(window, bg="#1e1e1e")
buttons.grid(row = 1, column = 0)

expression_label = tk.Label(expression, text="", font=("Arial", 24), bg="#1e1e1e", fg="#ffffff")
expression_label.grid(row = 0, column = 0)

expression_result = tk.Label(expression, text="", font=("Arial", 24), bg="#1e1e1e", fg="#ffffff")
expression_result.grid(row = 1, column = 0)



window.mainloop()