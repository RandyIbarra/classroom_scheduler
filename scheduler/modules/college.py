from scheduler.modules.classroom import Classroom

class College():

    classrooms = {}
    activity_days = []
    activity_schedules = []

    def __init__(self, classroom_ids, activity_days, activity_schedules, **kwargs):

        self.activity_days = activity_days
        self.activity_schedules = activity_schedules

        for classroom_id in classroom_ids:
            classroom = Classroom(
                id=classroom_id, 
                activity_days=self.activity_days, 
                activity_schedules=self.activity_schedules
            )
            self.classrooms[classroom_id] = classroom


    def update_classroom_day_s_activity_schedules(self, classroom_id, activity_day, activity_schedules_index, activity_name):

        self.classrooms[classroom_id].update_day_s_activity_schedules(activity_day, activity_schedules_index, activity_name)

    def check_classroom_day_s_activity_schedules(self, classroom_id, activity_day, activity_schedules_index):
        
        return self.classrooms[classroom_id].check_day_s_activity_schedules(activity_day, activity_schedules_index)