""" Using shelve to store portfolio instances """

import shelve
from class_acts import Portfolio, Holding, StockFund, BondFund

holding_1 = StockFund()
holding_2 = StockFund()
holding_3 = BondFund()

db = shelv.open('holdtestDB')
for obj in (holding_1, holding_2, holding_3):
    db[obj.name] = obj
db.close()
