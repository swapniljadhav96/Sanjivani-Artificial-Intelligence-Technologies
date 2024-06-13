# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:42:54 2023

@author: suraj
"""
'''offline file  web scrapping day 5 / 12 / 23'''

# My First Web Scrapper
from bs4 import BeautifulSoup
soup=BeautifulSoup(open('C:/Data Science/13-WebScraping/Web_file_dataset/sample_doc.html'),'html.parser')
print(soup)
# it is going to show all the html contents extracted
soup.text
#it will show only text
soup.contents
#it is going to show all the html contents extracted
soup.find('address')
# To find the all the addresses
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)

    #It will show all the rows expect first row
    # Now we want to display M.Tech which is located in third row we need to give [3][2]
    table.find_all('tr')[3].find_all('td')[2]
