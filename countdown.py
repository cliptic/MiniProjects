''' 
This is a countdown page for a specfic date. 
Originally created to see the time left until my AI course starts.
'''

from datetime import datetime, date, time, timedelta

dt = datetime.now()  
start_date = datetime(2019, 11, 9, 14, 0, 0)

# print((dt - start_date).days())
tot_secs = round((start_date - dt).total_seconds())

days = tot_secs // (3600*24) 
hours = tot_secs%(3600*24) // 3600
minutes = tot_secs%3600 // 60
seconds = tot_secs%60
# print(days, 'days')
# print(hours, 'hours')
# print(minutes, 'minutes')
# print(seconds, 'seconds')
# print('left')

print(days, 'd', hours, 'h', minutes, 'min', seconds, 's left until the start of the course')




