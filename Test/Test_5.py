# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:35:08 2024

@author: suraj
"""


#Q1write the python program to check if a list is empty
list1=[1,2,3,4]
i=len(list1)
if i==0:
       print('empty')
else:
       print('not empty')

#Q2 sing the list comprehension construct a list from the square of 
#each element in list
list1=[1,2,3,4]
lst=[num**2 for num in list1]
print(lst)


#Q3 write the python program to check whether a given key is already exist or not
dict1={
       'maha':'mumbai',
       'gujarat':'aheamdabad',
       'up':'asd',
       'rajastan':'kota'
       }
dict1
for maha in dict1:
    print('is present')
    break

#Q4
dict1={f'{x}':x for x in range(100,160,10)}

dict1


#Q5 create a dataframe which comparieses coureses,fees,duration
# add tutorcolumn
import pandas as pd
sample={
        'coures':['python','c','c++'],
        'fees':[1123,324,2334],
        'duration':['12days','23days','34days']
        }
df=pd.DataFrame(sample)
df
df['add_tutor']=[1,2,3,]
df

#Q6
file1=df.to_csv()
print('file1')

#Q7
n=int(input('Enter the number'))
def mult(n):
    for i in range(n):
        print(i)
        

mult(n)


#Q8 
mul=lambda a,b:a*b
mul(2,4)



#Q9
import numpy as np 
arr = np.array([2,4,0,3,7])    
arr.any()
    
#Q10

import matplotlib.pyplot as plt
languages = ['Java','Python','PHP','JavaScript','C#','C++']    
Popularity = [22.2,23.7,8.8,8,7.7,6.7]    
plt.bar(languages,Popularity)
plt.show()
