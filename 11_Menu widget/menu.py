from tkinter import *

master = Tk()

def hello():
	print("hello, world!")

menu = Menu(master)
menu.add_command(label="open", command=hello)
menu.add_command(label="exit", command=master.destroy)

# display menu
master.config(menu=menu)

master.mainloop()