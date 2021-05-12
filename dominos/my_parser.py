import pandas as pd


def parse_dominos(card, category):
    res = pd.DataFrame()
    url = f'https://dominos.by/{category}/'
    pizza_link = url + card.get('data-code').lower()
    pizza_name = card.find('div', {'class': 'product-card__title'}).text.strip()
    # название пиццы ^
    try:
        pizza_name = pizza_name.replace('new', '')
        pizza_name = pizza_name.replace('хит', '')
    except:
        pass
    pizza_description = card.find('div', {'class': 'product-card__description'}).text.strip()
    # ингридиенты пиццы ^
    pizza_price = card.find('p', {'class': 'product-card__modification-info-price'}).text.strip()
    pizza_weight = card.find('p', {'class': 'product-card__modification-info-weight'}).text.strip()
    pizza_img = card.find('img', {'class': 'product-card-media__element'}).get('src')

    res = res.append(pd.DataFrame(
        [[pizza_link, pizza_name, pizza_description, pizza_price, pizza_weight, pizza_img]],
        columns=['Ссылка', 'Название', 'Ингредиенты', 'Цена', 'Масса', 'Фото']),
        ignore_index=True
    )
    return res

