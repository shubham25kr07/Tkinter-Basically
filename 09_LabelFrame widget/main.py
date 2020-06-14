from tkinter import *

master = Tk()

x = LabelFrame(master, text="name", padx=5, pady=5)
x.pack(padx=10,pady=10)

entry = Entry(x)
entry.pack()

master.mainloop()