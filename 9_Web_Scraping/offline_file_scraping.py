# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:13:02 2023

@author: suraj
"""
#pip install BeautifulSoup4
from bs4 import BeautifulSoup
soup=BeautifulSoup(open("C:/Data Science/data_set/sample_doc.html"),'html.parser')
print(soup)

# it is going to show all the html contents extracted
soup.text
# it will show only text
soup.contents
# it is going to show all the html contents extracted
soup.find("address")    #it show only the first address
soup.find_all("address") # show all the result
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table

for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)


# it will show all the rows except afirst row
# now we want to display  M.Tech which is located in third row and second column
# i need to give [3][2]
table.find_all('tr')[3].find_all('td')[2]
    
