import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Calculator")
w, h = window.maxsize()
window.geometry(f"360x560+{(w - 360) // 2}+{(h - 560) // 2}")
window.resizable(False, False)
window.configure(bg="#1e1e1e")
