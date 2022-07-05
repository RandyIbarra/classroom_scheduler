from kivy.app import App
from kivy.lang import Builder

from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from scheduler.utils import get_classroom_ids
from scheduler.utils import get_activity_days
from scheduler.utils import get_activity_schedules

from scheduler.schedule.weekly_schedule2 import WeeklySchedule2
from scheduler.schedule.menu import SchedulerMenu

from scheduler.modules.college import College

def on_button_press(button):
    print(button.text)
    button.parent.parent.parent.parent.current = 'Menu'

class SchedulerMenu(Screen):

    def __init__(self, **kwargs):
        super(SchedulerMenu, self).__init__(**kwargs)

        grid_menu = GridLayout()

        layout_left = BoxLayout(orientation='vertical')
        button_left = Button(text='College Schedule', size=(200, 100), size_hint=(None, None), on_press = on_button_press)
        layout_left.add_widget(button_left)
        
        grid_menu.add_widget(layout_left)

        layout_right = BoxLayout(orientation='vertical')
        button_right = Button(text='Classroom Schedule', size=(200, 100), size_hint=(None, None), on_press = on_button_press)
        layout_right.add_widget(button_right)

        grid_menu.add_widget(layout_right)

        grid_menu.cols = 2

        self.add_widget(grid_menu)

class SchedulerApp(App):
    """
    This app helps you to make a college schedule
    """
    def on_start(self):
        
        print('starting app ...')

    def on_stop(self):
        
        print('stopping app ...')

    def build(self):

        print('building app ...')

        self.title = 'Scheduler'

        self.demat = College(
            classroom_ids=get_classroom_ids(),
            activity_days=get_activity_days(),
            activity_schedules=get_activity_schedules()
        )

        self.screen_manager = ScreenManager(transition=NoTransition())

        self.screen_manager.add_widget(SchedulerMenu(name='Menu'))
#        self.screen_manager.add_widget(WeeklySchedule2(name='Week', college=self.demat))

        self.screen_manager.current = 'Menu'

        return self.screen_manager