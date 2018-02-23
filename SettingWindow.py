from tkinter import *
import tkinter.messagebox
import apikey
import tinify

class Setting_GUI(Toplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        key = "Input your key here"
        self.keystringvar = StringVar()

        self.wm_title("Settings - TingImage")
        self.wm_attributes("-topmost", 1)

        title = Label(self, text="Settings")
        try:
            key = apikey.loadkey()
            statustext = "continue with this key"
        except Exception as e:
            statustext = e
        statuslabel = Label(self, text=statustext)
        self.keystringvar.set(key)
        keytext = Entry(self, textvariable=self.keystringvar, width=40)
        continuebutton = Button(self, text="Continue",command=self.loadkey, width=12)

        title.grid(row=0, sticky=W + E + N + S)
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
            self.parent.cont.set(str(tinify.compression_count))
            self.destroy()