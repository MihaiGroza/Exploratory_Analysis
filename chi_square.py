import pandas as pd
from scipy import stats
from yahoo_fin.stock_info import get_data
import matplotlib.pyplot as plt
import researchpy as rp
from scipy.stats import chisquare



#importing data
stock_data= get_data('AAPL','01/01/2017',"01/01/2018")['close']


#converting to stock returns
stock_data = stock_data.pct_change()
stock_data = stock_data.iloc[1:]


#creating a column with the day of each row
stock_data.index = pd.to_datetime(stock_data.index)
stock_data.weekday = stock_data.index.weekday_name


#creating dataframe
data = pd.DataFrame({'weekday' : stock_data.weekday, 'values' : stock_data.values}, index = stock_data.index)

#splitting data into mondays and non-mondays
data['is_monday'] = data['weekday']== 'Monday'

#splitting data into green and red days
data['is_green'] = data['values']>= 0


#variables to create tables
n_mon = data['is_monday'].sum()
n_wkd = 250 - n_mon
r_green=  data['is_green'].sum()/250
r_red = 1 -r_green


#creating expected observation matrix
exp_matrix = pd.DataFrame({'movement':['green','red'],'mondays':[n_mon*r_green,n_mon*r_red],'non-mondays':[n_wkd*r_green,n_wkd*r_red]})



data['is_red'] = data['values']<= 0

#observed observation matrix
data.groupby("is_monday")["is_green",'is_red'].sum()


#performing chi square test
print(chisquare([28,18,110,95],f_exp=[25.392,20.608,112.608,91.392]))

#cannot reject null hypothesis
