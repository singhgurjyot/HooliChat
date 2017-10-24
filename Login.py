from Tkinter import *

base = Tk()

v = IntVar(base)

def executeFile():
    if(v.get() == 1):
        execfile("host.pyw")
    elif(v.get() == 2):
        execfile("client.pyw")

base.title("Login")
base.geometry("300x500")

LoginLabel = Label(base, text="Login ID :")
LoginBox = Text(base, bg="white", width=20, height=1)

PasswordLabel = Label(base, text="Password :")
PasswordBox = Text(base, width=20, height=1)

hostButton = Radiobutton(base, text="Host", variable=v, value=1)
clientButton = Radiobutton(base, text="Client", variable=v, value=2)

LoginButton = Button(base, command=executeFile, text='Login')

LoginBox.place(x=50,y=100)
PasswordBox.place(x=50, y=200)
LoginLabel.place(x=52,y=70)
PasswordLabel.place(x=52, y=170)
hostButton.place(x=52, y=250)
clientButton.place(x=152, y=250)
LoginButton.place(x=100, y=300, width=100, height=50)


base.mainloop()
