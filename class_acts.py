"""Classes module for Value valuations """
"""++++Need to include some delimiters on allocations such that their sum is
    1.0+++"""
from abc import ABCMeta, abstractmethod
#from get_quotes import getQuote
from get_quotes import getQuote

class Owner(object):
    """defines the Holder of Portfolio here is where we can initialize all the
    target info, mahbe?"""
    def __init__(self, username, email, schedule, amt_to_invest_per,
                 real_return_needed):
        self.username = username
        self.email = email
        self.schedule = schedule
        self.installment = amt_to_invest_per
        self.real_return_needed = real_return_needed
        """ retrieve from forms ?"""

"""Need Portfolio and Holding classes to work together perhaps inherit from an
ABC"""

class Portfolio(object):
    """ class for the total of all holdings for individual"""
    def __init__(self, owner, num_of_holding, holdings=list(), taxable=True,
                 stock_allocation=0.80, bond_allocation=0.20):
        self.owner = owner
        self.asset_allocation = stock_allocation + bond_allocation
        self.num_of_holdings = len(holdings)
        #maybe Holding.numHoldings()
        #self.num_of_holdings = num_of_holdings
        self.taxable = taxable
        self.stock_allocation = stock_allocation
        self.bond_allocation = bond_allocation
        self.holdings = holdings

    def __str__(self):
        return """Portfilio-no-you-didn't {}'s portfolio currently contains {}
                  holdings {}""".format(self.owner, self.num_of_holdings,
                                        self.holdings)

        #return "{} portfolio. {}".format(self.owner, Holding.print_number_of_holdings())

    def __repr__(self):
        return "{} portfolio has {} holdings".format(self.owner,
                                                     self.num_of_holdings)

        # self.total = total_value
    def total_value(self):
        """total of all the holdings"""
        if len(list(Holding)) == self.num_of_holdings:
            return sum(list(Holdings.value))

    def asset_allocation():

        # something like this though out of scope
        # k = list()
        # for hold in (holding_1, holding_2, hold_2B):
        #     hold.total_allocation()
        #     k.append(hold.total_allocation())
        #     print(k)
        #     print(sum(k))
        # sum(k) = all_totes

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

    # def rebalance():
    #     """ compare values of holdings to asset allocation make adjustments""
    #     for holding in portfolio:
    #         if holding_name.value // portfolio.total_value
    #         < holding_name.total_allocation:
    #             return buy()
    #         elif holding_name.value // porfolio.total_value
    #         > holding_name.total_allocation:
    #             return sell()
    #         else:
    #             print("all good")
    #             pass


class Holding(object):
    """ creating a class for the different funds"""
    __metaclass__ = ABCMeta #since holding is an abstraction

    @abstractmethod
    def holding_type(self):
        """Throw the type of holding "down" to the child classes?"""
        pass

    numHoldings = 0
    def __init__(self, name, family, num_shares=0, value=0):
        self.name = name
        self.family = family
        # self.total_allocation = total_allocation
        self.num_shares = num_shares
        self.value = value
        #Holding.numHoldings += 1

    def __repr___(self):
        return "{} should be {}% of portfolio".format(self.name,
                                                      self.portfolio_allocation)

    def __str__(self):
        return "{} is a {} holding constituting {}% of portfolio".format(
            self.name, self.family, self.total_allocation() * 100)

    def print_number_of_holdings():
        print("There are currently {} holdings.".format(Holding.numHoldings))

    def target_value(self, current_value):
        """ Give the target_value of holding for this particular installment
        must be performed BEFORE current_value is updated."""
        self.target_value = value * freq_return + installment
        return self.target_value

    def update_value(self, num_shares):
        """price = get value from web"""
        price = getQuotes(self.name)
        current_value = self.num_shares * price
        self.value = current_value
        return self.value

    def update_num_shares(self, num_shares):
        """ update the num_shares after purchase or sale"""
        if sale:
            num_shares = num_shares - amt_to_sell // current_price
        elif buy:
            num_shares = num_shares + amt_to_buy // current_price

    def sell():
        pass

    def buy():
        pass

    def to_cash():
        pass

    def to_do(self):
        if self.value > self.target_value:
            amt_to_sell = self.value - self.target_value
            return sell(amt_to_sell)
        elif self.value < self.target_value:
            amt_to_buy = self.target_value - self.value
            return buy(amt_to_buy)
        elif self.value == self.target_value:
            return to_cash(installment)
        else:
            return "Something went wrong."




class StockFund(Holding):
    def __init__(self, name, stock_type, cap_size, stock_allocation,
                 portfolio_allocation=0.8):
        #super().__init__(name, 'Stock Fund', num_shares, value)
        self.name = name #inherits name from Holding
        #Holding.__init__(name, 'Stock Fund', num_shares, value)
        self.stock_type = stock_type
        self.cap_size = cap_size
        self.family = 'Stock Fund'
        #self.num_shares = num_shares
        #self.value = value
        self.stock_allocation = stock_allocation
        self.portfolio_allocation = portfolio_allocation
        Holding.numHoldings += 1

    def total_allocation(self):
        self.allocation = self.stock_allocation * self.portfolio_allocation
        return self.allocation


class BondFund(Holding):
    def __init__(self, name, bond_type, term_length, bond_allocation,
                 portfolio_allocation=0.2):
        self.name = name
        self.bond_type = bond_type
        self.term_length = term_length
        self.family = 'Bond Fund'
        self.bond_allocation = bond_allocation
        self.portfolio_allocation = portfolio_allocation
        Holding.numHoldings += 1

    def total_allocation(self):
        self.allocation = self.bond_allocation * self.portfolio_allocation
        return self.allocation
    """ updates allocation of holding to portfolio """


class Commodity(Holding):
    def __init__(self, name, family, num_shares, value, allocation=0):
        super().__init__(name, family, num_shares, value)
        self.allocation = allocation
        Holding.numHoldings += 1

    def total_allocation(self):
        return self.allocation

"""" Shelve database storing holdings """
# import shelve
#
# db = shelve.open('holdingsdb')
# for obj in (holding_1, holding_2, holding_3):
#     db[obj.name] = obj
# db.close()
#

if __name__ == '__main__':
    holding_X = Commodity('VGPMX', 'Commodity', 10, 300, 0.15)
    holding_2 = BondFund('VWAHX', 'Municipal', 'Intermediate', 1.0)
    #holding_2.name = 'VWAHX'
    holding_2.allocation = 0.20
    holding_1 = StockFund('VTSMX', 'Domestic', 'Total', 100, 0.30)
    #holding_1.name = 'VTSMX'
    holding_1.allocation = 0.50
    hold_2B = BondFund('VHAMBONE', 'Corporate', 'Long-Term', 0.3)
    #hold_2B.name = 'VHAMBONE'
    hold_2B.allocation = 0.20
    z = Portfolio("Jason", 3, [holding_1.name, holding_2.name, hold_2B.name])
    print(z)
    print(z.asset_allocation)
    # print(z.rebalance())
    print(hold_2B.allocation)
    hold_2B.num_shares = 8
    #print(hold_2B.update_value(hold_2B.num_shares))
    print(holding_1)
    print(holding_X)
    Holding.print_number_of_holdings()
    new_fund = StockFund('XXXX', 'Domestic', 'Small-Cap', 0.15)
    #new_fund.name = 'XXXX'
    print(new_fund)
    Holding.print_number_of_holdings()
    #print(z.total_value())
    print(holding_X.value)
    print(holding_1.update_value(200) + "hey now")
