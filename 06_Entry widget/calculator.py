from tkinter import *

# template
class Calculator(Frame):
	# const __init__
	def __init__(self,master=None):
		# call superclass
		super().__init__(master)
		self.master = master
		self.grid(padx=10,pady=5)
		# call method
		self.calculator_widgets()

	# method
	def calculator_widgets(self):

		# firstnumber label
		self.firstlbl = Label(self)
		self.firstlbl["text"] = "first number"
		self.firstlbl.grid()

		# firstnumber prompt
		self.firstpmt = Entry(self)
		self.firstpmt.grid(row=0,column=1)

		# operator label
		self.operatorlbl = Label(self)
		self.operatorlbl["text"] = "operator"
		self.operatorlbl.grid(row=1,column=0)

		# operator prompt
		self.operatorpmt = Entry(self)
		self.operatorpmt.grid(row=1,column=1)

		# secondnumber label
		self.secondlbl = Label(self)
		self.secondlbl["text"] = "second number"
		self.secondlbl.grid(row=2,column=0)

		# secondnumber prompt
		self.secondpmt = Entry(self)
		self.secondpmt.grid(row=2,column=1)

		# equal button 
		self.equal = Button(self)
		self.equal["text"] = "="
		self.equal["fg"] = "white"
		self.equal["bg"] = "black"
		self.equal["command"] = self.equals
		self.equal.grid(pady=5,row=3,column=0,columnspan=1)

		# clear button
		self.clear = Button(self)
		self.clear["text"] = "c"
		self.clear["fg"] = "white"
		self.clear["bg"] = "red"
		self.clear["command"] = self.clears
		self.clear.grid(pady=5,row=3,column=1,columnspan=1)


		# result label
		self.resultlbl = Label(self, text="result")
		self.resultlbl.grid(row=4,column=0)

		self.result = Entry(self)
		self.result.grid(row=4,column=1)

	def equals(self):
		first = self.firstpmt.get()
		operator = self.operatorpmt.get()
		second = self.secondpmt.get()

		if operator == "+":
			t = int(first) + int(second)
		elif operator == "-":
			t = int(first) - int(second)
		elif operator == "x":
			t = int(first) * int(second)
		elif operator == "/":
			t = int(first) // int(second)
		else:
			t = "not match!"

		self.result.insert(END, t)

	def clears(self):
		self.firstpmt.delete(0, END)
		self.operatorpmt.delete(0, END)
		self.secondpmt.delete(0, END)
		self.result.delete(0, END)


root = Tk()
root.title("calculator")
# object
app = Calculator(root)
app.mainloop()