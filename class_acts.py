"""Classes module for Value valuations """
"""++++Need to include some delimiters on allocations such that their sum is 1.0+++"""
# k = list()
# for hold in (holding_1, holding_2, hold_2B):
#     hold.total_allocation()
#     k.append(hold.total_allocation())
#     if sum(k) != 1.0:
#         print("Need more/less holdings or readjust allocations")
#     print(k)
#     print(sum(k))

class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, num_of_holdings, stock_allocation=0.80, bond_allocation=0.20):
        self.owner = owner
        self.asset_allocation = stock_allocation + bond_allocation
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

        # something like this though out of scope
        # k = list()
        # for hold in (holding_1, holding_2, hold_2B):
        #     hold.total_allocation()
        #     k.append(hold.total_allocation())
        #     print(k)
        #     print(sum(k))
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
        for holding in portfolio:
            if holding_name.value // portfolio.total_value() < holding_name.total_allocation:
                return buy()
            elif holding_name.value // porfolio.total_value() > holding_name.total_allocation:
                return sell()
            else:
                print("all good")
                pass



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

    # def __add__(self, other_holdings):
    #     return self.current_value + other_holdings.value
    #
    # def __radd__(self, total):
    #     return self.current_value + total

        """
            def current_value(self):
                c_v = get value from web
                return self.num_shares * c_v

            def target_value(self):
                return previous_value * percent_increase + installment

        """

class StockFund(Holding):
    def __init__(self, stock_type, cap_size, stock_allocation, portfolio_allocation=0.8):
        #self.name = name inherits name from Holding
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.family = 'Stock Fund'
        self.stock_allocation = stock_allocation
        self.portfolio_allocation = portfolio_allocation
    # def total_allocation(self, stock_allocation):
    #     total_allocation = self.allocation * self.stock_allocation
    #     return total_allocation
    def total_allocation(self):
        self.allocation = self.stock_allocation * self.portfolio_allocation
        return self.allocation

    pass

class BondFund(Holding):
    def __init__(self, bond_type, term_length, bond_allocation, portfolio_allocation=0.2):
        #self.name = name inherits name from holding
        self.bond_type = bond_type
        self.term_length = term_length
        self.family = 'Bond Fund'
        self.bond_allocation = bond_allocation
        self.portfolio_allocation = portfolio_allocation
    # def total_allocation(self, bond_allocation):
    #     total_allocation = self.allocation * self.bond_allocation
    #     return total_allocation
    def total_allocation(self):
        self.allocation = self.bond_allocation * self.portfolio_allocation
        return self.allocation
    """ updates allocation of holding to portfolio """


    pass

if __name__ == '__main__':
    z = Portfolio("Jason", 3)
    holding_2 = BondFund('Municipal', 'Intermediate', 1.0)
    holding_2.name = 'VWAHX'
    holding_2.allocation = 0.20
    holding_1 = StockFund('Domestic', 'Total', 0.30)
    holding_1.name = 'VTSMX'
    holding_1.allocation = 0.50
    hold_2B = BondFund('Corporate', 'Long-Term', 0.3)
    hold_2B.name = 'VHAMBONE'
    hold_2B.allocation = 0.20
    print(z)
    print(z.asset_allocation)
    print(holding_2)
    print(holding_1)
    # print(holding_2.total_allocation(holding_2.bond_allocation))
    # print(holding_1.total_allocation(holding_1.stock_allocation))
    print(holding_1.total_allocation())
    holding_1.total_allocation()
    print(holding_1)
    print(holding_2.total_allocation())
    print(hold_2B)
    print(hold_2B.total_allocation())
    hold_2B.total_allocation()
    print(hold_2B)
    print("--all--")
    k = list()
    for hold in (holding_1, holding_2, hold_2B):
        hold.total_allocation()
        k.append(hold.total_allocation())
        print(hold)
        print(k)
        print(sum(k))
    print(list(holding_2.__dict__.items()))
