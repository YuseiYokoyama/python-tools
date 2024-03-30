import datetime

now = datetime.datetime.now()
now.isoformat() # 2023-04-01T05:00:30.001000

d = datetime.date.fromisoformat("2023-04-01")
t = datetime.time.fromisoformat('05:00:30.001000')
dt = datetime.datetime.fromisoformat('2023-04-01T05:00:30.001000')

print(datetime.datetime(2023, 4, 1, 20, 15, 30, 2000)) # 2023-04-01 20:15:30.002000

s = "2022-03-07 15:10:21 +0900"
l = s.split(" ")
dt = datetime.datetime.fromisoformat(l[0] + " " + l[1])

# weeks, days, hours, minutes, seconds, milliseconds, microseconds
delta = datetime.timedelta(hours=3)

