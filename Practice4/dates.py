#Subtract five days from current date
from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print(five_days_ago)

#Print yesterday, today, tomorrow
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#Drop microseconds from datetime
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print(no_microseconds)

#Calculate difference between two dates in seconds
from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)

difference = date2 - date1

print(difference.total_seconds())



