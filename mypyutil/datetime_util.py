import datetime
from dateutil.relativedelta import relativedelta

def cheetsheet():
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

def using_dateutil_next_month(date):
    rd = relativedelta(months=+1)
    for i in range(12):
        date += rd
        print('date') # debug
        print(date) # debug

# d: Date, day: int
def get_day_of_next_month(d, day):
    if d.month == 12:
        target_date = d.replace(d.year + 1, 1)
    else:
        target_date = d.replace(month=d.month + 1)
    return target_date

def get_week_start(date):
    days_to_monday = date.weekday()
    monday = date - datetime.timedelta(days=days_to_monday)
    return monday

def get_next_day_8am(dt):
    """与えられたdatetimeオブジェクトの次の朝8時のdatetimeオブジェクトを返す"""
    next_day_8am = dt.replace(hour=8, minute=0, second=0, microsecond=0)
    if next_day_8am <= dt:
        next_day_8am += datetime.timedelta(days=1)
    return next_day_8am

def get_next_monty_day(d, day):
    rd = relativedelta(months=+1, day=day)
    return d + rd

