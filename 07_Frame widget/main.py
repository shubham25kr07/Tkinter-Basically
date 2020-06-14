from tkinter import *

master = Tk()

Label(master, text="one").pack()

Frame(master, height=5, bd=2, relief=GROOVE).pack(fill=X,expand=1)

Label(master, text="two").pack()

master.mainloop()