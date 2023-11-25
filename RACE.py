from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)
def insertText(s:str):
    textDiary.insert(INSERT,s + '\n')
    textDiary.see(END)
road_image = PhotoImage(file="road.png")
road = Label(root,image=road_image)
road.place(x=0, y=17)
x01, x02, x03, x04 = 20,20,20,20
horse01_image = PhotoImage(file="horse01.png")
horse1 = Label(root,image=horse01_image)
horse02_image = PhotoImage(file="horse02.png")
horse2 = Label(root,image=horse02_image)
horse03_image = PhotoImage(file="horse03.png")
horse3 = Label(root,image=horse03_image)
horse04_image = PhotoImage(file="horse04.png")
horse4 = Label(root,image=horse04_image)
