from flask import Flask, render_template, request, escape, session

from variables import time_frame, time_frame_rough
from class_acts import Portfolio, Holding, StockFund, BondFund
from contman import UseDatabase, ConnectionError, SQLError, CredentialsError

# quick question, do you have to import parents and children classes
"""*****Be sure and look into possible problems using floats with monies***"""
# round(N, 2) -- decimal type -- %.2f -- {0:.2f} -- money function formats


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
    4. Provide link to appropriate brokerage with results



Optional: signal buy/sell/hold alerts BLACK SWAN ALERTS
          Rebalance alert if allocations stray over/under threshold
           """

Portfolio = {holding_1: {'name': 'VTSMX',
                         'family': 'Stock',
                         'allocation': 50,
                         'value': 6000},
             holding_2: {'name': 'VGSTX',
                         'family': 'Stock',
                         'allocation': 30,
                         'value': 4000},
             holding_3: {'name': 'VWAHX',
                         'family': 'Bond',
                         'allocation': 20,
                         'value': 3000}}
# classes as keys???
holding_1 = Holding('VTSMX', 'Stock', 0.50, 6000)
previous_value = holding_1.value != holding_1[value]
""" __hash__ , __eq__ to make this work?"""
# 1
# form making


app.config['holdingsDB'] = {'host': '127.0.0.1',
                            ''}

install = input("Amount of money to invest per time_frame: ")
installment = install / holding.allocation  # see class
frequency = time_frame(time_frame_rough)
necessary_rate_of_ret = input("""How much return in a vacuum do is
                              necessary to meet ultimate target""")
real_return = necessary_rate_of_ret + inflation
percent_increase = real_return / frequency
previous_value = request.form['previous_value']
target_value = previous_value * percent_increase + installment


"""current_holding_value = number of shares * current_price pulled from a
get request? possibly have num_of_shares as an attribut within class?"""
# 2


def what_to_do(fund=str, current_holding_value=int, target_value=int):
    """if sell option turned off disable sell elif"""
    if current_holding < target_value:
        print("Buy {} amount of {}.".format(current_holding_value -
                                            target_value, fund))
    elif current_holding > target_value:
        print("Sell {} amount of {}.".format(target_value -
                                             current_holding_value, fund))
    else:
        print("Hold on, looking good.")

what_to_do("VGPMX", 3155, 7222)


""" Make templates for entry.html, dblog.html, invest.html, etc. """
val = Flask(__name__)


@val.route('/val_in')
def first_page():
    return render_template('sign_in.html',
                           the_title='Patient Investing to You!')
# ----->>> goes to /submit
""" need a page for intitial setup after sign in for more global variables
including ultimate target value, time_till_target, inflation,
return_percentage_needed"""


@val.route('/submit', methods=['POST'])
def second_page():
    return render_template('submission.html')


@val.route('/invest', method=['POST'])
""" this should post to database"""
""" and show results page"""


@val.route('/invest', methods=['POST'])
def invest_this():
    fund = request.form['name']
    current_holding_value = request.form['previous_value']
    target_value = current_holding_value * percent_increase + installment
    # percent_increase and installment get request from initial setup page?
    # other form request or seperate request function
    to_invest = what_to_do(fund, current_holding_value, target_value)
    log_request(requests, to_invest)
    return render_template('results.html',
                           the_fund=fund,
                           the_prev_value=current_holding_value,
                           to_do=to_invest)

val.run(debug=True)

# if __name__ = __main__:
