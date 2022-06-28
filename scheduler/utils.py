def get_classroom_ids():
    """
    Classroom id is a non-space squence of characteres.

        ~/scheduler/data/classroom_ids.txt
    
    This file has only one line. A list of space-separated classroom ids.
    """
    with open('../data/classroom_ids.txt') as data:
        classroom_ids = data.readline().split()
        
        print('\nclassroom_ids:\n')
        
        for classroom_id in classroom_ids:
            print(classroom_id)
        print()
        
        return classroom_ids

def get_activity_days():
    """
    Activity day is a non-space squence of characteres: a name of a day of week.

        ~/scheduler/data/acivity_days.txt
    
    This file has only one line. A list of space-separated activity days.
    """
    with open('../data/activity_days.txt') as data:
        activity_days = data.readline().split()
        
        print('\nactivity_days:\n')
        
        for activity_day in activity_days:
            print(activity_day)
        print()
        
        return activity_days

def get_schedule_options():
    """
    Schedule Option consist of two space-separated strings with "%02d:%02d" format: Activity Start Time and End Time

        ~/scheduler/data/schedule_options.txt
    
    This file contains several lines. One line per each schedule option.
    """
    with open('../data/schedule_options.txt') as data:
        lines = data.readlines()

        print('\nschedule_options:\n')

        schedule_options = []
        for line in lines:
            start_time, end_time = line.split()
            print(start_time, end_time)
            schedule_options.append((start_time, end_time))
        print()

        return schedule_options