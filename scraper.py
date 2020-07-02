# Scraper.py

import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.yahoo.com/quote/**?ltr=1'

def getPrice(ticker: str):
    newURL = url.replace('**', ticker)
    print(newURL)
    page = urlopen(newURL)
    soup = bs4.BeautifulSoup(page, 'html.parser')
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

tick = input('Which stock do you want to search for: ').lower()

stockPrice = getPrice(tick)

print('The stock price for ' + tick.upper() + ' is $' + stockPrice)
