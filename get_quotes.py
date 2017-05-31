from googlefinance import getQuotes
import json
import time

#fund_name = Holding.name
def quote_to_float(fund_name):
    quote = getQuote(fund_name)
    return float(quote)

def getQuote(fund_name):
    """retrieves the last price for fund"""
    info = json.dumps(getQuotes(fund_name))
    #return info[99:105]
    info_list = info.split()
    #return info_list[11]
    """need to turn info into dictionary in case of format changes at googlefinance
    thus searching by key ie, LastTradePrice"""
    info_dict = dict(info_list[n:n+2] for n in range(0, len(info_list), 2))
    print(info_dict.keys())
    tries = 0
    while tries < 3:
        try:
            return info_dict['"LastTradePrice":']
            # need to convert quote to float
        except KeyError:
            print("try again?")
            tries += 1
            #return info_dict['"LastTradePrice":'
            time.sleep(3)
        try:
            return info_dict['"LastTradePrice":']
            tries += 1
        except KeyError:
            pass


        # except KeyError:
        #     print("try again?")
        #     getQuote(fund_name)
        #     tries += 1
            #getQuote(fund_name)

        """Not sure if this is any better as it's a pretty wonky keyname"""
    #print(info_dict)
if __name__ == '__main__':
    print(getQuote('VTSMX'))
    #print(json.dumps(getQuotes('VTSMX'), indent=2))
    #print(quote_to_float('VTSMX'))
