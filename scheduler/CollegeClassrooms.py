class CollegeClassrooms():
    
    def __init__(self, **kwargs):
        super(CollegeClassrooms, self).__init__(**kwargs)

        self.classroom_ids = kwargs['classrooms_ids']
        self.n_classrooms = len(self.classrooms_ids)

        self.classrooms = {}

        for classroom_id in self.classroom_ids:

            days = [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday'
            ]

            classroom = Classroom(classoom_id=classroom_id, days=days)

            self.classrooms[classoom_id] = classroom

    def update_classroom_day_schedule_element(self, classroom_id, day, schedule_element_index, activity_name):
        self.classrooms[classroom_id].update_day_schedule_element(day, schedule_element_index, activity_name)

    def check_classroom_day_schedule_element(self, classroom_id, day, schedule_element_index):
        self.classrooms[classroom_id].check_day_schedule_element(day, schedule_element_index)