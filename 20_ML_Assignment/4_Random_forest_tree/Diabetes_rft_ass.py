# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:03:10 2024

@author: suraj
"""
#diabetes dataset
'''
Divide the diabetes data into train and test datasets and build a Random Forest
 and Decision Tree model with Outcome as the output variable. 
 # there are the these rows768 and this columns 9
 
1. Business Problem
    for a problem related to healthCare Sector , Diabetes is a condition that can 
    be predicted for any individual based on certain parameters of that person's
    overall health features , we have to develope a model that predicts that wheather
    a person is having the Diabetes or not . this prediction on the features help us 
    enable various analytics data , that a person having similar parameters have more
    chances of developing the diabetes in his near future and hence with this kind of
    insightful data the healthcare experts can ask the individual to take up the neccessary 
    tests to get the diabetes checked and if found positive , immediate medications can 
    be given to the individual 
    
1.1 what is business objective?
    ~To develope a model which predicts the chances of getting diabetes to a person 
    with the given feature or parameters
    ~To identify the Diabetes condition as early as possible and provide the right 
    medication as early as possible
    
1.2 Are there any constraints
    ~Data Collection 
    ~features contributing to diabetes can also be different than the features we are
    assuming and developing model for

2. Create a Data Dictionary 
name of feature 
description 
type 
relevance

1. Pregnancies , No of time the individual has been pregrant , ~ , Relavent data
2. Glucose , Glucose level of that individual , ~ , Relavent data
3. BloodPressure , the blood pressure levels of that indidual , ~  , Relevant data
4. SkinThickness , how thick the skin of that individula is  ,~ , irrelevant
5. Insuline , does the indvisual take insuline , ~ , releavant
6. BMI , BMI of an individual , ~ , relevant
7. Age , Age of that individual , ~ , relevant
8. DiabetesPredigreeFunction , ~ , ~ , irrelevant
"""
 '''

import pandas as pd

df = pd.read_csv("C:/Data Science/14_a_ML_Assigement/4_Random_forest_tree/dataset/Diabetes.csv")

df.head
###########################
#columns chaking
df.columns
###########################
#checking the datatype of the dataset
df.dtypes
""" 
df.dtypes
pregnant                      int64
Glucose                       int64
BloodPressure                 int64
skinThickness                 int64
Insuline                      int64
BMI                         float64
DiabetesPedigreeFunction    float64
Age                           int64
Outcome                      object
dtype: object
"""
#########################################
#applying  the lable encoding on the dataset
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
df['Outcome'] = enc.fit_transform(df['Outcome'])

#seprate the target variable
y = df.Outcome

X = df.drop(['Outcome'] , axis = "columns")

X.columns

X['pregnant_n'] = enc.fit_transform(X['pregnant'])
X['Glucose_n'] = enc.fit_transform(X['Glucose'])
X['BloodPressure_n'] = enc.fit_transform(X['BloodPressure'])
X['skinThickness_n'] = enc.fit_transform(X['skinThickness'])
X['Insuline_n'] = enc.fit_transform(X['Insuline'])
X['BMI_n'] = enc.fit_transform(X['BMI'])
X['DiabetesPedigreeFunction_n'] = enc.fit_transform(X['DiabetesPedigreeFunction'])
X['Age_n'] = enc.fit_transform(X['Age'])


Xn = X.drop(['pregnant', 'Glucose', 'BloodPressure', 'skinThickness', 'Insuline','BMI', 'DiabetesPedigreeFunction', 'Age'] , axis = 'columns')
y
#####################################################
#dividing the data for the traning and testing dataset

from sklearn.model_selection import train_test_split
Xn_train , Xn_test , y_train ,y_test = train_test_split(Xn,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
#n_estimators : number of trees in the forest

model.fit(Xn_train , y_train)

model.score(Xn_test , y_test)
y_predicted = model.predict(Xn_test)
######################################
#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm
##########################################################
#%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(cm , annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
