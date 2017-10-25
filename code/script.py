#! /usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://seti.ufla.br/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

print(soup)
