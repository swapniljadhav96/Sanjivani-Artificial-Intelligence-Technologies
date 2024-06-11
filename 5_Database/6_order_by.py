# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:41:00 2024

@author: suraj
"""


  
######################################################
#day 9/9/23
#order by
#using postgresal in python(with psycopg2)
import psycopg2 as pg2
#create the connection to the databases
#'password' is whatever we set for the postgresql
conn=pg2.connect(database='testme',user='postgres',password='root')
#establishing the connection and start the cursor to be ready
cur=conn.cursor()
#order by
cur.execute('select * from courses order by courses_instrutor')
#make the changes to the databases persistent
conn.commit()
rows=cur.fetchall()
for row in rows:
    print(row)