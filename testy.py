# from time_frame import time_frame, time_frame_rough
#
# freq = time_frame(time_frame_rough)
# print(freq * 2)
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
        return "{} is a holding that should be {}% of the portfolio".format(self.name, self.allocation*100)


VTSMX = Holding("VTSMX", "Stocks", .50, 3000)
type(VTSMX)
print(VTSMX)
