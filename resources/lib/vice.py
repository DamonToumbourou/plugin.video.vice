from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import re
import requests

BASE_URL = "http://www.vice.com"
SHOW_URL = "http://www.vice.com/en_au/videos"

def get_shows(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    sleep(2)
    page_content = driver.page_source
    driver.quit()
    
    soup = bs(page_content)
        
    content = soup.find('div', {'class': 'list-widget all-shows grid-view'})
    content = content.find_all('li')

    for i in content:
        label = i.get_text()
        print 'label: '
        print label
        print '\n'

        path = i.find('a')
        path = path.get('href')
        path = BASE_URL + path
        print 'path: '
        print path
        print '\n'



get_shows(SHOW_URL)
