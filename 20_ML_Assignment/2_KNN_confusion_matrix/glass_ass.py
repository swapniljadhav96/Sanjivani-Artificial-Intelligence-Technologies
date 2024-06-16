# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:52:08 2024

@author: suraj
"""

"""glass dataset
1.	A glass manufacturing plant uses different earth elements
 to design new glass materials based on customer requirements.
 For that, they would like to automate the process of classification
 as it’s a tedious job to manually classify them. Help the company 
 achieve its objective by correctly classifying the glass type based 
 on the other features using KNN algorithm.
 
 Refractive Index ('RI'): The refractive index might be related 
 to the composition of the material, with different elements 
 affecting how light passes through the substance.

Elements Content ('Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe'): These 
columns likely represent the relative amounts or concentrations of 
different chemical elements in the material. The relationships between 
these columns could indicate how the presence of one element correlates
 with another.

'RI': Refractive Index (float64)
'Na': Sodium content (float64)
'Mg': Magnesium content (float64)
'Al': Aluminum content (float64)
'Si': Silicon content (float64)
'K': Potassium content (float64)
'Ca': Calcium content (float64)
'Ba': Barium content (float64)
'Fe': Iron content (float64)

'Type': Type of material or category (int64)
"""
import pandas as pd
import numpy as np

glass=pd.read_csv("C:/Data Science/14_a_ML_Assigement/2_KNN_confusion_matrix/dataset/glass.csv")
glass

glass.shape         #Out[55]: (214, 10)
glass.columns

############################
glass.dtypes
'''RI      float64
Na      float64
Mg      float64
Al      float64
Si      float64
K       float64
Ca      float64
Ba      float64
Fe      float64
Type      int64
dtype: object'''
##############################
d=glass.describe()
d
#data are distributed normaly
##############################
a=glass.isnull()
a.sum()
# all value are present in the  data set no null entry are present in the dataset
##################################
# checking the outlier by using the outlier
from scipy import stats
def find_outliers_zscore(glass, threshold=3):
    z_scores = np.abs(stats.zscore(glass))
    outliers = np.where(z_scores > threshold)[0]
    return outliers

outliers_zscore = find_outliers_zscore(glass)
outliers_zscore.sum()
#outlier are present in the less number so it canot affect on the result
#######################################
#all the data and column in the normalize form so need to convert into the normal form 
# andd column rename is also not requried
#################################################
#let us now apply X as input and Y as output
X=np.array(glass.iloc[:,:])
##since in wbcd_n , we are alredy excluding output cloumn , hence all rows and 
y=np.array(glass['Type'])


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
knn=KNeighborsClassifier(n_neighbors=15)        #K=21
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
pred
# now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))         #0.9767441860465116
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
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred, y_test)    #Out[19]: 0.9767441860465116
pd.crosstab(pred, y_test)


#k=25
knn=KNeighborsClassifier(n_neighbors=25)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred, y_test)    #Out[32]: 0.8604651162790697
pd.crosstab(pred, y_test)

#k=15
knn=KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred, y_test)    #Out[40]: 0.9767441860465116
pd.crosstab(pred, y_test)

# for good accuracy yu can take the value of the k from 3 to 19