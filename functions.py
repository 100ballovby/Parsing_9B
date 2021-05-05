import pandas as pd


def parse_table(table):
    res = pd.DataFrame()

    question = ''
    question_link = ''
    question_id = 0

    user = ''
    user_link = ''
    user_id = ''
    user_city = ''

    answer = ''

    question_tr = table.find('tr', {'class': 'question'})
    # получаю текст вопроса
    question = question_tr.find_all('td')[1].find('div').text.replace('<br />', '\n').strip()

    widget_info = question_tr.find_all('div', {'class': 'widget__info'})
    # получаю ссылки на вопросы
    question_link = 'https://banki.ru' + widget_info[0].find('a').get('href').strip()
    # получаю id вопроса
    question_id = question_link.split('=')[1]

    # кто задал вопрос
    user = widget_info[1].find('a').text.strip()
    user_link = 'https://banki.ru' + widget_info[1].find('a').get('href').strip()
    user_id = user_link.split('=')[1]

    # город
    user_city = widget_info[1].text.split('(')[1].split(')')[0].strip()

    # ответы
    answer_tr = table.find('tr', {'class': 'answer'})
    if answer_tr is not None:
        answer = answer_tr.find_all('td')[1].find('div').text.replace('<br />', '\n').strip()

    res = res.append(pd.DataFrame([
        [question_id, question_link, question,
         user_id, user, user_link, user_city, answer]
    ], columns=['ID', 'Ссылка на вопрос', 'Вопрос', 'ID пользователя',
                'Ник', 'Профиль', 'Город', 'Ответ']), ignore_index=True)
    return res
