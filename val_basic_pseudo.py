from variables import time_frame, time_frame_rough

"""" Basic program template ideas in pseudocode."""


""" 1. Establish inputs: + schedule(daily, monthly, quarterly).
                      + default amt to invest
                      + number of holdings
                      + specific holdings and type
                      + asset allocation
                      + inflation prediction
                      + real return desired needed
                      + target amt. and date

    2. Compare valuations of holdings to current price (value),
       instruct amt to sell/buy/hold.

    3.


Optional: signal buy/sell/hold alerts BLACK SWAN ALERTS """
#1

install = input("Amount of money to invest per time_frame: ")
installment = install / holding.allocation#see class
frequency = time_frame(time_frame_rough)
real_return =

percent_increase = real_return / frequency
target_value = current_value * percent_increase + installment

#Maybe make class called holdings
class Holding:
    """ creating a class for the different funds"""
    def __init__(self, name, family, allocation, current_value=0):
        self.name = name
        self.family = family
        self.allocation = allocation
        self.current_value = current_value

    def __repr___(self):
        pass

    def __str__(self):
        pass

class StockFund(Holding):
    pass

class BondFund(Holding):
    pass
    

#2
def what_to_do(fund=str, current_holding=int, target_value=int):
    if current_holding < target_value:
        print("Buy {} amount of {}.".format(current_holding - target_value, fund))
    elif current_holding > target_value:
        print("Sell {} amount of {}.".format(target_value - current_holding, fund))
    else:
        print("Hold on, looking good.")

what_to_do("VGPMX", 3155, 7222)
