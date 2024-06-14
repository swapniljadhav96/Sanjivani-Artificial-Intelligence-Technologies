# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:08 2023

@author: suraj
"""


#####################################################################
'''-------------------------------day 10/10/23------8.00---------------------------'''
#one hot encoder
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
#use the ethnic diversity dataset
df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df
df.columns
'''Out[38]: 
Index(['Employee_Name', 'EmpID', 'Position', 'State', 'Zip', 'Sex',
       'MaritalDesc', 'CitizenDesc', 'EmploymentStatus', 'Department',
       'Salaries', 'age', 'Race'],
      dtype='object')'''
#we have Salaries and age as numerical column let us make them
#at position 0 and 1 so to make further data processing

df=df[['Salaries','age','Employee_Name', 'EmpID', 'Position', 'State', 'Zip', 'Sex',
       'MaritalDesc', 'CitizenDesc', 'EmploymentStatus', 'Department','Race']]
#check the dataframe in the varible explorer
#we want only nominal data and ordinal data for processing
#hence skipped 0 th and 1st column and applied to one hot encoder
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())
