# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:17:59 2024

@author: suraj
"""


###############################################
#outlier treatement
import pandas as pd
import seaborn as sns

#let us import the dataset
df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df

#now let us find the outlier in the salaries column
sns.boxplot(df.Salaries)
#there are outlier
#let us check there are outlier in the age column
sns.boxplot(df.age)
#there are no outlier
#we can calclaute the IQR

IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)

#have observation that the IQR in the variable explore
#no becaue the IQR are in the capaitalluze letter
#treated as constant
IQR
#Out[48]: 28359.945

#but if we will try as I,Iqr or iqr then it is showing
#I=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#Iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)

lower_limit=df.Salaries.quantile(0.25)-1.5*IQR    #make the lower limit value as 0 not the negative
lower_limit         #Out[51]: -19446.9675
upper_limit=df.Salaries.quantile(0.75)-1.5*IQR 
upper_limit         #Out[52]: 8912.9775

#negative vaule are not the lowre limit so make it as 0
# for change go to the varible explore and make it as 0 directly
###############################################
#trimming
import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#you can check outlier_df column in the varible explore
#floting the point number,if possible in varible explore
#now trimm that
df_trimmed=df.loc[~outliers_df]
df_trimmed      #it can show the trimmed element
df.shape        #without the trimed shape is
#Out[60]: (310, 13)
df_trimmed.shape        #we trimmed this elemnt
#Out[61]: (34, 13)

################################################################
##repalcemet technique
#masking technique
#drawback of trimming is we can loosing the data
import pandas as pd
import seaborn as sns
import numpy as np
#let us import the dataset

df=pd.read_csv("C:/Data Science/data_set/ethnic diversity.csv")
df.describe()
'''              EmpID           Zip       Salaries         age
count  3.100000e+02    310.000000     310.000000  310.000000
mean   1.199745e+09   6569.732258   36670.102742   38.696774
std    1.829600e+08  16933.864054   21075.942369    9.258163
min    6.020003e+08   1013.000000       0.000000   23.000000
25%    1.101024e+09   1901.250000   23092.950000   31.000000
50%    1.203032e+09   2132.000000   34554.745000   39.000000
75%    1.378814e+09   2357.000000   51452.895000   46.000000
max    1.988300e+09  98052.000000  108304.000000   54.000000'''
#recored number 23 has got the outliers
# map all the outlier to the upper limit
df_replace=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
df_replace
'''             0
0     674.2800
1     674.2800
2     674.2800
3    8912.9775
4    8912.9775
..         ...
305  8912.9775
306  8912.9775
307  8912.9775
308  8912.9775
309  8912.9775

[310 rows x 1 columns]'''
# if the value is lower than the lower limit ie is it has oulier
#so make it as the lower limit value  to that entry 
#if the value is greater than the upper limit ie is it has outlier
#so make it upper limit value to it 
#other wise make it as the same  for that columns
###################

sns.boxplot(df_replace[0])
#all the outiler are remove
###########################################################
#Winsorizer
#install the feature engine :- pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr',
                    tail='both',
                    fold=1.5,
                    variables=['Salaries']
                    )
#copy Winsorizer and paste in help tab of
#top right Windows , study the method

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])
