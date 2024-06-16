# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:15:15 2024

@author: suraj
"""
#time series analysis with predicting the model 
# model based--> auto regressive model
import pandas as pd 
Walmart=pd.read_csv("C:/Data Science/19_Time_series/datasets/Walmart Footfalls Raw.csv")
Walmart.shape

#pre prossing
import numpy as np

Walmart['t']=np.arange(1,160 )

Walmart["t_square"]=Walmart["t"]*Walmart["t"]
Walmart["log_footfalls"]=np.log(Walmart["Footfalls"])
Walmart.columns


# in walmart data we have jan 1991 in 0 th row we need only first thred
#exampe jan from each cell

p=Walmart["Month"][0]
#befor e we will exttract , let us create new column called
# month o store extraced values
p[0:3]

Walmart['months']=0
# you can check the dataframe with months nae with all values 0
# the total records are 159 in walmart
for i in range(159):
    p=Walmart["Month"][i]
    Walmart['months'][i]=p[0:3]
    
month_dummies= pd.DataFrame(pd.get_dummies(Walmart['months']))
# now let us concatenate these dummy values  to dataframe
Walmart1=pd.concat([Walmart, month_dummies], axis=1)
# you can check the dataframe walmart1


#visualization- Time plot
Walmart1.Footfalls.plot()

#data partition
Train=Walmart1.head(147)
Test=Walmart1.tail(12)

#to change the index value in pandas as data frgame
# Test.set_index(np.arange(1,13))

######################### L I N E A R######################
import statsmodels.formula.api as smf

linear_model=smf.ols('Footfalls ~ t', data=Train).fit()
pred_linear=pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
rmse_linear
#209.92559265462594

########################### E X P O N E N T I A L#################
Exp=smf.ols('log_footfalls ~ t', data=Train).fit()
pred_Exp=pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp
#217.05263566813454

################## Q U A D R A T I C############################
Quad=smf.ols('Footfalls ~ t + t_square', data=Train).fit()
pred_Quad=pd.Series(Quad.predict(pd.DataFrame(Test[['t','t_square']])))
rmse_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_Quad))**2))
rmse_Quad
# 137.1546274135642

################# ADDITIVE SEASONALITY ###########################
add_sea= smf.ols('Footfalls ~ Jan+Feb+Mar+Apr+ May+ Jun +Jul+ Aug+ Sep+ Oct+ Nov', data=Train).fit()
pred_add_sea=pd.Series(add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]))
rmse_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea
# 264.6643900568772

################## MULITIPLICATIVE SEASONALITY #####################
Mul_sea= smf.ols('log_footfalls ~ Jan+Feb+Mar+Apr+ May+ Jun +Jul+ Aug+ Sep+ Oct+ Nov', data=Train).fit()
pred_Mul_sea=pd.Series(Mul_sea.predict(Test))
rmse_Mul_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mul_sea)))**2))
rmse_Mul_sea
#  268.1970325309192

############################ Additive seanality with quardratic trend ###################
add_sea_Quad= smf.ols('Footfalls ~ t+t_square+Jan+Feb+Mar+Apr+ May+ Jun +Jul+ Aug+ Sep+ Oct+ Nov', data=Train).fit()
pred_add_sea_Quad=pd.Series(add_sea_Quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov', 't','t_square']]))
rmse_add_sea_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea_Quad))**2))
rmse_add_sea_Quad
#Out[79]: 50.60724584169114
#########################Mulitipicative  seanality with linear trend ##################
Mul_add_sea= smf.ols('log_footfalls ~t+ Jan+Feb+Mar+Apr+ May+ Jun +Jul+ Aug+ Sep+ Oct+ Nov', data=Train).fit()
pred_Mul_add_sea=pd.Series(Mul_add_sea.predict(Test))
rmse_Mul_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mul_add_sea)))**2))
rmse_Mul_add_sea
#172.7672678467003
######################### Consolidate #############################
data={'MODEL':pd.Series(['rmse_linear','rmse_Exp','rmse_Quad','rmse_add_sea','rmse_add_sea_Quad','rmse_Mult_sea','rmse_Mult_add_sea']),
      'RMSE_Values':pd.Series([rmse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_add_sea_Quad,rmse_Mul_sea,rmse_Mul_add_sea])
      }

table_rmse=pd.DataFrame(data)
table_rmse
#########################Testing ##############################
 # 'rmse_add_sea  has the least the value among the model preared so far predicating the new
 
predict_data=pd.read_excel("C:/Data Science/19_Time_series/datasets/Predict_new.xlsx")

model_full=smf.ols('Footfalls ~t+t_square+ Jan+Feb+Mar+Apr+ May+ Jun +Jul+ Aug+ Sep+ Oct+ Nov', data=Train).fit()

pred_new=pd.Series(model_full.predict(predict_data))
pred_new
'''0     2213.628216
1     2252.669534
2     2219.210851
3     2331.668836
4     2384.626820
5     2059.418138
6     2206.876122
7     2204.750773
8     2256.708757
9     2028.471300
10    1999.332467
11    2308.270556
dtype: float64'''

# error produce should be independent so not sataisfied
predict_data["forecasted_Footfalls"]=pd.Series(pred_new)

#autoregresssion model(AR)
# calaculating Residuals from best model applied on full data
#AV-FV
full_res=Walmart.Footfalls-model_full.predict(Walmart1)
full_res

#ACF plot residuals
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(full_res,lags=12)
#ACF is an (complete ) auto - correlated function gives values
# of auto correlation of any time series with its lagged  values

# PACF is a partial auto- correlation function.
# It finds correlations of  present with lags of the residuals of the 
tsa_plots.plot_pacf(full_res, lags=12)

# alternative  approach for ACF plot
# from pandas.plotting import autocorrelation_plot
#autocorrelation_pyplot.show()
###data-->resd--> acr-->ar

#AR model
from statsmodels.tsa.ar_model import AutoReg
model_ar=AutoReg(full_res, lags=[1])
# model_ar=AutoReg(full_res, lags=12)
model_fit=model_ar.fit()

print('Coefficients:%s'% model_fit.params)

pred_res=model_fit.predict(start=len(full_res), end=len(full_res)+len(predict_data)-1, dynamic=False)
pred_res.reset_index(drop=True, inplace=True)

# the final predictions usising ASQT and AR(1) model
final_pred=pred_new+pred_res+ pred_res
final_pred

#after you are getting the juice of the sugar cane then again check the juice is present in bagas
# angain check it g again for lag  from autocorrleation regraition upto go for the get  the auto Regression get the zero or all the lag value get the less than +-2se value
# 'pred_res-next_pred_res' for checking the again
# for the acf plot

# above is model based prediction--> nature of the data is fix


