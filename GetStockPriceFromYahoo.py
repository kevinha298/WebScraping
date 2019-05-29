import bs4
import requests
from bs4 import BeautifulSoup
import time


def parseStockPrice(stockSymbol):
    url = f'https://finance.yahoo.com/quote/{stockSymbol}?p={stockSymbol}'
    r = requests.get(url)
    # soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = bs4.BeautifulSoup(r.text, features="xml")
    price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

for i in range(9):
    time.sleep(1)
    print(parseStockPrice('FB'))




