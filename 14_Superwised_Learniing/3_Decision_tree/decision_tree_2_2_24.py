# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:24:29 '2024

@author: suraj
"""

#day 2_2_24
#decision tree
'''import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/Data Science/14-superwised_learniing/dataset_ml/credit.csv")

data.isnull().sum()
data.dropna()
data.columns
data=data.drop(['phone'],axis=1)


#converting into biner
lb=LabelEncoder()
data["checking_balance"]==lb.fit_transform(data["checking_balance"])
data["credit_history"]==lb.fit_transform(data["credit_history"]) 
data["purpose"]==lb.fit_transform(data["purpose"]) 
data["savings_balance"]==lb.fit_transform(data["savings_balance"]) 
data["employment_duration"]==lb.fit_transform(data["employment_duration"])  
data["other_credit"]==lb.fit_transform(data["other_credit"])
data["housing"]==lb.fit_transform(data["housing"]) 
data["job"]==lb.fit_transform(data["job"])  

#data["default"]= lb.fit_transform(data["default"])
data

data['default'].unique()

data["default"].value_counts()
colnames=list(data.columns)


predictors=colnames[:15]
predictors
target=colnames[15]

#splitting data into traing and testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(data,test_size=0.3)


from sklearn.tree import DecisionTreeClassifier as DT

#help(DT)
model=DT(criterion='entropy')
model.fit(train[predictors],train[target])
preds_test=model.predict(test[predictors])
preds_test
pd.crosstab(test[target],preds_test,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_test==test[target])
#################################
# now check the accuracy on training dataset
preds=model.predict(train[predictors])
preds
pd.crosstab(train[target],preds,rownames=['Actual'],colnames=['predictions'])
np.mean(preds==test[target])'''


##########################################################
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("C:/Data Science/14-superwised_learniing/dataset_ml/credit.csv")

data.isnull().sum()

data.dropna()
data.columns

data=data.drop(["phone"],axis=1)

#converting into binary

lb=LabelEncoder()
data["checking_balance"]=lb.fit_transform(data["checking_balance"])
data["credit_history"]=lb.fit_transform(data["credit_history"])
data["purpose"]=lb.fit_transform(data["purpose"])
data["savings_balance"]=lb.fit_transform(data["savings_balance"])
data["employment_duration"]=lb.fit_transform(data["employment_duration"])
data["other_credit"]=lb.fit_transform(data["other_credit"])
data["housing"]=lb.fit_transform(data["housing"])
data["job"]=lb.fit_transform(data["job"])

#data["default"]=lb.fit_transform(data[default])

data['default'].unique()
data['default'].value_counts()
colnames=list(data.columns)

predictors=colnames[:15]
target=colnames[15]


#splitting data into training and testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(data,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT

#help(dT)
model=DT(criterion='entropy')
model.fit(train[predictors],train[target])
preds=model.predict(test[predictors])
preds
pd.crosstab(test[target],preds,rownames=['Actual'],colnames=['predictions'])
np.mean(preds==test[target])
##################################################

#now let us check accuracy on training dataset

preds_train = model.predict(train[predictors])
pd.crosstab(train[target], preds_train,rownames=['Actual'],colnames=['predictions'])
np.mean(preds_train==train[target])

##############################################
##''' accuarcy of the train data is less than the test data so the model is over fit model'''
