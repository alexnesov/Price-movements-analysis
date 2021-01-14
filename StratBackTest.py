import pandas as pd
import numpy as np

stockA = [1,2,4,15,1,6]


"""
Scenario to come:

100 000 euros
split on 10 stock
"""

class Portfolio:
    """
    
    """
    positions = {}
    totalPL = 0
    totalPositions = 0

    def __init__(self, ID):
        self.ID = ID

    def addPosition(self, positionID, Iticker, Iamount, IinitialPrice):
        self.totalPositions = self.totalPositions + Iamount
        self.positions.update(
            {f'{positionID}':

                {'ticker':f'{Iticker}',
                'amount':f'{Iamount}',
                'initialPrice':f'{IinitialPrice}'}
                }

            )

    def addPrice(self,positionID,priceNow):
        """
        We add the current price market to the position
        """
        self.positions[f'{positionID}']['priceNow'] = f'{priceNow}'

    @property
    def portfolioAsDF(self):
        df = pd.DataFrame.from_dict(self.positions)
        return df










P1 = Portfolio("P1")
P1.addPosition("Pos001",'AAPL',1000,80)
P1.addPosition("Pos002",'PLUG',1000,63)


P1.addPrice("Pos001",60)

P1.positions['Pos001']['ticker']
P1.positions
P1.portfolioAsDF
