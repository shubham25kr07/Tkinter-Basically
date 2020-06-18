from tkinter import *

root = Tk()
root.title("menus")

def callback():
	print('testing!')

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="open", command=callback)
filemenu.add_command(label="save", command=callback)
filemenu.add_separator()
filemenu.add_command(label="exit", command=callback)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="about", command=callback)

# display menubar
root.config(menu=menubar)

root.mainloop()