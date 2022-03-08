import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


from stuffed import random_animal
#x = "what animal?"
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

lbl = tk.LabelFrame(
    window, 
    text="test text", 
    bg='white',
    fg='black', 
    font=(20)
    ).pack(pady=10)

def show_msg():
    x = random_animal()
    messagebox.showinfo("Message",x)

btn = tk.Button(window,text="Random Animal", command=show_msg()).pack(pady=30)

window.mainloop()

