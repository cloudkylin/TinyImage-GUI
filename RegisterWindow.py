from tkinter import *
import tkinter.messagebox
import apikey

class Register_GUI(Toplevel):
    def __init__(self):
        super(Register_GUI, self).__init__()
        self.name = StringVar()
        self.mail = StringVar()

        self.wm_title("Register - TinyImage")
        self.wm_attributes("-topmost", 1)

        title = Label(self, text="Regist")
        tiplabel = Label(self, text="Input your E-mail and Name, then check your E-mail.")
        Label(self, text="Name").grid(row=2, column=0, sticky=W)
        Label(self, text="E-mail").grid(row=3, column=0, sticky=W)
        nametext = Entry(self, textvariable=self.name, width=20).grid(row=2, column=1)
        mailtext = Entry(self, textvariable=self.mail, width=20).grid(row=3, column=1)
        submitbutton = Button(self, text="Submit", command=self.regiestekey)

        title.grid(row=0, columnspan=3)
        tiplabel.grid(row=1, columnspan=3)
        submitbutton.grid(row=2, column=2,rowspan=2, padx=5, pady=5, sticky=W + E + N + S)


    def regiestekey(self):
        name = self.name.get()
        mail = self.mail.get()
        try:
            apikey.registerkey(name, mail)
        except Exception as e:
            tkinter.messagebox.showerror("Error", e)
        else:
            tkinter.messagebox.showinfo("Success", "Register successfully, please check your email.")
            self.destroy()