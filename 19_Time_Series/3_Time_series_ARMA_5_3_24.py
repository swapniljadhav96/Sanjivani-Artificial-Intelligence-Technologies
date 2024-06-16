# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:01:24 2024

@author: suraj
"""

import numpy as np
import pandas as pd
import seaborn as sns


sns.set_theme()
# using the available dowjones data in seaborn
dowjones= sns.load_dataset('dowjones')
dowjones.head()
sns.lineplot(data=dowjones, x='Date',y='Price')
'''
A simple moving average (SMA) calculation the average of a selected 
range of values
by the number of periods in that range.
The most typical moving averages are 30 days 100 days and 365  days
moving averages. moving averages are nice cause they can determine trends
whie ignoring short term fluctuatins
On e can claulate the sma by simply using'''

dowjones['sma_30']=dowjones['Price'].rolling(window=30, min_periods=1).mean()

dowjones['sma_50']=dowjones['Price'].rolling(window=50, min_periods=1).mean()

dowjones['sma_100']=dowjones['Price'].rolling(window=100, min_periods=1).mean()

dowjones['sma_365']=dowjones['Price'].rolling(window=365, min_periods=1).mean()

sns.lineplot(x='Date', y='value',legend='auto', hue='variable', data=dowjones.melt('Date'))

''' As you can see the higher the value of the windows,
the lessser it is offected by short-term fluctuation
and it capture long-term  trends in the data.
Simple Moving averages are often used by tradersin the 
in the stack market for technical analysis.'''

# exponential moving average
'''simple moving averages are nice , but
theuy give equal weighted to each of the data points
what if  you awanted an average that will give higher weight
to more recent points and lesser to points in the past . in the case,
what you want is to compute the expeonetial moving average(EMA)'''


dowjones['ema_50']=dowjones['Price'].ewm(span=50, adjust=False).mean()
dowjones['ema_100']=dowjones['Price'].ewm(span=100, adjust=False).mean()
sns.lineplot(x='Date', y='value', legend='auto', hue='variable', data=dowjones[['Date','Price','ema_50','sma_50']].melt('Date'))

'''as you can see the ema_50 follows the price chart more closely
than  the sma_50 and is more sensitive to the recent data points.

 Which moving average you should use as a feature od you fragmenation'''
