import tinify
import apikey
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

class MainWindow:
    def __init__(self):
        root = Tk()
        root.title("TinyImage")
        root.geometry("250x80")

        menubar = Menu(root)
        menubar.add_command(label="Settings",command=self.load_GUI)
        menubar.add_command(label="Register",command=self.regist_GUI)
        root.config(menu=menubar)

        main = Frame(root)
        main.pack()
        self.cont = StringVar()
        self.cont.set('Unknown')
        compressions_this_month_text = Label(main, text="Compressions this month:")
        try:
            key = apikey.validate(apikey.loadkey())
        except:
            self.load_GUI()
        else:
            self.cont.set(str(tinify.compression_count))
        compressions_this_month = Label(main, textvariable=self.cont)
        uploadfile = Button(main, text="Compressions",command=self.uploadfile, width=20)

        compressions_this_month_text.grid(row=0,column=0,sticky = W)
        compressions_this_month.grid(row=0,column=1,sticky = E)
        uploadfile.grid(row=1, column=0, rowspan=2,padx=5, pady=10, sticky=W + E + N + S)

        root.mainloop()

    def uploadfile(self):
        filename = tkinter.filedialog.askopenfilename(filetypes=[("JPEG File", "jpg"),("PNG File","png")])
        if not filename:
            pass
        else:
            source = tinify.from_file(filename)
            strlen = len(filename)
            source.to_file(filename[0:strlen-4]+"_tiny"+filename[strlen-4:strlen])
            self.cont.set(str(tinify.compression_count))
            tkinter.messagebox.showinfo("Success", "File location: %s"% filename)

    def load_GUI(self):
        key = "Input your key here"
        load = Toplevel()
        load.wm_title("Settings - TingImage")
        load.wm_attributes("-topmost", 1)

        welcome = Label(load, text="Settings")
        try:
            key = apikey.loadkey()
            statustext = "continue with this key"
        except Exception as e:
            statustext = e
        statuslabel = Label(load, text=statustext)
        self.keystringvar = StringVar()
        self.keystringvar.set(key)
        keytext = Entry(load, textvariable=self.keystringvar, width=40)
        continuebutton = Button(load, text="Continue",command=self.loadkey, width=12)
        welcome.grid(row=0, sticky=W + E + N + S)
        statuslabel.grid(row=1, sticky=W + E + N + S)
        keytext.grid(row=2, sticky=W + E + N + S)
        continuebutton.grid(row=3,padx=5,pady=5)

    def loadkey(self):
        key = self.keystringvar.get()
        try:
            apikey.inputkey(key)
        except Exception as e:
            tkinter.messagebox.showerror("Error", e)
        else:
            tkinter.messagebox.showinfo("Success", "Update API-Key successful!")
            self.cont.set(str(tinify.compression_count))


    def regist_GUI(self):
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

if __name__ == "__main__":
    window = MainWindow()