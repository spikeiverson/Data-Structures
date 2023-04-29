import tkinter as tk
from tkinter import *

def create():
    title = title_entry.get()
    course = course_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()
    time = time_entry.get()
    return title, course, due_date, priority, time

new_task = tk.Tk()
new_task.title("Create New Task")

#title
title_label = tk.Label(new_task, text="Title:")
title_label.grid(row=1, column=0)

title_entry = tk.Entry(new_task)
title_entry.grid(row=1, column=1)

#course
course_label = tk.Label(new_task, text="Course:")
course_label.grid(row=2, column=0)

course_entry = tk.Entry(new_task)
course_entry.grid(row=2, column=1)

#due_date
due_date_label = tk.Label(new_task, text="Due date:")
due_date_label.grid(row=3, column=0)

due_date_entry = tk.Entry(new_task)
due_date_entry.grid(row=3, column=1)

#priority
priority_label = tk.Label(new_task, text="Priority:")
priority_label.grid(row=4, column=0)

priority_entry = tk.Entry(new_task)
priority_entry.grid(row=4, column=1)

#time
time_label = tk.Label(new_task, text="Time:")
time_label.grid(row=5, column=0)

time_entry = tk.Entry(new_task)
time_entry.grid(row=5, column=1)

create_button = tk.Button(new_task, text="Create", command=create)
create_button.grid(row=6, column=1)

new_task.mainloop()