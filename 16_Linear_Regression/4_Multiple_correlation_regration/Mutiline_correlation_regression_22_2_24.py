# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:59:00 2024

@author: suraj
"""
#multiline correlaation regression
import pandas as pd
import numpy as np
import seaborn as sns
cars=pd.read_csv("C:/Data Science/16_Linear_regression/4_Multiple_correlation_regration/datasets/Cars.csv")
#exploatary data analysis
#1. meauser the central tendency
#2.Measure the dispersion
#3.Third momenet busisness decision
#4. Fourth moment business decision
#5.probability  distribution
#6.6.Graphical representatiin(Histogram, Boxplot)

cars.describe()
#graphical representation
import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
#data is right skewed
plt.boxplot(cars.HP)
#there are several outlier in Hp column
# similar operation are excepected for other three columns
sns.displot(cars.MPG)
# data is slightlt left distributed
plt.boxplot(cars.MPG)
#ther are oultier
sns.distplot(cars.VOL)
#data is slightly left distributed
plt.boxplot(cars.VOL)
sns.displot(cars.SP)
#data is slightlt right skewed
plt.boxplot(cars.SP)
#ther are sevreal outlier
sns.distplot(cars.WT)
plt.boxplot(cars.WT)
# there are several outlier
#Now let us plot joint plot is to show scatter
#hisogram

import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars["MPG"])

#now let us plot the count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
#countt plot shows how many times the each value occured
# 92 HP value occured 7 times

#QQ plot
from scipy import stats
import pylab
stats.probplot(cars.MPG,dist="norm",plot=pylab)
plt.show()
# MPG data is normally distrubuted
# there are 10 scatter plots need to be plotted , one by one
# to plot so we can use pair plot
import seaborn as sns
sns.pairplot(cars.iloc[:,:])
# only for the pair plot use the theree factor# linear:- normal direction:- strenght:-
#you can check the collinerity problem between  the input
#you can check plot between SP AND HP , they are strongly correletade
#same way you can check WT AND VOL , it is also strong corrrelation


# now let us check the r value between variables
cars.corr()

# you cam check the SP and HP , r value is 0.97 and same way
# you can check WT and VOL  it has got 0.999 which is greater

# now let although we obsered that stogly correlate d pairs
#still we will go fro linear regression
import statsmodels.formula.api as smf
ml1=smf.ols('MPG~WT+VOL+SP+HP', data=cars).fit()

ml1.summary()

# R squared value obsered is 0.771<0.85
# p value of WT and VOL is 0.814 and 0.556 which is very heigh
# it means itis greater than 0.05 , WT and VOL columns
# we need to ignore
# or deleted. instead deleting 81 entries
# now let us check the row wise outlier
#identify is there any influential value.
# to check you can use influential index
import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
# 76 is the value which has got outliers
#go to data frame and check 76th entry 
# let us delete that entry
cars_new=cars.drop(cars.index[[76]])

#again apply the regression to cars_new
ml_new=smf.ols('MPG~WT+VOL+HP+SP', data=cars_new).fit()
ml_new.summary()
#r-sqaured value us 0.819 but p values are same , hence not scatter
# now next option is delete the column but
# question is which column is to be deleted
# we have alredy checked correlation fector r
# VOL has got -0.529 and  for WT=-0.526
#WT is less hence can  be deleted

#another apporocach is to check the collinearity
# rsquare is giving that value
# we will have to apply regression W.r.t .x1 and input
rsq_hp=smf.ols('HP~WT+VOL+SP', data=cars).fit().rsquared
vif_hp=1/(1-rsq_hp)

#VIF is variance influential factor calculating VIF help
rsq_wt=smf.ols('WT~HP+VOL+SP', data=cars).fit().rsquared
vif_wt=1/(1-rsq_hp)

rsq_vol=smf.ols('VOL~HP+WT+SP', data=cars).fit().rsquared
vif_vol=1/(1-rsq_vol)

rsq_sp=smf.ols('SP~HP+WT+VOL', data=cars).fit().rsquared
vif_sp=1/(1-rsq_sp)
# VIF_wt =639.53 and vif_vol=638.89 henec vif_wt
# is greater , thumb rule is vif sshould not be gerater than 1

#storing the values in dataframe
d1={'Variables':['HP','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
vif_frame=pd.DataFrame(d1)
vif_frame

# let us drop WT and apply correlation to remailing three
final_ml=smf.ols('MPG~VOL+SP+HP',data=cars).fit()
final_ml.summary()
#r square is 0.770 and p value 0.00,0.012<0.005

#prediction
pred=final_ml.predict(cars)

#QQ plot
res=final_ml.resid
sm.qqplot(res)
plt.show()
# this QQ plot is an residual which is obtained on training'
# errors are obtained on the test data

stats.probplot(res,dist="norm",plot=pylab)
plt.show()

# let us plot the residual plot which takes the residual value
# and the data
sns.residplot(x=pred,y=cars.MPG, lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt.title("Fitted VS Residual")
plt.show()
# residual plots 

# spliting the data into train and test data
from sklearn.model_selection import train_test_split
cars_train,cars_test=train_test_split(cars,test_size=0.2)
#preparingthe model on train data
model_train=smf.ols('MPG~VOL+SP+HP', data=cars_train).fit()
model_train.summary()
test_pred=model_train.predict(cars_test)
#test_errors
test_errors= test_pred-cars_test.MPG
test_rmse=np.sqrt(np.mean(test_errors*test_errors))
test_rmse
