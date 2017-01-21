import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
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
        Lb1.pack()
        #buttonOpen = Button(frame, text="Open",command = lambda: self.refresh_list_files(listNodeFiles,Lb1))
        buttonOpen = Button(frame, text="Open",command = lambda: self.load_file(listNodeFiles,Lb1))
        buttonOpen.pack( side = LEFT)
        buttonRemove = Button(frame, text="Remove",command = lambda: self.deleteSelection(listNodeFiles,Lb1))
        buttonRemove.pack( side = LEFT )
    def refresh_list_files(self, listFiles, listUI):
        #messagebox.showinfo("Say Hello", "Hello World")
        indiceArchivo = 0
        listUI.delete(0,END)
        for nodeFile in listFiles:
            listUI.insert(indiceArchivo , nodeFile.fileName)
            indiceArchivo = indiceArchivo + 1#Actualizamos el valor
            listUI.update_idletasks()
    def load_file(self,listFiles,listUI):
        fname = askopenfilename(filetypes=(("Rar files", "*.rar"),
                                           ("All files", "*.*") ))
        if fname:
            try:
                listFiles.append(node_file(fname,fname))
                self.refresh_list_files(listFiles, listUI)
            except Exception as e: print (e)
            return
    def deleteSelection(self,listFiles,listUI) :
        items = listUI.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            listUI.delete( idx,idx )
            listFiles.pop(idx)    #eliminamos de la lista
            pos = pos + 1
        listUI.update_idletasks()
