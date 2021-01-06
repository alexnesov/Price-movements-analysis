import pandas as pd

prices_stock_a = [10,10.2,9.8,12,10,8,7]



class StratBackTest:
    """
    """
    def __init__(self, prices, stop_loss):

        self.evol_stock_a = []
        self.stock_prices = prices
        self.stock_ret = 0
        self.valid_evols = []

    def getEvols(self):
        """
        """
        count = 0
        init = True

        for price in self.stock_prices:

            p_dMinus1 = self.stock_prices[count-1]

            if init==False:
                evol = (price-p_dMinus1)/p_dMinus1
                self.evol_stock_a.append(round(evol,2))
            else:
                evol = 0
                self.evol_stock_a.append(evol)

            count +=1
            init = False

    def retToStop(self):
        """
        """
        count = 0

        for evol in self.evol_stock_a:
            count+=1
            print(count)
            print(evol)
            if evol >-0.2:
                self.valid_evols.append(self.evol_stock_a[count])
            else:
                break



strat = StratBackTest(prices=prices_stock_a,stop_loss=0.2)
strat.getEvols()
strat.evol_stock_a
strat.retToStop()
strat.valid_evols





