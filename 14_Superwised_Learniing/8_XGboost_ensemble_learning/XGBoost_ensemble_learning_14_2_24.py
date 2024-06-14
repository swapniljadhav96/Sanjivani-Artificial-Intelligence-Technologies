# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:56:15 2024

@author: suraj
"""

#install the XGBoost


#XGBoost
import pandas as pd
df=pd.read_csv("C:/Data Science/movies_classification.csv")

#dummy varibale
df.head()
df.info()



#n-1 dummy varible will be created for n categories
df=pd.get_dummies(df,columns=["3D_available","Genre"], drop_first=True)

df.head()


#input And output split

predictors=df.loc[:, df.columns!="Start_Tech_Oscar"]
type(predictors)


target=df["Start_Tech_Oscar"]
type(target)


#trainn test partition of  the data
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)

#reffer the link
#
#

#pip install xgboost
import xgboost as xgb

xgb_clf=xgb.XGBClassifier(max_depths=5,n_estimators=10000, learning_rate=0.3,n_jobs=1)

#n_jobs - ny=umber of parallel threads used to run xgboost
#learning_rate (float) -boosting learning rate(xgb's "eta)

xgb_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix

#evalauting the testing data
confusion_matrix(y_test,xgb_clf.predict(x_test))
accuracy_score(y_test,xgb_clf.predict(x_test))

#finding the imporatant feature
xgb.plot_importance(xgb_clf)

xgb_clf=xgb.XGBClassifier(n_estimators=500,learning_rate=0.1,random_state=42)

param_test1={ 'max_depth':range(3,10,2),'gamma':[0.1,0.2,0.3],
             'subsample':[0.8,0.9],'colsample_bytree':[0.8,0.9],
             'rag_alpha':[1e-2,0.1,1]}

#grid search
from sklearn.model_selection import GridSearchCV
grid_search= GridSearchCV(xgb_clf, param_test1,n_jobs=1,cv=5,scoring='accuracy')


grid_search.fit(x_train,y_train)
cv_xg_clf=grid_search.best_estimator_

#evaluation on testing data with model with hyperparametere
accuracy_score(y_test, cv_xg_clf.predict(x_test))
grid_search.best_params_

