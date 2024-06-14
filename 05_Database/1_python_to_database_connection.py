# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:37:42 2024

@author: suraj
"""



# python to database connection
import psycopg2 as pg2
# create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn= pg2.connect(database='dvdrental',user='postgres', password='root')

#establities connection and start cursor to be ready to query
cur=conn.cursor()

#pass in postgresql  query as string
cur.execute('Select * from payment')

#returing a tuple of the first row as python objects
cur.fetchone()

#returing the N number of the rows
cur.fetchmany(10)

#return all the rows of the column
cur.fetchall()

# to save an index results,assign it to the variable
date =cur.fetchmany(10)

#dont forget to close the connection
#killing the kernal or shutting down jyputer will also close it
conn.close()



