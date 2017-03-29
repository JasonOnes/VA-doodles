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
# class Portfolio(object):
#     """ class for the total of all holdings for individual"""
#     def __init__(self, owner, asset_allocation, num_of_holdings, total_value):
#         self.owner = name
#         self.asset_allocation = asset_allocation
#         self.num_of_holdings = num_of_holdings
#         self.total = total_value
#     def total_value():
#         """total of all the holdings"""
#
# class Holding(object):
#     """ creating a class for the different funds"""
#     def __init__(self, name, family, allocation, num_shares):
#         self.name = name
#         self.family = family
#         self.allocation = allocation
#         self.num_shares = num_shares
#
#     def __repr___(self):
#         return ""
#
#     def __str__(self):
#         return "{} is a {} holding constituting {}% of porfolio".format(self.name,
#                 self.family, self.allocation * 100)
#
#
#     def current_value(self):
#         c_v = get value from web
#         return self.num_shares * c_v
#
#     def target_value(self):
#         return previous_value * percent_increase + installment
#
#     def __add__(self, other_holdings):
#         return self.current_value + other_holdings.value
#
#     def __radd__(self, total):
#         return self.current_value + total
#
# class StockFund(Holding):
#     def __init__(self, name, stock_type, cap_size, allocation):
#         self.name = name
#         self.stock_type = stock_type
#         self.cap_size = cap_size
#         self.family = 'Stock Fund'
#         self.allocation = allocation
#
#     pass
#
# class BondFund(Holding):
#     def __init__(self, name, bond_type, term_length):
#         self.name = name
#         self.bond_type = bond_type
#         self.term_length = term_length
#         self.family = 'Bond Fund'
#
#     pass
#
# VTSMX = StockFund('VTSMX', 'Domestic', 'total_market', 0.50)
# VWAHX = BondFund('VWAHX', 'Municipal', 'mid-term')
# # VWAHX.family = "Bonds"
# VWAHX.allocation = 0.20
#
# VGPMX = Holding('VGPMX', 'Commodities', 0.15, 4500)
# print(VGPMX)
# print(VWAHX)
# print(VTSMX)
# VWAHX

from flask import Flask, render_template, request

# test = Flask(__name__)
#
# @test.route('/test')
# def testing():
#     print("Testing 1 2 3")
#     return 'Testing'
# test.run(debug=True)
#
# val = Flask(__name__)
#
# @val.route('/val_in')
# def first_page():
#     return render_template('sign_in.html',
#                             the_title='Patient Investing to You!')
# #----->>> goes to /submit
# @val.route('/submit', methods=['POST'])
# def second_page():
#     return render_template('submission.html')
#
# @val.route('/invest', method=['POST'])
# """ this should post to database"""
# """ and show results page"""
#
# @val.route('/invest', methods=['POST'])
# def invest_this():
#     fund = request.form['name']
#     current_holding_value = request.form['previous_value']
#     target_value = current_holding_value * percent_increase + installment
#     #percent_increase and installment get request from initial setup page?
#     #other form request or seperate request function
#     to_invest = what_to_do(fund, current_holding_value, target_value)
#     log_request(requests, to_invest)
#     return render_template('results.html',
#                             the_fund = fund,
#                             the_prev_value = current_holding_value,
#                             to_do = to_invest)
#
# val.run(debug=True)




class Holding(object):
    """ creating a class for the different funds"""
    def __init__(self, name, family, total_allocation=0, num_shares=0, value=0):
        self.name = name
        self.family = family
        self.total_allocation = total_allocation
        self.num_shares = num_shares
        self.previous_value = value

    def __repr___(self):
        return "{} should be {}% of portfolio".format(self.name,
                                                      self.portfolio_allocation)

    def __str__(self):
        return "{} is a {} holding constituting {}% of portfolio".format(
            self.name, self.family, self.total_allocation() * 100)


class StockFund(Holding):
    def __init__(self, stock_type, cap_size, stock_allocation,
                 portfolio_allocation=0.8):
        # self.name = name inherits name from Holding
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.family = 'Stock Fund'
        self.stock_allocation = stock_allocation
        self.portfolio_allocation = portfolio_allocation


    def total_allocation(self):
        self.allocation = self.stock_allocation * self.portfolio_allocation
        return self.allocation


class BondFund(Holding):
    def __init__(self, bond_type, term_length, bond_allocation,
                 portfolio_allocation=0.2):
        # self.name = name inherits name from holding
        self.bond_type = bond_type
        self.term_length = term_length
        self.family = 'Bond Fund'
        self.bond_allocation = bond_allocation
        self.portfolio_allocation = portfolio_allocation

    def total_allocation(self):
        self.allocation = self.bond_allocation * self.portfolio_allocation
        return self.allocation


class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, num_of_holdings, holdings=list(), taxable=True,
                 stock_allocation=0.80, bond_allocation=0.20):
        self.owner = owner
        self.asset_allocation = stock_allocation + bond_allocation
        self.num_of_holdings = len(holdings)
        self.taxable = taxable
        self.stock_allocation = stock_allocation
        self.bond_allocation = bond_allocation
        self.holdings = holdings

    def __str__(self):
        return """Portfilio-no-you-didn't {}'s portfolio currently contains {}
                  holdings {}""".format(self.owner,
                                        self.num_of_holdings, self.holdings)

    def __repr__(self):
        return "{} portfolio has {} holdings".format(self.owner,
                                                     self.num_of_holdings)

        # self.total = total_value
    def total_value():
        """total of all the holdings"""
        if len(list(Holdings)) == self.num_of_holdings:
            sum(list(Holdings.value))

    def asset_allocation():

        # something like this though out of scope
        """ weight of each family such that total == 100 """
        k = list()
        for hold in (holding_1, holding_2, hold_2B):
            hold.total_allocation()
            k.append(hold.total_allocation())
            print(k)
            print(sum(k))
        all_totes = sum(k)
        if all_totes == 100:
            return True
        elif all_totes < 100:
            print("You need allocate {}% more to one of your holdings. "
                  .format(100-all_totes))
        elif all_totes > 100:
            print("You're askew, can't give more than a hundred percent.")
        else:
            print("?")


if __name__ == '__main__':

    holding_1 = StockFund('Domestic', 'Total', 0.7)
    holding_1.name = 'VTSMX'
    holding_2 = StockFund('Foreign', 'Total', 0.3)
    holding_2.name = 'VGSTX'
    x = Portfolio('Jason', 33, ['VTSMX', 'VGSTX'])
    print(holding_1)
    print(holding_1.total_allocation())
    print(x)
    print(x.asset_allocation())
