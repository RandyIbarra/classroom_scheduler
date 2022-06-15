class ClassroomDaySchedule():

    def __init__(self, **kwargs):
        super(ClassroomDaySchedule, self).__init__(**kwargs)

        self.day = kwargs['day']
        self.schedule_list = kwargs['schedule_list']

        self.schedule = []
        for (start_time, end_time) in self.schedule_list:
            schedule_element = ScheduleElement(start_time=start_time, end_time=end_time)
            self.schedule.append(schedule_element)
    
    def update_activity_by_index(self, schedule_element_index, activity_name=None):
        self.schedule[schedule_element_index].set_activity(activity_name)
    
    def check_activity_by_index(self, schedule_element_index):
        return self.schedule[schedule_element_index].is_there_activity()