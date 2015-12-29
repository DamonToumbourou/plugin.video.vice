from xbmcswift2 import Plugin
from resources.lib import vice


PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid'

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('latest_videos'),
        },
        {   
            'label': plugin.get_string(30001),
            'path': plugin.url_for('vice_on_hbo'),
        },
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('all_shows'),
        }
    ]

    return items


@plugin.route('/latest_videos/')
def latest_videos():
    url = 'https://www.youtube.com/user/vice/videos'

    items = []

    content = vice.get_latest_content(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return items


@plugin.route('/vice_on_hbo/')
def vice_on_hbo():
    url = 'http://www.youtube.com/user/vice/featured'
    
    items = []

    content = vice.get_hbo_content(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return items


@plugin.route('/all_shows/') 
def all_shows():
    url = 'https://www.youtube.com/user/vice/channels'
   
    items = []
    
    content = vice.get_shows(url)
    
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('all_shows_content', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/all_shows/<url>/')
def all_shows_content(url):
    
    plugin_url = 'plugin://plugin.video.youtube/?action=play_video&videoid'
    
    items = []

    content = vice.get_show_content(url)
    
    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return items


if __name__ == '__main__':
    plugin.run()
