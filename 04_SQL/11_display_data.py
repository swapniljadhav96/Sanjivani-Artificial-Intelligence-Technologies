# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:16:00 2023

@author: Dell
"""

#########################################
#     day 9/9/23
#dispalying the data ain the python itself
import psycopg2 as pg2
## create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn=pg2.connect(database='testme',user='postgres',password='root')
#establishing the connection and start the cursor to be ready
cur=conn.cursor()

cur.execute('select * from courses;')
rows=cur.fetchall()         # fetching all the data
conn.commit()
conn.close()
for row in rows:
    print(row)
#dispalying all the data of the databases