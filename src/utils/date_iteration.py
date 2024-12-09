import datetime
import calendar

def iteration(year, month):
    number = calendar.monthrange(year, month)[1]
    for day in range(1,number+1):
        yield datetime.date(year, month, day)