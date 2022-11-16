from tkinter import *

class Gui_probleme:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(self.frame, text="Hello", command=self.write_slogan)
        self.slogan.pack(side=LEFT)

    def write_slogan(self):
        print("Tkinter is easy to use!")