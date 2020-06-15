from tkinter import *

master = Tk()

m1 = PanedWindow()
m1.pack(fill=BOTH,expand=1)

left = Label(m1, text="left")
m1.add(left)

m2 = PanedWindow(orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top")
m2.add(top)

bottom = Label(m2, text="bottom")
m2.add(bottom)

master.mainloop()