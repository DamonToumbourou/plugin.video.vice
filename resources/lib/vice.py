from bs4 import BeautifulSoup as bs
import re
import requests

URL = "http://www.youtube.com"
CHANNEL_URL = "https://www.youtube.com/user/vice/channels"


def get_shows(url):
    page = requests.get(url, verify=False)
    soup = bs(page.text, 'html.parser') 
    soup = soup.find('li', {'class': 'feed-item-container yt-section-hover-container browse-list-item-container branded-page-box vve-check '}) 
    content = soup.find_all('div', {'class': 'yt-lockup clearfix  yt-lockup-channel yt-lockup-grid'})

    output = [] 
    
    for i in content:
        try:
            label = i.find('title')
            label = i.get_text()
            label = re.search(r'.+?(?=(- C))', label)
            label = label.group(0)
            print "label" 
            print label
            print '\n'

            path = i.find('a')
            path = path.get('href')
            path = URL + path
            print "path: "
            print path

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

#get_shows(CHANNEL_URL)

def get_shows_categorys(url):
    page = requests.get(url, verify=False)
    soup = bs(page.text, 'html.parser')

    content = soup.find_all('li', {'class': 'feed-item-container yt-section-hover-container browse-list-item-container branded-page-box vve-check '})
    
    output = []

    for i in content:
        label = i.find('span', {'class': 'branded-page-module-title-text'})
        label = label.get_text().strip()
        print 'label: '
        print type(label)
        print label
        print '\n'
        
        path = i.find('a')
        path = path.get('href')
        path = URL + path
        print 'path: '
        print path
        print '\n'

        items = {
                'label': label,
                'path': path,
        }

        output.append(items)
        print 'path type: '
        print type(path)
    
    return output
get_shows_categorys('https://www.youtube.com/channel/UCVfmHpXONv-LVACBV68tq5Q')


def get_playable_content(url):
    payload = {'list': 'PL1ryZU_Powd1ekQJtRz0tLand_PJrrneD'}
    page = requests.get(url, params=payload)
    soup = bs(page.text, 'html.parser')
    content = soup.find_all('td', {'class': 'pl-video-title'})
    print 'CONTEBNT: '
    print content
    
    output = []
    """
    for i in content:
        
        label = i.get_text().strip()
        print 'label: '
        print label
        print '\n'

        path = i.find('a')
        path = path.get('href')
        path = re.search(r'\=(.*)', path).group(0)
        print 'path: '
        print path
        print '\n'

        items = { 
                'label': label,
                'path': path,
         }

        output.append(items)
    """
    return output

get_playable_content('https://www.youtube.com/playlist')
