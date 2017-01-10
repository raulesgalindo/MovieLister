import tkinter
from ..logic.structures import *
from tkinter import *
class window_principal:
    listNodeFiles#List of Files to sync
    def show_window(self):
        top = tkinter.Tk()
        self.add_panel_load_files(top)
        # Code to add widgets will go here...
        top.mainloop()
    #Method to fill the panel to load files
    def add_panel_load_files(self, window):
        frame = Frame(window)
        frame.pack()
        Lb1 = Listbox(frame)
        Lb1.insert(1, "Python")
        Lb1.insert(2, "Perl")
        Lb1.insert(3, "C")
        Lb1.insert(4, "PHP")
        Lb1.insert(5, "JSP")
        Lb1.insert(6, "Ruby")
        Lb1.pack()
        buttonOpen = Button(frame, text="Open")
        buttonOpen.pack( side = LEFT)
        buttonRemove = Button(frame, text="Remove")
        buttonRemove.pack( side = LEFT )
