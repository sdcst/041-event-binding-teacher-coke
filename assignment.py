import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p


def dog(event):
    print(event)
    p.playsound("Dog Barking Sound Effect - Copyright free.mp3")


def cat(event):
    print(event)
    p.playsound("Cat Meow - Minecraft Sound Effect (HD).mp3")


def creeper(event):
    print(event)
    p.playsound("Creeper Minecraft Sound Effect.mp3")


def villager(event):
    print(event)
    p.playsound("[Sound Effect] Minecraft Villager.mp3")


def elephant(event):
    print(event)
    p.playsound("elephant.mp3")


win = tk.Tk()
win.title()

l1 = tk.Label(win, text="Press any button to play a sound")
l2 = tk.Button(win, text="Dog bark", relief=GROOVE, width=20)
l2.bind("<Button>", dog)
l3 = tk.Button(win, text="Cat Meow", relief=GROOVE, width=20)
l3.bind("<Button>", cat)
l4 = tk.Button(win, text="Creeper", relief=GROOVE, width=20)
l4.bind("<Button>", creeper)
l5 = tk.Button(win, text="Minecraft Villager", relief=GROOVE, width=20)
l5.bind("<Button>", villager)
l6 = tk.Button(win, text="elephant", relief=GROOVE, width=20)
l6.bind("<Button>", elephant)

l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)


win.mainloop()