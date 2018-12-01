import tkinter as tk
from tkinter import font  as tkfont
import os

class sampleApp(tk.Tk):
     #this class makes a webpage that will controll which frame we are on
     def __init__(self, *args, **kwargs):
          tk.Tk.__init__(self, *args, **kwargs)

          self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
          container = tk.Frame(self)
          container.pack(side="top", fill="both", expand=True)
          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)

          self.frames = {}
          #i think this makes the other pages
          for F in (startPage, pageOne, pageTwo):
               page_name = F.__name__
               frame = F(parent=container, controller=self)
               self.frames[page_name] = frame

               # put all of the pages in the same location;
               # the one on the top of the stacking order
               # will be the one that is visible.
               frame.grid(row=0, column=0, sticky="nsew")

          self.show_frame("startPage")

     def show_frame(self, page_name):
          '''Show a frame for the given page name'''
          frame = self.frames[page_name]
          frame.tkraise()



        
class scheduleMenu: #first window
     def __init__(self, parent, controller):

          top = self.top = Toplevel(parent)
          top.parent = parent
          top.geometry('300x300')
          top.grab_set() #gives the window a forced focus

          Button(top, text = "New User",command=lambda: controller.show_frame("PageOne")).pack()

     def OnDouble(self, event):
          widget = event.widget
          selection=widget.curselection()
          try:
               value = widget.get(selection[0])
               print ("selection:", selection, ": '%s'" % value)
               f = open ("userNameChosen.txt","w+")
               f.write (value+"\n")
               f.close()
               self.top.destroy()
               #self.readTitles()
          except:
               pass
     def newSchedule(self): #makes a popup and takes user input,
                                    #it then adds it to the text file                                    
          self.inputNewTitle = createNewTitle(self.top)
        


mainScreen = sampleApp()
mainScreen.mainloop()
