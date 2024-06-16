# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:38 2024

@author: suraj
"""

import pandas as pd
import numpy as np
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima.model import ARIMA
from sklearn . metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

Walmart=pd.read_csv("C:/Data Science/19_Time_series/datasets/Walmart Footfalls Raw.csv")
# Data partition
Train=Walmart.head(147)
Test= Walmart.tail(12)

#In order to use this model,  we need to first find out values of p, q, and d
#p represents number of Autoregressive terms - lags of dependent variable 
#q represents numner of Moving Average terms - lagged of forecast errors in prediction equation
#d represents number of non-seasonal differences 
#To find the values of p, d and q we use Autocorrelation function(ACF)
#and partial Autocorrelation (PACF) plots.
#p value is the value on x=axis of PACF 
#where the plot crosses the upper COnfidence INterval for the first time. 
#The first lne which crosse sthe confidence interval 
#q values is the value on x- axis of ACF where the plot crosses 
#the upper COnfidence Interval for the first time 

tsa_plots.plot_acf(Walmart.Footfalls, lags=12) # q  for MA 5 to  


tsa_plots.plot_pacf(Walmart.Footfalls, lags=12)# p for AR is 3 


# arima with ar=3 and ma =5
model1= ARIMA(Train.Footfalls, order=(3,1,5))
res1=model1.fit()
print(res1.summary())

# forecast for next 12 month
start_index= len(Train)
end_index= start_index+11
forecast_test=res1.predict(start=start_index, end=end_index)

print(forecast_test)


# evaluate forecasts
rmse_test= sqrt(mean_squared_error(Test.Footfalls, forecast_test))
print('Test RMSE: %.3f'%rmse_test)

# plots forecasts against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_test, color='red')
pyplot.show()

# Auto -ARIMA - Automatically discovevr the optimal order for ARIMA
# pip install pmdarima --user
import pmdarima as pm

ar_model= pm.auto_arima(Train.Footfalls, start_p=0, start_q=0,
                        max_p=12, max_q=12, # maxime p and q
                        m=1, # frequency of series
                        d= None,    # le the model determine 'd'
                        seasonal= False, # NO seasonality
                        start_P=0, trace=True,
                        error_action='warn', stepwise=True)

ar_model #Out[4]: ARIMA(order=(3, 1, 5), scoring_args={}, suppress_warnings=True)

res = ar_model.fit(Train.Footfalls)
print(res.summary())


# forecast for next 12 month
start_index= len(Train)
end_index= start_index+11
forecast_best=res1.predict(start=start_index, end=end_index)

print(forecast_best)


# evaluate forecasts
rmse_best= sqrt(mean_squared_error(Test.Footfalls, forecast_best))
print('Test RMSE: %.3f'%rmse_best)

# plots forecasts against actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_best, color='red')
pyplot.show()


# forecast for next 12 month
start_index= len(Walmart)
end_index= start_index + 11
forecast=res1.predict(start=start_index, end=end_index)

print(forecast)

