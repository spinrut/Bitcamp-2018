import csv
import numpy as np
import datetime as dt

def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def is_school_day(day):
    date_obj = dt.datetime.strptime(day, '%Y-%m-%d')
    if date_obj.month == 12 and date_obj.day >= 22:
        return False
    if date_obj.month == 1 and date_obj.day == 1:
        return False
    if date_obj.weekday() > 4:
        return False
    if day in scheduled_closings:
        return False
    return True

close_days = []
delay_days = []
scheduled_closings = []
file_names_1 = ['closed_', 'delay_']
file_names_2 = ['BaltCoPS', 'MCPS', 'PGCPS']

for f2 in file_names_2:
    with open('Data_Files/scheduled_closings_' + f2 + '.csv', 'r') as f:
        scheduled_closings.extend(f.readlines())

cols = np.genfromtxt('data/data.csv', dtype=None, delimiter=',', usecols = (5, 26, 27, 40), encoding = None)
cols = np.delete(cols, 0, axis=0)

i = 0

while i < cols.shape[0]:
    if str(cols[i, 0])[-5:] != '23:59' or not is_school_day(str(cols[i, 0])[0:10]):
        cols = np.delete(cols, i, axis=0)
    else:
        if not is_float(cols[i, 3]):
            cols[i, 3] = '0'
        i += 1
        if i % 100 == 0:
            print(i)

print('Done deleting')

for f in file_names_2:
    with open('data/' + file_names_1[0] + f + '.csv', 'r') as fin:
        close_days.extend(fin.readlines())
    with open('data/' + file_names_1[1] + f + '.csv', 'r') as fin:
        delay_days.extend(fin.readlines())

cols = np.hstack((cols, np.zeros((cols.shape[0], 2))))

for i in range(cols.shape[0]):
    for day in close_days:
        if (cols[i, 0])[0:10] == day[0:10]:
            cols[i, -2] = 1
    for day in delay_days:
        if (cols[i, 0])[0:10] == day[0:10]:
            cols[i, -1] = 1

cols = np.delete(cols, 0, axis=1)
cols = np.delete(cols, -1, axis=0)
cols = cols.astype(np.float32)

with open('data/processed.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerows(cols)

print('Done')
