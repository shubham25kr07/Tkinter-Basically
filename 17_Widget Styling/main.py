from tkinter import *

root = Tk()

def key(event):
	print("Pressed", repr(event.char))

def popup(event):
	print("clicked at", event.x,event.y)

frame = Frame(root, width=100, height=100)
frame.bind('Key',key)
frame.bind('<Button-3>',popup)
frame.pack()

root.mainloop()