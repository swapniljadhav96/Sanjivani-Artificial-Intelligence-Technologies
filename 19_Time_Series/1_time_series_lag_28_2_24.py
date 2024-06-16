# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:41:53 2024

@author: suraj
"""
#time series analysis with lag

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')

# load the data set
df=pd.read_csv("C:/Data Science/19_Time_series/datasets/AirPassengers.csv")

df.columns
df=df.rename({'#Passengers':'Passengers'},axis=1)


print(df.dtypes)
#month is text and passenger i sint
# now let us convert the into data and time
df['Month']=pd.to_datetime(df['Month'])
print(df.dtypes)

# let the make the Month columnn as index
df.set_index('Month', inplace=True)

plt.plot(df.Passengers)
#There are increassing trend and it has got seasonality

# Is the data Stationary
#dickey-Fuller test
from statsmodels.tsa.stattools import adfuller
adf,pvalue,usedlag_, nobs_, critical_values_,icbest_= adfuller(df)
print("pvalue=",pvalue," if above 0.05 data is not stationary")
#since data is not stationary , we  may need SARIMA and not just ARIMA
#now let us extrcat the year and month from the date and time columns

df['year']=[d.year for d in df.index]
df['month']=[d.strftime('%b') for d in df.index]
years=df['year'].unique()


#plot yearly and montly values as boxplots
sns.boxplot(x='year',y='Passengers', data=df)
# no . of passsengers are going up year by year
sns.boxplot(x='month', y='Passengers', data=df)
#over all there is heigher trend in July adnd Augst compared to rest  of the 


#extracted an plot trend , seasonal and residuals
from statsmodels.tsa.seasonal import seasonal_decompose
decomposed= seasonal_decompose(df['Passengers'],model='additive')

#additive time series:
# value=base level+ trend+seasonability+Error
# multipicative time series
# value = Base level* trend*seasonality* error

trend=decomposed.trend
seasonal=decomposed.seasonal    #cyclic  behavior may not be seasonal
residual=decomposed.resid


plt.figure(figsize=(12,8))
plt.subplot(411)
plt.plot(df['Passengers'], label='Original', color='yellow')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend,label='Trend', color='yellow')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonal', color='yellow')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residual', color='yellow')
plt.legend(loc='upper left')
plt.show()
'''

Trend is going  up from 1950s to 60 s
It is highky seasonal showing peaks at particular interval
this helps to select specific prediction model

'''

#Auto correlation
# values are not correlated with X-axis  but with its lag
# meaning yesturdays value i sdeped on day before yeasturday so on so forth
# aut correlation is simplyy the correlation of a series with its own lags
# plot lag on x axis and correlation on y axis
# any plot correlation above confidence lnes are statistically significant



from statsmodels.tsa.stattools import acf
acf_144= acf(df.Passengers, nlags=144)
plt.plot(acf_144)
# auto correlation above zeros means positive correlation and below as negative 
#obtain the same but with single line and more info.....
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.Passengers)
# any lag before 40 ha s positive corelation 
# horizonatl bands indicated 95% and 99%  (dashed ) confidence bands

