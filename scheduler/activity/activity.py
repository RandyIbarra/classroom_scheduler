class Activity():
    """Activity
    Is an object that represents an activity at specific classroom at specific day at specific schedule.
    """
    def __init__(self, **kwargs):
        
        # required and constants
        self.classroom_id = kwargs['classroom_id']
        self.activity_day = kwargs['activity_day']
        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']

        # if there is no activity, then name is None
        self.activity_name = 'Not Asigned'
        if 'activity_name' in kwargs:
            self.activity_name = kwargs['activity_name']

    def update_activity_name(self, activity_name):
        self.activity_name = activity_name
    
    def remove_activity(self):
        self.update_activity_name('Not Asigned')
    
    def get_schedule(self):
        return (self.start_time, self.end_time)
    
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

if __name__ == '__main__':
    activity = Activity(activity_name='Modern Algebra',
                        classroom_id='D - 101',
                        activity_day='Monday',
                        start_time='8:00',
                        end_time='9:20')
    print('{} | {} - {} {}'.format(activity.get_classroom_id(), activity.get_activity_name(), activity.get_activity_day(), activity.get_schedule()))

    activity.update_activity_name('Geometry')
    print('{} | {} - {} {}'.format(activity.get_classroom_id(), activity.get_activity_name(), activity.get_activity_day(), activity.get_schedule()))

    print()

    activity.remove_activity()
    print('is there activity - {}'.format(activity.is_there_activity()))