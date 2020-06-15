from tkinter import *

master = Tk()

var = StringVar()
var.set("default")  # initialize

items = [
	("ESTV-GTI", "grupo de tecnologi industria"),
	("ETI","escola informatica"),
	("NCL","escola nicolau lobato")
]

def ok():
	print("user choose", var.get())

for alias,name in items:
	x = Radiobutton(master, text=alias, variable=var, value=name)
	x.pack()

b = Button(master, text="ok", fg="white", bg="blue", command=ok)
b.pack()

master.mainloop()