from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from kivy.app import App as KivyApp

from scheduler.modules.college import College
from scheduler.schedule.activity import Activity
from scheduler.schedule.update_activity import UpdateActivity

from scheduler.setter import ActivitySetter

class ActivityList(GridLayout):

    updated_activities = ListProperty()

    text_input = StringProperty()
    start_time = StringProperty()
    end_time = StringProperty()
    day = StringProperty()

    college = ObjectProperty()
    index = NumericProperty()

    def __init__(self, **kwargs):
        super(ActivityList, self).__init__(**kwargs)

        self.updated_activities = []

        self.start_time =  kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.day = kwargs['day']

        self.college = kwargs['college']
        self.index = kwargs['index']

        self.cols = 2

        n_activities = 0
        for id, classroom in self.college.get_classrooms().items():
            
            self.add_widget(Label(text=id))

            for activity_day in classroom.get_activity_days():
                if activity_day == self.day:
                    for activity in classroom.get_day_schedule(activity_day).get_schedule():
                        (schedule, start_time, end_time) = activity.get_schedule()
                        if self.start_time == start_time and self.end_time == end_time:
                            btn = UpdateActivity(
                                classroom_id=id,
                                start_time=start_time,
                                end_time=end_time,
                                day=activity_day,
                                schedule=schedule,
                                # extra params
                                text=activity.get_activity_name()
                            )
                            btn.bind(on_press=self.on_enter)
                            self.add_widget(btn)

    def on_enter(self, value):
        self.popup = ActivitySetter(college=self.college, classroom_id=value.classroom_id, activity_day=value.day, schedule=value.schedule)
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open()
        self.updated_activities.append(Activity(activity_name=value.text,
                                                classroom_id=value.classroom_id,
                                                activity_day=value.day,
                                                start_time=value.start_time,
                                                end_time=value.end_time,
                                                schedule=value.schedule))

    def on_dismiss(self, arg):
      pass  