from View.gui_probleme import Gui_probleme
from tkinter import Tk

class App():
    def __init__(self, master):
        self.master = master
        self.gui = Gui_probleme(master)
        
if __name__ == "__main__":
    root = Tk()
    app= App(root)
    root.mainloop()