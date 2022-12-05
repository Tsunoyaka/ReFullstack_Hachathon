# from bs4 import BeautifulSoup, Tag, ResultSet
# import requests 
# import json

# HOST = 'https://rupoem.ru'
# HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}



# def get_db():
#     with open('hotel.json', 'r') as file:
#         return json.load(file)


# def write_db(data):
#     with open('hotel.json', 'w') as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
    

# def get_html(url: str, category: str, headers: dict='', params: str=''):
#     """ Функция для получения html кода """
#     html = requests.get(
#         url + category,
#         headers=headers,
#         params=params,
#         verify=False
#     )
#     return html.text



# def get_card_from_html(html: str) -> ResultSet:
#     soup = BeautifulSoup(html, 'lxml')
#     cards: ResultSet = soup.find('div', class_='_0c9ol').text
#     print(cards)
#     return cards