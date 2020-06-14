from tkinter import *

master = Tk()

x = Listbox(master)
x.pack()

x.insert(END,"hello, world!")

def delt():
	x.delete(0,END)

for item in ["tic","tac","toe"]:
	x.insert(END, item)

b = Button(master, text="delete list", bg="red", fg="white", command=delt)
b.pack()

master.mainloop()