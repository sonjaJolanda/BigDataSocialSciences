name= "Heidi"
coffee="Americano"
print(f'Hello, {name}, would you like to drink your {coffee}?')


import selenium
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd

quote_list=[]
author_list=[]

#cause thats from 1 to 10
for i in range(1,11):
    url = f'http://quotes.toscrape.com/page/{i}/'
    response = requests.get(url)
    html = response.text
    soup = bs(html, 'html.parser')

    quotes = soup.find_all('span', itemprop='text')
    authors = soup.find_all('small', class_='author')

    for quote in quotes:
        quote_list.append(quote.get_text())

    for author in authors:
        author_list.append(author.get_text())

df1 = pd.DataFrame(data=quote_list, columns=['Quotes'])
df2 = pd.DataFrame(data=author_list, columns=['Authors'])

quotes = pd.concat([df1,df2], axis=1)
quotes.to_excel('quotes_week2.xlsx')

#selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
#-------------------------------




