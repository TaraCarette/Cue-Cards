import tkinter as tk
from tkinter import font as tkfont
import os


class pageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.card = tk.Label(self, text="yay", height = 20, width = 15) #have the card!!!
        self.card.pack(padx = 30, pady = 10)

        self.answerBox = tk.Label(self, text="Click Answer Button to Reveal Answer", height = 5, width = 50, relief="sunken")

        self.answerBox.pack()


        #user can type here to record their guess
        userEntry = tk.Text(self, height = 4)
        userEntry.pack(padx = 70, pady = 10)


        #frame to get 3 bottoms on same row
        bottomFrame = tk.Frame(self)

        quitButton = tk.Button(bottomFrame, width = 15, text="Quit", command=lambda: controller.show_frame("startPage")).grid(column=1, row=0, padx = 30, pady = 10)
        answerButton = tk.Button(bottomFrame, width = 15, text="Answer", command=self.answer).grid(column=2, row=0, padx = 30, pady = 10)
        nextButton = tk.Button(bottomFrame, width = 15, text="Next Question", command=self.next).grid(column=3, row=0, padx = 30, pady = 10)

        bottomFrame.pack()

    def answer(self):
        self.answerBox["text"]="the answer" #variable here!!!

    def next(self):

        self.answerBox["text"]="next"