# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:18:52 2024

@author: suraj
"""
#HR_DT dataset
'''4.	In the recruitment domain, HR faces the challenge of predicting
 if the candidate is faking their salary or not. 
 For example, a candidate claims to have 5 years of experience and earns
 70,000 per month working as a regional manager.
 The candidate expects more money than his previous CTC. We need a way to 
 verify their claims (is 70,000 a month working as a regional manager 
with an experience of 5 years a genuine claim or does he/she make
 less than that?) Build a Decision Tree and Random Forest model with 
 monthly income as the target variable. '''
'''
Business Objective
Minimize: To reduce costs, risks, or inefficiencies in a business process.

Maximize: To increase profits, efficiency, or positive outcomes.
'''
"""
Data Dictionary

 Features                                      Type             Relevance
0   Position of the employee                 Qualititative data  Relevant
1   no of Years of Experience of employee    Continious data     Relevant
2   monthly income of employee               Continious data     Relevant

"""

import pandas as pd

df = pd.read_csv("C:/Data Science/14_a_ML_Assigement/4_Random_forest_tree/dataset/HR_DT.csv")
###########################
#shape of the dataset
df.shape
#############################
#column of the dataset
df.columns 
############################
#sample from the dataset
df.head
##############################
#datatype of the dataset
df.dtypes
##############################
#now we convert into numeric data 
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()

df.rename(columns = {' monthly income of employee' : 'Monthly_income_of_employee' , 
                     'Position of the employee' : 'Position_of_the_employee' ,
                     'no of Years of Experience of employee': 'no_of_Years_of_Experience_of_employee'} 
          , inplace = True)

df['Monthly_income_of_employee_n'] = enc.fit_transform(df['Monthly_income_of_employee'])
y = df.Monthly_income_of_employee_n

df['Position_of_the_employee_n'] = enc.fit_transform(df['Position_of_the_employee'])
df['no_of_Years_of_Experience_of_employee_n'] = enc.fit_transform(df['no_of_Years_of_Experience_of_employee'])

df.columns
df.drop(['Position_of_the_employee' , 'Monthly_income_of_employee' , 'no_of_Years_of_Experience_of_employee' ] , axis = "columns")
######################################################
#spliting the dataset into th traning and testing dataset
from sklearn.model_selection import train_test_split
df_train , df_test , y_train ,y_test = train_test_split(df,y,test_size=0.2)
#######################################################
#now applying the random forest algo on the taring  dataset
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
#n_estimators : number of trees in the forest

model.fit(df_train , y_train)

model.score(df_test , y_test)
y_predicted = model.predict(df_test)
###########################################################
#creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm
###############################
#%matplotlib inline
#checking the matplot for the confusion matrix
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(cm , annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
