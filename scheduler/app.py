from kivy.app import App as KivyApp

from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from scheduler.college import College
from scheduler.activity import Activity

DEMAT_SCHEDULE_OPTIONS = [
    # morning classes
    (' 8:00', ' 9:20'),
    (' 9:30', '10:50'),
    ('11:00', '12:20'),
    ('12:30', '13:50'),
    #
    # lunch time
    #
    # evening classes
    ('15:00', '16:20'),
    ('16:30', '17:50')
]

WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

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

class ActivityList(GridLayout):

    updated_activities = ListProperty()

    text_input = StringProperty()

    start_time = StringProperty()
    end_time = StringProperty()
    day = StringProperty()

    college = ObjectProperty()
    index = NumericProperty()

    def __init__(self, **kwargs):
        super(ActivityList, self).__init__(**kwargs)

        self.updated_activities = []

        self.start_time =  kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.day = kwargs['day']

        self.college = kwargs['college']
        self.index = kwargs['index']

        self.cols = 2

        n_activities = 0
        for id, classroom in self.college.get_classrooms().items():
            
            self.add_widget(Label(text=id))

            for activity_day in classroom.get_activity_days():
                if activity_day == self.day:
                    for activity in classroom.get_day_schedule(activity_day).get_schedule():
                        (start_time, end_time) = activity.get_schedule()
                        if self.start_time == start_time and self.end_time == end_time:
                            textinput = UpdateActivity(
                                classroom_id=id,
                                start_time=start_time,
                                end_time=end_time,
                                day=activity_day,
                                # extra params
                                text=activity.get_activity_name(), 
                                multiline=False
                            )
                            textinput.bind(on_text_validate=self.on_enter)
                            self.add_widget(textinput)

    def on_enter(self, value):
        self.updated_activities.append(Activity(activity_name=value.text,
                                                classroom_id=value.classroom_id,
                                                activity_day=value.day,
                                                start_time=value.start_time,
                                                end_time=value.end_time))

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

class WeeklySchedule(GridLayout):

    college = ObjectProperty()

    def __init__(self, **kwargs):
        super(WeeklySchedule, self).__init__(**kwargs)
        
        self.college = kwargs['college']
        self.college.info()

        self.class_days = WEEKDAYS
        self.cols = len(self.class_days) + 1

        # adding columnames: first one for sctivities schedule and later one per weekday
        self.add_widget(Label(text='Schedule'))
        for class_day in self.class_days:
            self.add_widget(Label(text=class_day))

        self.schedule_options = DEMAT_SCHEDULE_OPTIONS
        for activity_schedule_index, (start_time, end_time) in enumerate(self.schedule_options): 

            self.add_widget(Label(text='{} \n{}'.format(start_time, end_time)))
            
            for class_day in self.class_days:
                
                layout = BoxLayout(padding=2)
                button = ScheduleButton(start_time=start_time,
                                        end_time=end_time,
                                        day=class_day,
                                        college=self.college,
                                        index=activity_schedule_index,
                                        # extra params
                                        on_release=self.on_release, 
                                        text='{}'.format(0)) # numero de clases, salones disponibles
                layout.add_widget(button)
                
                self.add_widget(layout)
    
    def on_dismiss(self, arg):
        
        day = ''
        (start_time, end_time) = ('','')
        for activity in self.popup.content.updated_activities:
            id = activity.get_classroom_id()
            day = activity.get_activity_day()
            name = activity.get_activity_name()
            index = self.popup.content.index
            (start_time, end_time) = activity.get_schedule()
            
            self.college.update_classroom_day_s_activity_schedule(
                classroom_id=id, 
                activity_day=day, 
                activity_schedule_index=index, 
                activity_name=name
            )
            

        print('{} - {}-{}'.format(day, start_time, end_time))                            

    def on_release(self, event):
        print('schedule clicked at \n\t{} - ({},{})'.format(event.day, event.start_time, event.end_time))
        event.background_color = 1,0,0,1
        self.popup = Popup(
            title= event.day,
            content = ActivityList(
                start_time=event.start_time, 
                end_time=event.end_time,
                day=event.day,
                index=event.index,
                college=event.college
            ),
            size_hint=(None, None), 
            size=(self.width*3/4, self.height)
        )
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open() 
        event.background_color = 1,1,1,1

class App(KivyApp):

    def build(self):

        self.title = 'Scheduler'

        classroom_ids = [
            'A - 101', 'B - 201', 'C - 301'
        ]
        print(classroom_ids)

        self.college = College(
            classroom_ids=classroom_ids,
            activity_days=WEEKDAYS,
            schedule_options=DEMAT_SCHEDULE_OPTIONS
        )
        
        self.weekly_schedule = WeeklySchedule(college=self.college)

        return self.weekly_schedule