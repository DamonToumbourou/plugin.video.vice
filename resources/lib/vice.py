from bs4 import BeautifulSoup as bs
from time import sleep
import re
import requests
import os

URL = "https://www.youtube.com"
CHANNEL_URL = "https://www.youtube.com/user/vice/channels"

def get_channels(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser') 
    
    soup = soup.find('li', {'class': 'feed-item-container yt-section-hover-container browse-list-item-container branded-page-box vve-check '}) 
    content = soup.find_all('div', {'class': 'yt-lockup clearfix  yt-lockup-channel yt-lockup-grid'})
    #thumbnails = soup.find_all('span', {'class': 'yt-thumb-clip'})

    output = []

    for i in content:
        try:
            label = i.find('title')
            label = i.get_text()
            label = re.search(r'.+?(?=(- C))', label)
            label = label.group(0)
            
            path = i.find('a')
            path = path.get('href')
            
            thumbnail = i.img['data-thumb']

            items = {
                'label': label,
                'path': path,
                'thumbnail': thumbnail,
            }

            output.append(items)

        except AtrributeError:
            continue

    return output

get_channels(CHANNEL_URL)

#def get_sub_shows(url):



