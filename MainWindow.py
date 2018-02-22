import tinify
import apikey
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

import SettingWindow
import RegisterWindow

class Main_GUI:
    def __init__(self,root):
        root.title("TinyImage")
        root.geometry("250x80")

        menubar = Menu(root)
        menubar.add_command(label="Settings",command=self.setting_GUI)
        menubar.add_command(label="Register",command=self.register_GUI)
        root.config(menu=menubar)

        main = Frame(root)
        main.pack()
        self.cont = StringVar()
        self.cont.set('Unknown')
        compressions_this_month_text = Label(main, text="Compressions this month:")
        try:
            key = apikey.validate(apikey.loadkey())
        except:
            self.setting_GUI()
        else:
            self.cont.set(str(tinify.compression_count))
        compressions_this_month = Label(main, textvariable=self.cont)
        uploadfile = Button(main, text="Compressions",command=self.uploadfile, width=20)

        compressions_this_month_text.grid(row=0,column=0,sticky = W)
        compressions_this_month.grid(row=0,column=1,sticky = E)
        uploadfile.grid(row=1, column=0, rowspan=2,padx=5, pady=10, sticky=W + E + N + S)

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

    def setting_GUI(self):
        SettingWindow.Setting_GUI()

    def register_GUI(self):
        RegisterWindow.Register_GUI()