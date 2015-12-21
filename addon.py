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
    url = "http://www.vice.com/en_au/videos"

    items = vice.get_shows(url)
    
    return items

if __name__ == '__main__':
    plugin.run()
