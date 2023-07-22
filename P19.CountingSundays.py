from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def counting_sundays(start, end):
    start_day = datetime.strptime(start, '%Y-%m-%d')
    end_day = datetime.strptime(end, '%Y-%m-%d')

    number_of_sundays = 0
    myday = start_day
    while myday < end_day:
        if myday.weekday() == 6:
            number_of_sundays += 1
            print(myday.strftime('%Y-%m-%d'))
        myday = myday + relativedelta(months=+1)

    return number_of_sundays


print(counting_sundays('1901-01-01', '2000-12-31'))
