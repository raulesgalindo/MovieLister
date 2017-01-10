import tkinter
from tkinter import *
from tkinter import messagebox
from ..logic.structures import *

class window_principal:
    listNodeFiles = []#List of Files to sync
    Lb1 = ""
    def show_window(self):
        top = tkinter.Tk()
        self.add_panel_load_files(top,self.listNodeFiles,self.Lb1)
        # Code to add widgets will go here...
        top.mainloop()
    #Method to fill the panel to load files
    def add_panel_load_files(self, window,listNodeFiles,Lb1):
        frame = Frame(window)
        frame.pack()
        Lb1 = Listbox(frame)
        listNodeFiles.append(node_file("lara","vel"))
        for nodeFile in listNodeFiles:
            Lb1.insert(7, nodeFile.fileName)
        Lb1.pack()
        buttonOpen = Button(frame, text="Open",command = lambda: self.refresh_list_files(listNodeFiles,Lb1))
        buttonOpen.pack( side = LEFT)
        buttonRemove = Button(frame, text="Remove")
        buttonRemove.pack( side = LEFT )
    def refresh_list_files(self, listFiles, listUI):
        messagebox.showinfo("Say Hello", "Hello World")
