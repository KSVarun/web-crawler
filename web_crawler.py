import requests
from bs4 import BeautifulSoup


def ecommerse(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.flipkart.com/bags-wallets-belts/pr?sid=reh&marketplace=FLIPKART&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2BMore&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2527s&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&p%5B%5D=facets.ideal_for%255B%255D%3DBoys&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&fm=neo%2Fmerchandising&iid=M_a063c635-fec5-4ce4-a2dc-66710f5d0fb5_19.LOM1P6PMFGME&ppt=Homepage&ppn=Homepage&otracker=hp_omu_Fashion%2BAccessories_1_LOM1P6PMFGME_1&cid=LOM1P6PMFGME&page=' + \
            str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        product_count = 0
        for link in soup.findAll('a', {'class': '_2cLu-l'}):
            product_count += 1
            href = "https://www.flipkart.com"+link.get('href')
            title = link.string
            print(str(product_count) + " Title : " + title)
            print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for cost in soup.findAll('div', {'class': '_1vC4OE _3qQ9m1'}):
        price = cost.string
        print("Cost : " + price)


ecommerse(1)
