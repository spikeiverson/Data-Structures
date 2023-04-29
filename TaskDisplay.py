from tkinter import *

root = Tk()

titlelabel = Label(root, text = "Title")
courselabel = Label(root, text = "Course")
prioritylabel = Label(root, text = "Priority")
timelabel = Label(root, text = "Time")
duelabel = Label(root, text = "Due Date")

titlelabel.grid(row = 0, column = 0)
courselabel.grid(row = 0, column = 1)
prioritylabel.grid(row = 0, column = 2)
timelabel.grid(row = 0, column = 3)
duelabel.grid(row = 0, column = 4)

root.mainloop()