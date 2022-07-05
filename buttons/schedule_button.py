from .classroom_schedule_button import ClassroomScheduleButton

from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class ScheduleButton(Button):

    college = ObjectProperty()
    activity_day = StringProperty()
    activity_schedule = StringProperty()
    
    def __init__(self, **kwargs):
        super(ScheduleButton, self).__init__(**kwargs)

        self.text = '...'
        self.college = kwargs['college']

    def on_release(self):
        content = BoxLayout(orientation='vertical')
        for name in self.college.keys():
            row = BoxLayout(orientation='horizontal')
            row.add_widget(Label(text=name))
            row.add_widget(ClassroomScheduleButton(classroom_day_schedule=self.college[name][self.activity_day][self.activity_schedule]))
            content.add_widget(row)
        content.add_widget(Button(text='Return', size_hint=(1.0,0.5), on_release=self.on_close))
        self.popup = Popup(title='Select Activity', content=content, size_hint=(.8, 1), auto_dismiss=True)
        self.popup.open()

    def on_close(self, button):
        if button.text == 'Accept':
            self.classroom_day_schedule.activity_name = self.popup.content.children[1].text
        self.popup.dismiss()
        # how to clean self.popup memory?