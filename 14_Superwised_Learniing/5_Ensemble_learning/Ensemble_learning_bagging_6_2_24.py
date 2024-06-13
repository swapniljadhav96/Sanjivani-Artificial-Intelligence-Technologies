# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:24:37 2024

@author: suraj
"""

#ensemble techquine
import pandas as pd
df=pd.read_csv("C:/Data Science/14-superwised_learniing/dataset_ml/puma_diabetes.csv")
df
df.head()
df.isnull
df.isnull().sum()
df.describe()
df.Outcome.value_counts()
#0 500
#1 268
# there is slight imbalance in our dataset but since it is not
# major we will not worry about it!
#train test split
X=df.drop("Outcome",axis="columns")
y=df.Outcome
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
X_scaled[:3]

#in order to make your data balanced while splitting you can use Stratify
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X_scaled,y,stratify=y,random_state=10)

X_train.shape
X_test.shape
y_train.value_counts()
'''Out[26]: 
0    375
1    201
Name: Outcome, dtype: int64'''

201/375
#0.536

y_test.value_counts()
'''
0    125
1     67
Name: Outcome, dtype: int64
'''
67/125
#Out[30]: 0.536

#training using the stand alone model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
# here K fold cross validation is used
scores=cross_val_score(DecisionTreeClassifier(), X,y,cv=5)
scores
scores.mean()
#accuracy=0.7123673711909005


#########################
#train iusing the Bagging
from sklearn.ensemble import BaggingClassifier
bag_model=BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
)

bag_model.fit(X_train,y_train)
bag_model.oob_score_
# 0.7534722222222222
#Note here we are not using test data using
#OOB samples results are tested
bag_model.score(X_test,y_test)
#0.7760416666666666
# now let us apply cross validation
bag_model= BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    max_samples=0.8,
    oob_score=True,
    random_state=0
    ) 

scores=cross_val_score(bag_model,X, y,cv=5)
scores
scores.mean()
# 0.7578728461081402

#we can see some improvement in test score with bagging classifier as comp

#training the Random Forest

from sklearn.ensemble import RandomForestClassifier
scores=cross_val_score(RandomForestClassifier(n_estimators=50), X, y ,cv=5)
scores.mean()
#0.7617859264918089