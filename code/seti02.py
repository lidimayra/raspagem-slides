#! /usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://seti.ufla.br/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

boxes = soup.findAll('div', { 'class': 'box-nome-palestrante' })

for box in boxes:
    name = box.find('p', { 'class': 'nome-palestrante' })
    print(name.text)
