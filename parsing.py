import requests
from bs4 import BeautifulSoup
from csv import DictWriter

DOMAIN = 'https://pythondigest.ru'

url = f'/feed/?q=python'

with open('data.csv', mode='w', encoding='utf8') as f:
    tt = DictWriter(f, fieldnames=['date', 'title', 'link', 'description'], delimiter=';')
    tt.writeheader()
    while url:
        response = requests.get(f'{DOMAIN}{url}')
        soup = BeautifulSoup(response.text, 'html.parser')

        # Поиск по тегу див (контейнеры с новостями, статьями и т.д)

        news_tag = soup.find_all('div', class_='item-container')
        for one_news_tag in news_tag:
            data = {}
            # data_news = []
            # Поиск даты
            date = one_news_tag.find('small').text[1:13]
            data['date'] = date
            # print(date)

            # поиск заголовков статей
            title = one_news_tag.find('a', rel='nofollow').text
            data['title'] = title
            # print(title)

            # Ссылки на источники
            href = one_news_tag.find('a', rel='nofollow').get('href')
            data['link'] = href
            # print(href)

            # краткое описание
            description = []
            text_p = one_news_tag.find_all('p')
            for p in text_p:
                description.append(p.get_text())
                # print(p.get_text())
                data['description'] = description
                # print(data)
            # запись данных в блокнот
            tt.writerow(data)

        # Перебор страничек
        ss = soup.find('ul', class_='pagination pagination-sm')
        p = ss.find_all('li')[2]  # [] - число страничек
        url = p.a.get('href')
