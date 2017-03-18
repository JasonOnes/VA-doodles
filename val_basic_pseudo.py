from flask import Flask, render_template, request, escape, session

from variables import time_frame, time_frame_rough
from class_acts import Portfolio, Holding, StockFund, BondFund
#quick question, do you have to import parents and children classes


"""" Basic program template ideas in pseudocode."""


""" 1. Establish inputs: + schedule(daily, monthly, quarterly).
                      + default amt to invest
                      + number of holdings
                      + specific holdings and type
                      + asset allocation
                      + inflation prediction
                      + real return desired needed
                      + target amt. and date
    Make forms to receive inputs
    jinja2 templates ?
    2. Compare valuations of holdings to current price (value),
       instruct amt to sell/buy/hold.

    3.Send e-mail with at specified times with instructions



Optional: signal buy/sell/hold alerts BLACK SWAN ALERTS
          Rebalance alert if allocations stray over/under threshold
           """
#1
#form making


app.config['holdingsDB'] = {'host': '127.0.0.1',
                            ''}

install = input("Amount of money to invest per time_frame: ")
installment = install / holding.allocation#see class
frequency = time_frame(time_frame_rough)
necessary_rate_of_ret = input("How much return in a vacuum do is necessary to meet ultimate target")
real_return = necessary_rate_of_ret + inflation
percent_increase = real_return / frequency
previous_value = request.form['previous_value']
target_value = previous_value * percent_increase + installment


"""current_holding_value = number of shares * current_price pulled from a get request?
    possibly have num_of_shares as an attribut within class?"""
#2
def what_to_do(fund=str, current_holding_value=int, target_value=int):
    if current_holding < target_value:
        print("Buy {} amount of {}.".format(current_holding_value - target_value, fund))
    elif current_holding > target_value:
        print("Sell {} amount of {}.".format(target_value - current_holding_value, fund))
    else:
        print("Hold on, looking good.")

what_to_do("VGPMX", 3155, 7222)


""" Make templates for entry.html, dblog.html, invest.html, etc. """
@val.route('/val_in')
def first_page():
    return render_template('entry.html',
                            the_title='Welcome to the Value AVerage calculator!')

@val.route('/invest', methods=['POST'])
def invest_this():
    fund = request.form['name']
    current_holding_value = request.form['previous_value']
    target_value = current_holding_value * percent_increase + installment
    #percent_increase and installment get request from initial setup page?
    #other form request or seperate request function
    to_invest = what_to_do(fund, current_holding_value, target_value)
    log_request(requests, to_invest)
    return render_template('results.html',
                            the_fund = fund,
                            the_prev_value = current_holding_value,
                            to_do = to_invest)

if __name__ = __main__:
