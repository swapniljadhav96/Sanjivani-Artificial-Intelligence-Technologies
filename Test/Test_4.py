# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:34:10 2024

@author: suraj
"""


#Q1 write the python function that takes liste and returns true 
list1=[1,2,4,5]
list2=[6,5,77,7]
for i in list1:
    for j in list2:
        if i==j:
            print("True")
            break
        
    
#Q2
list1=[1,2,3,4,5]
list2=[num+6 for num in list1]
list2

#Q3
#write the python program to reverse the a string
x='abcdef'
print(x[::-1])
#Q4
dict1={
       'maha':'mumbai',
       'gujarat':'ahmadabad',
       'up':'lakhow',
       'karanatka':'bangolre'
       }
for i in dict1:
    print(i,dict1[i])

#Q6
x='suraj.txt'
with open(x) as file:
    content=file.read()
print(content)

#Q7
n=int(input("Enter the value:"))
for i in range(n):
    print(' ')

#Q8
even=lambda x:x%2==0
lst=[num for num in range(10) if even(num)]
lst 
#Q9
import pandas as pd
sample={
        'name':['Anan','Dinu','Ramu','Ganu','Emilly','Mahesh',"jayesh",'Venkat','Ajay','Dhanesh'],
        'Score':[12.59,16.5,'np.nan',9,20,14.5,'np.nan',8,19,77],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes'],
        'labels':['a','b','c','d','e','f','j','i','j','g']
        }
df=pd.DataFrame(sample)
df
df.columns
df.index

#Q10
import matplotlib.pyplot as plt    

plt.plot(list1,'-')
