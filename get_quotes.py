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
    data = json.loads(info)
    data_dict = {k: v for d in data for k, v in d.items()}
    return(data_dict['LastTradePrice'])
    
    # tries = 0
    # while tries < 3:
    #     try:
    #         return info_dict['"LastTradePrice":']
    #         # need to convert quote to float
    #     except KeyError:
    #         print("try again?")
    #         tries += 1
    #         #return info_dict['"LastTradePrice":'
    #         time.sleep(3)
    #     try:
    #         return info_dict['"LastTradePrice":']
    #         tries += 1
    #     except KeyError:
    #         pass


        # except KeyError:
        #     print("try again?")
        #     getQuote(fund_name)
        #     tries += 1
            #getQuote(fund_name)

   
if __name__ == '__main__':
    print(getQuote('VTSMX'))
    print(getQuote('VGTSX'))
    print(getQuote("VGPMX"))
    #print(json.dumps(getQuotes('VTSMX'), indent=2))
    print((quote_to_float('VTSMX')))
