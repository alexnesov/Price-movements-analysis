import pandas as pd
import numpy as np


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


    def calculatePosPL(self,initialPrice,priceNow):
        
        pl = int(priceNow) - int(initialPrice)
        print("pl: ", pl)
        return pl

        
    def addPrice(self,positionID,priceNow):
        """
        1. We add the current price market to the position
        2. It then calculates automatically the PL and adds it to 
        the corresponding position column
        """
        self.positions[f'{positionID}']['priceNow'] = f'{priceNow}'

        pl = self.calculatePosPL(
                self.positions[f'{positionID}']['initialPrice'],
                self.positions[f'{positionID}']['priceNow'])

        self.positions[f'{positionID}']['PL'] = f'{pl}'


    @property
    def portfolioAsDF(self):
        """
        Transforms dictionnary into a dataframe
        Propoerty decorator allows us to visualize the portfolio 
        in a nice DF format
        """
        df = pd.DataFrame.from_dict(self.positions)
        return df



P1.positions['Pos001']


P1 = Portfolio("P1")
P1.addPosition("Pos001",'AAPL',1000,80)
P1.addPosition("Pos002",'PLUG',1000,63)


P1.addPrice("Pos001",60)

P1.positions['Pos001']['ticker']
P1.positions
P1.portfolioAsDF
