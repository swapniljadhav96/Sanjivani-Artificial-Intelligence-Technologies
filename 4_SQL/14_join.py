# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:16:00 2023

@author: Dell
"""

#######################################
#       day 9/9/23
#Join 
#testme(courses admine(coure_fees,duration,id))
#table creation
import psycopg2 as pg2
# create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn=pg2.connect(database='testme', user='postgres',password='root')

#establities connection and start cursor to be ready to query
cur=conn.cursor()


# exectute the command: create courses table
cur.execute('''create table courses_admine(courses_id serial primary key,courses_fees decimal(10,0)  not null, courses_duration varchar(20) not null);''')

#make the change to the database persistent
conn.commit()

#close the cursor and communication with the databases
cur.close()
#################################################################
#inserting  the data 
import psycopg2 as pg2
# create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn= pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cursor()

cur.execute("insert into courses_admine(courses_duration,courses_fees) values('23days',1234)");
              
cur.execute("insert into courses_admine(courses_duration,courses_fees) values('25days',123460)");
cur.execute("insert into courses_admine(courses_duration,courses_fees) values('24days',12354)");
cur.execute("insert into courses_admine(courses_duration,courses_fees) values('20days',126534)");
cur.execute("insert into courses_admine(courses_duration,courses_fees) values('29days',123498)");
cur.execute("insert into courses_admine(courses_duration,courses_fees) values('40days',123784)");
conn.commit()

cur.close()

conn.close()

#############################################################################
#join operation
import psycopg2 as pg2
# create a connection  with postgresql
#'password' whatever password you set,we set the password in the install of the postgresql
conn= pg2.connect(database='testme',user='postgres',password='root')

cur=conn.cursor()

cur.execute("""select courses_name,courses_instrutor,topic,courses_fees,courses_duration from courses inner join courses_admine 
            on courses.courses_id=courses_admine.courses_id""")
            
rows=cur.fetchall()
for row in rows:
    print(row)

