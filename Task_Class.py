class Task:

    def __init__(self, course, title, duedate, time = None, priority = None):             #please always refer to the title of the course as 
                                                                                          #COURSE rather than CLASS to avoid confusion
        """
        Creates a "Task" object, usually a homework assignment or an exam.
        
        Args:
            course: (str) the name of the course the task belongs to
            title: (str) title of the tast
            time: (int) amount of time the task is estimated to take in hours
            priority: (int) urgency of the task on a scale from 1-5 (1 is lowest priority, 5 is highest)
            duedate: (str) when the task is due, formatted as MM/DD"""

        self.course = course
        self.title = title
        self.duedate = duedate
        self.time = time
        self.priority = priority

    def __repr__(self):
        rep = "Task: " + self.title
        return rep

    def get_course(self):
        """Returns title of the course the task belongs to"""
        return self.course
    
    def get_title(self):
        """Returns title of the task"""
        return self.title
    
    def get_time(self):
        """Returns amount of time the task is estimated to take"""
        return self.time
    
    def get_priority(self):
        """Returns a number from 1-5 indicating task's priority"""
        return self.priority
    
    def get_duedate(self):
        """Returns the task's due date"""
        return self.duedate

"""task = Task("Data Structures", "Zybooks", 1, 3, "5/3")
print(task.get_course())
print(task.get_title())
print(task.get_time())
print(task.get_priority())
print(task.get_duedate())"""





def read_Task(f):
    """Reads the next task from the file, returning None at the end.
    Args:
        f (file handle)
    Returns:
        Task or None
    """
    course = f.readline().rstrip()

    title = f.readline().rstrip()

    time = f.readline().rstrip()
    if time == "":
        return None
    priority = f.readline().rstrip()
    if priority == "":
        return None
    duedate = f.readline().rstrip()
    
    f.readline()

    return Task(course, title, time, priority, duedate)





