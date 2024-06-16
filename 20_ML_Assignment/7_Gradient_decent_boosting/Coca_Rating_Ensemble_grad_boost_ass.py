# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:57:52 2024

@author: suraj
"""
#Coca_Rating_Ensemble
'''3.	A sample of global companies and their ratings are 
given for the cocoa bean production along with the location
 of the beans being used. Identify the important features 
 in the analysis and accurately classify the companies based
 on their ratings and draw insights from the data. 
 Build ensemble models such as Bagging, Boosting, Stacking,
 and Voting on the dataset given.'''
''' 
Business understanding

Index(['Company', 
       'Name', 
       'REF', 
       'Review', 
       'Cocoa_Percent',
       'Company_Location',
       'Rating', 
       'Bean_Type',
       'Origin'
'''
import pandas as pd
data=pd.read_excel("C:/Data Science/14_a_ML_Assigement/7_Gradient_decent_boosting/dataset/Coca_Rating_Ensemble.xlsx")

#dummy varibale
data.head()
data.info()

data.columns
'''
Index(['Company', 'Name', 'REF', 'Review', 'Cocoa_Percent', 'Company_Location',
       'Rating', 'Bean_Type', 'Origin'],
      dtype='object')'''