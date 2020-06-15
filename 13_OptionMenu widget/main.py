from tkinter import *

master = Tk()

def checked():
	print("user choose", var.get())

var = StringVar()

option = OptionMenu(master, var,"one","two","three")
option.pack()
var.set("one")

b = Button(master, text="ok", fg="white", bg="blue", command=checked)
b.pack()

master.mainloop()