""" Tackling the classes for ValAv from another angle, embedding to make
composites"""


class Portfolio(object):
    def __init__(self, *args):
        self.holdings = list(args)

    def AddHolding(self, fund):
        self.holdings.append(fund)

    def showPort(self):
        for fund in self.holdings:
            print(fund)


class Holding(object):
    """ creating a class for the different funds"""
    def __init__(self, name, family, portfolio_allocation=0, num_shares=0,
                 value=0):
        self.name = name
        self.family = family
        self.portfolio_allocation = portfolio_allocation
        self.num_shares = num_shares
        self.previous_value = value

    def __repr___(self):
        return "{} should be {}% of portfolio".format(self.name,
                                                      self.allocation)

    def __str__(self):
        return "{} is a {} holding constituting {}% of porfolio".format
        (self.name, self.family, self.portfolio_allocation * 100)


class StockFund:
    def __init__(self, name, stock_type, cap_size,
                 stock_allocation, portfolio_allocation=0.8):
        self.fund = Holding(name, 'Stock Fund', portfolio_allocation)
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.name = name
        self.stock_allocation = stock_allocation
        self.portfolio_allocation = portfolio_allocation

    def total_allocation(self):
        self.allocation = self.stock_allocation * self.portfolio_allocation
        return self.allocation

    def __getattr__(self, attr):
        return getattr(self.fund, attr)

    def __repr__(self):
        return str(self.fund)


class BondFund:
    def __init__(self, name, bond_type, term_length, bond_allocation,
                 portfolio_allocation=0.2):
        self.fund = Holding(name, 'Bond Fund')
        self.bond_type = bond_type
        self.term_length = term_length
        self.bond_allocation = bond_allocation
        self.portfolio_allocation = portfolio_allocation
        self.name = name

    def total_allocation(self):
        self.allocation = self.bond_allocation * self.portfolio_allocation
        return self.allocation

    def __getattr__(self, attr):
        return getattr(self.fund, attr)

    def __repr__(self):
        return str(self.fund)

if __name__ == '__main__':
    holding_1 = StockFund('VTSMX', 'Domestic', 'Total', 0.75)
    holding_2 = StockFund('VGTSX', 'Foreign', 'Mid-Cap', 0.25)
    holding_3 = BondFund('VWAHX', 'Municipal', 'mid-term', 1.0)
    print(holding_1)
    print(holding_2)
    print(holding_3)
    my_money = Portfolio(holding_1, holding_2, holding_3)
    my_money.showPort()
