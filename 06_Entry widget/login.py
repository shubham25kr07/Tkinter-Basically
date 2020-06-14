from tkinter import *

# template
class Login:
	# const __init__
	def __init__(self,master=None):
		# local variable
		frame = Frame(master)
		frame.grid(padx=10,pady=10)

		# label username
		self.lbluser = Label(frame, text="Username")
		self.lbluser.grid(row=0,column=0)

		# prompt username
		self.prmuser = Entry(frame)
		self.prmuser.grid(row=0,column=1)

		# label password
		self.lblpassword = Label(frame)
		self.lblpassword["text"] = "password"
		self.lblpassword.grid(row=1,column=0)

		# prompt password
		self.prmpassword = Entry(frame)
		self.prmpassword["show"] = "*"
		self.prmpassword.grid(row=1,column=1)

		# login button
		self.login = Button(frame)
		self.login["text"] = "login"
		self.login["fg"] = "white"
		self.login["bg"] = "blue"
		self.login["command"] = self.checked
		self.login.grid(row=2,columnspan=1,pady=5)

		# cancel button
		self.cancel = Button(frame, text="cancel", fg="white", bg="red", command=self.clear)
		self.cancel.grid(row=2,columnspan=2,pady=2)

	# method
	def checked(self):
		username = self.prmuser.get()
		password = self.prmpassword.get()

		# verify username & password
		if (username.lower() == "juliao martins" and password.lower() == "jm-kodigu"):
			print("success login")
		elif (len(username) == 0 and len(password) == 0):
			print("please insert username and password")
		else:
			print("username and password incorrect!")


	def clear(self):
		self.prmuser.delete(0, END)
		self.prmpassword.delete(0, END)

root = Tk()
root.title("login")
# object
app = Login(master=root)
root.mainloop()