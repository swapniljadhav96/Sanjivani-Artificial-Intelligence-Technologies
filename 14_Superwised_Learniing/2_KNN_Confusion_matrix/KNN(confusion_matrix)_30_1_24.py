# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:27:50 2024

@author: suraj
"""

#k-nearset-Neighbors Algo(Confusion_Matrix)
#30/9/24

import pandas as pd
import numpy as np
wbcd= pd.read_csv("C:/Data Science/14-superwised_learniing/dataset_ml/wbcd.csv")
#there are 569 rows and 32 columns
wbcd.describe()
# in output column there is  only B for Benium And M for Malignant
# let us first convert it in Benign and Malignant
wbcd['diagnosis']= np.where(wbcd['diagnosis']=='B','Beniegn',wbcd['diagnosis'])
# in wbcd there is column named 'disgnosis, where ever there is 'B  replace with 'Beniegn

# similary where ever there is M  in the same column replace with "Malignant"
wbcd['diagnosis']= np.where(wbcd['diagnosis']=='M','Malignant',wbcd['diagnosis'])

############################################################
#0th column is patient Id let us drop it
wbcd=wbcd.iloc[:, 1:32]
############################################################
#normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now let us apply this function to the dataframe
wbcd_n=norm_func(wbcd.iloc[:,1:32])
# because now 0 th column is output or label it is not considedred hence 1:32

##############################################################
#let us now apply X as input and Y as output
X=np.array(wbcd_n.iloc[:,:])
##since in wbcd_n , we are alredy excluding output cloumn , hence all rows and 
y=np.array(wbcd['diagnosis'])

##############################################################
# m=now let us split the data into traning and testing 
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test=train_test_split(X,y,test_size=0.2)


#here you are passing X,y instead dataframe handler
# there colud chances of unbalancing of data.
# let us assume you have 100 data points , out of which 80 NC qnd 29 Cancled
#this data point must be equally distribuuted
# there is statified sampling concept is used

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=21)        #K=21
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
pred
# now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))
pd.crosstab(pred,y_test)
#let us check the applicability of the model
#i.e. miss classification , Actula pateint is alignant
# i.e. cancer patient but predivcted is Benien is 1
# actual patient is Benien and predicted as cancer pateient is 5
# heneve this model is not aceptable
#########################################
# let us try to select correct value of k
acc=[]
# running KNN algo for k=3 to k=50 in the step of 2
# k value selected is odd value
for i in range(3,50,2):
    #declare the model
    neigh=KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train,y_train)
    train_acc=np.mean(neigh.predict(X_train)==y_train)
    test_acc=np.mean(neigh.predict(X_test)==y_test)
    acc.append([train_acc, test_acc])
    
# if you will see the acc , it ha sgot two accurarcy ,i[0]=train_acc
#i[1]=test_acc
# to plot the graph of train_acc and test_acc
import matplotlib.pyplot as plt
plt.plot(np.arange(3,50,2),[i[0] for i in acc],"ro-")
plt.plot(np.arange(3,50,2),[i[1] for i in acc],'bo-')
#there ase 3,5,7 and 9 are possible values where accuracy is good\
# let us check for k=3
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred, y_test)
pd.crosstab(pred, y_test)
#ie.miss classification , actual  pateint is malignant
#i.e. cancer patient but predicted is Benien is 1
#Actual patient is Benien and predicted as cancer patient is 2
#henece this model is not acceptale
#for 5 same sinario
# for k=7 we are getting zero false positive and good accuracy
#hence k=7 is appropriate value of k
