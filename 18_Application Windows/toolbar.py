from tkinter import *

root = Tk()

def ok():
	print("ok")

frame = Frame(root)

b = Button(frame, text="open", width=6, command=ok)
b.pack(side="left",padx=2,pady=2)

b = Button(frame, text="exit", width=6, command=ok)
b.pack(side="left",padx=2,pady=2)

frame.pack(side="top",fill=X)

root.mainloop()