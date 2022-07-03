def get_classroom_ids():
    """
    Classroom id is a non-space squence of characteres.

        ~/scheduler/data/classroom_ids.txt
    
    This file has only one line. A list of space-separated classroom ids.
    """
    with open('data/classroom_ids.txt') as data:
        classroom_ids = data.readline().split()
        return classroom_ids

def get_activity_days():
    """
    Activity day is a non-space squence of characteres: a name of a day of week.

        ~/scheduler/data/acivity_days.txt
    
    This file has only one line. A list of space-separated activity days.
    """
    with open('data/activity_days.txt') as data:
        activity_days = data.readline().split()
        return activity_days

def get_activity_schedules():
    """
    Schedule Option consist of two space-separated strings with "%02d:%02d" format: Activity Start Time and End Time

        ~/scheduler/data/activity_schedules.txt
    
    This file contains several lines. One line per each schedule option.
    """
    with open('data/activity_schedules.txt') as data:
        lines = data.readlines()

        activity_schedules = []
        for line in lines:
            start_time, end_time = line.split()
            activity_schedules.append((start_time, end_time))
        
        return activity_schedules