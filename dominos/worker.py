import requests
import pandas as pd
from bs4 import BeautifulSoup
from my_parser import *
# ^ это файл с парсером

df = pd.DataFrame()  # таблица для результатов
url = 'https://dominos.by/bread'  # урл страницы для парсинга
connection = requests.get(url)  # подключение к странице
soup = BeautifulSoup(connection.text, features='html.parser')
cards = soup.find_all('div', {'class': 'product-card'})

for item in cards:
    r = parse_dominos(item, 'bread')
    df = df.append(r, ignore_index=True)

df.to_excel('dominos_bread.xlsx')


