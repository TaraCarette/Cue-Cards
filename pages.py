import tkinter as tk
from tkinter import font as tkfont
import os


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
                            command=lambda: controller.show_frame("pageTwo"), font=(None,15))
          button1.pack(side=tk.TOP)
          button2.pack(side=tk.BOTTOM, pady=10)


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


class pageTwo(tk.Frame):

     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          label = tk.Label(self, text="This is page 2", font=controller.title_font)
          label.pack(side="top", fill="x", pady=10)
          button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("startPage"))
          button.pack()
