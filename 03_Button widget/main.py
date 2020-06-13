from tkinter import *

master = Tk()

def ok():
	print("Button on click!")

f = Frame(master, width=20, height=25)
f.pack_propagate(0)
f.pack(padx=10,pady=5)

x = Button(f, text="ok", fg="white", bg="lightgreen", command=ok, state=DISABLED)
x.pack(fill=BOTH,expand=1)

master.mainloop()