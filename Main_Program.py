from Task_Class import Task, read_Task
import create_new_task 

task_list = []

def main_read():
    with open("TaskText") as f:
            finished = False
            while not finished:
                new_task = read_Task(f)
                if new_task is None:
                    finished = True
                else:
                    task_list.append(new_task)
    print(task_list)


def sort_course():
    pass

def sort_duedate():
    pass

def sort_time_descending():
    task_list.sort(key=lambda x: x.time)
    return task_list

def sort_time_ascending():
    task_list.sort(key=lambda x: x.time, reverse = True)
    return task_list
    
def sort_priority_descending():
    task_list.sort(key=lambda x: x.priority)
    return task_list

def sort_priority_ascending():
    task_list.sort(key=lambda x: x.priority, reverse = True)
    return task_list
