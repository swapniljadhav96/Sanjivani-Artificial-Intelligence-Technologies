# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:24:07 2023

@author: suraj
"""
'''web scrapping sentiment analysis'''
from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/motorola-edge-40-neo-caneel-bay-256-gb/p/itm55813a9671489?pid=MOBGQFX6APUFAPMS&lid=LSTMOBGQFX6APUFAPMSO5N7CJ&marketplace=FLIPKART&q=mobile&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=6a034a79-d4d8-4961-bcc6-a543880ca510.MOBGQFX6APUFAPMS.SEARCH&ppt=hp&ppn=homepage&ssid=lh1c0f9tio0000001701746929438&qH=532c28d5412dd75b'
page =requests.get(link)
page                        #respond 200 successfuly
page.content

soup=bs(page.content, 'html.parser')
print(soup.prettify())
title= soup.find_all('p' , class_='_2-N8zT')
title
#store the title of the rating and reviews
review_title=[]
#store the reviews in the lst 
for i in range(0, len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)
#we got  10 review title
############
#now let us scrap the rating

rating= soup.find_all('div',  class_='_3LWZlK _1BLPMq')
rating
rate=[]
for i in range(0, len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.append(' ')
rate.append(' ')
#rate.append(' ')
len(rate)
#################
#now let us try scrape the review body
review= soup.find_all('div',  class_='t-ZTKy')
review
review_body=[]
for i in range(0, len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)

# we got 10 review body
#################
# now we have to save the data in csv
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title

df['Rate']=rate
df['Review']=review_body
df
#################
# to create the .csv file
df.to_csv('C:/Data Science/13-WebScraping/flipcart_reviews.csv', index=True)

###########################
#sentiment anlysis
import pandas as pd
from textblob import TextBlob 
sent=' This is excellent garden'
pol= TextBlob(sent).sentiment.polarity
pol

df=pd.read_csv('C:/Data Science/13-WebScraping/flipcart_reviews.csv')
df.head()
df['polarity']=df["Review"].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

################################################
