# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:42:38 2024

@author: suraj
"""

#ols model:- is called optimization of the cod# it give the detaile executaion of the program
#when you are checking data the train data--> residual
#testing data-->error
import pandas as pd
import numpy as np
import seaborn as sns

wcat=pd.read_csv("C:/Data Science/16_Linear_regression/3_ordinary_least_sqaure_Regression/datasets/wc-at.csv")
wcat.size
#Exploratory data analysis
#1.Measuiring the central tendency
#2.Meaures the dispersion
#3.Third moment business decision
#4.Fourth moment busuiness decison
wcat.info()
wcat.describe()
#Graphical representation
import matplotlib.pyplot as plt
plt.bar(height=wcat.AT,x=np.arange(1,110,1))
plt.hist(wcat.AT)
sns.distplot(wcat.AT)
#data are normal but right skeweed
plt.boxplot(wcat.AT)
#data is right skewed with no outlier
plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns.distplot(wcat.Waist)
#data is normal bimodel
plt.boxplot(wcat.Waist)
#data is right skewed with no outlier
############################
#scatter plot
#bivariant analysis
plt.scatter(x=wcat.Waist,y=wcat.AT)
plt.scatter(x=wcat['Waist'],y=wcat['AT'], color='green')
#direction:positive, lineraity: moderate,, strenghth;poor
# now let us calsulate the correlation coefficient
np.corrcoef(wcat.Waist,wcat.AT)
#let us check the direction using covar factor
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output
# its value give the dirs=ection as per the values postive and negativeness
#################################
# now let us apply to linera regression model
import statsmodels.formula.api as smf
# all machine learning algorithm are implemanet using Sklearn
# but for this statsmodel
#package is being used because it gives you
# backend  calaculatonof bita-0 and bita-1
model=smf.ols('AT~ Waist', data=wcat).fit()
#y is AT and X is Waist
model.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     AT   R-squared:                       0.670
Model:                            OLS   Adj. R-squared:                  0.667
Method:                 Least Squares   F-statistic:                     217.3
Date:                Wed, 21 Feb 2024   Prob (F-statistic):           1.62e-27
Time:                        18:44:59   Log-Likelihood:                -534.99
No. Observations:                 109   AIC:                             1074.
Df Residuals:                     107   BIC:                             1079.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   -215.9815     21.796     -9.909      0.000    -259.190    -172.773
Waist          3.4589      0.235     14.740      0.000       2.994       3.924
==============================================================================
Omnibus:                        3.960   Durbin-Watson:                   1.560
Prob(Omnibus):                  0.138   Jarque-Bera (JB):                4.596
Skew:                           0.104   Prob(JB):                        0.100
Kurtosis:                       3.984   Cond. No.                         639.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
#ols helps to find best fit model, which cause
#least square error
#first you check R squared value=0.670 , if R square =0.8
#means that model is best fit
# fit , if R-square=0.8 to 0.6 moderate fit
# next you check p>|t| =0 , it means  less than alpha
# alpha is 0.05 , henece the model is accepted


pred1=model.predict(pd.DataFrame(wcat['Waist']))
pred1
#####################
#regression line for the predicated value
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,"r")
plt.legend('actual data', 'Predicated data')
plt.show()
####################
#error calculation
res1=wcat.AT-pred1
np.mean(res1)
# it must be zero and here it 10^-14 =~0
res_sqr1=res1*res1
mse1=np.mean(res_sqr1)
rmse1=np.sqrt(mse1)
rmse1
##32.76 lesser the value better the model
####################################3
#let us try to anther model
#x=log(WAsit)
# how to impore this model transformation of
plt.scatter(x=np.log(wcat['Waist']),y=wcat['AT'],color='green')
#data is linnearly scayttterd  direction postive and strength is poor
# now let us check the correlation coefficent
np.corrcoef(np.log(wcat.Waist), wcat.AT)
#r value is 0.82 <0.85 henece moderate lineraliy
model2=smf.ols('AT~np.log(Waist)', data=wcat).fit()
model2.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     AT   R-squared:                       0.675
Model:                            OLS   Adj. R-squared:                  0.672
Method:                 Least Squares   F-statistic:                     222.6
Date:                Wed, 21 Feb 2024   Prob (F-statistic):           6.80e-28
Time:                        18:50:46   Log-Likelihood:                -534.11
No. Observations:                 109   AIC:                             1072.
Df Residuals:                     107   BIC:                             1078.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -1328.3420     95.923    -13.848      0.000   -1518.498   -1138.186
np.log(Waist)   317.1356     21.258     14.918      0.000     274.994     359.277
==============================================================================
Omnibus:                        3.317   Durbin-Watson:                   1.599
Prob(Omnibus):                  0.190   Jarque-Bera (JB):                2.908
Skew:                           0.235   Prob(JB):                        0.234
Kurtosis:                       3.647   Cond. No.                         145.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
#again check  the R square value =0.67 which is less than 0.8 so scope of the impprovement
# p value is 0 less than 0.05
#################
pred2=model2.predict(pd.DataFrame(wcat['Waist']))
pred2
#check wcat and pred2 from the variable explorer
###################
#scatter diagram
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist), pred2,"r")
plt.legend(['predicated line', 'obsereved data'])
plt.show()
###################
# error calculation
res2=wcat.AT-pred1
res_sqr2=res2*res2
mse2=np.mean(res_sqr2)
rmse2=np.sqrt(mse2)
rmse2
#there is no significant chenage so go fro the another model
#there is no consideration changes
# now let us change y value instead of x
plt.scatter(x=wcat['Waist'],y=np.log(wcat['AT']),color='orange')
#linerayl scatter and direction positiev and strength poor
np.corrcoef(wcat.Waist, np.log(wcat.AT))
#r value is 0.84 <0.85 henece moderate lineraliy
###########
model3=smf.ols('np.log(AT)~Waist', data=wcat).fit()
model3.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     AT   R-squared:                       0.675
Model:                            OLS   Adj. R-squared:                  0.672
Method:                 Least Squares   F-statistic:                     222.6
Date:                Wed, 21 Feb 2024   Prob (F-statistic):           6.80e-28
Time:                        18:50:46   Log-Likelihood:                -534.11
No. Observations:                 109   AIC:                             1072.
Df Residuals:                     107   BIC:                             1078.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept     -1328.3420     95.923    -13.848      0.000   -1518.498   -1138.186
np.log(Waist)   317.1356     21.258     14.918      0.000     274.994     359.277
==============================================================================
Omnibus:                        3.317   Durbin-Watson:                   1.599
Prob(Omnibus):                  0.190   Jarque-Bera (JB):                2.908
Skew:                           0.235   Prob(JB):                        0.234
Kurtosis:                       3.647   Cond. No.                         145.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
#again check  the R square value =0.707 which is less than 0.8
# p value is 0.02 less than 0.05
pred3=model3.predict(pd.DataFrame(wcat['Waist']))
pred3_at=np.exp(pred3)
pred3_at
##check wcat and pred3_at from the variable explorer
##########################
#scattter diagram
#going to add the non linear component ie log(AT)
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist, pred3,"r")
plt.legend(['predicated line', 'obsereved data'])
plt.show()
###############################
# error calculation
res3=wcat.AT-pred3_at
res_sqr3=res3*res3
mse3=np.mean(res_sqr3)
rmse3=np.sqrt(mse3)
rmse3
#there is no significant chenage in r , r-squaredso go fro the another model
#there is no consideration changes
# now let us go for another model
#RMSE is 38.53
#################################
#now let us make y=log(At) and x=waist x*x=Waist*waist
#ploynomial Transformation
#here are r can not be change
#x=Waist, x^2=Waist*Waist,y=log(AT)
model4=smf.ols('np.log(AT)~Waist+I(Waist*Waist)', data=wcat).fit()
model4.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             np.log(AT)   R-squared:                       0.779
Model:                            OLS   Adj. R-squared:                  0.775
Method:                 Least Squares   F-statistic:                     186.8
Date:                Wed, 21 Feb 2024   Prob (F-statistic):           1.80e-35
Time:                        18:52:09   Log-Likelihood:                -24.779
No. Observations:                 109   AIC:                             55.56
Df Residuals:                     106   BIC:                             63.63
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept           -7.8241      1.473     -5.312      0.000     -10.744      -4.904
Waist                0.2289      0.032      7.107      0.000       0.165       0.293
I(Waist * Waist)    -0.0010      0.000     -5.871      0.000      -0.001      -0.001
==============================================================================
Omnibus:                        0.325   Durbin-Watson:                   1.464
Prob(Omnibus):                  0.850   Jarque-Bera (JB):                0.271
Skew:                           0.119   Prob(JB):                        0.873
Kurtosis:                       2.949   Cond. No.                     4.49e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.49e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
#R square is 0.779<0.8885 ,there is acope of the improvement
# p value is 0<0.005 henece accepetd
#bita-0=-7.8241
#bita-1= 0.2289
###
pred4=model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at=np.exp(pred4)
pred4_at
##########################
##check wcat and pred4_at from the variable explorer
############################
#if you add more and more componenet in the equation then model get the overfit
##########################
#regression line
#scattter diagram
#going to add the non linear component ie log(AT)
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist, pred4,"r")
plt.legend(['predicated line', 'obsereved data_model3'])
plt.show()
###############################
# error calculation
res4=wcat.AT-pred4_at
res_sqr4=res4*res4
mse4=np.mean(res_sqr4)
rmse4=np.sqrt(mse4)
rmse4

#RMSE is  32.24444782776013
#among all the model model4 is the best
########################################
data={"model":pd.Series(['SLR',"log_model","exp_model","poly_model"])}
data
table_rmse=pd.DataFrame(data)
table_rmse

##########################
#we have to generalize the  best model
from sklearn.model_selection import train_test_split
train,test=train_test_split(wcat,test_size=0.2)
train.size
test.size
plt.scatter(train.Waist, np.log(train.AT))
final_model=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
#y is log(AT) and x=Waist
final_model.summary()
# r-squraed=0.779<0.85 there is scope of the imporment
# p=0.000<0.05 hence accepteable
#b0=-7.821
#b1=0.2289

test_pred=final_model.predict(pd.DataFrame(test))
test_pred_at=np.exp(test_pred)
test_pred_at
##########################
train_pred=final_model.predict(pd.DataFrame(train))
train_pred_at=np.exp(train_pred)
train_pred_at
########################################
#evaluation on the test data
test_err=test.AT-test_pred_at
test_sqr=test_err*test_err
test_mse=np.mean(test_sqr)
test_rmse=np.sqrt(test_mse)
test_rmse
#Out[69]: 40.95156573738322
######################################
#evalution of the train data
train_res=train.AT-train_pred_at
train_sqr=train_res*train_res
train_mse=np.mean(train_sqr)
train_rmse=np.sqrt(train_mse)
train_rmse
#]: 29.640199697160668
##########################
#test_rmse>train_rmse
# so the model is overfit

