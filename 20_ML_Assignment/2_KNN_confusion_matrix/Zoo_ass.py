# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:58:57 2024

@author: suraj
"""

#zoo dataset
"""
2.	A National Zoopark in India is dealing with the problem of 
segregation of the animals based on the different attributes they 
have. Build a KNN model to automatically classify the animals. 
Explain any inferences you draw in the documentation.

'animal name': The name of the animal (string).
'hair': Presence of hair (binary: 0 for no, 1 for yes).
'feathers': Presence of feathers (binary: 0 for no, 1 for yes).
'eggs': Lays eggs (binary: 0 for no, 1 for yes).
'milk': Produces milk (binary: 0 for no, 1 for yes).
'airborne': Capable of flying or airborne (binary: 0 for no, 1 for yes).
'aquatic': Lives in the water or is aquatic (binary: 0 for no, 1 for yes).
'predator': Is a predator (binary: 0 for no, 1 for yes).
'toothed': Has teeth (binary: 0 for no, 1 for yes).
'backbone': Has a backbone or spine (binary: 0 for no, 1 for yes).
'breathes': Can breathe (binary: 0 for no, 1 for yes).
'venomous': Is venomous (binary: 0 for no, 1 for yes)
'fins': Has fins (binary: 0 for no, 1 for yes).
'legs': Number of legs (integer).
'tail': Presence of a tail (binary: 0 for no, 1 for yes)
'domestic': Is domesticated (binary: 0 for no, 1 for yes).
'catsize': Has a cat-like size (binary: 0 for no, 1 for yes).
'type': Type of animal or category (integer).

Descriptions:

'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 
'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 
'tail', 'domestic', 'catsize' are binary features indicating the 
presence or absence of certain characteristics.

'legs' is an integer feature representing the number of legs.

'type' is the target variable, likely representing different 
types or categories of animals.

"""

import pandas as pd
import numpy as np

zoo=pd.read_csv("C:/Data Science/14_a_ML_Assigement/2_KNN_confusion_matrix/dataset/Zoo.csv")
zoo

zoo.shape           #Out[45]: (101, 18)
zoo.columns

############################
zoo.dtypes
'''Out[48]: 
animal name    object
hair            int64
feathers        int64
eggs            int64
milk            int64
airborne        int64
aquatic         int64
predator        int64
toothed         int64
backbone        int64
breathes        int64
venomous        int64
fins            int64
legs            int64
tail            int64
domestic        int64
catsize         int64
type            int64
dtype: object'''

####################################
a=zoo.describe()
#data are distributed normaly

#####################################
b=zoo.isnull()
b.sum()
# no null value are present in the dataset all entry or row with feature having the some value

######################################
zoo=zoo.drop(columns=['animal name'])
'''##################################
# checking the outlier by using the outlier
from scipy import stats
def find_outliers_zscore(zoo, threshold=3):
    z_scores = np.abs(stats.zscore(zoo))
    outliers = np.where(z_scores > threshold)[0]
    return outliers

outliers_zscore = find_outliers_zscore(zoo)
outliers_zscore.sum()
#outlier are present in the less number so it canot affect on the result
#######################################
#all the data and column in the normalize form so need to convert into the normal form 
# andd column rename is also not requried'''
#################################################
#let us now apply X as input and Y as output
X=np.array(zoo.iloc[:,:])
##since in wbcd_n , we are alredy excluding output cloumn , hence all rows and 
y=np.array(zoo['type'])


# m=now let us split the data into traning and testing 
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test=train_test_split(X,y,test_size=0.2)
X_train.sum()
X_test.sum()
#here you are passing X,y instead dataframe handler
# there colud chances of unbalancing of data.
# let us assume you have 100 data points , out of which 80 NC qnd 29 Cancled
#this data point must be equally distribuuted
# there is statified sampling concept is used
###############################################
#KNN algo
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=15)        #K=15
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
pred
# now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))        
pd.crosstab(pred,y_test)

################################
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
accuracy_score(pred, y_test)    #Out[19]: 0.9523809523809523
pd.crosstab(pred, y_test)
