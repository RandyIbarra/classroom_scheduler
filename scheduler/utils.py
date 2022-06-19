def get_activity_days():
    """
    Activity day is a squence of characteres (Important) non-space: a name of a day of week.

        ~/scheduler/data/acivity_days.txt
    
    This file has only one line. A list of space-separatted activity days.
    """
    with open('data/activity_days.txt') as data:
        activity_days = data.readline().split()
        
        print('\nactivity_days:\n')
        
        for activity_day in activity_days:
            print(activity_day)
        return activity_days

def get_classroom_ids():
    """
    Classroom id is a squence of characteres (Important) non-space.

        ~/scheduler/data/classroom_ids.txt
    
    This file has only one line. A list of space-separatted classroom ids.
    """
    with open('data/classroom_ids.txt') as data:
        classroom_ids = data.readline().split()
        
        print('\nclassroom_ids:\n')
        
        for classroom_id in classroom_ids:
            print(classroom_id)
        return classroom_ids

def get_schedule_options():
    with open('data/schedule_options.txt') as data:
        lines = data.readlines()

        print('\nschedule_options:\n')

        schedule_options = []
        for line in lines:
            start_time, end_time = line.split()
            print(start_time, end_time)
            schedule_options.append((start_time, end_time))
        return schedule_options