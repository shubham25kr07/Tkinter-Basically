from tkinter import *

master = Tk()

count = 0

def test():
	global count

	count += 1

	menu.entryconfig(0,label=str(count))

menubar = Menu(master)

menu = Menu(menubar, tearoff=0, postcommand=test)
menu.add_command(label=str(count))
menu.add_command(label="exit", command=master.destroy)
menubar.add_cascade(label="menu", menu=menu)

# display menu
master.config(menu=menubar)

master.mainloop()