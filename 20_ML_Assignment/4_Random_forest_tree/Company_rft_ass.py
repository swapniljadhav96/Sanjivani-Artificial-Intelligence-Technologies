# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:56:56 2024

@author: suraj
"""


"""
1. Business Problem
    For a Cloth Manufacturing company , it is an important of them to know about
    what are the factors that are responsible for high sales for their product.
    so that they can take care of these aspect and develope their product 
    accordingly
    
1.1 what is business objective?
    ~To understand the factors that are leading to high sales of the product and 
    maintain them
    ~
    
1.2 Are there any constraints
    ~
    ~

2. Create a Data Dictionary 
name of feature 
description 
type 
relevance

1. CompPrice , Component Price , ~ , Relavent data
2. Income , Income associated with that product , ~ , Relavent data
3. Advertising , Advertising cost associated with that product , ~  , Relevant data
4. Population , Population to which that product is accesseble ,~ , irrelevant
5. Price , Price of that product , ~ , irreleavant
6. ShelveLoc , Occupation of an individual , ~ , relevant
7. Age , Age group for which that product is targeted to , ~ , irrelevant
8. Education , ~ , ~ , irrelevant
9. Urban  , ~ , ~ , irrelevant
10. US , ~ , ~ , relevant
"""

""" 
3. Data Preprocessing
3.1 Data Cleaning , feature engineering ,etc
"""

import pandas as pd

#read the csv file
df = pd.read_csv("C:/Data Science/14_a_ML_Assigement/4_Random_forest_tree/dataset/Company_Data.csv")
##################################
#display the top 5 records
df.head()
####################################
#checking the columns
df.columns
#################################
#checking the DataTypes
df.dtypes
""" 
Sales          float64
CompPrice        int64
Income           int64
Advertising      int64
Population       int64
Price            int64
ShelveLoc       object
Age              int64
Education        int64
Urban           object
US              object
dtype: object
"""
####################################

#converting the Target variable to categorical data by rounding it 
y = round(df['Sales'])
####################################

#Seperating the Target variable from the main dataframe
X = df.drop('Sales' ,  axis = 'columns')
###################################

#now we use the labelEncoder in order to convert the numeric data to 
#categorical data
from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()

X.columns

X['CompPrice_n'] = enc.fit_transform(X['CompPrice'])
X['Income'] = enc.fit_transform(X['Income'])
X['Advertising_n'] = enc.fit_transform(X['Advertising'])
X['Population_n'] = enc.fit_transform(X['Population'])
X['Price_n'] = enc.fit_transform(X['Price'])
X['ShelveLoc_n'] = enc.fit_transform(X['ShelveLoc'])
X['Age_n'] = enc.fit_transform(X['Age'])
X['Education_n'] = enc.fit_transform(X['Education'])
X['Urban_n'] = enc.fit_transform(X['Urban'])
X['US_n'] = enc.fit_transform(X['US'])

#now we drop the old features
Xn = X.drop(['CompPrice', 'Income', 'Advertising', 'Population', 'Price','ShelveLoc', 'Age', 'Education', 'Urban', 'US'] , axis = 'columns')
y

########################################
#we spliting the data for training and testing
from sklearn.model_selection import train_test_split
Xn_train , Xn_test , y_train ,y_test = train_test_split(Xn,y,test_size=0.2)

##########################################
#now we use the random_forest_algo
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
#n_estimators : number of trees in the forest

model.fit(Xn_train , y_train)

model.score(Xn_test , y_test)
y_predicted = model.predict(Xn_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm

#%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(cm , annot = True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
