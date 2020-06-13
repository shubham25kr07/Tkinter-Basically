from tkinter import *

# template
class App(Frame):
	# const __init__
	def __init__(self,master=None):
		# call superclass
		super().__init__(master)
		self.master = master
		self.pack()
		# call method
		self.widgets()

	# method
	def widgets(self):

		self.hello = Button(self)
		self.hello["text"] = "click here"
		self.hello["command"] = self.clicked
		self.hello.pack(side="left")

		self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="right")

	def clicked(self):
		print("Hello, World!")


root = Tk()
# object
app = App(master=root)
root.mainloop()