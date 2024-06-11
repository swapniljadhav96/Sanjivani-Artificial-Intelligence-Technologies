# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:07 2023

@author: suraj
"""


#######################################################
#missing value
#three type
#1.mcar
#2. MAR
#3. MNCR
import pandas as pd
import numpy as np
df=pd.read_csv("C:/Data Science/data_set/modified ethnic.csv")
df
#check the null value
df.isna()
#how many null value count
df.isna().sum()
'''Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries            32
age                 35
Race                25
dtype: int64'''