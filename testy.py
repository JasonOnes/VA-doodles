# from time_frame import time_frame, time_frame_rough
#
# freq = time_frame(time_frame_rough)
# print(freq * 2)
# class Holding:
#     """ creating a class for the different funds"""
#     def __init__(self, name, family, allocation, current_value=0):
#         self.name = name
#         self.family = family
#         self.allocation = allocation
#         self.current_value = current_value
#
#     def __repr___(self):
#         pass
#
#     def __str__(self):
#         return "{} is a holding that should be {}% of the portfolio".format(self.name, self.allocation*100)
#
#
# VTSMX = Holding("VTSMX", "Stocks", .50, 3000)
# type(VTSMX)
# print(VTSMX)
# from datetime import timedelta
#
# retirement = 2/23/2023
# d = timedelta(retirement)
#
# #print(d)
#
# import time
# import datetime
# from dateutil.rrule import rrule, MONTHLY
#
# def years_left(retirement_date_year, month, day):#format (year, month, day)
#     #retunrs time left in months for help in calculating rate of return needed
#     today = datetime.datetime.now()
#     retirement = datetime.date(retirement_date_year, month, day)#might suggest retirement calculator
#     #interval = time_frame_rough# THis might work with tweaking of input
#     time_till_target = [date for date in rrule(MONTHLY, dtstart=today, until=retirement)]
#     months_left = len(time_till_target) - 1
#     years_left = months_left // 12 #floor division least amount of time in years
#
#     print(today)
#     print(time_till_target[0])
#     print(time_till_target[-1])
#
#     print(months_left)
#     print(years_left)
#
# years_left(2040, 12, 31)
class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, asset_allocation, num_of_holdings, total_value):
        self.owner = name
        self.asset_allocation = asset_allocation
        self.num_of_holdings = num_of_holdings
        self.total = total_value
    def total_value():
        """total of all the holdings"""

class Holding(object):
    """ creating a class for the different funds"""
    def __init__(self, name, family, allocation, num_shares):
        self.name = name
        self.family = family
        self.allocation = allocation
        self.num_shares = num_shares

    def __repr___(self):
        return ""

    def __str__(self):
        return "{} is a {} holding constituting {}% of porfolio".format(self.name,
                self.family, self.allocation * 100)

    def current_value(self):
        c_v = get value from web 
        self.num_shares * c_v
    def __add__(self, other_holdings):
        return self.current_value + other_holdings.value

    def __radd__(self, total):
        return self.current_value + total

class StockFund(Holding):
    def __init__(self, name, stock_type, cap_size, allocation):
        self.name = name
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.family = 'Stock Fund'
        self.allocation = allocation

    pass

class BondFund(Holding):
    def __init__(self, name, bond_type, term_length):
        self.name = name
        self.bond_type = bond_type
        self.term_length = term_length
        self.family = 'Bond Fund'

    pass

VTSMX = StockFund('VTSMX', 'Domestic', 'total_market', 0.50)
VWAHX = BondFund('VWAHX', 'Municipal', 'mid-term')
# VWAHX.family = "Bonds"
VWAHX.allocation = 0.20

VGPMX = Holding('VGPMX', 'Commodities', 0.15, 4500)
print(VGPMX)
print(VWAHX)
print(VTSMX)
VWAHX
