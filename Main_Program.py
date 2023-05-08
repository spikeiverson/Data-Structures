from Task_Class import Task, read_Task
import create_new_task 

task_list = []

#Reads the text file and creates objects to populate the text file
def main_read():
    with open("TaskText") as f:
            finished = False
            while not finished:
                new_task = read_Task(f)
                if new_task is None:
                    finished = True
                else:
                    task_list.append(new_task)
    return task_list