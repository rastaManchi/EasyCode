import datetime


print(datetime.datetime.now().time())
print(datetime.date.today())

birthday = datetime.datetime(2001, 12, 29, 2, 45)
timedelta = datetime.timedelta(weeks=3)
print(birthday + timedelta)