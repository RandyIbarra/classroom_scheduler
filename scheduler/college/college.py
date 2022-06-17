from scheduler.classroom import Classroom

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

        self.activity_days = kwargs['activity_days']
        self.schedule_options = kwargs['schedule_options']

        self.classroom_ids = kwargs['classroom_ids']
        self.n_classrooms = len(self.classroom_ids)

        self.classrooms = {}
        for classroom_id in self.classroom_ids:
            classroom = Classroom(id=classroom_id, 
                                  activity_days=self.activity_days, 
                                  schedule_options=self.schedule_options)
            self.classrooms[classroom_id] = classroom
    
    @classmethod
    def info(cls):
        print(cls.about)
    
    def get_classrooms(self):
        return self.classrooms

    def update_classroom_day_s_activity_schedule(self, classroom_id, activity_day, activity_schedule_index, activity_name):
        self.classrooms[classroom_id].update_day_s_activity_schedule(activity_day, activity_schedule_index, activity_name)

    def check_classroom_day_s_activity_schedule(self, classroom_id, activity_day, activity_schedule_index):
        self.classrooms[classroom_id].check_day_s_activity_schedule(activity_day, activity_schedule_index)

    
if __name__ == '__main__':

    classroom_ids = [
        'A - 101', 'B - 201', 'C - 301'
    ]
    
    college = College(classroom_ids=classroom_ids)

    for id, classroom in college.get_classrooms().items():
        print('++++++++++++++++++++++++++++++++++++++++')
        for activity_day in classroom.get_activity_days():
            for activity in classroom.get_day_schedule(activity_day).get_schedule():
                if activity.is_there_activity():
                    print('{} | {} - {} {}'.format(activity.get_classroom_id(), activity.get_activity_name(), activity.get_activity_day(), activity.get_schedule()))
                else:
                    print('{} | {} {}'.format(activity.get_classroom_id(), activity.get_activity_day(), activity.get_schedule()))
            print('---')
