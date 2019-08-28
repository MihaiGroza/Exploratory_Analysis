import pandas as pd
from scipy import stats
from yahoo_fin.stock_info import get_data
import matplotlib.pyplot as plt
import researchpy as rp

stock_data= get_data('AAPL','01/01/2017',"01/01/2018")['close']

stock_data = stock_data.pct_change()
stock_data = stock_data.iloc[1:]

stock_data.index = pd.to_datetime(stock_data.index)
stock_data.weekday = stock_data.index.weekday_name

data = pd.DataFrame({'weekday' : stock_data.weekday, 'values' : stock_data.values}, index = stock_data.index)

#stock_data['day']= pd.Series(days)
 

data['is_monday'] = data['weekday']== 'Monday'

data['is_green'] = data['values']>= 0
#stock_data.to_frame()

n_mon = data['is_monday'].sum()

n_wkd = 250 - n_mon
r_green=  data['is_green'].sum()/250
r_red = 1 -r_green

print(data) 
