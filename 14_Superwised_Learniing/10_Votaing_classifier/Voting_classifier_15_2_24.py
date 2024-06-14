# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:54:32 2024

@author: suraj
"""
#voting classifier:- it is majorely used for the classifiey 
#the model with the good predictaion so we can get the more acuurate model
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets
iris=datasets.load_iris()
X,y =iris.data[:,1:3],iris.target       # taking the entire data as training data
clf1=LogisticRegression()
clf2=RandomForestClassifier(random_state=1)
clf3=GaussianNB()
###################################
print("After the 5 fold cross validation")
labels=['Logistic Regression','Random Forest model', 'Naive Bayes model']
for clf,label in zip([clf1,clf2,clf3],labels):
    scores=model_selection.cross_val_score(clf, X,y,cv=5, scoring='accuracy')
    print("Accuracy:", scores.mean(),"for ",label)

#hard voting
voting_clf_hard=VotingClassifier(estimators=[(labels[0],clf1),
                                             (labels[1],clf2),
                                             (labels[2],clf3)],
                                 voting='hard')

#soft voting
voting_clf_soft=VotingClassifier(estimators=[(labels[0],clf1),
                                             (labels[1],clf2),
                                             (labels[2],clf3)],
                                 voting='soft')


labels_new=['Logistic Regression','Random Forest model', 'Naive Bayes model','voting_classifier_hard','voting_classifier_soft']
for clf,label in zip([clf1,clf2,clf3,voting_clf_hard,voting_clf_soft],labels_new):
    scores=model_selection.cross_val_score(clf, X,y,cv=5, scoring='accuracy')
    print("Accuracy:", scores.mean(),"for ",label)