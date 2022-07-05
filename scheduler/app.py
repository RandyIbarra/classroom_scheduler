from kivy.app import App
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.label import Label

from os.path import dirname, join
from json import dump, load

from scheduler.buttons.classroom_schedule_button import ClassroomScheduleButton
from scheduler.buttons.schedule_button import ScheduleButton

from scheduler.utils import get_activity_schedules
from scheduler.utils import get_classroom_ids
from scheduler.utils import get_activity_days

class SchedulerApp(App):

    def build(self):

        # college data
        self.activity_schedules = get_activity_schedules()
        self.classroom_names = get_classroom_ids()
        self.activity_days = get_activity_days()

        with open('data/data.json') as json_file: 
            self.college = load(json_file)
        
        print(self.college.keys())

        # app title
        self.title = 'Scheduler'

        # app screens
        self.screens = {}
        self.classrooms = {}

        # app main screen names
        self.available_screens = [
            'MainScreen',
            'Classrooms',
            'WeekSchedules'
        ]
        self.screen_names = self.available_screens

        curdir = dirname(__file__)

        # make paths to .kv files for main screen
        self.available_screens = {fn: join(curdir, 'screens', '{}.kv'.format(fn).lower()) for fn in self.available_screens}

        # path to .kv classroom weekly schedule screen base
        self.classroom_screen_file = join(curdir, 'screens', '{}.kv'.format('classroomscreen').lower())
        
        print(self.available_screens)
        print(self.classroom_screen_file)

        # swith current app screen to MainScreen 
        self.root.switch_to(self.load_screen('MainScreen'))

    def load_screen(self, name):
        """
        Description:
        Load one of the principal screens: 
            
            Main Screen, 
            Classrooms Screen, 
            Week Schedules Screen.
        
        Args:
            name (string): Options {'MainScreen', 'WeekSchedules', 'Classrooms'}

        Returns:
            builded_screen (Screen Kivy object):  Screen to show in app window
        """
        # if screen has been loaded, then its screen object is returned
        if name in self.screens:
            return self.screens[name]
        # read the .kv with the principal components        
        screen = Builder.load_file(self.available_screens[name])
        # build corresponding screen
        if screen.name == 'classrooms':
            screen_builded = self.build_left(screen) 
        elif screen.name == 'weekschedules':
            screen_builded = self.build_right(screen)
        else:
            screen_builded = screen
        # save loaded screen object
        self.screens[name] = screen_builded
        # return to show
        return screen_builded
    
    def build_left(self, screen):
        """
        Build left screen: A list of college classrooms to make a weekly classroom screen.
        """  
        screen_builded = screen      
        for classroom_name in self.classroom_names:
            screen_builded.ids['content'].add_widget(Button(text=classroom_name, on_release=self.build_classroom_screen))
        return screen_builded

    def build_right(self, screen):
        """
        Build right screen: A weekly college screen.
        """
        screen_builded = self.build_week_grid('WeekSchedules', screen, is_college=True)
        return screen_builded

    def build_week_grid(self, name, screen, is_classroom=False, is_college=False):
        """
        Description:
        Get a Screen object and add Labels and Buttons for a week schedule view, 
        based in the list o schedules and the activity days.
        
        Args:
            screen: Kivy object which contains GridLayout with id=content. content will 
                    contain #(activity_days)+1 columns and #(activity_schedules)+1 rows
            is_classroom: Indicate if var screen comes from a weekly classroom screen view.
            is_college: Indicate if var screen comes from a weekly college screen view.
        """
        # first row in gridlayout (labels only: the column names)
        screen.ids['content'].add_widget(Label(text='Schedule'))
        for activity_day in self.activity_days:
            screen.ids['content'].add_widget(Label(text=activity_day))
        # add each row to gridlayout: first schedule and then buttons
        for activity_schedule in self.activity_schedules:
            screen.ids['content'].add_widget(Label(text=activity_schedule))
            for activity_day in self.activity_days:
                if is_college:
                    screen.ids['content'].add_widget(ScheduleButton(college=self.college, activity_day=activity_day, activity_schedule=activity_schedule))
                if is_classroom:
                    screen.ids['content'].add_widget(ClassroomScheduleButton(classroom_day_schedule=self.college[name][activity_day][activity_schedule]))    
        # return builded screen, ready to show
        return screen

    def load_classroom(self, name):
        """
        Description:
        Load one of the principal screens: 
            
            Main Screen, 
            Classrooms Screen, 
            Week Schedules Screen.
        
        Args:
            name (string): Options {'MainScreen', 'WeekSchedules', 'Classrooms'}

        Returns:
            builded_screen (Screen Kivy object):  Screen to show in app window
        """
        
        if name in self.classrooms:
            return self.classrooms[name]

        classroom = Builder.load_file(self.classroom_screen_file)
        classroom.name = name.lower()
        
        classroom_builded = self.build_week_grid(name, classroom, is_classroom=True)
    
        self.classrooms[name] = classroom_builded
        
        return classroom_builded

    def build_classroom_screen(self, classroom_button):
        """
        If classroom button was pressed on classrooms menu screen, then
        build weekly classroom screen and switch app screen to it. 
        
        A weekly schedule screen for the selected classroom.  
        """
        classroom_name = classroom_button.text

        self.root.switch_to(self.load_classroom(classroom_name), direction='up')
    
    def on_stop(self):
        # save data when app stops
        with open('data/data.json', 'w') as fd:
            dump(self.college, fd, indent=2)