# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:09:18 2024

@author: suraj
"""


'''-------------------test 3 coding---------------------------------------------'''
"""-------------------
branch :-computer(sy)
"""
import pandas as pd
df=pd.read_csv('Data_Science_Attendance_Sheet2.csv')

#Que1  rename the colummn  name
df2=df.rename({'Suraj_Chothe':'suraj'},axis='columns')
print(df2)
#rename the file column with the new name 
#Q2
column_headers=list(df['Suraj Chothe'])
print(column_headers)
#Q3
column_headers.count(0)
column_headers.count(1)
column_headers.count(2)
column_headers.count(3)
column_headers.count(4)
column_headers.count(5)
column_headers.count(7)
#Q4


#Q5
df['Suraj Chothe'].describe()

#Q6
import seaborn as sns
sns.boxplot(column_headers)

#Q7
import seaborn as sns
sns.jointplot(column_headers)

#Q8 
df.describe()
######################################################
#marksheet  csv
import pandas as pd
df=pd.read_csv('Marksheet.csv')
df
#Q9
lst=list(df['Chothe_Suraj'])
print(lst)


#############################################
file_name='AI_jobs_in_2024.txt'
with open(file_name,'r')  as obj:
    obj.read()


##########################Resolve paper#############################
import pandas as pd
df=pd.DataFrame(pd.read_csv('Data_Science_Attendance_Sheet2.csv'))
df

#Q1
df2=df.rename({'Suraj Chothe':'Suraj'},axis='columns')
df2

#Q2
column_headers=list(df['Suraj Chothe'])
print(column_headers)

#Q3
column_headers.count(0)
#for 0 sessions 1day
column_headers.count(1)
#for 1 sessions 1day
column_headers.count(2)
#for 2 sessions 2days
column_headers.count(3)
#for 3 sessions 5days
column_headers.count(4)
#for 4 sessions 14day
column_headers.count(5)
#for 5 sessions 3days
column_headers.count(7)
#for 0 sessions 0day

#Q4
import matplotlib.pyplot as plt
fig=plt.figure()
df['Suraj Chothe'].plot(kind='bar')
plt.legend()

#Q5
df['Suraj Chothe'].describe()
#Q6
import seaborn as sns
sns.boxplot(column_headers)
#Q7
import seaborn as sns
sns.jointplot(column_headers)

#Q8*
df.rename(index={27: 'NewRow'}, inplace=True)

total_attendance = df.loc['NewRow']
total_attendance = total_attendance.drop(['year', 'month', 'weekday', 'datum'])

regular=0
moderate=0
poor=0

for i in total_attendance:
    if i>=80:
        regular+=1
    elif i<80 and i>=45:
        moderate+=1
    elif i<45:
        poor+=1

print("Total regular students are: ",regular)
print("Total moderate students are: ",moderate)
print("Total poor attendace students are: ",poor)


"""------2nd File-----------"""
#Q9
import pandas as pd
mark=pd.DataFrame(pd.read_csv('Marksheet.csv'))
mark

#Q9
mymarks=mark.iloc[44]
print(mymarks['List'])
print(mymarks['Dictionary'])
if mymarks['List'] > mymarks['Dictionary']:
    print('I am strong in list and weak in dictionary')
else:
    print('I am strong in dictionary and weak in list')
    
#Q10
count1=0
count2=0
count=0
last_col=mark['Total']  
last_col
for i in range(0,len(last_col)):
    
    if last_col[i]>=8:
        count1=count1+1
        
    elif last_col[i]>=4:
        count=count+1
       
    else:
        count2=count2+1

print('low performance',count)
print('good performance',count1)
print('study hard',count2)

########################3

#Q11
obj = open("C:/Data Science/1-python/AI_jobs_in_2024.txt" , "r")
obj.read()


################################################################
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7'] 			#row labelling for the dataframe
df = pd.DataFrame(technologies, index=row_labels)
print(df)
###################################
#DataFrame properties
#shape of the dataframe
df.shape
#o.p:-(8, 4)
###################################
df.size
#o.p:-32
##################################
df.columns
df.columns.values
df.index
df2=df[6:]
df2
df['Duration'][3]
df['Fee'] = df['Fee'] - 500
df['Fee']
df.describe()

df = pd.DataFrame(technologies, index=row_labels)
df
# Drop rows by labels
df1 = df.drop(['r1','r2'])
df1
# Delete Rows by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
# Delete Rows by Index Range
df1=df.drop(df.index[2:])
df1
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1
df = pd.DataFrame(technologies)
df1 = df.drop([0, 3])
df1#it will delete row0 n row3
df1 = df.drop(range(0,2))#it will delete 0 and 1
df1
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)
df2 = df.iloc[[2,3,6]]    
df2

import pandas as pd
songs_69=pd.Series([7,56,34,1],
                   index=['aa','ss','dd','ff'],
                   name='Counts')

import matplotlib.pyplot as plt
flg=plt.figure()
songs_69.plot()
plt.legend()
import pandas as pd
songs_66=pd.Series([3,None,11,9],
                   index=['a','s','d','f'],
                   name='Counts')


import numpy as np
data=pd.Series(np.random.randn(500),
name='500 random')
flg=plt.figure()
ax=flg.add_subplot(111)
data.hist()

import numpy as np
arr1=np.array([24,2,34,45])
arr2=np.array([23,2,34,56])
arr1
arr2
arr1.dtype      
