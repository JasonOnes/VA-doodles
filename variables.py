""" modules for the various variables in val_basic"""
import datetime


time_frame_rough = input("""How often would you like to invest? Daily, monthly,
                          quarterly, biannually, yearly: """)


def time_frame(time_frame_rough):
    """ convert scheduled investment periods into integers for formulae"""
    time_table = {"Daily": 365, "monthly": 12, "quarterly": 4, "biannually": 2,
                  "yearly": 1}
    if time_frame_rough in time_table:
        frequency = time_table[time_frame_rough]
    else:
        print("Sorry, not an option")
        frequency = None
    print(frequency)
    return frequency

# time_frame(time_frame_rough)
"""
Need:
utv = Ultimate target value
utv_date = Ultimate target value date, online reitirement calculator
#time_left = utv_date - today(datetime.date)
return_percentage_needed = incremental_investment_amt * increment * time_left
real_return = return_percentage_needed + inflation
asset allocation => dict of dicts {"Stocks" : {'Domestic': 0.40,
                                               'Foreign': 0.20}}
# frequency of investments
"""

import time
import datetime
from dateutil.rrule import rrule, MONTHLY


def years_left(retirement_date_year, month, day):  # format (year, month, day)
    # retunrs time left in months for help in calculating rate of return needed
    today = datetime.datetime.now()
    retirement = datetime.date(retirement_date_year, month, day)  # might
    # suggest retirement calculator
    # i nterval = time_frame_rough# THis might work with tweaking of input
    time_till_target = [date for date in rrule(MONTHLY, dtstart=today,
                                               until=retirement)]
    months_left = len(time_till_target) - 1
    years_left = months_left // 12
    # floor division least amount of time in years
    print(years_left)
    return years_left
