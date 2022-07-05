from os.path import dirname, join
from json import dump, load

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.button import Button
from kivy.uix.label import Label

from buttons.classroom_schedule_button import ClassroomScheduleButton
from buttons.schedule_button import ScheduleButton

def build_college():
    classroom_names = [
        'Seminarios',
        'Astrofisica',
        'DEMAT3',
        'DEMAT4',
        'DEMAT5',
        'DEMAT6',
        'DEMAT7',
        'DEMAT8',
    ]

    classroom_activity_days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]

    activity_day_schedules = [
        '08:00-09:20', 
        '09:30-10:50',
        '11:00-12:20',
        '12:30-13:50',
        '15:00-16:20', # END CLASSES == GREEN OUR
    ]
    college = {}
    for classroom_name in classroom_names:
        activity_days = {}
        for activity_day in classroom_activity_days:
            activity_schedules = {}
            for activity_schedule in activity_day_schedules:
                classroom_day_schedule = {'activity_name': 'Not Assigned'}
                activity_schedules[activity_schedule] = classroom_day_schedule
            activity_days[activity_day] = activity_schedules
        college[classroom_name] = activity_days
    with open('data.json', 'w') as fd:
        dump(college, fd, indent=2)

class ManagerApp(App):

    def on_start(self):
        print('start')

    def on_stop(self):
        print('stop')
        with open('data.json', 'w') as fd:
            dump(self.college, fd, indent=2)

    def build(self):
        print('build')
        build_college()

        self.classroom_names = [
            'Seminarios',
            'Astrofisica',
            'DEMAT3',
            'DEMAT4',
            'DEMAT5',
            'DEMAT6',
            'DEMAT7',
            'DEMAT8',
        ]
        
        self.activity_days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
        ]

        self.activity_schedules = [
            '08:00-09:20', 
            '09:30-10:50',
            '11:00-12:20',
            '12:30-13:50',
            '15:00-16:20', # END CLASSES == GREEN OUR
        ]

        self.title = 'Scheduler'

        self.screens = {}
        self.classrooms = {}
        self.available_screens = [
            'MainScreen',
            'Classrooms',
            'WeekSchedules'
        ]
        self.screen_names = self.available_screens
        
        with open('data.json') as json_file: 
            self.college = load(json_file)

        curdir = dirname(__file__)

        self.available_screens = {fn: join(curdir, 'screens', '{}.kv'.format(fn).lower()) for fn in self.available_screens}
        self.classroom_screen_file = join(curdir, 'screens', '{}.kv'.format('classroomscreen').lower())

        self.root.switch_to(self.load_screen('MainScreen'))

    def load_screen(self, name):

        if name in self.screens:
            return self.screens[name]
        
        screen = Builder.load_file(self.available_screens[name])

        if screen.name == 'classrooms':
            screen_builded = self.build_left(screen) 
        elif screen.name == 'weekschedules':
            screen_builded = self.build_right(screen)
        else:
            screen_builded = screen
        
        self.screens[name] = screen_builded
        
        return screen_builded
    
    def build_left(self, screen):
        
        for classroom_name in self.classroom_names:
            screen.ids['content'].add_widget(Button(text=classroom_name, on_release=self.build_classroom_screen))

        return screen

    def build_right(self, screen):
        
        screen.ids['content'].add_widget(Label(text='Schedule'))
        for activity_day in self.activity_days:
            screen.ids['content'].add_widget(Label(text=activity_day))

        for activity_schedule in self.activity_schedules:
            screen.ids['content'].add_widget(Label(text=activity_schedule))
            for activity_day in self.activity_days:
                screen.ids['content'].add_widget(ScheduleButton(college=self.college, activity_day=activity_day, activity_schedule=activity_schedule))

        return screen

    def load_classroom(self, name):

        if name in self.classrooms:
            return self.classrooms[name]

        classroom = Builder.load_file(self.classroom_screen_file)
        classroom.name = name.lower()
        
        classroom.ids['content'].add_widget(Label(text='Schedule'))
        for activity_day in self.activity_days:
            classroom.ids['content'].add_widget(Label(text=activity_day))

        for activity_schedule in self.activity_schedules:
            classroom.ids['content'].add_widget(Label(text=activity_schedule))
            for activity_day in self.activity_days:
                classroom.ids['content'].add_widget(ClassroomScheduleButton(classroom_day_schedule=self.college[name][activity_day][activity_schedule]))
        
        self.classrooms[name] = classroom
        
        return classroom

    def build_classroom_screen(self, classroom_button):

        classroom_name = classroom_button.text

        self.root.switch_to(self.load_classroom(classroom_name), direction='up')


if __name__ == '__main__':
    Window.maximize()
    ManagerApp().run()