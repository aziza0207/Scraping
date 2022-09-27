from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup


CSV = 'aziza.txt'
URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
              'signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}


def get_html(url: str, params=''):
    response = requests.get(url, params=params, headers=HEADERS)
    return response


def get_content(response):
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('div', class_='clearfix')
    ads = []
    for data in items:
        d = {}
        if data.find('img') is None:
            continue
        else:
            d["image"] = data.find('img').get('data-src')
            price = data.find('div', 'price').text.strip().replace('$', '').replace(',', '')[:-3]
            if price.isdigit():
                d["price"] = int(price)
            else:
                d["price"] = 0
            date_info = data.find('span', class_='date-posted').text.strip()
            if date_info.startswith('<'):
                d["date"] = date.today().strftime("%d/%m/%Y")
            elif date_info == 'Yesterday':
                d["date"] = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")
            else:
                d["date"] = date_info
        ads.append(d)

    return ads
