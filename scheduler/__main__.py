"""

Usage (On proect folder):

python -m scheduler

"""
from scheduler.utils import build_college
from scheduler.app import SchedulerApp
from kivy.core.window import Window

if __name__ == '__main__':
    #build_college()
    # maximize screen app
    Window.maximize()
    # build and run app
    SchedulerApp().run()