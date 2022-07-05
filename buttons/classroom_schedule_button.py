from kivy.properties import ObjectProperty

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class ClassroomScheduleButton(Button):
    classroom_day_schedule = ObjectProperty()
    def __init__(self, **kwargs):
        super(ClassroomScheduleButton, self).__init__(**kwargs)
        
        self.classroom_day_schedule = kwargs['classroom_day_schedule']
        self.text = self.classroom_day_schedule['activity_name']

        content = BoxLayout(orientation='vertical')
        content.add_widget(TextInput(
            text=self.text, 
            multiline=False, 
            on_text_validate=self.on_close_input, 
            halign='center', 
            size=(100, 30), 
            size_hint=(1.0, None)))
        box = BoxLayout(orientation='horizontal')
        box.add_widget(Button(text='Accept', on_release=self.on_close_button))
        box.add_widget(Button(text='Cancel', on_release=self.on_close_button))
        content.add_widget(box)
        self.popup = Popup(title='Enter Activity Name', content=content, size_hint=(0.8, 0.25), auto_dismiss=False)

    def on_release(self):
        self.popup.open()

    def on_close_input(self, inputtext):
        self.classroom_day_schedule['activity_name'] = inputtext.text
        self.text = inputtext.text
        self.popup.dismiss()

    def on_close_button(self, button):
        if button.text == 'Accept':
            self.classroom_day_schedule['activity_name'] = self.popup.content.children[1].text
            self.text = self.popup.content.children[1].text
        self.popup.content.children[1].text = self.text
        self.popup.dismiss()