import tkinter as tk

#change the text to be the answer
def answer():
    x= "hello"
    answerBox["text"] = x
    newCard = tk.PhotoImage(file="Kara and Ichi- twister kick in face.png", height = 350)
    cardLabel["image"] = newCard
    # cardLabel.configure(image=newCard)
    root.update_idletasks()

def next():
    answerBox["text"]=beforeAnswer
    #clear box
    newCard = tk.PhotoImage(file="Undyne- writing letter with fire.png", height = 350)
    cardLabel["image"] = newCard
    root.update_idletasks()

root = tk.Tk()

root.title("First GUI")

#have variable name so can find right picture
card = tk.PhotoImage(file="Kara and Ichi- twister kick in face.png", height = 350)
cardLabel = tk.Label(root, image=card)
cardLabel.pack( padx = 20, pady = 10)


#answer box that will change is have answer in it
beforeAnswer="Click Answer Button to Reveal Answer"
answerBox = tk.Label(root, text=beforeAnswer, height = 5, width = 50, relief="sunken")
answerBox.pack()

#user can type here to record their guess
userEntry = tk.Text(root, height = 4)
userEntry.pack(padx = 70, pady = 10)


#frame to get 3 bottoms on same row
bottomFrame = tk.Frame(root)

quitButton = tk.Button(bottomFrame, width = 15, text="Quit", command=lambda: controller.show_frame("startPage")).grid(column=1, row=0, padx = 30, pady = 10)
answerButton = tk.Button(bottomFrame, width = 15, text="Answer", command=answer).grid(column=2, row=0, padx = 30, pady = 10)
nextButton = tk.Button(bottomFrame, width = 15, text="Next Question", command=next).grid(column=3, row=0, padx = 30, pady = 10)

bottomFrame.pack()




root.mainloop()


