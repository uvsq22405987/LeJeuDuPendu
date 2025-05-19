#bouton quitter

import tkinter as tk
from tkinter import *

root2 = tk.Tk()

def bouton_quitter() :
    root2.destroy()

Quitter = tk.Button(root2, text="Quitter la partie", font=("Arial", 15), command= bouton_quitter)
Quitter.place(x=1, y=50)

root2.mainloop()
