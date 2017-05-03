from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getQuote(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("uhoh HTTPError")
        return None
    try:
        bsObject = BeautifulSoup(html.read(), "lxml")
        quote = bsObject.body.div
    except AttributeError as e:
        print("uh AttributeError")
        return None
    print(quote)
    return quote
    quote = getQuote("https://finance.yahoo.com/quote/VGPMX?p=VGPMX")
    if quote == None:
        print("Quote for that fund could not be found.")
    else:
        print(quote)

getQuote("https://finance.yahoo.com/quote/VGPMX?p=VGPMX")
