from urllib import request
from bs4 import BeautifulSoup

# solve for ssl error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# date may 11 2020
url = "https://live.mystocks.co.ke/price_list/20200511"


html = request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

pricelist_table = soup.find("table", {"id": "pricelist"})


def get_table_rows(pricelist_table):
      for r in pricelist_table.findAll("tr"):
            for i in r.find_all('td', class_='nm'):
                  link = i.find('a')
                  if link:
                        h = i.find('a')['href']
                        print(h.text.strip())

get_table_rows(pricelist_table)