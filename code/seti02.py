#! /usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS()

url = 'http://seti.ufla.br/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

divs = soup.findAll('div', { 'ng-repeat': 'palestrante in palestrantes' })

for div in divs:
    name = div.find('p').text
    company = div.find('h4').text

    print(name, '-', company)
