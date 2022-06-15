from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

from datetime import time

class WeeklySchedule(GridLayout):

    def __init__(self, **kwargs):
        super(WeeklySchedule, self).__init__(**kwargs)
        
        self.class_days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
        ]
        self.cols = len(self.class_days) + 1

        # adding columnames
        self.add_widget(Label(text='Schedule'))
        for class_day in self.class_days:
            self.add_widget(Label(text=class_day))

        self.schedules = [
            # first block
            (time(hour =  8, minute = 00, second = 00), time(hour =  9, minute = 20, second = 00)),
            (time(hour =  9, minute = 30, second = 00), time(hour = 10, minute = 50, second = 00)),
            (time(hour = 11, minute = 00, second = 00), time(hour = 12, minute = 20, second = 00)),
            (time(hour = 12, minute = 30, second = 00), time(hour =  1, minute = 50, second = 00)),
            
            # free time

            # second block
            (time(hour = 15, minute = 00, second = 00), time(hour = 16, minute = 20, second = 00)),
            (time(hour = 16, minute = 30, second = 00), time(hour = 17, minute = 50, second = 00))
        ]
        for (start_time, end_time) in self.schedules: 

            self.add_widget(Label(text='{} \n{}'.format(start_time, end_time)))
            
            for class_day in self.class_days:
                
                layout = BoxLayout(padding=2)
                button = Button(text='Empty') # numero de salones disponibles
                layout.add_widget(button)
                
                self.add_widget(layout)

class MyApp(App):

    def build(self):

        self.title = 'Scheduler'

        self.weekly_schedule = WeeklySchedule()

        return self.weekly_schedule

if __name__ == '__main__':
    MyApp().run()