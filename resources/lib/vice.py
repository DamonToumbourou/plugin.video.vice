import requests
from BeautifulSoup import BeautifulSoup
import re



def get_videos():
    
    url = "http://www.vice.com/en_au/video/latest-on-vice-robot-hotels-keith-richards-and-freerasool-1031"
    title = "vice shit"

    output = []

    item = [{ 

