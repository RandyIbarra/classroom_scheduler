from kivy.uix.popup import Popup

from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.lang import Builder

def on_button_press(button):
    print(button.id)

    classroom_id = button.parent.parent.parent.parent.parent.classroom_id
    activity_day = button.parent.parent.parent.parent.parent.activity_day
    schedule = button.parent.parent.parent.parent.parent.schedule

    if button.id == 'accept_button':
        activity_name = button.parent.parent.children[1].text
        print(classroom_id)
        print(activity_day)
        print(schedule)
        print(activity_name)
        button.parent.parent.parent.parent.parent.college.update_classroom_day_s_activity_schedule(classroom_id=classroom_id, activity_day=activity_day, activity_schedule_index=schedule, activity_name=activity_name)
    if button.id == 'cancel_button':
        button.parent.parent.children[1].text = button.parent.parent.parent.parent.parent.college.check_classroom_day_s_activity_schedule(classroom_id = classroom_id, activity_day = activity_day, activity_schedule_index = schedule)

    button.parent.parent.parent.parent.parent.dismiss()

def on_enter(value):
    classroom_id = value.parent.parent.parent.parent.classroom_id
    activity_day = value.parent.parent.parent.parent.activity_day
    schedule = value.parent.parent.parent.parent.schedule
    activity_name = value.text
    print(classroom_id)
    print(activity_day)
    print(schedule)
    print(activity_name)
    value.parent.parent.parent.parent.college.update_classroom_day_s_activity_schedule(classroom_id=classroom_id, activity_day=activity_day, activity_schedule_index=schedule, activity_name=activity_name)

    value.parent.parent.parent.parent.dismiss()

class AcceptButton(Button):
    def __init__(self, **kwargs):
        super(AcceptButton, self).__init__(**kwargs)
        self.id = 'accept_button'
        self.text = 'Accept'
        self.bind(on_press = on_button_press)

class CancelButton(Button):
    def __init__(self, **kwargs):
        super(CancelButton, self).__init__(**kwargs)
        self.id = 'cancel_button'
        self.text = 'Cancel'
        self.bind(on_press = on_button_press)

class ActivityInput(TextInput):
    def __init__(self, **kwargs):
        super(ActivityInput, self).__init__(**kwargs)
        self.id = 'input'
        self.multiline = False
        self.halign = 'center'
        self.size_hint = (1, None)
        self.height = 30
        self.bind(on_text_validate = on_enter)

class ActivitySetter(Popup):

    college = ObjectProperty()

    classroom_id = StringProperty() 
    activity_day = StringProperty()
    schedule = NumericProperty()
    
    def __init__(self, **kwargs):
        super(ActivitySetter, self).__init__(**kwargs)
        self.title = 'Enter activity'
                
        self.size_hint = None, None
        self.size = 500, 150

        content = GridLayout(rows = 2)

        content.add_widget(ActivityInput(text=self.college.check_classroom_day_s_activity_schedule(classroom_id = self.classroom_id, activity_day = self.activity_day, activity_schedule_index = self.schedule)))

        buttons = BoxLayout(orientation ='horizontal')

        buttons.add_widget(AcceptButton())
        buttons.add_widget(CancelButton())

        print(buttons.ids)

        content.add_widget(buttons)

        self.content = content