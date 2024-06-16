# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:23:46 2024

@author: suraj
"""

import scipy.stats as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

data=pd.read_csv("C:/Data Science/16_Linear_regression/1_Corelation/datasets/SampleSuperstore.csv")

#corelation using numpy

np.corrcoef(data["Sales"],data['Profit'])
'''
Out[5]: 
array([[1.        , 0.47906435],
       [0.47906435, 1.        ]])
'''

#correlation using scipy
st.pearsonr(data["Sales"], data["Profit"])
'''Out[6]: PearsonRResult(statistic=0.47906434973770595, pvalue=0.0)'''

#scatter plot
sns.scatterplot(data["Sales"],data["Profit"])

# form the above diagram we can see that the data are the distributed moderate postive correction correlation is 
# 

#paiplot
sns.pairplot(data)

#check the each correlation realtion in the graph

#in padans 
data.corr()
'''Out[9]: 
             Postal Code     Sales  Quantity  Discount    Profit
Postal Code     1.000000 -0.023854  0.012761  0.058443 -0.029961
Sales          -0.023854  1.000000  0.200795 -0.028190  0.479064
Quantity        0.012761  0.200795  1.000000  0.008623  0.066253
Discount        0.058443 -0.028190  0.008623  1.000000 -0.219487
Profit         -0.029961  0.479064  0.066253 -0.219487  1.000000'''


#heatmap
sns.heatmap(data.corr())
#read each and every part of the column of the heatmap
#you need to make the heatmap fro eda

#scatter plot
plt.figure(figsize=(15,8))
plt.subplot(231)
sns.scatterplot(data["Sales"],data['Profit'])
plt.subplot(232)
sns.scatterplot(data["Discount"],data['Profit'])
plt.subplot(233)
sns.scatterplot(data["Quantity"],data['Profit'])
plt.subplot(234)
sns.scatterplot(data["Discount"],data['Sales'])
plt.subplot(235)
sns.scatterplot(data["Discount"],data['Quantity'])


#spearman r
from scipy.stats import spearmanr
spearmanr(data['Sales'],data['Profit'])

st.pearsonr(data['Sales'], data['Profit'])
