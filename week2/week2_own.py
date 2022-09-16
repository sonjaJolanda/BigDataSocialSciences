import pandas as pd
quotes_df = pd.DataFrame(data = quotes, columns=["quotes"])
print(quotes_df)
#----------------------------------------------
import requests
page = requests.get("http://quotes.toscrape.com/")
print(page.content)
#----------------------------------------------
from bs4 import BeautifulSoup as bs
soup = bs(page.content, 'html.parser')
print(soup)
soup.head
soup.footer
soup.body
#--
print(soup.prettify())
# soup.find_all('span', class='text') !!!!!!!!!
print(soup.find('span', class_='text'))  #(element name, attributes) -> i think
print(soup.find_all('span', class_='text'))
print(soup.find_all('span', itemprop='text'))
#----------------------------------------------
txt = soup.find_all('span', itemprop='text')
print(txt)
#----------------------------------------------
for i in txt:
    print(i.get_text())
#----------------------------------------------
quotes = []
for i in txt:
    quotes.append((i.get_text()))
#----------------------------------------------
import pandas as pd
quotes_df = pd.DataFrame(data=quotes, columns=["quotes"])
quotes_df.to_excel('../week2/quotes_excel_sheet_week2.xlsx')
#----------------------------------------------
authors_txt = soup.find_all('small', class_='author')
authors = []
for i in authors_txt:
    authors.append(i.get_text())
authors_df = pd.DataFrame(data=authors, columns=["authors"])
authors_df.to_excel('../week2/authors_excel_sheet_week2.xlsx')
#----------------------------------------------
quotes_and_authors_df = pd.concat([quotes_df, authors_df], axis=1)
quotes_and_authors_df
quotes_and_authors_df.to_excel('../week2/quotes_and_authors_excel_sheet_week2.xlsx')
#----------------------------------------------
quotes_and_authors_dic = dict(zip(authors, quotes))
print(quotes_and_authors_dic)
df_dict = pd.DataFrame(quotes_and_authors_dic, index=[0])
df_dict.to_excel('../week2/q_a_dict_excel_sheet_week2.xlsx')

from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet from the dictionary')

counter = 1;
for key, value in quotes_and_authors_dic.items():
    sheet1.write(counter, 0, key)
    sheet1.write(counter, 1, value)
    counter += 1

wb.save('xlwt q_a_dict_excel_sheet_week2.xlsx')