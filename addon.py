from xbmcswift2 import Plugin
from resources.lib import vice

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_shows'),
        }
    ]

    return items


@plugin.route('/all_shows/') 
def all_shows():
    url = "https://www.youtube.com/user/vice/channels"
   
    items = []
    
    content = vice.get_channels(url)
    
    for con in content:
        items.append({
            'label': con['label'],
            'path': con['path'],
            'thumbnail': con['thumbnail'],
        })

    return items


if __name__ == '__main__':
    plugin.run()
