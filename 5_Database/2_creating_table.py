# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:38:44 2024

@author: suraj
"""


###############################################################
#createing the table in the database
#aftre installing the pip install psycopg2
import psycopg2 as pg2

#crete the connection with postgresql
conn=pg2.connect(database='testme', user='postgres',password='root')

#establities connection and start cursor to be ready to query
cur=conn.cursor()


# exectute the command: create courses table
cur.execute('''create table courses(courses_id serial primary key,
            courses_name varchar(200) unique not null,
            courses_instrutor varchar(20) not null,
            topic varchar(200) not null);''')

#make the change to the database persistent
conn.commit()

#close the cursor and communication with the databases
cur.close()