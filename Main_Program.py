from Task_Class import Task, read_Task

def main():
    task_list = []

    with open("TaskText") as f:
            finished = False
            while not finished:
                new_task = read_Task(f)
                if new_task is None:
                    finished = True
                else:
                    task_list.append(new_task)

    print("Create a Task")

    input_course = input("Course: ")
    while input_course == "":
        print("Please select a course.")
        input_course = input("Course: ")

    input_title = input("Assignment Title: ")
    while input_title == "":
        print("Please assign a name to your task.")
        input_title = input("Assignment Title: ")

    input_due = input("Due Date (MM/DD): ")
    while input_due == "":
        print("Please select a due date.")
        input_due = input("Due Date (MM/DD): ")

    input_time = input("Estimated time (in hours) it will take: ")          #optional

    input_priority = input("Priority level (1 = low, 5 = high): ")          #optional

    new_task = Task(input_course, input_title, input_due, input_time, input_priority)
    task_list.append(new_task)

    filename = "TaskText"
    with open(filename, "a") as f:
        f.write(input_course)
        f.write("\n")
        f.write(input_title)
        f.write("\n")
        f.write(input_due)
        f.write("\n")
        f.write(input_time)
        f.write("\n")
        f.write(input_priority)
        f.write("\n")


    print(task_list)





if __name__ == "__main__":
    main()