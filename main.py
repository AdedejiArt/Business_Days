from datetime import datetime, timedelta
import datetime


def date_by_adding_business_days(from_date, add_days):

    while add_days > 0:
        from_date += datetime.timedelta(days=1)
        print (from_date)
        weekday = from_date.weekday()
        print(weekday)
        if weekday >= 5: #saturday = 5 & sunday = 6
            continue
        add_days -= 1
        print(add_days)
    return from_date

print (date_by_adding_business_days (datetime.datetime.now(), 7))
