from kivy.app import App

from kivy.uix.button import Button

from utils import get_classroom_ids
from utils import get_activity_days
from utils import get_schedule_options

from modules.college import College

from setter import ActivitySetter
class MyApp(App):
    def build(self):
        self.college = College(
            classroom_ids=get_classroom_ids(),
            activity_days=get_activity_days(),
            schedule_options=get_schedule_options()
        )
        button = Button(text = 'text')
        button.bind(on_press = self.on_button_press)
        print("fdfasfdfsafdsa")
        self.popup = ActivitySetter(college=self.college, classroom_id='Astrofisica', activity_day='Monday', schedule=1)
        print("fdfasfdfsafdsa")
        return button
    def on_button_press(self, button):
        print(self.college.check_classroom_day_s_activity_schedule(classroom_id = 'Astrofisica', activity_day = 'Monday', activity_schedule_index = 1))
        print(self.popup.children[0].children)
        self.popup.open()

MyApp().run()