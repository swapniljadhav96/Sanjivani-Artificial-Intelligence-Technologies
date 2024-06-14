#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


iris = pd.read_csv("C:/Data_Set/iris.csv")


# In[29]:


# (Q) how many data-points and features?
print (iris.shape)


# In[30]:


#(Q) What are the column names in our dataset?
print (iris.columns)


# In[31]:


#(Q) How many data points for each class are present? 
#(or) How many flowers for each species are present?

iris["Species"].value_counts()
# balanced-dataset vs imbalanced datasets
#Iris is a balanced dataset as the number of data points for every class is 50.


# In[32]:


#2-D scatter plot:
#ALWAYS understand the axis: labels and scale.

iris.plot(kind='scatter', x='Sepal_Length', y='Sepal_Width') ;
plt.show()

#cannot make much sense out it. 
#What if we color the points by thier class-label/flower-type.


# In[34]:


import numpy as np
iris_setosa = iris.loc[iris["Species"] == "Iris-setosa"];
iris_virginica = iris.loc[iris["Species"] == "Iris-virginica"];
iris_versicolor = iris.loc[iris["Species"] == "Iris-versicolor"];
#print(iris_setosa["Petal_Length"])
plt.plot(iris_setosa["Petal_Length"], np.zeros_like(iris_setosa['Petal_Length']), 'o')
plt.plot(iris_versicolor["Petal_Length"], np.zeros_like(iris_versicolor['Petal_Length']), 'o')
plt.plot(iris_virginica["Petal_Length"], np.zeros_like(iris_virginica['Petal_Length']), 'o')

plt.show()


# In[17]:


iris.head()


# In[35]:


print("Means:")
print(np.mean(iris_setosa["Petal_Length"]))
#Mean with an outlier.
print(np.mean(np.append(iris_setosa["Petal_Length"],50)));
print(np.mean(iris_virginica["Petal_Length"]))
print(np.mean(iris_versicolor["Petal_Length"]))

print("\nStd-dev:");
print(np.std(iris_setosa["Petal_Length"]))
print(np.std(iris_virginica["Petal_Length"]))
print(np.std(iris_versicolor["Petal_Length"]))


# In[36]:


print(np.median(np.append(iris_setosa["Petal_Length"])))


# In[6]:


iris.describe()

