class ScheduleElement():

    def __init__(self, **kwargs):
        super(ScheduleElement, self).__init__(**kwargs)

        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']

        if 'activity_name' in kwargs:
            self.activity_name = kwargs['activity_name']
        else:
            self.activity_name = None

    def set_activity(self, activity_name):
        self.activity_name = activity_name
    
    def remove_activity(self):
        self.activity_name = None
    
    def get_schedule(self):
        return (self.start_time, self.end_time)
    
    def is_there_activity(self):
        if self.activity_name == None:
            return False
        return True