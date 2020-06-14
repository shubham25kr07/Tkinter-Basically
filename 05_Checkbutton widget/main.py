from tkinter import *

master = Tk()

var = IntVar()
cpp = StringVar()

label = Label(master, text="which you choose programming languague?")

python = Checkbutton(master, text="python", variable=var)
java = Checkbutton(master, text="java", variable=var)
javascript = Checkbutton(master, text="javascript", variable=var)
cplusplus = Checkbutton(master, textvariable=cpp, variable=var)

cpp.set("c++")

label.pack()
python.pack(side="left")
java.pack(side="left")
javascript.pack(side="left")
cplusplus.pack(side="left")

master.mainloop()