

class Task:

    def __init__(self, course, title, time, priority, duedate):             #please always refer to the title of the course as 
                                                                            #COURSE rather than CLASS to avoid confusion
        """
        Creates a "Task" object, usually a homework assignment or an exam.
        
        Args:
            course: (str) the name of the course the task belongs to
            title: (str) title of the tast
            time: (str) amount of time the task is estimated to take
            priority: (int) urgency of the task on a scale from 1-5 (1 is lowest priority, 5 is highest)
            duedate: (str) when the task is due, formatted as MM/DD"""

        self.course = course
        self.title = title
        self.time = time
        self.priority = priority
        self.duedate = duedate

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