from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import Screen

from scheduler.utils import get_classroom_ids
from scheduler.utils import get_activity_days
from scheduler.utils import get_schedule_options

from scheduler.schedule.weekly_schedule import WeeklySchedule
from scheduler.schedule.menu import SchedulerMenu

from scheduler.modules.college import College

class SchedulerApp(App):
    """
    This app helps you to make a college schedule
    """
    def on_start(self):
        
        print('starting app ...')

    def on_stop(self):
        
        print('stopping app ...')

    def build(self):
        # app window title
        self.title = 'Scheduler'
        # build a college object
        self.demat = College(
            classroom_ids=get_classroom_ids(),
            activity_days=get_activity_days(),
            schedule_options=get_schedule_options()
        )
        self.weekly_schedule = WeeklySchedule(college=self.demat)
        # screen manager
        self.screen_manager = ScreenManager(transition=NoTransition())
        # define screens
        self.screen_manager.add_widget(SchedulerMenu(name='Menu'))
        self.screen_manager.current = 'Menu'
        return self.screen_manager