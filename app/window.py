import tkinter as tk
from app.formula import *

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        ves_text = "vvedyte ves (v kg):"
        self.ves_text = tk.Label(text=ves_text, bg="yellow")
        self.ves_text.pack(side="top")

        self.ves_pole = tk.Entry(self.master)
        self.ves_pole.pack()

        rost_text = "vvedyte rost (v cm):"
        self.rost_text = tk.Label(text = rost_text )
        self.rost_text.pack(side="top")
        self.rost_pole = tk.Entry(self.master)
        self.rost_pole.pack()

        vozrast_text = "vvedyte vozrast (v godah):"
        self.vozrast_text = tk.Label(text = vozrast_text )
        self.vozrast_text.pack(side="top")
        self.vozrast_pole = tk.Entry(self.master)
        self.vozrast_pole.pack()

        pol_text = "vvedyte pol (0 male, 1 female):"
        self.pol_text = tk.Label(text = pol_text )
        self.pol_text.pack(side="top")
        self.pol_pole = tk.Entry(self.master)
        self.pol_pole.pack()


        self.calculate_btn = tk.Button(self)
        self.calculate_btn["text"] = "Вычислять"
        self.calculate_btn["command"] = self.show_rezultat
        self.calculate_btn.pack()

        self.rezultat = tk.Label(text = "" )
        self.rezultat.pack(side="top")

    def show_rezultat(self):
        pol = self.pol_pole.get()
        vozrast = self.vozrast_pole.get()
        rost = self.rost_pole.get()
        ves = self.ves_pole.get()

        kalory = calculate(int(ves), int(vozrast), int(rost), int(pol))

        self.rezultat["text"] = "vam nado zgugat stolko kalory: " + str(kalory)