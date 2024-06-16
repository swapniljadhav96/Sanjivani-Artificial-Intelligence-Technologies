# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:49:54 2024

@author: suraj
"""
#gradient_descend boosting
#Diabeted_Ensemlbel
'''
1.	Given is the diabetes dataset. Build an ensemble model to correctly classify
 the outcome variable and improve your model prediction by using GridSearchCV.
 You must apply Bagging, Boosting, Stacking, and Voting on the dataset.  '''
'''
Business understanding

column name
Index([' Number of times pregnant',
       ' Plasma glucose concentration',
       ' Diastolic blood pressure',
       ' Triceps skin fold thickness',
       ' 2-Hour serum insulin', 
       ' Body mass index',
       ' Diabetes pedigree function',
       ' Age (years)',
       ' Class variable'
      
'''
import pandas as pd
data=pd.read_csv("C:/Data Science/14_a_ML_Assigement/7_Gradient_decent_boosting/dataset/Diabeted_Ensemble.csv")

#dummy varibale
data.head()
data.info()

data.columns
'''Index([' Number of times pregnant', ' Plasma glucose concentration',
       ' Diastolic blood pressure', ' Triceps skin fold thickness',
       ' 2-Hour serum insulin', ' Body mass index',
       ' Diabetes pedigree function', ' Age (years)', ' Class variable'],
      dtype='object')'''

#rename the column name from the data set
data.columns=('Number_of_times_pregnant', 'Plasma_glucose_concentration',
       'Diastolic_blood_pressure', 'Triceps_skin_fold_thickness',
       '2-Hour_serum_insulin', 'Body_mass_index',
       'Diabetes_pedigree_function', 'Age', 'Class_variable')

data.columns
#we are speparting the column name from the dataset
predictors=data.loc[:, data.columns!="Class_variable"]
type(predictors)


target=data["Class_variable"]
type(target)


#trainn test partition of  the data

from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(predictors,target,test_size=0.2,random_state=0)
x_train.size    #Out[51]: 4912
x_test.size     #Out[52]: 1232


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
