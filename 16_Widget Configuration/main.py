from tkinter import *

root = Tk()
root.title("config")

def clr():
	jm.config(fg="chocolate")
def cpt():
	jm.config(text="Juliao Martins")
def rst():
	jm.config(fg="black",text="jm-kodigu")

jm = Label(root, text="jm-kodigu", bg="lightgreen", font=("fira code", 12))
jm.grid(columnspan=3)

color = Button(root, text="change color", command=clr)
color.grid(row=1,column=0)

caption = Button(root, text="change caption", command=cpt)
caption.grid(row=1,column=1)

reset = Button(root, text="reset", command=rst)
reset.grid(row=1,column=2)

root["bg"] = "lightgreen" # or root.config(bg="lightgreen")
root.mainloop()