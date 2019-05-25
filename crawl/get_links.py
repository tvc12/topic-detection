from bs4 import BeautifulSoup
import urllib.request
import re
from const import *


def not_relative_uri(href):
    return re.compile('^https://').search(href) is not None


def get_urls_new(url, num):
    if num <= 0:
        return
    num_link = 0
    num_page = 1
    if url in type_1:
        url_page = page_type_1
    else:
        url_page = page_type_2

    urls = []
    while True:
        try:
            print('{}: {}{}{}'.format(num_link, url, url_page, num_page))
            page = urllib.request.urlopen('{}{}{}'.format(url, url_page, num_page))
            soup = BeautifulSoup(page, 'html.parser')
            slidebar = soup.find('section', class_='sidebar_1')
            if slidebar is None:
                continue
            new_feeds = slidebar.find_all('a', class_='', href=not_relative_uri)
            if new_feeds is None:
                continue
            for feed in new_feeds:
                link = feed.get('href')
                urls.append(link)
                print('{} : {}'.format(num_link, link))
                num_link = num_link + 1
                if (num_link >= num):
                    return urls
            num_page = num_page + 1
        except:
            continue
    return urls
    
