# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:12:31 2024

@author: suraj
"""
#fraud check dataset 
'''3.	Build a Decision Tree & Random Forest model 
on the fraud data. Treat those who have 
taxable_income <= 30000 as Risky 
and others as Good (discretize the taxable income column).'''
#business understanding of the dataset 
'''
'1. Business Problem
    ~for a banking related or finance related application , it is important to 
    track a customer for the banks and identify them and classify them into 
    different categories of customers based on certain parametrs , thoughts having 
    high taxable amount are earning more money and based on few more features we
    can identify that which customers have high potential of taking the loans from
    the bank ,Treat those who have taxable_income <= 30000 as Risky 
    and others as Good 
    
    
1.1 what is business objective?
    ~To understand the features of the customers on classify them into risky and good 
    customers
    ~develope understanding of the customers features
    
1.2 Are there any constraints
    ~Correctness of data, and deviation from the results
    ~some feature might not be contributing to the end results

2. Create a Data Dictionary 
name of feature 
description 
type 
relevance

1. Undergrad , is the individual a Undergrad student ,  Relavent data
2. Maritial_Status , is the individual married ,  Relavent data
3. Taxable_Income , what is the income of the individual, Relevant data
4. city_Population , Population of the city,irrelevant
5. Work_experience , for how long that individual is working for ,  releavant
6. Urban , is that individual a resident of a urban city ,  relevant

"""

""" 
3. Data Preprocessing
3.1 Data Cleaning , feature engineering ,etc
"""
'''
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Data Science/14_a_ML_Assigement/4_Random_forest_tree/dataset/Fraud_check.csv")
##################################
#shape of the dataset
df.shape
#################################
#column of the dataset
df.columns
####################################
#datatype of the dataset
df.dtypes
"""

Undergrad          object
Marital.Status     object
Taxable.Income      int64
City.Population     int64
Work.Experience     int64
Urban              object
dtype: object
 """

##############################
#taking the sample from the dataset
df.head
############################
#performing descitization on the Taxable.Income Data based on given condition
#Taxable.Income <= 30000 ,into Risky or good
# Define the condition
condition = (df['Taxable.Income'] <= 30000)

# Create a new column 'Risk_Category' based on the condition
df['Label'] = np.where(condition, 'Risky', 'Good')
###########################################
#label encoding
#now we convert into numeric data 
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
df['Label'] = enc.fit_transform(df['Label'])

#seprate the target variable
y = df.Label

X = df.drop(['Label'] , axis = "columns")

X.columns

X['Undergrad_n'] = enc.fit_transform(X['Undergrad'])
X['Marital.Status_n'] = enc.fit_transform(X['Marital.Status'])
X['Taxable.Income_n'] = enc.fit_transform(X['Taxable.Income'])
X['City.Population_n'] = enc.fit_transform(X['City.Population'])
X['Work.Experience_n'] = enc.fit_transform(X['Work.Experience'])
X['Urban_n'] = enc.fit_transform(X['Work.Experience'])

Xn = X.drop(['Undergrad', 'Marital.Status', 'Taxable.Income', 'City.Population', 'Work.Experience','Urban'] , axis = 'columns')
y

############################################
#the data is split into the traning and testing dataset
from sklearn.model_selection import train_test_split
Xn_train , Xn_test , y_train ,y_test = train_test_split(Xn,y,test_size=0.2)
##########################################
#now applying the random forest _algo on it
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
#n_estimators : number of trees in the forest

model.fit(Xn_train , y_train)

model.score(Xn_test , y_test)
y_predicted = model.predict(Xn_test)
############################################
#confusion matrix is created
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm
#############################################
#%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(cm , annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
