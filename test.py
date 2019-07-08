import requests
from bs4 import BeautifulSoup


def ecommerse():
    url = 'https://www.myntra.com/6529663'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    product_count = 0
    for link in soup.findAll('span', {'class': 'pdp-title'}):
        print("inside")


ecommerse()
