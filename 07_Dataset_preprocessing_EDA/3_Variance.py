# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:07 2023

@author: suraj
"""



#################################day 9_10_23
#variance
#zero and naer zero variance features
#if there are no variance in the feature , then ml model
#will not get any intellgence , so it is betttre  to ignore that feature

import pandas as pd
#let us import the dataset
df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df.var()
'''EmpID       3.347435e+16
Zip         2.867558e+08
Salaries    4.441953e+08
age         8.571358e+01
dtype: float64'''
#here email and zip are the nominal data
#salarries has    4.441953e+08 it has no feature near to zero as also in the age
#you can check directly var by using the column wise also 
df.var()==0
#non of them are equal to zero
'''EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool'''
#axis =0 then it is gonig to give the sam e results 
# if there are varienace then it give true 
df.var(axis=0)==0
'''EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool'''