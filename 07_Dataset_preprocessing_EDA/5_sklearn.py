# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:07 2023

@author: suraj
"""



#######################################################
#sklearn
#install:- pip install sklearn
'''Scikit-Learn, also known as sklearn is a python library to
 implement machine learning models and statistical modelling. 
 Through scikit-learn, we can implement various machine learning 
 models for regression, classification, clustering, 
 and statistical tools for analyzing these'''
import pandas as pd
import numpy as np
#give the file path and correct the error
from sklearn.impute import SimpleImputer
df=pd.read_csv("C:/Data Science/data_set/modified ethnic.csv")
df
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
mean_imputer
#Out[16]: SimpleImputer()
#check the dataframe
df["Salaries"]=pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))
df["Salaries"]
'''Out[18]: 
0        674.280000
1        674.280000
2        674.280000
3      47822.000000
4      36725.396007
    
305    36725.396007
306    27603.000000
307    27587.460000
308    12126.530000
309    37257.000000
Name: Salaries, Length: 310, dtype: float64'''
# After athat check the NUll vale in the dataframe
df["Salaries"].isna().sum()
#: 0
