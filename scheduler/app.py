from kivy.app import App as KivyApp

from scheduler.utils import get_classroom_ids
from scheduler.utils import get_activity_days
from scheduler.utils import get_schedule_options

from scheduler.schedule.weekly_schedule import WeeklySchedule
from scheduler.modules.college import College

class App(KivyApp):

    def build(self):
        # app window title
        self.title = 'Scheduler'

        self.demat = College(
            classroom_ids=get_classroom_ids(),
            activity_days=get_activity_days(),
            schedule_options=get_schedule_options()
        )

        self.weekly_schedule = WeeklySchedule(college=self.demat)

        return self.weekly_schedule