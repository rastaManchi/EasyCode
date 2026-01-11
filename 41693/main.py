import datetime


print(datetime.date.today())
print(datetime.datetime.now().time())
print(datetime.datetime.now().minute)

time_object = datetime.time(12, 00, 00)
datetime_object = datetime.datetime(2026, 1, 11, 12, 00)
print(datetime_object - datetime.timedelta(seconds=6000000))