# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:13:10 2024

@author: suraj
"""

#handling the duplicates
#identifing the duplicates and remove the that duplicate record
#duplicated and drop_duplicated are both are two function/methods two identifiy that record
#in this we can apply the duplicate function over the row not the column
import pandas as pd
df_new=pd.read_csv("education.csv")
df_new
duplicate=df_new.duplicated()
#we can apply the duplicate method on the single column
#output of this function is single column

#if the duplicate record are occur it can show  the output true
#if there is no duplicte record output is false
#series will be creted
duplicate
sum(duplicate)
#output will 0
'''sum(duplicate)
Out[24]: 0'''
#let us import the another dataset

import pandas as pd
df_new1=pd.read_csv("C:/Data Science/data_set/mtcars_dup.csv")
df_new1

duplicate1=df_new1.duplicated()
duplicate1
'''
0     False1     False2     False3     False4     False5     
False6     False7     False8     False9     False10    False11    False12    
False13    False14    False15    False16    False17     True18    False19    False
20    False21    False22    False23     True24    False25    
False26    False27     True28    False29    False30    False31    False
dtype: bool'''
sum(duplicate1)     #3
#there are 3 duplicate record
#drop_duplictes
# we will drop all the duplicte
df_new2=df_new1.drop_duplicate()
duplicate1=df_new1.duplicated()
duplicate
sum(duplicate)
'''sum(duplicate)
Out[37]: 0'''