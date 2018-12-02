import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
import os
import Database

class pageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #directory = "Anatomy"
        self.array = Database.call()
        print (self.array)
        self.card = tk.Label(self, text = self.array[1], height = 20, width = 50, wraplength=300) #have the card!!!
        self.card.pack(padx = 30, pady = 10)

        self.answerBox = tk.Label(self, text="Click Answer Button to Reveal Answer", height = 5, width = 50, relief="sunken", wraplength=300)

        self.answerBox.pack()


        #user can type here to record their guess
        self.userEntry = tk.Text(self, height = 4, wrap=WORD)
        self.userEntry.pack(padx = 70, pady = 10)


        #frame to get 3 bottoms on same row
        bottomFrame = tk.Frame(self)

        quitButton = tk.Button(bottomFrame, width = 15, text="Quit", command=lambda: controller.show_frame("startPage")).grid(column=1, row=0, padx = 30, pady = 10)
        answerButton = tk.Button(bottomFrame, width = 15, text="Answer", command=self.answer).grid(column=2, row=0, padx = 30, pady = 10)
        nextButton = tk.Button(bottomFrame, width = 15, text="Next Question", command=self.next).grid(column=3, row=0, padx = 30, pady = 10)

        bottomFrame.pack()

    def answer(self):
        self.answerBox["text"] = self.array[0] #variable here!!!

    def next(self):
        #directory = "Anatomy"
        self.array = Database.call()
        self.card["text"] = self.array[1] #variable here!!!
        #self.card["text"] = "Hi"
        #print("Hi")
        self.answerBox["text"]="Click Answer Button to Reveal Answer"
        self.userEntry.delete('1.0', tk.END)
