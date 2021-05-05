import requests
from bs4 import BeautifulSoup
from functions import parse_table
import pandas as pd


bank_id = 1771062  # ID банка на сайте
page, max_page = 1, 20
url = f'https://www.banki.ru/services/questions-answers/?id={bank_id}&p={page}'
r = requests.get(url)  # подключаюсь по указанному урлу
result = pd.DataFrame()  # создаю таблицу
soup = BeautifulSoup(r.text, features='html.parser')  # это сам парсер
tables = soup.find_all('table', {'class': 'qaBlock'})

for item in tables:
    res = parse_table(item)  # я вызываю функцию парсинга для каждой таблицы с сайта


# .find('table') - ищет первое вхождение элемента в тексте
# .find_all('table') - ищет ВСЕ вхождения элемента в тексте
# find('table').text - возврат текста, который находится в объекте
# find('table').get('href') - вернет ссылки


#with open('test.html', 'w') as f:
    # открываю файл test.html в режиме записи (write)
#    f.write(r.text)  # И записываю в него ответ от сайта

