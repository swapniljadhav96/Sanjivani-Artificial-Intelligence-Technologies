# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:34:26 2024

@author: suraj
"""
'''2.	Most cancers form a lump called a tumour. But not all lumps are cancerous.
 Doctors extract a sample from the lump and examine it to find out if it’s 
 cancer or not. Lumps that are not cancerous are called benign (be-NINE).
 Lumps that are cancerous are called malignant (muh-LIG-nunt). 
 Obtaining incorrect results (false positives and false negatives) especially
 in a medical condition such as cancer is dangerous. So, perform Bagging, 
 Boosting, Stacking, and Voting algorithms to increase model performance and 
 provide your insights in the documentation.'''
'''
business understanding

column understanding
Index(['id', 
       'diagnosis',
       'radius_mean', 
       'texture_mean', 
       'perimeter_mean',
       'area_mean',
       'smoothness_mean',
       'compactness_mean', 
       'concavity_mean',
       'points_mean',
       'symmetry_mean', 
       'dimension_mean', 
       'radius_se',
       'texture_se',
       'perimeter_se', 
       'area_se',
       'smoothness_se',
       'compactness_se', 
       'concavity_se',
       'points_se',
       'symmetry_se',
       'dimension_se',
       'radius_worst',
       'texture_worst', 
       'perimeter_worst',
       'area_worst', 
       'smoothness_worst',
       'compactness_worst',
       'concavity_worst', 
       'points_worst', 
       'symmetry_worst',
       'dimension_worst'
'''

import pandas as pd
data=pd.read_csv("C:/Data Science/14_a_ML_Assigement/7_Gradient_decent_boosting/dataset/Tumor_Ensemble.csv")

#dummy varibale
data.head()
data.info()

data.columns
'''Index(['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'points_mean', 'symmetry_mean', 'dimension_mean', 'radius_se',
       'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'points_se', 'symmetry_se',
       'dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
       'area_worst', 'smoothness_worst', 'compactness_worst',
       'concavity_worst', 'points_worst', 'symmetry_worst', 'dimension_worst'],
      dtype='object')'''



#we are speparting the column name from the dataset
predictors=data.loc[:, data.columns!="diagnosis"]
type(predictors)


target=data["diagnosis"]
type(target)
target.value_counts()
#changing the value of the dataset
target=target.apply(lambda x: 1 if x=='M' else 0 )
target
#trainn test partition of  the data

from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)
x_train.size    
x_test.size     


from sklearn.ensemble import GradientBoostingClassifier
boost_clf=GradientBoostingClassifier()
boost_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix
confusion_matrix(y_test,boost_clf.predict(x_test))
accuracy_score(y_test,boost_clf.predict(x_test))


#

#hyperparameters
boost_clf2=GradientBoostingClassifier(learning_rate=0.02,n_estimators=1000,max_depth=1)
boost_clf2.fit(x_train,y_train)

from sklearn.metrics import accuracy_score,confusion_matrix
#evaluating the testing data

confusion_matrix(y_test,boost_clf2.predict(x_test))
accuracy_score(y_test, boost_clf2.predict(x_test))      #Out[66]: 0.7922077922077922

#evalation of the traininng data
accuracy_score(y_train, boost_clf2.predict(x_train))    #Out[68]: 0.8045602605863192
