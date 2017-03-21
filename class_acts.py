"""Classes module for Value valuations """


class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, num_of_holdings):
        self.owner = owner
        # self.asset_allocation = asset_allocation
        self.num_of_holdings = num_of_holdings
    def __str__(self):
        return "Portfilio-no-you-didn't {}'s portfolio currently contains {} holdings".format(self.owner, self.num_of_holdings)
    def __repr__(self):
        return "{} portfolio has {} holdings".format(self.owner,
                self.num_of_holdings)

        # self.total = total_value
    def total_value():
        """total of all the holdings"""
        if len(list(Holdings)) == self.num_of_holdings:
           sum(list(Holdings.value))
    def asset_allocation():
        """ weight of each family such that total == 100 """
        all_totes = sum(list(Holding.allocation))
        if all_totes == 100:
            return True
        elif all_totes < 100:
            print("You need allocate {}% more to one of your holdings. "
                  .format(100-all_totes))
        elif all_totes > 100:
            print("You're askew, can't give more than a hundred percent.")
        else:
            print("?")


    def rebalance():
        """ compare values of holdings to asset allocation make adjustments"""


class Holding(object):
    """ creating a class for the different funds"""
    def __init__(self, name, family, allocation=0, num_shares=0, value=0):
        self.name = name
        self.family = family
        self.allocation = allocation
        self.num_shares = num_shares
        self.previous_value = value


    def __repr___(self):
        return "{} should be {}% of portfolio".format(self.name, self.allocation)

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
    def __init__(self, name, stock_type, cap_size, stock_allocation):
        self.name = name
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.family = 'Stock Fund'
        self.allocation = allocation

    pass

class BondFund(Holding):
    def __init__(self, name, bond_type, term_length, bond_allocation):
        self.name = name
        self.bond_type = bond_type
        self.term_length = term_length
        self.family = 'Bond Fund'

    pass

if __name__ == '__main__':
    z = Portfolio("Jason", 3)

    print(z)
