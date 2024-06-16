# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:35:13 2024

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
####################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("C:/Data Science/14_a_ML_Assigement/4_Random_forest_tree/dataset/Fraud_check.csv")

df.head(10)
df.tail()

# 5 number summary
df.describe()

df.shape
# 600 rows and 6 columns

df.columns
'''
['Undergrad', 'Marital.Status', 'Taxable.Income', 'City.Population',
'Work.Experience', 'Urban']
'''

# check for null values
df.isnull()
# False
df.isnull().sum()
# 0 no null values

# Pair-Plot
plt.close();
sns.set_style("whitegrid");
sns.pairplot(df);
plt.show()

#####################
#rename the column
df.columns = [
    'Undergrad',
    'Marital_Status',
    'Income',
    'Population',
    'Experience',
    'Urban'
]

# Now you can access the columns
print(df.columns)

# boxplot
# boxplot on Income column
sns.boxplot(df.Income)
# In Income column 1 outliers 

sns.boxplot(df.Population)
# In Population column no outliers

# boxplot on df column
sns.boxplot(df)
# There is outliers on all columns

# histplot - show distributions of datasets
sns.histplot(df['Income'],kde=True)
# right skew and the distributed

sns.histplot(df['Population'],kde=True)
# right skew and the distributed

sns.histplot(df,kde=True)
#The data is showing the skewness 
# most of the right skiwed data

# Data Preproccesing
df.dtypes
# Some columns in int data types and some Object

# Identify the duplicates
duplicate=df.duplicated()
# Output of this function is single columns
# if there is duplicate records output- True
# if there is no duplicate records output-False
# Series is created
duplicate
# False
sum(duplicate)
# sum is 0.
# Normalize data 
# Normalize the data using norm function
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
# Apply the norm_fun to data 
df1=norm_fun(df.iloc[:,2:5])
df1
#####################################
#We merge the all the column in the df1 dataset 
df['Undergrad']
df1['Undergrad']=df['Undergrad']

df['Marital_Status']
df1["Marital_Status"]=df["Marital_Status"]

df["Urban"]
df1["Urban"]=df["Urban"]


#########################################
df.isnull().sum()
df.dropna()
df.columns
#########################################
# Converting into binary
lb=LabelEncoder()
df1["Undergrad"]=lb.fit_transform(df1["Undergrad"])
df1["Marital_Status"]=lb.fit_transform(df1["Marital_Status"])
df1["Urban"]=lb.fit_transform(df1["Urban"])

df1["Urban"].unique()
df1['Urban'].value_counts()
colnames=list(df1.columns)

predictors=colnames[:5]
target=colnames[5]

# Spliting data into training and testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(df1,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT

model=DT(criterion='entropy')
model.fit(train[predictors], train[target])
preds_test=model.predict(test[predictors])
preds_test
pd.crosstab(test[target], preds_test,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_test==test[target])

# Now let us check accuracy on training dataset
preds_train=model.predict(train[predictors])
pd.crosstab(train[target], preds_train,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_train==train[target])

# 100 % accuracy 
# Accuracy of train data > Accuracy test data i.e Overfit model
