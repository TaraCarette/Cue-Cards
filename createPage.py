import tkinter as tk
from tkinter import font as tkfont
import os


class pageOne(tk.Frame):

     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
##          label = tk.Label(self, text="This is page 1", font=controller.title_font)
##          label.pack(side="top", fill="x", pady=10)
          #tell the controlling parent to call show_frame with another frame 
          button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("startPage"))
          button.pack(side=tk.TOP)

          
          middleFrame = tk.Frame(self)
          #left side
          word = tk.Text(middleFrame, height=14, width=30, font=(None, 15))
          word.pack(side=tk.LEFT, padx=10, pady=10)

          #right side
          listOfCategories = ["choose a category"]
          if os.path.exists("./Databases"):
               print("hello")
               filenames= os.listdir ("./Databases") # get all files' and folders' names in the current directory

               for filename in filenames: # loop through all the files and folders
                    print(os.path.join(os.path.abspath("./Databases"), filename))
                    if os.path.isdir(os.path.join(os.path.abspath("./Databases"), filename)): # check whether the current object is a folder or not
                         listOfCategories.append(filename)
                         print("hello")
          createCategory = tk.Button(middleFrame, text="Create Category")
          createCategory.pack(pady=(30, 0), padx=10, fill="x")
          
          variable = tk.StringVar(self)
          variable.set(listOfCategories[0]) # default value

##          chooseCategory = tk.OptionMenu(middleFrame, variable, "one", "two", "three")
          chooseCategory = tk.OptionMenu(middleFrame, variable, *listOfCategories)
##          chooseCategory = apply(tk.OptionMenu, (self, variable) + tuple(listOfCategories))
          chooseCategory.config(width=20)
          chooseCategory.config(height=1)
          chooseCategory.pack(pady=(0, 10), padx=10)
          
          answerLabel = tk.Label(middleFrame, text="answer description")
          answerLabel.pack(pady=(10, 0))
          answer = tk.Text(middleFrame, height=15, width=20)
          answer.pack(pady=(0, 10), padx=10)

          middleFrame.pack()

          button = tk.Button(self, text="Cancel",
                           command=lambda: controller.show_frame("startPage"))
          button.pack(side=tk.LEFT, fill="x", expand=True, padx=10)
          button = tk.Button(self, text="Create!",
                           command=lambda: controller.show_frame("startPage"))
          button.pack(side=tk.LEFT, fill="x", expand=True, padx=30, pady=10)   
##          userName.grid(row=0, column=1)
