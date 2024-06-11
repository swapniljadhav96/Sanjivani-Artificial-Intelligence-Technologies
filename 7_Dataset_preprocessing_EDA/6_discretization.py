# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:00:07 2023

@author: suraj
"""


##################################################################
'''------------------day-9-10-23 3.00pm--------------------------------'''
#discretization
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
data.head()     #show the first five record of the dataset/smaple data
data.head(10)  # 0 to 9 record are display
data.info()         #size of the data
#it gives size , null values,rows ,columns and datatype of the columns

data.describe()     #appllicabe fro numerical value  only
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=['low','High'])
data.Salaries_new.value_counts()

#in the above code we can descriteze the data from the variou ppoint and mark them
#with the high value and low value  
# we can divide that data from the mena and label with them with the high value
# and more value from the mean are mark with the high value
'''Out[16]: 
low     166
High    143
Name: Salaries_new, dtype: int64'''

data['Salaries_new']=pd.cut(data['Salaries'], bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(), data.Salaries.quantile(0.75),max(data.Salaries)], labels=['group1','group2','group3','group4'])
data.Salaries_new.value_counts()
'''Out[20]: 
group2    89
group4    78
group1    77
group3    65
Name: Salaries_new, dtype: int64'''
