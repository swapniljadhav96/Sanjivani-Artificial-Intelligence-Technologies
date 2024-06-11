# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:07 2023

@author: suraj
"""

########################################
#dummy variable
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Data Science/data_set/animal_category.csv")
df
#shape
df.shape
#Out[8]: (30, 5)
#drop 
df.drop(['Index'],axis=1, inplace=True)
#check of again
df_new=pd.get_dummies(df)
df_new.shape
#Out[12]: (30, 14)
#here we are getting 30 rows and 14 column
# we are getting two columns for homely and gender , one column is sufficient for each catogeriacl
#delete the second column of gender and second column of homely
df_new.drop(['Gender_Male', 'Homly_Yes'],axis=1,inplace=True)
df_new.shape
#Out[14]: (30, 12)
#now we are getting the 30,12
df_new.rename(columns={'Gender_female':'Gender','Homly_No':'house_no'})

###############################################################
#dummy varaible on the another dataset 
#do the same process for the ethnic diversity
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df
df.dtypes
'''Out[21]: 
Employee_Name        object
EmpID                 int64
Position             object
State                object
Zip                   int64
Sex                  object
MaritalDesc          object
CitizenDesc          object
EmploymentStatus     object
Department           object
Salaries            float64
age                   int64
Race                 object
dtype: object'''
#shape
df.shape
#Out[22]: (310, 13)

df.drop(['EmpID','Zip','Salaries','age'],axis=1,inplace=True)
df.shape
#Out[24]: (310, 9)
#drop the column the dummy variable
df_new2=pd.get_dummies(df)
df_new2.shape
#Out[26]: (310, 397)
df_new2.drop(['Sex_F', 'CitizenDesc_US Citizen'],axis=1,inplace=True)
df_new2.shape
#Out[28]: (310, 395)
# rename the drop column contain
df_new2.rename(columns={'Sex_M':'Gender','CitizenDesc_Non-Citizen':'Citizen'})
