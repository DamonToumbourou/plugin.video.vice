from bs4 import BeautifulSoup as bs
from time import sleep
import re
import requests
import os

SHOWS_URL = "https://www.youtube.com/user/vice/channels"

def get_shows(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser') 
    
    content = soup.find_all('div', {'class': 'yt-lockup-content'})
    
    output = []
    for i in content:
        label = i.find('title')
        label = i.get_text()
        label = re.search(r'.+?(?=[-])', label)
        label = label.group(0)
        print 'label: '
        print label
        print '\n'
    
        path = i.find('a')
        path = path.get('href')
        print 'href: '
        print path
        print '\n'

get_shows(SHOWS_URL)
