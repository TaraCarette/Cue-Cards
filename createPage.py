import tkinter as tk
from tkinter import font as tkfont
import os
import Database


class makeCategory:
    def __init__(self,parent):
        self.parent=parent
        top = self.top = tk.Toplevel()
##        top.geometry('250x80')
        top.grab_set() #gives the window a forced focus
        
        answerLabel = tk.Label(top, text="Enter the Category name")
        answerLabel.grid(row=0)
        
##        self.word = tk.Text(top, height=2, width=20, font=(None, 10))
        self.word = tk.Entry(top, font=(None, 15))        
        self.word.grid(row=1, padx=10, pady=5, columnspan=2)
        
        b = tk.Button(top, text="Cancel", command=self.cancel, font=(None, 15), height = 1, width = 10)
        b.grid(row=2,column=0, pady=5)
                
        b = tk.Button(top, text="Make", command=self.ok, font=(None, 15), height = 1, width = 10)
        b.grid(row=2,column=1, pady=5)
    def ok(self):
        
        userInput = self.word.get()
        print(userInput)
        userInput.rstrip("\r\n")
        if not os.path.exists("Databases/" + userInput):
            os.mkdir("Databases/" + userInput)
            self.parent.updateMenu()
        self.top.grab_release()
        self.top.destroy()
    def cancel(self):
        self.top.grab_release()
        self.top.destroy()
        
class pageOne(tk.Frame):

    def __init__(self, parent, controller):
        #here
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##    label = tk.Label(self, text="This is page 1", font=controller.title_font)
        ##    label.pack(side="top", fill="x", pady=10)
        #tell the controlling parent to call show_frame with another frame 
        button = tk.Button(self, text="Go to the start page",
                       command=lambda: controller.show_frame("startPage"))
        button.pack(side=tk.TOP)


        middleFrame = tk.Frame(self)
        #left side
        self.question = tk.Text(middleFrame, height=14, width=30, font=(None, 15))
        self.question.pack(side=tk.LEFT, padx=10, pady=10)

        #right side
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
        
        #createbutton
        createCategory = tk.Button(middleFrame, text="Create Category", command=self.createPopup)
        createCategory.pack(pady=(30, 0), padx=10, fill="x")

        self.variable = tk.StringVar(self)
        self.variable.set(self.listOfCategories[0]) # default value
        ##          chooseCategory = tk.OptionMenu(middleFrame, variable, "one", "two", "three")
        self.chooseCategory = tk.OptionMenu(middleFrame, self.variable, *self.listOfCategories)
        ##          chooseCategory = apply(tk.OptionMenu, (self, variable) + tuple(listOfCategories))
        self.chooseCategory.config(width=20)
        self.chooseCategory.config(height=1)
        self.chooseCategory.pack(pady=(0, 10), padx=10)

        answerLabel = tk.Label(middleFrame, text="answer description")
        answerLabel.pack(pady=(0, 0))
        self.answer = tk.Text(middleFrame, height=15, width=20)
        self.answer.pack(pady=(0, 10), padx=10)

        middleFrame.pack()

        button = tk.Button(self, text="Cancel",
                       command=lambda: controller.show_frame("startPage"))
        button.pack(side=tk.LEFT, fill="x", expand=True, padx=10)
        button = tk.Button(self, text="Create!",
                       command=self.saveEntry)
        button.pack(side=tk.LEFT, fill="x", expand=True, padx=30, pady=10)   

        
    def createPopup(self): #makes a popup and takes user input,
                                    #it then adds it to the text file                                    
        self.inputNewCategory = makeCategory(self)

#send the data over
    def saveEntry(self):

        userQuestion = self.question.get("1.0",'end-1c')
        print(userQuestion)           

        userCategory = self.variable.get()
        print(userCategory)
        
        userAnswer = self.answer.get("1.0",'end-1c')
        print(userAnswer)        
        Database.save(1,userQuestion,userAnswer,userCategory)
        self.question.delete('1.0', tk.END)
        self.answer.delete('1.0', tk.END)
        self.variable.set(self.listOfCategories[0])
        self.controller.show_frame("startPage")
    #function call
    #save(datatype,question,answer, directory) 
    def updateMenu(self):
        #refills and updates the categories
        self.listOfCategories = []
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

        menu = self.chooseCategory["menu"]
        menu.delete(0, "end")
        for string in self.listOfCategories:
            menu.add_command(label=string, 
                             command=lambda value=string: self.variable.set(value))
