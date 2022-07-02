from scheduler.modules.classroom_day_schedule import ClassroomDaySchedule
#from modules.classroom_day_schedule import ClassroomDaySchedule

class Classroom():
    """Classroom

    A classroom is a object of an entity called college (In this case DEMAT). 

    instance attributes:
        id: classroom identifier
        activities_day: classroom activity days 
        schedule_options: schedule options for the classroom 
    """

    def __init__(self, **kwargs):
        
        self.id = kwargs['id']
        self.activity_days = kwargs['activity_days']
        self.schedule_options = kwargs['schedule_options']

        self.day_schedules = {}
        for activity_day in self.activity_days:

            classroom_day_schedule = ClassroomDaySchedule(classroom_id=self.id,
                                                          activities_day=activity_day, 
                                                          schedule_options=self.schedule_options)

            self.day_schedules[activity_day] = classroom_day_schedule

    def id(self):
        return self.id
    
    def get_activity_days(self): 
        return self.activity_days
    
    def get_day_schedule(self, activity_day):
        return self.day_schedules[activity_day]

    def check_day_s_activity_schedule(self, activity_day, activity_schedule_index):
        return self.day_schedules[activity_day].check_activity_by_index(activity_schedule_index)

    def update_day_s_activity_schedule(self, activity_day, activity_schedule_index, activity_name):
        self.day_schedules[activity_day].update_activity_by_index(activity_schedule_index, activity_name)

if __name__ == '__main__':

    DEMAT_SCHEDULE_OPTIONS = [
        # morning classes
        (time(hour =  8, minute = 00).strftime("%H:%M:%S"), time(hour =  9, minute = 20).strftime("%H:%M:%S")),
        (time(hour =  9, minute = 30).strftime("%H:%M:%S"), time(hour = 10, minute = 50).strftime("%H:%M:%S")),
        (time(hour = 11, minute = 00).strftime("%H:%M:%S"), time(hour = 12, minute = 20).strftime("%H:%M:%S")),
        (time(hour = 12, minute = 30).strftime("%H:%M:%S"), time(hour =  1, minute = 50).strftime("%H:%M:%S")),
        #
        # lunch time
        #
        # evening classes
        (time(hour = 15, minute = 00).strftime("%H:%M:%S"), time(hour = 16, minute = 20).strftime("%H:%M:%S")),
        (time(hour = 16, minute = 30).strftime("%H:%M:%S"), time(hour = 17, minute = 50).strftime("%H:%M:%S"))
    ]
    WEEKDAYS = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]

    classroom = Classroom(id='A - 101', 
                          activity_days=WEEKDAYS,
                          schedule_options=DEMAT_SCHEDULE_OPTIONS)
    
    for activity_day in classroom.get_activity_days():
        for activity in classroom.get_day_schedule(activity_day).get_schedule():
            if activity.is_there_activity():
                print('{} | {} - {} {}'.format(activity.get_classroom_id(), activity.get_activity_name(), activity.get_activity_day(), activity.get_schedule()))
            else:
                print('{} | {} {}'.format(activity.get_classroom_id(), activity.get_activity_day(), activity.get_schedule()))
        print('---')