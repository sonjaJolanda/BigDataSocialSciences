name= "Heidi"
coffee="Americano"
print(f'Hello, {name}, would you like to drink your {coffee}?')
#---------------------------
import selenium
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
#---------------------------
quote_list = []
author_list = []

#cause thats from 1 to 10
for i in range(1, 11):
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
quotes = pd.concat([df1, df2], axis=1)
quotes.to_excel('quotes_week2.xlsx')
#---------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.youtube.com/c/brettconti/videos'
driver.get(url)
# time.sleep(5) # because the page might need some time to load
driver.implicitly_wait(10)  # kinda the same as the line before,
# but if the loading is done it will continue (not like time.sleep()
videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-grid-video-renderer")
# specify a class name that occurs multiple times and use find_eelements to get a list returned
video_list = []

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # put a dit at front!
    views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    posted = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
    video_item = {'title': title, 'views': views, 'posted': posted}

    video_list.append(video_item)

df = pd.DataFrame(video_list)
df

driver.quit()  # just closes the tab -> always do that!
#---------------------------
from pygooglenews import GoogleNews
gn = GoogleNews()
top = gn.top_news()
top
business = gn.topic_headlines('business')
search = gn.search('%22New+York%22')  #, when = '6m')
print(search.keys())
print(search['feed'])
print(search['entries'])
#---------------------------
for item in search['entries']:
    print(item['title'])

def get_title(search):
    stories = []
    search = gn.search(search)
    newsitems = search['entries']
    for item in newsitems:
        story = {'title': item.title, 'link': item.link}
        stories.append(story)
        print(item.title)
    return stories

a = get_title('weather')
weather = pd.DataFrame(a)
weather['Title'] = weather['title'].str.split(' - ', expand=True)[0]
weather['Source'] = weather['title'].str.split(' - ', expand=True)[1]
weather.drop(['title'], axis=1)

weather.rename(columns={'link': 'Link'}, inplace=True)
weather = weather[['Title', 'Source', 'Link']]
weather.to_excel('weather.xlsx')
