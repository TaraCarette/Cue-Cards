from tkinter import *
import os

class scheduleMenu: #first window
#label.config(font=("Courier", 44))
    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        top.parent = parent
        top.geometry('300x300')
        top.grab_set() #gives the window a forced focus

        #self.readTitles()
        scheduleSelect = Listbox(top, font=(None, 15))
        if not(os.path.isfile("userNames.txt")):
            q = open("userNames.txt","w+")
            q.close()
        f = open("userNames.txt","r")
        for line in f:
            scheduleSelect.insert(END, line)
        f.close()

        scheduleSelect.bind("<Double-Button-1>", self.OnDouble)
        scheduleSelect.pack()
        
        Button(top, text = "New User", command=self.newSchedule).pack()

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
        



def create_menu():
    window = scheduleMenu(mainScreen)    

mainScreen = Tk()
mainScreen.geometry('300x300')#size of the window
new = Button(mainScreen, text = "Create!", command=create_menu) #adds a button to window, gives text to button, what to do when button is pressed
# switchFormatImage = Button(mainScreen, text = "Switch to Image") #adds a button to window, gives text to button, what to do when button is pressed
# create_menu()
#scheduleMenu(mainScreen)
new.pack()
mainloop()
