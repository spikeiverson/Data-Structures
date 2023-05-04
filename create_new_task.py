import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from Task_Class import Task, read_Task
from Main_Program import task_list, main_read

def open_new_task():
    def create():
        error_label = Label(task_screen, text='Fill out all fields marked with *')
        error_label_2 = Label(task_screen, text='Fill out all fields correctly')
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
        input_priority = priority_entry.get()
        if input_priority != '':
            if input_priority.isnumeric() == False:
                error_label_2.grid(row=7, column=0)
                return
            elif int(input_priority) > 5 or int(input_priority) < 1:
                error_label_2.grid(row=7, column=0)
                return
        input_time = time_entry.get()
        tk.Label(text="Task created!").grid(row=7, column=1)
        new_task = Task(input_course, input_title, input_due_date, input_time, input_priority)
        task_list.append(new_task)
    
        filename = "TaskText"
        with open(filename, "a") as f:
            f.write(input_course)
            f.write("\n")
            f.write(input_title)
            f.write("\n")
            f.write(input_due_date)
            f.write("\n")
            if input_time == "":
                f.write("~")
            else:
                f.write(input_time)
            f.write("\n")
            if input_priority == "":
                f.write("~")
            else:
                f.write(input_priority)
            f.write("\n")
    
    task_screen = Tk()
    task_screen.title("Create New Task")
    task_screen.config(bg='#90EE90')
    task_screen.geometry("450x325")

    #title
    title_label = Label(task_screen, text="Title *", bg='#90EE90')
    title_label.grid(row=1, column=0, sticky='w')

    title_entry = Entry(task_screen)
    title_entry.grid(row=1, column=1, sticky='ew')

    #course
    course_label = Label(task_screen, text="Course *", bg='#90EE90')
    course_label.grid(row=2, column=0, sticky='w')

    course_entry = Entry(task_screen)
    course_entry.grid(row=2, column=1, sticky='ew')


    #priority
    priority_label = Label(task_screen, text="Priority (5-1)", bg='#90EE90')
    priority_label.grid(row=3, column=0, sticky='w')

    priority_entry = Entry(task_screen)
    priority_entry.grid(row=3, column=1, sticky='ew')

    #time
    time_label = Label(task_screen, text="Time", bg='#90EE90')
    time_label.grid(row=4, column=0, sticky='w')

    time_entry = Entry(task_screen)
    time_entry.grid(row=4, column=1, sticky='ew')

    #due_date
    due_date_label = Label(task_screen, text="Due date *", bg='#90EE90')
    due_date_label.grid(row=5, column=0, sticky='nw')

    due_date_entry = Calendar(task_screen, selectmode='day', year=2023, month=5, day=1)
    due_date_entry.grid(row=5, column=1, sticky='w')

    #Button
    create_button = Button(task_screen, text="Create", command=create, bg='green', fg='white')
    create_button.grid(row=6, column=1)

    task_screen.mainloop()



root = Tk()
root.title('Main Menu')
root.geometry("500x500")



titlelabel = Label(root, text = "Title")
courselabel = Label(root, text = "Course")
prioritylabel = Label(root, text = "Priority")
timelabel = Label(root, text = "Time")
duelabel = Label(root, text = "Due Date")
open_new_task_button = Button(root, text='New Task', command=open_new_task, fg='white', bg='green')

titlelabel.grid(row = 0, column = 0)
courselabel.grid(row = 0, column = 1)
prioritylabel.grid(row = 0, column = 2)
timelabel.grid(row = 0, column = 3)
duelabel.grid(row = 0, column = 4)
open_new_task_button.grid(row=1, column=2)


root.after(1, main_read)
root.mainloop()