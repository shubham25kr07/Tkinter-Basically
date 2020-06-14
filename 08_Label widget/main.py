from tkinter import *

master = Tk()
master.title("label")
master.geometry("230x160")

photo = PhotoImage(file="img/py.png")
test = Label(master, image=photo)
test.photo = photo
test.pack()

var = StringVar()

label = Label(master, textvariable=var, fg="blue", font=("fira code", 17), anchor=W)
label.pack()

var.set("Python Developer")

master.mainloop()