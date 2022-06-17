from kivy.app import App as KivyApp

from scheduler.activity import Activity
from scheduler.college import College

DEMAT_CLASSROOM_IDS = ['Seminarios DEMAT', 'Astrofisica', 'DEMAT 3', 'DEMAT 4', 'DEMAT 5', 'DEMAT 6', 'DEMAT 7', 'DEMAT 8']
DEMAT_SCHEDULE_OPTIONS = [(' 8:00', ' 9:20'),(' 9:30', '10:50'),('11:00', '12:20'),('12:30', '13:50'),('15:00', '16:20'),('16:30', '17:50')]
WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday']

class App(KivyApp):

    def build(self):

        self.title = 'Scheduler'

        classroom_ids = DEMAT_CLASSROOM_IDS

        self.college = College(
            classroom_ids=classroom_ids,
            activity_days=WEEKDAYS,
            schedule_options=DEMAT_SCHEDULE_OPTIONS
        )
        
        self.weekly_schedule = WeeklySchedule(college=self.college)

        return self.weekly_schedule