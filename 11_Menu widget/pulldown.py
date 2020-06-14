from tkinter import *

master = Tk()

def hello():
	print("hello, world!")
def quit():
	print("program is closed!")
	master.destroy()

menubar = Menu(master)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="open", command=hello)
filemenu.add_command(label="save", command=hello)
filemenu.add_command(label="save as", command=hello)
filemenu.add_separator()
filemenu.add_command(label="close", command=quit)
menubar.add_cascade(label="file", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="copy", command=hello)
editmenu.add_command(label="cut", command=hello)
editmenu.add_separator()
editmenu.add_command(label="paste", command=hello)
menubar.add_cascade(label="edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="about", command=hello)
menubar.add_cascade(label="help", menu=helpmenu)

# display menu
master.config(menu=menubar)

master.mainloop()