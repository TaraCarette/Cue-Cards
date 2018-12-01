import tkinter as tk
from tkinter import font as tkfont
import os


class pageOne(tk.Frame):

     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          label = tk.Label(self, text="This is page 1", font=controller.title_font)
          label.pack(side="top", fill="x", pady=10)
          #tell the controlling parent to call show_frame with another frame 
          button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("startPage"))
          button.pack()
