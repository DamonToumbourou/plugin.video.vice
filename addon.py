from xbmcswift2 import Plugin
from resources.lib import abcradionational

plugin = Plugin()


@plugin.route('/')
def main_menu():
    url = "plugin://plugin.video.youtube/?action=play_video&videoid="

    items = []
    
    

    items.append({
        'label': 'vice',
        'path': url + "69LDbyl4Xjs",
        'is_playable': True,
    })

    return items


if __name__ == '__main__':
    plugin.run()
