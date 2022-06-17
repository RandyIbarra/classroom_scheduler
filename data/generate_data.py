import pandas

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

WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday']

CLASSROOM_IDS = [
    'Seminarios DEMAT', 
    'Astrofisica', 
    'DEMAT 3', 
    'DEMAT 4', 
    'DEMAT 5', 
    'DEMAT 6', 
    'DEMAT 7', 
    'DEMAT 8'
]

data_id = []
data_weekday = []
data_end_time = []
data_start_time = []
data_activity_name = []
print(len(CLASSROOM_IDS)*len(WEEKDAYS)*len(DEMAT_SCHEDULE_OPTIONS))
for id in CLASSROOM_IDS:
    for weekday in WEEKDAYS:
        for (start_time, end_time) in DEMAT_SCHEDULE_OPTIONS:
            data_id.append(id)
            data_weekday.append(weekday)
            data_end_time.append(end_time)
            data_start_time.append(start_time)
            data_activity_name.append('No Assigned')

data = {
    'classroom_id': data_id, 
    'activity_day': data_weekday, 
    'start_time': data_start_time,
    'end_time': data_end_time,
    'activity_name': data_activity_name
}
df = pandas.DataFrame(data=data)
df.to_csv('data.csv', index=False)

print(df.size)

d = pandas.read_csv('data.csv')

print(d.size)
