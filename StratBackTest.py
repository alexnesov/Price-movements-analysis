import pandas as pd
import numpy as np
prices_stock_a = [10,10.2,9.8,12,10,8,7]




class StratBackTest:
    """
    """
    def __init__(self, prices, stop_loss):

        self.evol_stock_a = []
        self.stock_prices = prices
        self.stock_ret = 0
        self.valid_evols = []
        self.stop_loss = stop_loss
        self.index_stop = 0
        self.ListOfLists = []

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

            count +=1
            init = False

    def retToStop(self):
        """
        Get index to know which price to take to calculate final return
        """
        count = 0
        init = True

        for evol in self.evol_stock_a:
            print(evol, ",", count)
            if evol >self.stop_loss:
                self.valid_evols.append(evol)
            else:
                break
            count +=1

        
        self.index_stop = count + 1
    
    @property
    def getLastPrice(self):

        lastPrice = self.stock_prices[self.index_stop]
        
        return lastPrice
        



strat = StratBackTest(prices=prices_stock_a,stop_loss=-0.2)
strat.getEvols()
strat.evol_stock_a
strat.retToStop()
strat.valid_evols
strat.getLastPrice





