from tkinter import *

master = Tk()

x = Entry()
x.pack(pady=10,padx=10)

x.insert(END, "a default value!")

def ok():
	t = x.get()
	print(t.capitalize())

def delt():
	x.delete(0, END)

b = Button(master, text="ok", command=ok)
c = Button(master, text="delete", fg="red", command=delt)

b.pack()
c.pack()

master.mainloop()