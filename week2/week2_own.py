import requests
from bs4 import BeautifulSoup as bs
page = requests.get("http://quotes.toscrape.com/") # Sends a GET request. Returns:response-object
soup = bs(page.content, 'html.parser') # constructor, needs itself and the markup-parser ToDo Remember this
print(soup)
soup.head
soup.footer
soup.body
#--
print(soup.prettify())
# soup.find_all('span', class='text') !!!!!!!!!
print(soup.find('span', class_='text'))  #(element name, attributes) -> i think
print(soup.find_all('span', class_='text'))
txt = soup.find_all('span', itemprop='text')
#----------------------------------------------
quotes = []
for i in txt: # there is no normal for loop in python
    quotes.append((i.get_text()))
#----------------------------------------------
import pandas as pd
quotes_df = pd.DataFrame(data=quotes, columns=["quotes"]) # create a DF
quotes_df.to_excel('../week2/quotes_excel_sheet_week2.xlsx') # convert into excel file
#----------------------------------------------
authors_txt = soup.find_all('small', class_='author')
authors = []
for i in authors_txt:
    authors.append(i.get_text())
authors_df = pd.DataFrame(data=authors, columns=["authors"])
authors_df.to_excel('../week2/authors_excel_sheet_week2.xlsx')
#----------------------------------------------
quotes_and_authors_df = pd.concat([quotes_df, authors_df], axis=1) # concat two DFs
quotes_and_authors_df.to_excel('../week2/quotes_and_authors_excel_sheet_week2.xlsx')
#----------------------------------------------
quotes_and_authors_dic = dict(zip(authors, quotes)) # make a dictionary out of two DFs
df_dict = pd.DataFrame(quotes_and_authors_dic, index=[0])
df_dict.to_excel('../week2/q_a_dict_excel_sheet_week2.xlsx')
#----------------------------------------------
from xlwt import Workbook as wb
sheet1 = wb.add_sheet('Sheet from the dictionary')

counter = 1;
for key, value in quotes_and_authors_dic.items():
    sheet1.write(counter, 0, key)
    sheet1.write(counter, 1, value)
    counter += 1
wb.save('xlwt q_a_dict_excel_sheet_week2.xlsx')