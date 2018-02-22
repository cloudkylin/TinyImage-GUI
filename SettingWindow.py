from tkinter import *
import tkinter.messagebox
import apikey
import tinify

class Setting_GUI:
    def __init__(self):
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