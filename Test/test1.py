# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:45:14 2023

@author: suraj
"""

'''Python
Q.1
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
import pandas as pd
import numpy as np
exam_data = {
             'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
             }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(exam_data, index=labels)
df
lst=df['qualify']
lst
for i in lst:
    if i=='yes':
        print('True')
    else:
        print('False')

#Q2Write a Python program to plot two or more lines  with different styles. 
import matplotlib.pyplot as plt
plt.plot(df['attempts'],df['score'])
plt.show()


#Q.3 Create an array[1,2,3] write L1 and L2 norm value for it
import numpy as np
from numpy import norm
array=[1,2,3]
arr=np.array
arr
l1=norm.arr()



#Q.4 Write a NumPy program create [[1, 0], [1, 2]] square array and  
#compute the determinant of a given square array.
import numpy as np 
from numpy import linalg
array=[[1,0],[1,2]]
arr=np.array([[0,1],[0,2]])
arr
a=np.linalg.det(arr)
a
#Q.5 Write a Python function to find the kth smallest element in a list.
lst=[1,2,3,4]
min(lst)
#############################
lst=[1,2,3,4]
lst=[10,15,9,8,20]
small=lambda x : min(lst)
p=small(lst)
print(p)
lst.index(p)
