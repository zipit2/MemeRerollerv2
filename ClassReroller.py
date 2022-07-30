from calendar import c
import tkinter as tk
from tkinter import * 
import webbrowser
import random

#Main Gui Body
m = tk.Tk()
#Title of Program
m.title('Class Reroller')
i = BooleanVar()
j = BooleanVar()
k = BooleanVar()
l = BooleanVar()

Tanks = ["BM Monk", "Prot War", "Prot Pala", "BDK", "GBear"]
Healer = ["Disc Priest", "Holy Priest", "Resto Druid", "Resto Sham", "Holy Pala"]

mLabel = Label(m)
mLabel.pack

#Set Window Size
m.geometry("500x500")
m.resizable(False, False)

#Functions
def Classselect():
    global mLabel
    if i.get() == True & j.get() == True & k.get() == True & l.get() == True:
        mLabel.config(text="You Cannot Have this Combination") 
    elif i.get() == True & j.get() == True & k.get() == True:
        mLabel.config(text="Welcome to Life of Kirbi")
    elif i.get() == True & j.get() == True:
        a = random.choice(Tanks)
        mLabel.config(text="Tank Carries harder, play: "  + a)    
    elif i.get() == True & l.get() == True:
        webbrowser.open("https://www.youtube.com/watch?v=q225u-qGpas")   
    elif j.get() == True & l.get() == True:
        mLabel.config(text="Go watch Star Wars, trying to break the program logic?")
    elif i.get() == True & k.get() == True:
        mLabel.config(text="Play DPS")
    elif j.get() == True & k.get() == True:
        mLabel.config(text="Play DPS")    
    elif k.get() == True & l.get() == True:
        mLabel.config(text="Stop it Nangs")
    elif i.get() == True:
        a = random.choice(Tanks)
        mLabel.config(text=a)
    elif j.get() ==True:
        b = random.choice(Healer)
        mLabel.config(text=b)
    elif k.get() == True:
        webbrowser.open("https://mplus.subcreation.net/")
    elif l.get() == True:
        webbrowser.open("https://www.youtube.com/watch?v=1VYD9zbXzpo")

#Widgets
c1 = Checkbutton(m, text = 'Tank',variable=i)
c1.pack()
c2 = Checkbutton(m, text = 'Healer',variable=j)
c2.pack()
c3 = Checkbutton(m, text = 'DPS',variable=k)
c3.pack()
c4 = Checkbutton(m, text = 'Mage',variable=l)
c4.pack()

b1 = Button(m, text = "What Class Shall I Play?",height=3, width=50, command=Classselect)
b1.pack()

mLabel.pack()

#Just need this kappa
m.mainloop()
