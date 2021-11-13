from tkinter import *
from tkinter import filedialog
import os

print("Source: https://github.com/Cyber-Coding-Scripts/OS")
def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()