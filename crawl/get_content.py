from bs4 import BeautifulSoup
import urllib.request
import re

def get_content(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('article', class_='content_detail')
    if content is None:
        return ''
    news = content.find_all('p', class_='Normal')
    if news is None:
        return ''
    news.insert(0, soup.find('h1', class_='title_news_detail'))
    return ' '.join([new.text for new in news])