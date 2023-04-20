

class Task:

    def __init__(self, course, title, time, priority, duedate):
        self.course = course
        self.title = title
        self.time = time
        self.priority = priority
        self.duedate = duedate

    def get_course(self):
        return self.course
    
    def get_title(self):
        return self.title
    
    def get_time(self):
        return self.time
    
    def get_priority(self):
        return self.priority
    
    def due_date(self):
        return self.duedate