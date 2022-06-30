from tkinter import * 
from classes.status import *

class Interface:
    def __init__(self):
        """Status discord"""
        self.root =Tk()  
        self.root.resizable(width=False, height=False)    
        self.root.title('Status discord')
        Label(self.root,
              text ="message status::").grid(row =1,column=1)
        Button(self.root, text ='Set status',
               command = self.setStatus).grid(row = 9,column=2, sticky = W)
        Button(self.root, text ='Quitter',
               command =self.root.quit).grid(row =9, column= 0,sticky = E)
        self.entree = Entry(self.root, width =100)

        Label(self.root,
              text ="Lists emoji:").grid(row =4, column=1)


        self.entree.grid(row =2,column=1)
        self.entree.emoji = Entry(self.root, width =100)
        self.entree.emoji.grid(row =5,column=1)
        self.root.mainloop()
        

    def setStatus(self):
        status = Status(self.entree.emoji.get(),self.entree.get())
        status.startStatus()


   