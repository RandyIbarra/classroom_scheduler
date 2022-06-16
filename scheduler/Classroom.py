from datetime import time

class Classroom():
    
    def __init__(self, **kwargs):
        super(Classroom, self).__init__(**kwargs)

        self.classroom_id = kwargs['classoom_id']
        self.days = kwargs['days']

        self.class_schedules_per_day = {}
        for day in self.days:

            schedule_list = [
                # first block
                (time(hour =  8, minute = 00, second = 00), time(hour =  9, minute = 20, second = 00)),
                (time(hour =  9, minute = 30, second = 00), time(hour = 10, minute = 50, second = 00)),
                (time(hour = 11, minute = 00, second = 00), time(hour = 12, minute = 20, second = 00)),
                (time(hour = 12, minute = 30, second = 00), time(hour =  1, minute = 50, second = 00)),
                
                # free time

                # second block
                (time(hour = 15, minute = 00, second = 00), time(hour = 16, minute = 20, second = 00)),
                (time(hour = 16, minute = 30, second = 00), time(hour = 17, minute = 50, second = 00))
            ]

            classroom_day_schedule = ClassroomDaySchedule(day=day, schedule_list=schedule_list)

            self.class_schedules_per_day[day] = classroom_day_schedule

    def update_day_schedule_element(self, day, schedule_element_index, activity_name):
        self.class_schedules_per_day[day].update_activity_by_index(schedule_element_index, activity_name)

    def check_day_schedule_element(self, day, schedule_element_index):
        return self.class_schedules_per_day[day].check_activity_by_index(schedule_element_index)