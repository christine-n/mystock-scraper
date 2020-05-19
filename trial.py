import requests
import pprint
# import sys
from bs4 import BeautifulSoup


# sys.setrecursionlimit(10000)
URL = 'http://live.mystocks.co.ke/price_list/20200511'
page = requests.get(URL)
pp = pprint.PrettyPrinter(indent=4)
soup = BeautifulSoup(page.content, 'html5lib')
results = soup.find(id='pricelist')
# print(results.prettify())
tr = results.find_all('tr', class_='row')

category = ''
for i in tr:
    print('\n\n')
    price = 0
    name = ''
    volume = 0

    td = i.find('td', class_='b2')
    if td:
        category = td.text

    nm = i.find(lambda tag: tag.name == 'a')
    if nm:
        name = nm.text

    td = i.find('td', class_='n bl b')
    if td:
        price = td.text

    n = i.find(lambda tag: tag.name == 'td' and tag.get('class') == ['n'])
    if n:
        volume = n.text
    print('Name {}  Price {}  Volume {}  Category {}'.format(name, price, volume, category))




