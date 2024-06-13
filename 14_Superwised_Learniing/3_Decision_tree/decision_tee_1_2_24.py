# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:15:35 2024

@author: suraj
"""

#decision tree
#1/1/24
# to get any value information you select the word and type ctrl+i 
import pandas as pd

df=pd.read_csv("C:/Data Science/14-superwised_learniing/dataset_ml/salaries.csv")
df.head()
# we are separate the input and output column in separte dataframe
inputs=df.drop("salary_more_then_100k", axis='columns')
target=df["salary_more_then_100k"]

# we are converting the datafram eword into the numerical form
from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()
# we are rename the column which is made with the numerical value
inputs['company_n']= le_company.fit_transform(inputs['company'])
inputs['job_n']= le_company.fit_transform(inputs['job'])
inputs['degree_n']= le_company.fit_transform(inputs['degree'])
# we are ddroping the column  which is  requried for the decision tree
inputs_n=inputs.drop(['company','job','degree'], axis='columns')
target
# applying the decision tree algo on the dataset
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
#checking the output for the target value and checking the value into the output value 
# is salary of  google, Computer Engineerr, Bachelaor degree>100K?
model.predict([[2,1,0]])    # each value assing in the dataframe after applying labelencoding


# is salary of google , computer Engineer , Master degree>100K?
model.predict([[2,1,1]])
