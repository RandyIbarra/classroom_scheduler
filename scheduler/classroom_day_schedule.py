from scheduler.activity import Activity

class ClassroomDaySchedule():

    def __init__(self, **kwargs):

        # rerquired and constant
        self.classroom_id = kwargs['classroom_id']
        self.activities_day = kwargs['activities_day']
        self.schedule_options = kwargs['schedule_options']

        self.schedule = []
        for (start_time, end_time) in self.schedule_options:

            activity = Activity(activity_day=self.activities_day,
                                classroom_id=self.classroom_id,
                                start_time=start_time, 
                                end_time=end_time)
            
            self.schedule.append(activity)
    
    def update_activity_by_index(self, activity_schedule_index, activity_name):
        self.schedule[activity_schedule_index].update_activity_name(activity_name)
    
    def check_activity_by_index(self, activity_schedule_index):
        return self.schedule[activity_schedule_index].is_there_activity()
    
    def get_schedule(self):
        return self.schedule

if __name__ == '__main__':
    classroom_day_schedule = ClassroomDaySchedule(
        schedule_options=DEMAT_SCHEDULE_OPTIONS,
        activities_day='Monday',
        classroom_id='D - 101'
    )

    schedule = classroom_day_schedule.get_schedule()
    for activity in schedule:
        if activity.is_there_activity():
            print('{} | {} - {} {}'.format(activity.get_classroom_id(), activity.get_activity_name(), activity.get_activity_day(), activity.get_schedule()))
        else:
            print('{} | {} {}'.format(activity.get_classroom_id(), activity.get_activity_day(), activity.get_schedule()))