from tkinter import *

master = Tk()

draw = Canvas(master, width=200, height=100)
draw.pack()

draw.create_line(0,0,200,100)
draw.create_line(0,100,200,0,fill="red", dash=(4,4))
draw.create_rectangle(50,25,150,75,fill="blue")

master.mainloop()