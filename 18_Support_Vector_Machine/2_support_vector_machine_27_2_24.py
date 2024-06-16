# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 08:31:55 2024

@author: suraj
"""

#svm 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
forest=pd.read_csv("C:/Data Science/18_Support_vector_machine/datasets/forestfires.csv")

forest.dtypes
####################
#eda
forest.shape

plt.figure(1,figsize=(16,10))
sns.countplot(data=forest, x=forest.month)

#Aug and sep has hights value
sns.countplot(data=forest, x=forest.day)
#friday sunday and saturday has highest value

sns.distplot(forest.FFMC)
#data is normal and slight left skeweed
sns.boxplot(forest.FFMC)
#there are several outlier
sns.displot(forest.DMC)
#data is noramal and slight left skewed
sns.boxplot(forest.DMC)
#there are outlier 
sns.displot(forest.DC)
#data is noramal and slight left skewed
sns.boxplot(forest.DC)
#there are outlier
sns.displot(forest.ISI)
#data is noramal and slight left skewed
sns.boxplot(forest.ISI)
#there are outlier

sns.displot(forest.temp)
#data is noramal and slight left skewed
sns.boxplot(forest.temp)
#there are outlier

sns.displot(forest.RH)
#data is noramal and slight left skewed
sns.boxplot(forest.RH)
#there are outlier
sns.displot(forest.wind)
#data is noramal and slight left skewed
sns.boxplot(forest.wind)
#there are outlier

sns.displot(forest.rain)
#data is noramal and slight left skewed
sns.boxplot(forest.rain)
#there are outlier

sns.displot(forest.area)
#data is noramal and slight left skewed
sns.boxplot(forest.area)
#there are outlier

sns.displot(forest.dayfri)
#data is noramal and slight left skewed
sns.boxplot(forest.dayfri)
#there are outlier


#now let us check the highest fire in KM?

forest.sort_values(by='area', ascending=False).head(5)

highest_fire_area= forest.sort_values(by='area', ascending=True)

plt.figure(figsize=(8,9))

plt.title("temp vs area of fire")

plt.bar(highest_fire_area['temp'],
        highest_fire_area['area'])

plt.xlabel("temp")
plt.ylabel("area")

plt.show()
#once the fire starts almost 1000+ sq areas
#temp goes beyond 25 and
#around 750 Km area is facting temp 30+
# now let us check the highest rain in the forest
highset_rain= forest.sort_values(by='rain', ascending=False)[['month','day','rain']].head(5)
highset_rain
#highset rain observed in the month of aug
# let us check highest and lowest temp in mont and day
highset_temp= forest.sort_values(by='temp', ascending=False)[['month','day','rain']].head(5)
lowest_temp= forest.sort_values(by='temp', ascending=True)[['month','day','rain']].head(5)

print("highset temp",highset_temp)
# highest temp obsered in AUG
print("lowest temp",lowest_temp)
#lowest temp obserd in Dec

forest.isna().sum()
#ther is no misssing value in both
########################3
#now there arvarious outlier are presen t in the data set co chevk it

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
forest.month=labelencoder.fit_transform(forest.month)
forest.day=labelencoder.fit_transform(forest.day)
forest.size_category=labelencoder.fit_transform(forest.size_category)


# now the winsorization are apply to remove the outlier

forest.dtypes

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method = "iqr",tail='both',fold=1.5, variables=['month'])
df_t = winsor.fit_transform(forest[['month']])
sns.boxplot(df_t.month)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['day'])
df_t=winsor.fit_transform(forest[['day']])
sns.boxplot(df_t.day)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['FFMC'])
df_t=winsor.fit_transform(forest[['FFMC']])
sns.boxplot(df_t.FFMC)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['DMC'])
df_t=winsor.fit_transform(forest[['DMC']])
sns.boxplot(df_t.DMC)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['DC'])
df_t=winsor.fit_transform(forest[['DC']])
sns.boxplot(df_t.DC)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['ISI'])
df_t=winsor.fit_transform(forest[['ISI']])
sns.boxplot(df_t.ISI)


from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['temp'])
df_t=winsor.fit_transform(forest[['temp']])
sns.boxplot(df_t.temp)

from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['RH'])
df_t=winsor.fit_transform(forest[['RH']])
sns.boxplot(df_t.RH)

from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['wind'])
df_t=winsor.fit_transform(forest[['wind']])
sns.boxplot(df_t.wind)

from feature_engine.outliers import Winsorizer 
winsor = Winsorizer(capping_method = "iqr", tail='both',fold=1.5, variables=['rain'])
df_t = winsor.fit_transform(forest[['rain']])
sns.boxplot(df_t.rain)

from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5, variables=['area'])
df_t=winsor.fit_transform(forest[['area']])
sns.boxplot(df_t.area)


########################
tc=forest.corr()
tc
fig,ax=plt.subplots()

fig.set_size_inches(200,10)

sns.heatmap(tc,annot=True)

# all the varibles are moderaterly correlated with the size_category

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test=train_test_split(forest, test_size=0.3)
train_x=train.iloc[:,:30]
train_y=train.iloc[:,30]
test_x=test.iloc[:,:30]
test_y=test.iloc[:,30]

#kernel linerar

model_linear=SVC(kernel="linear")
model_linear.fit(train_x,train_y)
pred_test_linear=model_linear.predict(test_x)
np.mean(pred_test_linear==test_y)


#RBF
model_rbf=SVC(kernel="rbf")
model_rbf.fit(train_x,train_y)
pred_test_rbf=model_rbf.predict(test_x)
np.mean(pred_test_rbf==test_y)


#gamma
model_g=SVC(gamma=10)
model_g.fit(train_x, train_y)
model_g.score(test_x, test_y)