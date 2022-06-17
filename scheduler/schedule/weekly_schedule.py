from kivy.properties import ObjectProperty

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from scheduler.college import College
from scheduler.activity import Activity

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