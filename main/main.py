
from tkinter import *
#import time
#from random import random
from clearfile import *
from mouseEvents import *




if __name__ == "__main__":

    window = Tk()

    window.title("Welcome to Macro Controller")

    window.geometry('400x250')

    lbl = Label(window, text="Macro Controller")
    lbl.grid(column=3, row=0)
    #lb2 = Label(window, text=f"{query}\n")
    #lb2.grid(column=5, row=3)
    btn = Button(window, text="StartRecording", bg="red",)# command=wishMe)
    btn.grid(column=4, row=6)
    btn1 = Button(window, text="Exit ", bg="red", command=exit)
    btn1.grid(column=7, row=15)
    btn2 = Button(window, text="PlayRecord", bg="red")# command=mouseEvent.py)
    btn2.grid(column=8, row=6)
    btn3 = Button(window, text="ClearRecord", bg="red", command=clearFile)
    btn3.grid(column=5, row=15)

    window.mainloop()