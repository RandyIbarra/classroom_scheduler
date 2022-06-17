from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

class ScheduleButton(Button):

    start_time = StringProperty()
    end_time = StringProperty()
    day = StringProperty()

    college = ObjectProperty()
    index = NumericProperty()

    def __init__(self, **kwargs):
        super(ScheduleButton, self).__init__(**kwargs)

        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.day = kwargs['day']

        self.college = kwargs['college']
        self.index = kwargs['index']