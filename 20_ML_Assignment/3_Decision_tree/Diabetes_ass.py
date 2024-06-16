# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:50:42 2024

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

1. Pregnancies , No of time the individual has been pregrant , Relavent data
2. Glucose , Glucose level of that individual ,  Relavent data
3. BloodPressure , the blood pressure levels of that indidual , Relevant data
4. SkinThickness , how thick the skin of that individula is   irrelevant
5. Insuline , does the indvisual take insuline, releavant
6. BMI , BMI of an individual ,  relevant
7. Age , Age of that individual ,  relevant
8. DiabetesPredigreeFunction  , irrelevant
"""

 '''
import pandas as pd
import numpy as np
diabe=pd.read_csv("C:/Data Science/14_a_ML_Assigement/3_Decision_tree/dataset/Diabetes.csv")
diabe
##################
#shape of the data
diabe.shape     #Out[79]: (768, 9)
###############################
#size o fthe dataset
diabe.size      #Out[80]: 6912
###############################
#columns
diabe.columns
##############################
#columns
diabe.describe()
'''        Number of times pregnant  ...   Age (years)
count                 768.000000  ...    768.000000
mean                    3.845052  ...     33.240885
std                     3.369578  ...     11.760232
min                     0.000000  ...     21.000000
25%                     1.000000  ...     24.000000
50%                     3.000000  ...     29.000000
75%                     6.000000  ...     41.000000
max                    17.000000  ...     81.000000 '''

#######################################
# checking te null value
a=diabe.isnull()
a.sum()
########################################
diabe.dtypes
''' Number of times pregnant          int64
 Plasma glucose concentration      int64
 Diastolic blood pressure          int64
 Triceps skin fold thickness       int64
 2-Hour serum insulin              int64
 Body mass index                 float64
 Diabetes pedigree function      float64
 Age (years)                       int64
 Class variable                   object'''
#####################################
#now we Want to rename the column name 
diabe.columns = diabe.columns.str.replace(' ', '_')
diabe
##################################################

# now let us convert th class varible column into the  numerical form
from sklearn.preprocessing import LabelEncoder
le_class=LabelEncoder()

# we are rename the column which is made with the numerical value
diabe['Outcome']= le_class.fit_transform(diabe['_Class_variable'])
diabe=diabe.drop(['_Class_variable'], axis='columns' )
X=diabe.drop('Outcome', axis='columns')
y =diabe.Outcome
############################################
#now split the dataset into the test and train dataset form

from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test= train_test_split(X,y,test_size=0.2)
################################################
#now we can apply the decision tree on the dataset
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

#now let us a 
model.predict([[6,148,72,35,0,33.6,0.627,50]])

model.predict([[1,85,66,29,0,26.6,0.351,31]])
