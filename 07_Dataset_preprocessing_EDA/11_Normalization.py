# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:17:05 2023

@author: suraj
"""

######################################################
#Normalization
import pandas as pd
ethnic=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
ethnic
#now read the columns
ethnic.columns
#there are some column which are not useful , we need to drop
ethnic.drop(['Employee_Name','EmpID','Zip'],axis=1, inplace=True)
#now read minimum value and maximum value of salarie s and age
a1=ethnic.describe()
#check a1 data frame in the varible explorer
#you find minimum saralies is 0 and max is 108304
#same way you check for age, there is huge difference
#in min and max .value . Hence we are going for normalization
#first we will have to convert non-numerical data to label encoding'
ethnic =pd.get_dummies(ethnic, drop_first=True)
#Normalization function written where ethnic argument is passed
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(ethnic)
b=df_norm.describe()
#error in the function are braces
#if you will observe the b frame
#it has dimension 8,81
#earlier in a they were 8,11 it is because all non_numeric
#data has been converted to numeric using label encoding

##########################################################