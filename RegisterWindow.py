from tkinter import *
import tkinter.messagebox
import apikey

class Register_GUI:
    def __init__(self):
        regist = Toplevel()
        regist.wm_title("Register - TinyImage")
        regist.wm_attributes("-topmost", 1)

        tittle = Label(regist, text="Regist")
        tiplabel = Label(regist, text="Input your E-mail and Name, then check your E-mail.")
        tittle.grid(row=0, columnspan=3)
        tiplabel.grid(row=1, columnspan=3)

        Label(regist, text="Name").grid(row=2,column=0, sticky=W)
        Label(regist, text="E-mail").grid(row=3,column=0, sticky=W)
        self.name = StringVar()
        self.mail = StringVar()
        nametext = Entry(regist, textvariable=self.name, width=20).grid(row=2, column=1)
        mailtext = Entry(regist, textvariable=self.mail, width=20).grid(row=3, column=1)
        submitbutton = Button(regist, text="Submit",command=self.regiestekey)
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