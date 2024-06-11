# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:46:39 2023

@author: suraj
"""

#package is requests

from bs4 import BeautifulSoup as bs
import requests
link="https://sanjivanicoe.org.in/"
'''link:-https://sanjivanicoe.org.in/index.php/contact'''
page=requests.get(link)

page
#<response [200]> it means connection is successfully esatablilshed
#<response[503]> error sevrver not find''https://developer.mozilla.org/en-US/docs/Web/HTTP/Status'''

page.content

#it will get all html source code but very crowdy text
# let us apply the html parser

soup=bs(page.content,'html.parser')
soup

# now the text is clean but not upto expectation
# now let us apply prettify method
print(soup.prettify())
# the text is neat and clean
list(soup.children)
#fimding all the content using the tab


soup.find_all('p')

#suppose you want to extract contents from first row
soup.find_all('p')[1].get_text()
#content from second row
soup.find_all('p')[2].get_text()

# finding th etext using the class

soup.find_all('div',class_='table')
