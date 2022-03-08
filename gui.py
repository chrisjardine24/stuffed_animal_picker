import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


from stuffed import random_animal
x = str(random_animal())

window = tk.Tk()
window.title("Noa's Stuffed Animal Picker")
window.minsize(300,200)
window['bg'] = 'white'

mn = Menu(window)
window.config(menu=mn)
file_menu = Menu(mn)
mn.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='About')

def update_button():
    x = random_animal()
    btn.configure(text=x)

btn = tk.Button(window, text="Which Stuffed Animal?", command=update_button)
btn.pack()

window.mainloop()

