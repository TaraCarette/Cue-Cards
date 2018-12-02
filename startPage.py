import tkinter as tk
from tkinter import font as tkfont
import os
import Database

class startPage(tk.Frame):

     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          label = tk.Label(self, text="This is the start page", font=controller.title_font)
          label.pack(side="top", fill="x", pady=10)
          #tell the controlling parent to call show_frame with another frame 
          button1 = tk.Button(self, text="Create",
                            command=lambda: controller.show_frame("pageOne"), font=(None,15))
          button2 = tk.Button(self, text="Test",
                            command=self.goToPageTwo, font=(None,15))
          button1.pack(side=tk.TOP)
          button2.pack(side=tk.BOTTOM, pady=10)
          
          self.listOfCategories = ["choose a category"]
        
          if os.path.exists("./Databases"):
               #
               print("hello")
               filenames= os.listdir ("./Databases") # get all files' and folders' names in the current directory

               for filename in filenames: # loop through all the files and folders
                    #
                    print(os.path.join(os.path.abspath("./Databases"), filename))
                    if os.path.isdir(os.path.join(os.path.abspath("./Databases"), filename)): # check whether the current object is a folder or not
                         #
                         self.listOfCategories.append(filename)
                         print("hello")

          self.variable = tk.StringVar(self)
          self.variable.set(self.listOfCategories[0]) # default value
          ##          chooseCategory = tk.OptionMenu(middleFrame, variable, "one", "two", "three")
          self.chooseCategory = tk.OptionMenu(self, self.variable, *self.listOfCategories)
          ##          chooseCategory = apply(tk.OptionMenu, (self, variable) + tuple(listOfCategories))
          self.chooseCategory.config(width=20)
          self.chooseCategory.config(height=1)
          self.chooseCategory.pack(side=tk.TOP, pady=(0, 10), padx=10)
          

     def goToPageTwo(self):
          userCategory = self.variable.get()
          print(userCategory)
          Database.getters(userCategory)
          self.controller.show_frame("pageTwo")
