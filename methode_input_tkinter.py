import tkinter as tk
from tkinter import simpledialog

def input_tkinter(message):
    root = tk.Tk()
    root.withdraw()
    input = simpledialog.askstring(message, message)
    return input


