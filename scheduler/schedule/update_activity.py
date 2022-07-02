from kivy.properties import NumericProperty
from kivy.properties import StringProperty

from kivy.uix.button import Button

class UpdateActivity(Button):

    classroom_id = StringProperty()
    start_time = StringProperty()
    end_time = StringProperty()
    day = StringProperty()

    schedule = NumericProperty()

    def __init__(self, **kwargs):
        super(UpdateActivity, self).__init__(**kwargs)
        self.classroom_id = kwargs['classroom_id']
        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.day = kwargs['day']

        self.schedule = kwargs['schedule']