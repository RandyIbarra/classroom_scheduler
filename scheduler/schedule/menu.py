from kivy.uix.screenmanager import Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def on_button_press(button):
    print(button.text)
    button.parent.parent.parent.parent.current = 'Week'

class SchedulerMenu(Screen):

    def __init__(self, **kwargs):
        super(SchedulerMenu, self).__init__(**kwargs)

        grid_menu = GridLayout()

        layout_left = BoxLayout(orientation='vertical')
        button_left = Button(text='College Schedule', size=(200, 100), size_hint=(None, None), on_press = on_button_press)
        layout_left.add_widget(button_left)
        
        grid_menu.add_widget(layout_left)

        layout_right = BoxLayout(orientation='vertical')
        button_right = Button(text='Classroom Schedule', size=(200, 100), size_hint=(None, None), on_press = on_button_press)
        layout_right.add_widget(button_right)

        grid_menu.add_widget(layout_right)

        grid_menu.cols = 2

        self.add_widget(grid_menu)
