from json import dump

def get_classroom_ids():
    """
    Classroom id is a non-space squence of characteres.

        ~/scheduler/data/classroom_ids.txt
    
    This file contains several lines. One line per each classroom name.
    """
    with open('data/classroom_ids.txt') as data:
        lines = data.readlines()

        classroom_ids = []
        for line in lines:
            classroom_ids.append(line[:-1])
        
        return classroom_ids

def get_activity_days():
    """
    Activity day is a non-space squence of characteres: a name of a day of week.

        ~/scheduler/data/acivity_days.txt
    
    This file contains several lines. One line per each activity day.
    """
    with open('data/activity_days.txt') as data:
        lines = data.readlines()

        activity_days = []
        for line in lines:
            activity_days.append(line[:-1])
        
        return activity_days

def get_activity_schedules():
    """
    Activity Schedule consist of a '-'-separated strings with "%02d:%02d-%02d:%02d" format: Activity Start Time and End Time

        ~/scheduler/data/activity_schedules.txt
    
    This file contains several lines. One line per each schedule option.
    """
    with open('data/activity_schedules.txt') as data:
        lines = data.readlines()

        activity_schedules = []
        for line in lines:
            activity_schedules.append(line[:-1])
        
        return activity_schedules

def build_college():

    activity_day_schedules = get_activity_schedules()
    classroom_activity_days = get_activity_days()
    classroom_names = get_classroom_ids()
    
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
    with open('data/data.json', 'w') as fd:
        dump(college, fd, indent=2)