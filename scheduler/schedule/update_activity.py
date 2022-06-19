from kivy.properties import StringProperty

from kivy.uix.textinput import TextInput

class UpdateActivity(TextInput):

    classroom_id = StringProperty()
    start_time = StringProperty()
    end_time = StringProperty()
    day = StringProperty()

    def __init__(self, **kwargs):
        super(UpdateActivity, self).__init__(**kwargs)
        classroom_id = kwargs['classroom_id']
        start_time = kwargs['start_time']
        end_time = kwargs['end_time']
        day = kwargs['day']