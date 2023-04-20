def main():

    print("Create a task")

    input_course = input("Course: ")
    while input_course == "":
        print("Please select a course.")
        input_course = input("Course: ")

    input_title = input("Assignment Title: ")
    while input_title == "":
        print("Please assign a name to your task.")
        input_title = input("Assignment Title: ")

    input_time = input("Estimated time (in hours) it will take: ")          #optional

    input_priority = input("Priority level (1 = low, 5 = high): ")          #optional

    input_due = input("Due Date (MM/DD): ")
    while input_due == "":
        print("Please select a due date.")
        input_due = input("Due Date (MM/DD): ")

if __name__ == "__main__":
    main()