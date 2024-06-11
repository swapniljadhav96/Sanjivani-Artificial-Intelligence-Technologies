# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:17:05 2023

@author: suraj
"""


'''-------------------3.00----------------------'''
#standardization 
#normalization(x)=(x-xmin)/(xmax-xmin)

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/Data Science/data_set/mtcars.csv")
d.describe()
a=d.describe()

#intialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()
#here if you will check res, in varaible explorer or in the vraible environment then
##########################################
#standardization 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/Data Science/data_set/Seeds_data.csv")
d.describe()
a=d.describe()

#intialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()
#fromthe bove we can get the standardize data
