from service import get_html, get_content, URL
from database import data_base


def parser():
    html = get_html(URL)
    print(html)
    if html.status_code == 200:
        print("The parsing in progress...")
        ads = []
        pages = 94
        for page in range(1, pages + 1):
            html = get_html(f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273')
            ads.extend(get_content(html.text))
        print(ads)
        data_base(ads)
    else:
        print("Error")


parser()
