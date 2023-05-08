import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from Task_Class import Task, read_Task
from Main_Program import task_list, main_read

def open_new_task():
    task_screen = Tk()
    task_screen.title("Create New Task")
    task_screen.config(bg='#90EE90')


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
        Label(task_screen, text="Task created!").grid(row=7, column=1)
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

    create_button = Button(task_screen, text="Create", command=lambda:[create(),add_new_screen()], bg='green', fg='white')
    create_button.grid(row=6, column=1)

    task_screen.mainloop()



root = Tk()
root.title('Main Menu')
root.geometry('500x500')


def sort_method():
    sorting = clicked.get()
    if sorting == 'Time Ascending':
        task_list.sort(key=lambda x: x.time)
    elif sorting == 'Time Descending':
        task_list.sort(key=lambda x: x.time, reverse=True)
    elif sorting == 'Priority Ascending':
        task_list.sort(key=lambda x: x.priority)
    elif sorting == 'Priority Descending':
        task_list.sort(key=lambda x: x.priority, reverse=True)
    elif sorting == 'Due Date Ascending':
        task_list.sort(key=lambda x: x.duedate)
    elif sorting == 'Due Date Descending':
        task_list.sort(key=lambda x: x.duedate, reverse=True)
    else:
        return
    rearrange(task_list)



task_list = main_read()
i = len(task_list)
methods = ['Due Date Ascending', 'Due Date Descending', 'Priority Ascending', 'Priority Descending', 'Time Ascending', 'Time Descending']
clicked = StringVar()
clicked.set('Sort by')

def root_labels():
    dropdown = OptionMenu(root, clicked, *methods)
    titlelabel = Label(root, text = "Title", bg='#90EE90')
    courselabel = Label(root, text = "Course", bg='#90EE90')
    prioritylabel = Label(root, text = "Priority", bg='#90EE90')
    timelabel = Label(root, text = "Time", bg='#90EE90')
    duelabel = Label(root, text = "Due Date", bg='#90EE90')
    open_new_task_button = Button(root, text='New Task', command=open_new_task, fg='white', bg='green')
    sort_button = Button(root, text='Sort', command=sort_method, fg='white', bg='#505050')


    titlelabel.grid(row = 0, column = 0)
    courselabel.grid(row = 0, column = 1)
    prioritylabel.grid(row = 0, column = 2)
    timelabel.grid(row = 0, column = 3)
    duelabel.grid(row = 0, column = 4)
    open_new_task_button.grid(row=6, column=5, padx=50)
    sort_button.grid(row=2, column=5, padx=50)
    dropdown.grid(row=1, column=5, padx=50)

def rearrange(task_list):
    for everything in root.grid_slaves():
        everything.destroy()

    root_labels()
    
    i = len(task_list)
    for t in range(i):
        task_title = Label(root, text=task_list[t].title)
        task_course = Label(root, text=task_list[t].course)
        task_priority = Label(root, text=task_list[t].priority)
        task_time = Label(root, text=task_list[t].time)
        task_duedate = Label(root, text=task_list[t].duedate)


        task_title.grid(row=t+1, column=0)
        task_course.grid(row=t+1, column=1)
        task_priority.grid(row=t+1, column=2)
        task_time.grid(row=t+1, column=3)
        task_duedate.grid(row=t+1, column=4)

def add_new_screen():
    i = len(task_list) - 1
    task_title = Label(root, text=task_list[i].title)
    task_course = Label(root, text=task_list[i].course)
    if task_list[i].priority == "":
        task_priority = Label(root, text="~")
    else:
        task_priority = Label(root, text=task_list[i].priority)
    if task_list[i].time == "":
        task_time = Label(root, text="~")
    else:
        task_time = Label(root, text=task_list[i].time)
    task_duedate = Label(root, text=task_list[i].duedate)

    task_title.grid(row=i+1, column=0)
    task_course.grid(row=i+1, column=1)
    task_priority.grid(row=i+1, column=2)
    task_time.grid(row=i+1, column=3)
    task_duedate.grid(row=i+1, column=4)
    
    
rearrange(task_list)
root.mainloop()
