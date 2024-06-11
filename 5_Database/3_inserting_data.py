# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:39:26 2024

@author: suraj
"""



#day 2
################---- 9/9/23--------------------------
#inserting the data
import psycopg2 as pg2

## create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn= pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cursor()

cur.execute("insert into courses(courses_name,courses_instrutor,topic) values('introduction to sql','ram','Julia')");
              
cur.execute("insert into courses(courses_name,courses_instrutor,topic) values('analysis the survay data python','raj','Jpython')");

cur.execute("insert into courses(courses_name,courses_instrutor,topic) values('introduction to chatgpt','ganesh','chatgpt')");
              
cur.execute("insert into courses(courses_name,courses_instrutor,topic) values('introduction to c','raghav','c')");
              
cur.execute("insert into courses(courses_name,courses_instrutor,topic) values('introduction to c++','ramraj','c++')");

conn.commit()

cur.close()

conn.close()




 