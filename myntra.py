import requests
from bs4 import BeautifulSoup


def ecommerse():
    url = 'https://www.myntra.com/6529663'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")

    for link in soup.findAll('meta', {'name': "description"}):
        print(link.get('content'))


# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for cost in soup.findAll('div', {'class': '_1vC4OE _3qQ9m1'}):
#         price = cost.string
#         print("Cost : " + price)


ecommerse()
