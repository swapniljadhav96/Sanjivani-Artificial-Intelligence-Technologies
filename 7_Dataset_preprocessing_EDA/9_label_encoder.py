# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:08 2023

@author: suraj
"""

#################################################
#label encoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df
#creating the instance the label encoder
labelencoder=LabelEncoder()

#split your data ito the input and out put varaible
X=df.iloc[:,0:9]  #first 8  column in x and 9 column in y
y=df['Race']
df.columns
'''Out[48]: 
Index(['Salaries', 'age', 'Employee_Name', 'EmpID', 'Position', 'State', 'Zip',
       'Sex', 'MaritalDesc', 'CitizenDesc', 'EmploymentStatus', 'Department',
       'Race'],
      dtype='object')'''
#we have nominal data sex ,MartialDesc CitizenDesc #
#we wnt to convert the lable encoder
#you can apply the any column over the dataset
X['Sex']=labelencoder.fit_transform(X['Sex'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])
#label encoder y
y=labelencoder.fit_transform(y)

#this is going to create an array hence convert
#it back into the dataframe
y=pd.DataFrame(y)
df_new=pd.concat([X,y],axis=1)
#if you will see the vraible explorer  , y do not have the column name
#hence rename the column
df_new=df_new.rename(columns={0:'Race'})
####################################################################
