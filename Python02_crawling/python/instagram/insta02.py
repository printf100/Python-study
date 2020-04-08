# -*- coding:utf-8 -*-

# pip install selenium

from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

# chrome 버전에 맞는 web driver가 필요함
driver = webdriver.Chrome('C:/test_workspace/chromedriver.exe')

driver.implicitly_wait(3)   # 기다렸다가 화면이 다 만들어지면 가져와줘라
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

div = soup.find_all('div', class_='KL4Bh')
print(div)