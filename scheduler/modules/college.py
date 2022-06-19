from scheduler.modules.classroom import Classroom

DEMAT_CLASSROOMS_DESCRIPTION = """ 
    College

    Description:
    A set of classrooms with own activity days and activities schedule.

    Some conventions for now:

    + Every classroom has the same activity days: Weekdays. 
    + Every classroom has the same schedule: 
        - Classes start at 8:00.
        - There are 1 hour of free time for lunch at 15:00.
        - Each class lasts 1 hour and 20 minutes.
        - There are 10 minutes of free time between classes.
"""

class College():
    
    about = DEMAT_CLASSROOMS_DESCRIPTION

    def __init__(self, **kwargs):

        self.classroom_ids = kwargs['classroom_ids']
        self.activity_days = kwargs['activity_days']
        self.schedule_options = kwargs['schedule_options']

        self.n_classrooms = len(self.classroom_ids)

        self.classrooms = {}
        for classroom_id in self.classroom_ids:
            classroom = Classroom(
                id=classroom_id, 
                activity_days=self.activity_days, 
                schedule_options=self.schedule_options
            )
            self.classrooms[classroom_id] = classroom
    
    @classmethod
    def info(cls):
        print(cls.about)

    def get_classrooms(self):
        return self.classrooms
    
    def count_classrooms(self):
        return self.n_classrooms

    def get_classroom_ids(self):
        return self.classroom_ids
    
    def get_activity_days(self):
        return self.activity_days

    def get_schedule_options(self):
        return self.schedule_options

    def update_classroom_day_s_activity_schedule(self, classroom_id, activity_day, activity_schedule_index, activity_name):
        self.classrooms[classroom_id].update_day_s_activity_schedule(activity_day, activity_schedule_index, activity_name)

    def check_classroom_day_s_activity_schedule(self, classroom_id, activity_day, activity_schedule_index):
        self.classrooms[classroom_id].check_day_s_activity_schedule(activity_day, activity_schedule_index)