import pandas as pd
import numpy as np

class Portfolio:
    """
    The Porfolio aims to be made of approx. 10 stocks
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

    @property
    def portfolioAsDF(self):
        """
        Transforms dictionnary into a dataframe
        Propoerty decorator allows us to visualize the portfolio 
        in a nice DF format
        """
        df = pd.DataFrame.from_dict(self.positions)
        return df

    def calculatePosPL(self,initialPrice,priceNow):
        pl = int(priceNow) - int(initialPrice)
        return pl


    def calculateTotalPL(self):
        df = pd.DataFrame.from_dict(self.positions)
        rowPL = df.loc['PositionPL']
        rowPLfloats = pd.to_numeric(rowPL, errors='coerce')
        self.totalPL = sum(rowPLfloats)
        print('Total PL: ', self.totalPL)

    def addPrice(self,positionID,priceNow):
        """
        1. We add the current price market to the position
        2. Calcultes automatically the PL for POSITION and adds it to 
        the corresponding position column
        3. Updates TOTAL PL

        """
        self.positions[f'{positionID}']['priceNow'] = f'{priceNow}'

        pl = self.calculatePosPL(
                self.positions[f'{positionID}']['initialPrice'],
                self.positions[f'{positionID}']['priceNow'])

        self.positions[f'{positionID}']['PositionPL'] = f'{pl}'
        
        self.calculateTotalPL()



##### Testing the code #####
P1.positions['Pos001']


P1 = Portfolio("P1")
P1.addPosition("Pos001",'stonksXYZ',1000,80)
P1.addPosition("Pos002",'stonksABX',1000,63)

P1.addPrice("Pos001",60)
P1.addPrice("Pos002",100)

P1.positions
P1.portfolioAsDF
