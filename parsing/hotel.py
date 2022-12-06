from bs4 import BeautifulSoup, Tag, ResultSet
import requests 
import json

HOST = 'https://www.booking.com/searchresults.ru.html?aid=1703515&label=Icw2&sid=add3b9361bd9b57007b84e0e2f70769a&city=-2331392&srpvid=780364de44aa0327&'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}



def get_db(db):
    with open(f'{db}.json', 'r') as file:
        return json.load(file)


def write_db(data, db):
    with open(f'{db}.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    

def get_html(url: str, headers: dict='', params: str=''):
    """ Функция для получения html кода """
    html = requests.get(
        url,
        headers=headers,
        params=params,
        verify=False
    )
    return html.text



def get_card_from_html(html: str) -> ResultSet:
    soup = BeautifulSoup(html, 'lxml')
    cards: ResultSet = soup.find_all('div', class_='c90a25d457')
    # print(cards)
    return cards


def hotel_url(cards):
    result_ = []
    num = 0
    db = get_db('hotel')
    for card in cards:
        hotel = card.find('a').get('href') 
        db.append(hotel)
    write_db(db, 'hotel')
    return result_


def get_card_from_hotel(html: str) -> ResultSet:
    soup = BeautifulSoup(html, 'lxml')
    return soup


def hotel():
    db = get_db('hotel')
    dbs = get_db('hotels')
    for hotel in range(20):
        html = get_html(db[hotel])
        cards = get_card_from_hotel(html)
        stars = cards.find('span', class_="fbb11b26f5 e23c0b1d74") 
        num=0
        if stars is not None:
            for i in stars:
                num+=1
        else:
            num = None
        desc_list = cards.find('div', id='property_description_content').text
        obj = {
            'title': cards.find('h2', class_='d2fee87262 pp-header__title').text,
            'desc': desc_list,
            'desc_list': desc_list.split('\n')[1],
            'stars': num
            }

        dbs.append(obj)
    write_db(dbs, 'hotels')
    
hotel()
