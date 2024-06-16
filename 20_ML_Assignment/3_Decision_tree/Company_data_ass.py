# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:55:38 2024

@author: suraj
"""

#assigment_decision tree
#dataset Company_data

"""1.	A cloth manufacturing company is interested to know about the different
attributes contributing to high sales. Build a decision tree & random forest 
model with Sales as target variable (first convert it into categorical variable).

 Business Problem
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

1. CompPrice , Component Price , Relavent data
2. Income , Income associated with that product ,  Relavent data
3. Advertising , Advertising cost associated with that product , Relevant data
4. Population , Population to which that product is accesseble , irrelevant
5. Price , Price of that product ,irreleavant
6. ShelveLoc , Occupation of an individual  relevant
7. Age , Age group for which that product is targeted to  irrelevant
8. Education  irrelevant
9. Urban  irrelevant
10. US  relevant
"""



import pandas as pd

company=pd.read_csv("C:/Data Science/14_a_ML_Assigement/3_Decision_tree/dataset/Company_Data.csv")
company
company.head(10)
################################
#checking the column of the dataset
company.columns
'''Index(['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price',
       'ShelveLoc', 'Age', 'Education', 'Urban', 'US'],
      dtype='object')
'''
################################
company.size    #these number of the data entry are present:-4400
company.shape   #Out[55]: (400, 11) 
################################
#checking the null value
a=company.isnull()  
a.sum()
# in the datset there are no null value are present
#################################
a=company.isna()
a.sum()
# no nana value are present in the dataset
################################
#we will apply the describe function to check the description
a=company.describe()
a
'''            Sales   CompPrice      Income  ...       Price         Age   Education
count  400.000000  400.000000  400.000000  ...  400.000000  400.000000  400.000000
mean     7.496325  124.975000   68.657500  ...  115.795000   53.322500   13.900000
std      2.824115   15.334512   27.986037  ...   23.676664   16.200297    2.620528
min      0.000000   77.000000   21.000000  ...   24.000000   25.000000   10.000000
25%      5.390000  115.000000   42.750000  ...  100.000000   39.750000   12.000000
50%      7.490000  125.000000   69.000000  ...  117.000000   54.500000   14.000000
75%      9.320000  135.000000   91.000000  ...  131.000000   66.000000   16.000000
max     16.270000  175.000000  120.000000  ...  191.000000   80.000000   18.000000

[8 rows x 8 columns]'''

##############################
# getting the information of the dataset  we use the info function
company.info
#############################
company.dtypes
'''Sales          float64
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
dtype: object"'''

########################################################
# from the above line we can say that in the above dataset there are there are 
#text data are present so we want to convet that dataset into the categorical form
 
'''Categorical data'''
# we are separate the input and output column in separte dataframe
# we are converting the datafram eword into the numerical form
from sklearn.preprocessing import LabelEncoder
le_ShelveLoc=LabelEncoder()
le_Urban=LabelEncoder()
le_Us=LabelEncoder()

# we are rename the column which is made with the numerical value
company['ShelveLoc']= le_ShelveLoc.fit_transform(company['ShelveLoc'])
company['Urban']= le_ShelveLoc.fit_transform(company['Urban'])
company['US']= le_ShelveLoc.fit_transform(company['US'])

########################

# Separate features and target variable
from sklearn.tree import DecisionTreeRegressor
X = company.drop("Sales", axis='columns')
y = company["Sales"]

# Decision Tree model
model = DecisionTreeRegressor()
model.fit(X, y)

# Example predictions
# Assuming ShelveLoc=2, Urban=1, US=0 for the first example
prediction_1 = model.predict([[115, 95, 5, 110, 117, 26, 20, 0, 1, 1]])
print("Prediction 1:", prediction_1)
# Assuming ShelveLoc=2, Urban=1, US=1 for the second example
prediction = model.predict([[165, 70, 8, 200, 130, 33, 20, 1, 0, 1]])
print("Prediction 1:", prediction)


    
    
    
  
