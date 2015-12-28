from xbmcswift2 import Plugin
from resources.lib import vice
import urllib3.contrib.pyopenssl

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_shows'),
        },
        {
            'label': 'test',
            'path': plugin.url_for('test_shows'),
        }
    ]

    return items

@plugin.route('/test_shows/')
def test_shows():
    
    url = 'https://www.youtube.com/playlist?list=PL1ryZU_Powd1ekQJtRz0tLand_PJrrneD'
    
    items = vice.get_playable_content(url)

    print 'Content: ^^^^^'
    print len(items)
    print items

    return items
    

@plugin.route('/all_shows/') 
def all_shows():
    url = "https://www.youtube.com/user/vice/channels"
   
    items = []
    
    content = vice.get_shows(url)
    
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('all_shows_categorys', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/all_shows/<url>/')
def all_shows_categorys(url):

    items = []

    content = vice.get_shows_categorys(url)
    print 'CONTENT ############'
    print content
    print len(content)
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('playable_content', url=i['path']),
        })

    return items


@plugin.route('/all_shows/all_shows_categorys/<url>/')
def playable_content(url): 
   
    items = []

    plugin_url = 'plugin://plugin.video.youtube/?action=play_video&videoid'
    
    items.append({
        'label': 'Damon',
        })

    url = 'https://www.youtube.com/playlist?list=PL1ryZU_Powd18tKG3q9D-oLOnrtOFMMpy'
    content = vice.get_playble_content(url)

    print 'Content: ######$$@@@'
    print content
    print len(content)

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin_url + i['path'],
        })

    return items


if __name__ == '__main__':
    plugin.run()
