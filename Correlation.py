import pandas as pd
from scipy import stats
from yahoo_fin.stock_info import get_data
import matplotlib.pyplot as plt
import researchpy as rp


tickers = ["SPY","AAPL","TSLA"]

portfolio_data = pd.DataFrame(columns = tickers)

for ticker in tickers:

    portfolio_data[ticker] = get_data(ticker,"01/01/2018", "01/01/2019")['close']
    
portfolio_data = portfolio_data.pct_change()
portfolio_data = portfolio_data.iloc[1:]
print(portfolio_data.head())

portfolio_data.plot.scatter("SPY", "AAPL")


#Homogeneity Test
print(stats.levene(portfolio_data["SPY"],portfolio_data["AAPL"]))
#plt.show()


#Pearson Correlation Test
print(stats.pearsonr(portfolio_data["SPY"], portfolio_data["AAPL"]))

#Spearman Correlation Test

print(stats.spearmanr(portfolio_data["SPY"], portfolio_data["AAPL"]))


#correlation matrix

print(rp.corr_pair(portfolio_data[["SPY","AAPL","TSLA"]]))




