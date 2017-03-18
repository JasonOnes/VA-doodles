"""Classes module for Value valuations """


class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, asset_allocation, num_of_holdings, total_value):
        self.owner = name
        self.asset_allocation = asset_allocation
        self.num_of_holdings = num_of_holdings
        self.total = total_value
    def total_value():
        """total of all the holdings"""

    def rebalance():
        """ compare values of holdings to asset allocation make adjustments"""


class Holding(object):
    """ creating a class for the different funds"""
    def __init__(self, name, family, allocation=0, num_shares=0):
        self.name = name
        self.family = family
        self.allocation = allocation
        self.num_shares = num_shares


    def __repr___(self):
        pass

    def __str__(self):
        return "{} is a {} holding constituting {}% of porfolio".format(self.name,
                self.family, self.allocation * 100)

    def __add__(self, other_holdings):
        return self.current_value + other_holdings.value

    def __radd__(self, total):
        return self.current_value + total

        """
            def current_value(self):
                c_v = get value from web
                return self.num_shares * c_v

            def target_value(self):
                return previous_value * percent_increase + installment

        """

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
