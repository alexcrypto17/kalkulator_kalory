from app.window import Window
import tkinter as tk

def run_window():
    root = tk.Tk()
    app = Window(master=root)
    app.mainloop()