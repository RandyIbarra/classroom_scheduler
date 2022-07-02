class Activity():
    """Activity
    Is an object that represents an activity at specific 
    classroom at specific day at specific schedule.
    """
    def __init__(self, **kwargs):
        
        # required and constants
        self.classroom_id = kwargs['classroom_id']
        self.activity_day = kwargs['activity_day']
        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.schedule = kwargs['schedule']

        # if there is no activity, then name is None
        self.activity_name = 'Not Assigned'
        if 'activity_name' in kwargs:
            self.activity_name = kwargs['activity_name']

    def update_activity_name(self, activity_name):
        self.activity_name = activity_name
    
    def remove_activity(self):
        self.update_activity_name('Not Asigned')
    
    def get_schedule(self):
        return (self.schedule, self.start_time, self.end_time)
    
    def get_activity_name(self):
        return self.activity_name
    
    def get_activity_day(self):
        return self.activity_day
    
    def get_classroom_id(self):
        return self.classroom_id
    
    def is_there_activity(self):
        if self.activity_name != 'Not Asigned':
            return True
        return False