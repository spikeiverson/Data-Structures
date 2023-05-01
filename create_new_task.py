import tkinter as tk
from tkinter import *
from tkcalendar import Calendar

def create():
    error_label = tk.Label(text='Fill out all fields marked with *')
    error_label_2 = tk.Label(text='Fill out all fields correctly')
    input_title = title_entry.get()
    if input_title == '':
        error_label.grid(row=7, column=0)
        return
    input_course = course_entry.get()
    if input_course == '':
        error_label.grid(row=7, column=0)
        return
    input_due_date = due_date_entry.get_date()
    if input_due_date == '':
        error_label.grid(row=7, column=0)
        return
    input_priority = int(priority_entry.get())
    if int(input_priority) > 5 or (input_priority) < 1:
        error_label_2.grid(row=7, column=0)
        return
    input_time = time_entry.get()
    tk.Label(text="Task created!").grid(row=7, column=1)
    return input_title, input_course, input_due_date, input_priority, input_time

new_task = tk.Tk()
new_task.title("Create New Task")

#title
title_label = tk.Label(new_task, text="Title *")
title_label.grid(row=1, column=0, sticky='w')

title_entry = tk.Entry(new_task)
title_entry.grid(row=1, column=1)

#course
course_label = tk.Label(new_task, text="Course *")
course_label.grid(row=2, column=0, sticky='w')

course_entry = tk.Entry(new_task)
course_entry.grid(row=2, column=1)

#due_date
due_date_label = tk.Label(new_task, text="Due date *")
due_date_label.grid(row=5, column=0, sticky='nw')

due_date_entry = Calendar(new_task, selectmode='day', year=2023, month=5, day=1)
due_date_entry.grid(row=5, column=1, sticky='w')

#priority
priority_label = tk.Label(new_task, text="Priority (5-1)")
priority_label.grid(row=3, column=0, sticky='w')

priority_entry = tk.Entry(new_task)
priority_entry.grid(row=3, column=1)

#time
time_label = tk.Label(new_task, text="Time")
time_label.grid(row=4, column=0, sticky='w')

time_entry = tk.Entry(new_task)
time_entry.grid(row=4, column=1)

create_button = tk.Button(new_task, text="Create", command=create)
create_button.grid(row=6, column=1)

new_task.mainloop()
